# Usage Examples - Heavy Thinking Tool

This document provides practical examples of using the Heavy Thinking tool in Open WebUI for various use cases.

## Basic Usage

### Simple Invocation

**User**: 
```
Use heavy thinking to analyze: What are the implications of quantum computing?
```

**What happens**:
1. Question generation agent creates 4 specialized questions
2. 4 agents research in parallel:
   - Agent 1: Research quantum computing fundamentals
   - Agent 2: Analyze implications for cryptography and security
   - Agent 3: Explore alternative quantum technologies
   - Agent 4: Verify current state and timeline
3. Synthesis combines all perspectives into comprehensive answer

### Direct Tool Call

You can also directly invoke the tool in Open WebUI:

**User**:
```
heavy_think("What is the best programming language for AI development in 2025?")
```

## Advanced Use Cases

### 1. Research & Analysis

#### Market Research
**Query**:
```
Use heavy thinking: Should I invest in renewable energy stocks in 2025?
```

**Agent Perspectives**:
- Financial analysis and market trends
- Technology and innovation assessment
- Policy and regulatory landscape
- Risk factors and alternatives

**Result**: Multi-dimensional investment analysis with balanced perspectives

---

#### Scientific Research
**Query**:
```
heavy_think("What are the latest breakthroughs in mRNA vaccine technology?")
```

**Agent Perspectives**:
- Recent research and clinical trials
- Technical mechanisms and innovations
- Alternative vaccine approaches
- Verification of claims and sources

**Result**: Comprehensive scientific overview with validated information

---

### 2. Problem Solving

#### Technical Decisions
**Query**:
```
Use heavy thinking to help me decide: Should I use microservices or monolith architecture for my startup?
```

**Agent Perspectives**:
- Technical requirements analysis
- Cost and resource implications
- Scalability and maintenance considerations
- Industry best practices and case studies

**Result**: Detailed decision framework with pros/cons

---

#### Business Strategy
**Query**:
```
heavy_think("How should a SaaS company approach AI integration in their product?")
```

**Agent Perspectives**:
- Technical implementation strategies
- Business model and pricing
- Competitive analysis
- Risk management and compliance

**Result**: Actionable roadmap with multiple viewpoints

---

### 3. Learning & Education

#### Deep Dives
**Query**:
```
Use heavy thinking: Explain blockchain technology from first principles
```

**Agent Perspectives**:
- Core cryptographic concepts
- Consensus mechanisms and distributed systems
- Real-world applications and limitations
- Common misconceptions and clarifications

**Result**: Comprehensive educational overview

---

#### Comparative Analysis
**Query**:
```
heavy_think("Compare and contrast different approaches to machine learning: supervised, unsupervised, and reinforcement learning")
```

**Agent Perspectives**:
- Theoretical foundations of each approach
- Practical applications and use cases
- Strengths and weaknesses
- When to use each method

**Result**: Detailed comparison with examples

---

### 4. Creative Exploration

#### Thought Experiments
**Query**:
```
Use heavy thinking: What would happen if we discovered intelligent alien life tomorrow?
```

**Agent Perspectives**:
- Scientific implications
- Societal and cultural impact
- Technological and economic effects
- Philosophical and existential considerations

**Result**: Multi-faceted exploration of hypothetical scenario

---

#### Future Predictions
**Query**:
```
heavy_think("What will the job market look like in 2030 with advanced AI?")
```

**Agent Perspectives**:
- Technological trends and capabilities
- Economic transformation patterns
- Social and educational adaptations
- Policy and regulatory responses

**Result**: Comprehensive future scenario analysis

---

### 5. Code & Technical Review

#### Architecture Review
**Query**:
```
Use heavy thinking to review this system design:
[paste your architecture diagram or description]
```

**Agent Perspectives**:
- Scalability and performance analysis
- Security and reliability concerns
- Cost optimization opportunities
- Alternative approaches

**Result**: Multi-angle technical review

---

#### Technology Selection
**Query**:
```
heavy_think("Which database should I use: PostgreSQL, MongoDB, or DynamoDB for a real-time analytics platform?")
```

**Agent Perspectives**:
- Technical capabilities comparison
- Performance and scalability analysis
- Cost and operational considerations
- Use case fit assessment

**Result**: Data-driven technology recommendation

---

## Configuration Examples

### Scenario 1: Quick Research (Low Cost)

**Settings**:
```python
HEAVY_THINKING_AGENTS = 2
HEAVY_THINKING_MODEL = "openai/gpt-4o-mini"
HEAVY_THINKING_TIMEOUT = 60
HEAVY_THINKING_PROVIDER = "openrouter"
```

**Best for**:
- Quick fact-checking
- Simple comparisons
- Rapid prototyping ideas
- Budget-conscious usage

**Example Query**:
```
Use heavy thinking: What's the difference between REST and GraphQL?
```

**Cost**: ~$0.01 per query

---

### Scenario 2: Balanced Analysis (Medium Cost)

**Settings**:
```python
HEAVY_THINKING_AGENTS = 4
HEAVY_THINKING_MODEL = "openai/gpt-4o-mini"
HEAVY_THINKING_TIMEOUT = 180
HEAVY_THINKING_PROVIDER = "openrouter"
```

**Best for**:
- Most use cases
- Professional work
- Research projects
- Content creation

