# 🧠 Heavy Thinking Tool for Open WebUI

A powerful multi-agent reasoning tool for [Open WebUI](https://github.com/open-webui/open-webui) that emulates advanced "heavy thinking" modes like Grok Heavy. Deploy multiple AI agents in parallel to analyze complex queries from different perspectives, then synthesize their insights into comprehensive answers.

## 🌟 Features

- **🔀 Multi-Agent Orchestration**: Deploy 2-8 parallel AI agents for comprehensive analysis
- **🎯 Dynamic Question Generation**: AI automatically creates specialized research questions
- **⚡ Parallel Execution**: All agents run simultaneously for maximum efficiency
- **🔄 Intelligent Synthesis**: Combines multiple perspectives into unified, coherent answers
- **🛠️ Multi-Provider Support**: Works with OpenRouter, OpenAI, Anthropic, Google Gemini, or any OpenAI-compatible API
- **📊 Real-time Status Updates**: Live progress feedback in Open WebUI
- **⚙️ Fully Configurable**: Customize agent count, timeouts, models, and providers via valves

## 🚀 Quick Start

### 1. Installation

1. Copy `heavy_thinking.py` to your Open WebUI tools directory
2. Restart Open WebUI or reload tools
3. The tool will appear in your available tools list

### 2. Configuration

Open the tool settings in Open WebUI and configure the valves:

#### Required Settings
- **API Provider**: Choose from `openrouter`, `openai`, `anthropic`, `google`, or `custom`
- **API Key**: Your API key for the selected provider

#### Optional Settings
- **Number of Agents**: 2-8 agents (default: 4)
- **Timeout**: Seconds per agent (default: 300)
- **Model**: The model to use (default: `openai/gpt-4o-mini` for OpenRouter)
- **Base URL**: Custom API endpoint (for OpenRouter or custom providers)

### 3. Usage

In any Open WebUI chat, call the heavy thinking tool:

```
Please use heavy thinking to analyze: "What are the implications of quantum computing on cryptography?"
```

Or directly invoke the tool:
```
heavy_think("Explain the economic impact of AI automation")
```

## 📖 How It Works

### Architecture Flow

```
User Query
    ↓
Question Generation Agent
    ↓
Generate 4 Specialized Questions
    ↓
┌─────────────────────────────────────┐
│   Parallel Agent Execution          │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐│
│  │Agent1│ │Agent2│ │Agent3│ │Agent4││
│  │  🔍  │ │  🔍  │ │  🔍  │ │  🔍  ││
│  └──────┘ └──────┘ └──────┘ └──────┘│
└─────────────────────────────────────┘
    ↓
Synthesis Agent
    ↓
Comprehensive Final Answer
```

### Agent Specialization

By default, the tool creates 4 specialized perspectives:

1. **Research Agent**: Gathers comprehensive factual information
2. **Analysis Agent**: Explores implications, patterns, and deeper insights
3. **Alternatives Agent**: Finds different perspectives and counterarguments
4. **Verification Agent**: Cross-checks facts and validates reliability

### Synthesis

All agent responses are combined by a synthesis agent that:
- Merges the best insights from each perspective
- Resolves contradictions
- Creates a unified, coherent narrative
- Maintains factual accuracy

## ⚙️ Configuration Guide

### Provider Setup

#### OpenRouter (Recommended)
```python
HEAVY_THINKING_PROVIDER = "openrouter"
HEAVY_THINKING_API_KEY = "sk-or-v1-..."
HEAVY_THINKING_BASE_URL = "https://openrouter.ai/api/v1"
HEAVY_THINKING_MODEL = "openai/gpt-4o-mini"  # or any OpenRouter model
```

#### OpenAI
```python
HEAVY_THINKING_PROVIDER = "openai"
HEAVY_THINKING_API_KEY = "sk-..."
HEAVY_THINKING_MODEL = "gpt-4o-mini"
```

#### Anthropic
```python
HEAVY_THINKING_PROVIDER = "anthropic"
HEAVY_THINKING_API_KEY = "sk-ant-..."
HEAVY_THINKING_MODEL = "claude-3-5-sonnet-20241022"
```

#### Google Gemini
**Recommended**: Use via OpenRouter for easier setup:
```python
HEAVY_THINKING_PROVIDER = "openrouter"
HEAVY_THINKING_API_KEY = "sk-or-v1-..."
HEAVY_THINKING_MODEL = "google/gemini-2.0-flash-exp"
```

Or use direct Google API (advanced):
```python
HEAVY_THINKING_PROVIDER = "google"
HEAVY_THINKING_API_KEY = "AIza..."
HEAVY_THINKING_MODEL = "gemini-2.5-flash"
```

#### Custom OpenAI-Compatible API
```python
HEAVY_THINKING_PROVIDER = "custom"
HEAVY_THINKING_API_KEY = "your-api-key"
HEAVY_THINKING_BASE_URL = "https://your-api.example.com/v1"
HEAVY_THINKING_MODEL = "your-model-name"
```

### Environment Variables

You can also set API keys via environment variables:
```bash
export OPENROUTER_API_KEY="sk-or-v1-..."
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."
export GOOGLE_API_KEY="..."
```

### Performance Tuning

#### For Cost Efficiency
- Use fewer agents (2-3)
- Use cheaper models (gpt-4o-mini, gemini-flash)
- Reduce timeout if questions are simple

#### For Maximum Quality
- Use more agents (6-8)
- Use premium models (claude-3.5-sonnet, gpt-4o)
- Increase timeout for complex research

#### Recommended Configurations

**Fast & Cheap**:
```python
HEAVY_THINKING_AGENTS = 2
HEAVY_THINKING_MODEL = "openai/gpt-4o-mini"
HEAVY_THINKING_TIMEOUT = 60
```

**Balanced**:
```python
HEAVY_THINKING_AGENTS = 4
HEAVY_THINKING_MODEL = "openai/gpt-4o-mini"
HEAVY_THINKING_TIMEOUT = 180
```

**Maximum Depth**:
```python
HEAVY_THINKING_AGENTS = 6
HEAVY_THINKING_MODEL = "anthropic/claude-3.5-sonnet"
HEAVY_THINKING_TIMEOUT = 300
```

## 🎮 Examples

### Research Query
```
User: Use heavy thinking to analyze the future of renewable energy
```

**Process**:
- 4 agents research different aspects (technology, economics, policy, environmental impact)
- Each provides specialized insights
- Synthesis combines into comprehensive analysis

### Complex Problem
```
User: heavy_think("How should a startup approach AI integration in 2025?")
```

**Process**:
- Agents explore: technical requirements, business strategy, cost analysis, risk management
- Combined perspective provides actionable roadmap

### Creative Analysis
```
User: What would happen if we discovered alien life tomorrow? Use heavy thinking.
```

**Process**:
- Multiple perspectives: scientific, societal, philosophical, practical
- Synthesis creates multi-faceted exploration

## 🔧 Troubleshooting

### Common Issues

**"API key not configured"**
- Set `HEAVY_THINKING_API_KEY` in tool valves
- Or set environment variable for your provider

**"All thinking agents failed"**
- Check your API key is valid
- Verify the model name is correct for your provider
- Check network connectivity
- Review Open WebUI logs for detailed errors

**"Agent timeout"**
- Increase `HEAVY_THINKING_TIMEOUT`
- Try a faster model
- Reduce number of agents
- Check API rate limits

**Slow performance**
- Reduce number of agents
- Use faster models (e.g., gpt-4o-mini vs gpt-4)
- Check your internet connection

### Debug Mode

To see detailed logs, check your Open WebUI console or logs for:
- Question generation output
- Individual agent responses
- Synthesis process
- Error messages

## 📊 Comparison with Standard Queries

| Aspect | Standard Query | Heavy Thinking |
|--------|---------------|----------------|
| Perspectives | Single viewpoint | 2-8 parallel perspectives |
| Depth | Limited by single pass | Multi-layered analysis |
| Speed | Faster (1 API call) | Slower (N+2 API calls) |
| Cost | Lower | Higher (multiple agents) |
| Quality | Good for simple queries | Excellent for complex topics |
| Best For | Quick answers, simple facts | Research, analysis, complex problems |

## 🤝 Contributing

Contributions welcome! This tool is open source and designed to be extended.

### Adding Features

Some ideas for enhancements:
- Custom agent specializations
- Tool-using agents (web search, calculator, etc.)
- Streaming responses
- Result caching
- Quality scoring and agent ranking
- Agent debate/discussion mode

## 📝 License

MIT License - see LICENSE file for details

### Attribution

Inspired by:
- [Make It Heavy](https://github.com/Doriandarko/make-it-heavy) by Pietro Schirano
- Grok Heavy mode functionality
- Multi-agent AI systems research

## 🙏 Acknowledgments

- Built for [Open WebUI](https://github.com/open-webui/open-webui)
- Uses OpenAI-compatible APIs (OpenRouter, OpenAI, Anthropic, Google)
- Inspired by advanced multi-agent reasoning systems

## 🔗 Links

- [Open WebUI](https://github.com/open-webui/open-webui)
- [OpenRouter](https://openrouter.ai/)
- [Original Make It Heavy](https://github.com/Doriandarko/make-it-heavy)

---

**Ready to think heavy?** 🚀

Install the tool, configure your API provider, and start getting multi-perspective AI analysis on complex queries!
