import os
import json
import asyncio
from typing import Optional, Dict, Any, List
from concurrent.futures import ThreadPoolExecutor, as_completed
from pydantic import BaseModel, Field
from openai import OpenAI


class Tools:
    class Valves(BaseModel):
        HEAVY_THINKING_ENABLED: bool = Field(
            default=True,
            description="Enable heavy thinking mode"
        )
        HEAVY_THINKING_AGENTS: int = Field(
            default=4,
            description="Number of parallel thinking agents (2-8 recommended)"
        )
        HEAVY_THINKING_TIMEOUT: int = Field(
            default=300,
            description="Timeout per agent in seconds"
        )
        HEAVY_THINKING_PROVIDER: str = Field(
            default="openrouter",
            description="API provider: openrouter, openai, anthropic, google, or custom"
        )
        HEAVY_THINKING_API_KEY: str = Field(
            default="",
            description="API key for the selected provider"
        )
        HEAVY_THINKING_BASE_URL: str = Field(
            default="",
            description="Base URL for API (only needed for 'custom' provider - auto-set for openrouter/openai/anthropic/google)"
        )
        HEAVY_THINKING_MODEL: str = Field(
            default="openai/gpt-4o-mini",
            description="Model to use - Examples: OpenRouter: 'anthropic/claude-3.5-haiku', OpenAI: 'gpt-4o-mini', Anthropic: 'claude-3-5-haiku-20241022', Google: 'gemini-2.0-flash-exp' or 'models/gemini-flash-latest'"
        )
        HEAVY_THINKING_MAX_ITERATIONS: int = Field(
            default=3,
            description="Maximum iterations per agent"
        )

    def __init__(self):
        self.valves = self.Valves()

    def _get_api_client(self) -> OpenAI:
        provider = self.valves.HEAVY_THINKING_PROVIDER.lower()
        api_key = self.valves.HEAVY_THINKING_API_KEY or os.getenv(
            f"{provider.upper()}_API_KEY"
        )

        if not api_key:
            raise ValueError(
                f"API key not configured for provider: {provider}. "
                f"Set HEAVY_THINKING_API_KEY in valves or {provider.upper()}_API_KEY environment variable."
            )

        if provider == "openrouter":
            base_url = "https://openrouter.ai/api/v1"
        elif provider == "openai":
            base_url = "https://api.openai.com/v1"
        elif provider == "anthropic":
            base_url = "https://api.anthropic.com/v1"
        elif provider == "google":
            # Google Gemini via OpenAI-compatible endpoint
            base_url = "https://generativelanguage.googleapis.com/v1beta/openai"
        elif provider == "custom":
            base_url = self.valves.HEAVY_THINKING_BASE_URL
            if not base_url:
                raise ValueError(
                    "HEAVY_THINKING_BASE_URL must be set when using custom provider"
                )
        else:
            raise ValueError(
                f"Unknown provider: {provider}. "
                f"Supported: openrouter, openai, anthropic, google, custom"
            )

        return OpenAI(base_url=base_url, api_key=api_key)

    def _generate_research_questions(
        self, query: str, num_agents: int
    ) -> List[str]:
        try:
            client = self._get_api_client()

            prompt = f"""You are an orchestrator that needs to create {num_agents} different specialized research questions to thoroughly analyze the following query from multiple angles.

Original Query: {query}

Generate exactly {num_agents} focused research questions that will help gather comprehensive information. Each question should explore a different aspect:
- Question 1: Research comprehensive factual information
- Question 2: Analyze implications, patterns, or deeper insights
- Question 3: Find alternative perspectives or counterarguments
- Question 4: Verify facts and cross-check reliability

Return ONLY a valid JSON array of {num_agents} strings, nothing else. Example format:
["Research question 1?", "Analysis question 2?", "Alternative perspective question 3?", "Verification question 4?"]"""

            response = client.chat.completions.create(
                model=self.valves.HEAVY_THINKING_MODEL,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=500,
            )

            content = response.choices[0].message.content.strip()
            
            if content.startswith("```json"):
                content = content[7:]
            if content.endswith("```"):
                content = content[:-3]
            content = content.strip()

            questions = json.loads(content)

            if not isinstance(questions, list) or len(questions) != num_agents:
                raise ValueError("Invalid question format")

            return questions

        except Exception as e:
            print(f"Question generation failed: {e}, using fallback")
            return [
                f"Research comprehensive information about: {query}",
                f"Analyze and provide insights about: {query}",
                f"Find alternative perspectives on: {query}",
                f"Verify and cross-check facts about: {query}",
            ][:num_agents]

    def _run_thinking_agent(self, agent_id: int, question: str) -> Dict[str, Any]:
        try:
            client = self._get_api_client()

            system_prompt = """You are a specialized research and analysis agent. Your task is to thoroughly investigate the given question and provide comprehensive, well-reasoned insights.

Focus on:
- Accurate, factual information
- Clear reasoning and analysis
- Multiple perspectives when relevant
- Practical implications

Provide a complete, detailed response."""

            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question},
            ]

            response = client.chat.completions.create(
                model=self.valves.HEAVY_THINKING_MODEL,
                messages=messages,
                temperature=0.7,
            )

            content = response.choices[0].message.content

            return {
                "agent_id": agent_id,
                "status": "success",
                "response": content,
                "question": question,
            }

        except Exception as e:
            error_msg = str(e)
            if "google" in self.valves.HEAVY_THINKING_PROVIDER.lower():
                error_msg += "\n\nNote: For easier Google Gemini access, use provider='openrouter' with model='google/gemini-2.5-flash' instead of direct Google API."
            
            return {
                "agent_id": agent_id,
                "status": "error",
                "response": f"Agent {agent_id + 1} failed: {error_msg}",
                "question": question,
            }

    def _synthesize_responses(
        self, query: str, agent_results: List[Dict[str, Any]]
    ) -> str:
        successful_results = [
            r for r in agent_results if r["status"] == "success"
        ]

        if not successful_results:
            return "All thinking agents failed. Please try again or check your API configuration."

        if len(successful_results) == 1:
            return successful_results[0]["response"]

        agent_responses_text = ""
        for i, result in enumerate(successful_results, 1):
            agent_responses_text += f"""=== AGENT {i} PERSPECTIVE ===
Question: {result['question']}
Response: {result['response']}

"""

        try:
            client = self._get_api_client()

            synthesis_prompt = f"""You have {len(successful_results)} different AI agents that analyzed the same query from different angles.

Original Query: {query}

{agent_responses_text}

Your task is to synthesize these {len(successful_results)} perspectives into ONE comprehensive, coherent answer that:
1. Combines the best insights from all agents
2. Resolves any contradictions
3. Provides a complete, unified response
4. Maintains factual accuracy

Provide a well-structured, thorough response that represents the collective intelligence of all agents."""

            response = client.chat.completions.create(
                model=self.valves.HEAVY_THINKING_MODEL,
                messages=[{"role": "user", "content": synthesis_prompt}],
                temperature=0.5,
            )

            return response.choices[0].message.content

        except Exception as e:
            print(f"Synthesis failed: {e}, using concatenated responses")
            combined = [f"# Heavy Thinking Analysis\n\nOriginal Query: {query}\n"]
            for i, result in enumerate(successful_results, 1):
                combined.append(f"\n## Agent {i} Perspective")
                combined.append(f"**Focus:** {result['question']}")
                combined.append(result["response"])
            return "\n\n".join(combined)

    async def heavy_think(
        self,
        query: str = Field(
            ...,
            description="The complex question or problem that requires deep, multi-perspective analysis"
        ),
        __event_emitter__=None,
    ) -> str:
        """
        Activate heavy thinking mode: Deploy multiple AI agents in parallel to analyze
        a query from different perspectives, then synthesize their insights into a
        comprehensive answer. This emulates advanced reasoning systems like Grok Heavy.

        Use this for complex questions that benefit from multi-perspective analysis,
        research tasks, or when you need thorough exploration of a topic.
        """

        if not self.valves.HEAVY_THINKING_ENABLED:
            return "Heavy thinking mode is disabled. Enable it in the tool valves configuration."

        num_agents = max(2, min(8, self.valves.HEAVY_THINKING_AGENTS))

        try:
            if __event_emitter__:
                await __event_emitter__(
                    {
                        "type": "status",
                        "data": {
                            "description": f"🧠 Generating {num_agents} research questions...",
                            "done": False,
                        },
                    }
                )

            questions = self._generate_research_questions(query, num_agents)

            if __event_emitter__:
                questions_preview = "\n".join([f"  • Agent {i+1}: {q[:80]}..." for i, q in enumerate(questions)])
                await __event_emitter__(
                    {
                        "type": "status",
                        "data": {
                            "description": f"🔄 Deploying {num_agents} thinking agents in parallel:\n{questions_preview}",
                            "done": False,
                        },
                    }
                )

            agent_results = []
            with ThreadPoolExecutor(max_workers=num_agents) as executor:
                future_to_agent = {
                    executor.submit(self._run_thinking_agent, i, questions[i]): i
                    for i in range(num_agents)
                }

                for i, future in enumerate(
                    as_completed(future_to_agent, timeout=self.valves.HEAVY_THINKING_TIMEOUT),
                    1
                ):
                    try:
                        result = future.result()
                        agent_results.append(result)
                        
                        agent_id = result["agent_id"]
                        status_icon = "✅" if result["status"] == "success" else "❌"
                        
                        if __event_emitter__:
                            await __event_emitter__(
                                {
                                    "type": "status",
                                    "data": {
                                        "description": f"{status_icon} Agent {i}/{num_agents} completed ({num_agents - i} remaining)\nFocus: {questions[agent_id][:60]}...",
                                        "done": False,
                                    },
                                }
                            )
                    except Exception as e:
                        agent_id = future_to_agent[future]
                        agent_results.append(
                            {
                                "agent_id": agent_id,
                                "status": "timeout",
                                "response": f"Agent {agent_id + 1} timed out or failed: {str(e)}",
                                "question": questions[agent_id],
                            }
                        )
                        
                        if __event_emitter__:
                            await __event_emitter__(
                                {
                                    "type": "status",
                                    "data": {
                                        "description": f"⚠️ Agent {agent_id + 1} timeout/error: {str(e)[:50]}...",
                                        "done": False,
                                    },
                                }
                            )

            agent_results.sort(key=lambda x: x["agent_id"])

            successful_count = sum(1 for r in agent_results if r["status"] == "success")
            
            if __event_emitter__:
                await __event_emitter__(
                    {
                        "type": "status",
                        "data": {
                            "description": f"🔮 Synthesizing insights from {successful_count}/{num_agents} successful agents...",
                            "done": False,
                        },
                    }
                )

            final_result = self._synthesize_responses(query, agent_results)

            if __event_emitter__:
                await __event_emitter__(
                    {
                        "type": "status",
                        "data": {
                            "description": f"✨ Heavy thinking complete! ({successful_count}/{num_agents} agents contributed)",
                            "done": True,
                        },
                    }
                )

            return final_result

        except Exception as e:
            error_msg = f"Heavy thinking failed: {str(e)}"
            if __event_emitter__:
                await __event_emitter__(
                    {
                        "type": "status",
                        "data": {"description": f"❌ {error_msg}", "done": True},
                    }
                )
            return error_msg