**Example Query**:
```
heavy_think("Analyze the pros and cons of remote work for software companies")
```

**Cost**: ~$0.02-0.05 per query

---

### Scenario 3: Deep Research (High Quality)

**Settings**:
```python
HEAVY_THINKING_AGENTS = 6
HEAVY_THINKING_MODEL = "anthropic/claude-3.5-sonnet"
HEAVY_THINKING_TIMEOUT = 300
HEAVY_THINKING_PROVIDER = "openrouter"
```

**Best for**:
- Critical business decisions
- Research papers
- Comprehensive analysis
- High-stakes scenarios

**Example Query**:
```
Use heavy thinking to analyze: Should our company adopt a 4-day work week?
```

**Cost**: ~$0.50-1.00 per query

---

### Scenario 4: Maximum Depth (Premium)

**Settings**:
```python
HEAVY_THINKING_AGENTS = 8
HEAVY_THINKING_MODEL = "anthropic/claude-3.5-sonnet"
HEAVY_THINKING_TIMEOUT = 600
HEAVY_THINKING_PROVIDER = "openrouter"
```

**Best for**:
- Strategic planning
- Investment decisions
- Critical research
- Complex problem-solving

**Example Query**:
```
heavy_think("Comprehensive analysis: What are all factors to consider when choosing a city to relocate our company headquarters?")
```

**Cost**: ~$1.00-2.00 per query

---

## Integration Examples

### With Open WebUI Functions

You can integrate heavy thinking with other Open WebUI tools:

```python
# In your custom function
def analyze_complex_topic(topic: str) -> str:
    # First get quick overview
    quick_answer = llm.chat(f"Quick summary of {topic}")
    
    # Then deep dive with heavy thinking
    deep_analysis = heavy_think(
        f"Comprehensive analysis of {topic} including: "
        f"technical details, implications, alternatives, and verification"
    )
    
    return f"Quick Overview:\n{quick_answer}\n\nDeep Analysis:\n{deep_analysis}"
```

### Chained Analysis

Break complex problems into stages:

**Stage 1 - Problem Definition**:
```
heavy_think("What are the key challenges in building a sustainable AI business?")
```

**Stage 2 - Solution Exploration** (using Stage 1 output):
```
heavy_think("Given these challenges [paste Stage 1 results], what are the most promising solutions?")
```

**Stage 3 - Action Plan**:
```
heavy_think("Create a 6-month action plan based on these solutions [paste Stage 2 results]")
```

---

## Real-World Use Cases

### Startup Founder

**Use Case**: Validate business idea
```
heavy_think("Comprehensive analysis: Should I build a B2B SaaS for automated code review? Include market size, competition, technical feasibility, and go-to-market strategy.")
```

### Developer

**Use Case**: Architecture decision
```
heavy_think("My app has 1M users and growing 20% monthly. Should I migrate from Django monolith to microservices? Include migration strategy, risks, and timeline.")
```

### Researcher

**Use Case**: Literature review
```
heavy_think("What are the current approaches to AI alignment and safety? Include recent papers, different schools of thought, and open problems.")
```

### Product Manager

**Use Case**: Feature prioritization
```
heavy_think("Analyze which feature to build first: real-time collaboration, advanced analytics, or mobile app. Context: B2B project management tool, 5K users, 3 engineers, 6-month timeline.")
```

### Student

**Use Case**: Study assistance
```
heavy_think("Explain machine learning optimization algorithms (gradient descent, Adam, RMSprop) with mathematical intuition, practical examples, and when to use each.")
```

---

## Tips & Best Practices

### Getting Better Results

1. **Be Specific**: Include context and constraints
   - ❌ "Should I use React?"
   - ✅ "Should I use React or Vue for a real-time dashboard with 100+ charts, considering our team knows TypeScript?"

2. **Ask for Structure**: Request specific format
   - "Use heavy thinking to analyze X and provide: 1) Summary, 2) Pros/Cons, 3) Recommendation"

3. **Provide Context**: The more information, the better
   - Include: budget, timeline, team size, technical constraints, business goals

4. **Use for Complex Topics**: Simple queries don't need heavy thinking
   - ✅ Complex: "Comprehensive market analysis for entering the AI healthcare space"
   - ❌ Simple: "What is Python?" (use regular chat)

### Cost Management

1. **Start Small**: Test with 2 agents before scaling to 8
2. **Use Cheaper Models**: gpt-4o-mini works great for most cases
3. **Strategic Use**: Reserve heavy thinking for important decisions
4. **Monitor Usage**: Track costs through your API provider

### Performance Optimization

1. **Timeout**: Start with 180s, adjust based on query complexity
2. **Agent Count**: 4 agents is the sweet spot for most queries
3. **Model Selection**: Balance cost vs quality based on importance
4. **Provider**: OpenRouter offers best model variety and pricing

---

## Comparison: Regular Chat vs Heavy Thinking

### When to Use Regular Chat
- Simple factual questions
- Quick clarifications
- Code snippets
- Straightforward tasks
- Cost-sensitive applications

### When to Use Heavy Thinking
- Complex decisions
- Multi-faceted analysis
- Research projects
- Strategic planning
- Critical thinking required
- Multiple perspectives needed

---

**Ready to think heavy?** Start with a simple query and scale up based on your needs!
