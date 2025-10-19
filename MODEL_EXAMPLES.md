# Model Configuration Examples

This guide shows you exactly which model names to use for each API provider. The model name format varies by provider, so use this reference when configuring `HEAVY_THINKING_MODEL` in the tool valves.

## Quick Reference Table

| Provider | Model Name Format | Example |
|----------|------------------|---------|
| OpenRouter | `provider/model-name` | `anthropic/claude-3.5-haiku` |
| OpenAI | `model-name` | `gpt-4o-mini` |
| Anthropic | `model-name-date` | `claude-3-5-haiku-20241022` |
| Google | `model-name` or `models/model-name` | `gemini-2.0-flash-exp` |
| Custom | Varies by provider | Check your API docs |

---

## OpenRouter

OpenRouter uses the format: `provider/model-name`

### Recommended Models

#### Budget-Friendly (Fast & Cheap)
```
anthropic/claude-3.5-haiku       # Best value, very fast
openai/gpt-4o-mini              # Cheap, reliable
google/gemini-2.0-flash-exp     # Fast, experimental
google/gemini-flash-1.5         # Stable, free tier available
meta-llama/llama-3.3-70b-instruct  # Open source, good quality
```

#### Balanced (Good Quality)
```
openai/gpt-4o                   # High quality, reasonable cost
anthropic/claude-3.5-sonnet     # Excellent reasoning
google/gemini-pro-1.5           # Good balance
```

#### Premium (Best Quality)
```
anthropic/claude-3-opus         # Top-tier reasoning
openai/o1-preview               # Advanced reasoning
google/gemini-ultra-1.5         # Google's best (when available)
```

#### Specialized Models
```
perplexity/llama-3.1-sonar-large-128k-online  # With web search
x-ai/grok-beta                  # Grok access via OpenRouter
deepseek/deepseek-chat          # Excellent for code
```

### How to Find Model Names

1. Visit https://openrouter.ai/models
2. Find the model you want
3. Copy the model ID (e.g., `anthropic/claude-3.5-haiku`)
4. Paste into `HEAVY_THINKING_MODEL` valve

### Cost Comparison (OpenRouter)

| Model | Cost per Query* | Speed | Quality |
|-------|----------------|-------|---------|
| `google/gemini-flash-1.5` | $0.001 | ⚡⚡⚡ | ⭐⭐⭐ |
| `anthropic/claude-3.5-haiku` | $0.01 | ⚡⚡⚡ | ⭐⭐⭐⭐ |
| `openai/gpt-4o-mini` | $0.02 | ⚡⚡ | ⭐⭐⭐⭐ |
| `anthropic/claude-3.5-sonnet` | $0.15 | ⚡⚡ | ⭐⭐⭐⭐⭐ |
| `openai/gpt-4o` | $0.25 | ⚡ | ⭐⭐⭐⭐⭐ |

*Approximate cost for 4-agent query with typical response lengths

---

## OpenAI

OpenAI uses simple model names (no provider prefix).

### Available Models

```
gpt-4o-mini                     # Recommended: cheap, fast, good quality
gpt-4o                          # High quality, more expensive
gpt-4-turbo                     # Previous generation, still good
gpt-3.5-turbo                   # Cheapest, basic quality
o1-preview                      # Advanced reasoning (expensive)
o1-mini                         # Reasoning model (cheaper)
```

### Configuration Example

```python
HEAVY_THINKING_PROVIDER = "openai"
HEAVY_THINKING_API_KEY = "sk-proj-..."
HEAVY_THINKING_MODEL = "gpt-4o-mini"
# Base URL auto-set to: https://api.openai.com/v1
```

### Model Selection Guide

**For most use cases**: `gpt-4o-mini`
- Fast, cheap, great quality
- Perfect for 4-agent heavy thinking

**For important decisions**: `gpt-4o`
- Higher quality reasoning
- Better at complex analysis

**For budget constraints**: `gpt-3.5-turbo`
- Cheapest option
- Good for simple queries

**For advanced reasoning**: `o1-preview` or `o1-mini`
- Specialized reasoning models
- More expensive but deeper thinking

---

## Anthropic (Claude)

Anthropic uses model names with date suffixes.

### Available Models

```
claude-3-5-haiku-20241022       # Recommended: fast, smart, affordable
claude-3-5-sonnet-20241022      # Best: excellent reasoning, balanced cost
claude-3-5-sonnet-20240620      # Previous version, still great
claude-3-opus-20240229          # Premium: best quality, expensive
claude-3-haiku-20240307         # Budget: fast and cheap
```

### Configuration Example

```python
HEAVY_THINKING_PROVIDER = "anthropic"
HEAVY_THINKING_API_KEY = "sk-ant-..."
HEAVY_THINKING_MODEL = "claude-3-5-haiku-20241022"
# Base URL auto-set to: https://api.anthropic.com/v1
```

### Model Selection Guide

**For most use cases**: `claude-3-5-haiku-20241022`
- Newest Haiku, very fast
- Excellent value for money

**For best quality**: `claude-3-5-sonnet-20241022`
- Industry-leading reasoning
- Great for complex analysis

**For premium results**: `claude-3-opus-20240229`
- Absolute best quality
- Use for critical decisions only

### Finding Latest Versions

Visit https://docs.anthropic.com/en/docs/models-overview for the latest model names and dates.

---

## Google Gemini

Google uses simple model names (works via OpenAI-compatible endpoint).

### Available Models

```
gemini-2.0-flash-exp            # Latest experimental, fast
gemini-2.5-flash                # Recommended: fast, good quality
gemini-2.5-pro                  # Best quality, advanced reasoning
gemini-1.5-flash                # Stable version, reliable
gemini-1.5-pro                  # Previous gen, still great
```

### Configuration Example (Recommended)

```python
HEAVY_THINKING_PROVIDER = "google"
HEAVY_THINKING_API_KEY = "AIza..."
HEAVY_THINKING_MODEL = "gemini-2.5-flash"
# Base URL auto-set to: https://generativelanguage.googleapis.com/v1beta/openai/
```

### Configuration Example (Vertex AI - Advanced)

If you need to use Google Cloud Vertex AI instead:

```python
HEAVY_THINKING_PROVIDER = "custom"
HEAVY_THINKING_API_KEY = "your-gcp-key"
HEAVY_THINKING_BASE_URL = "https://YOUR-REGION-aiplatform.googleapis.com/v1/openai"
HEAVY_THINKING_MODEL = "gemini-2.5-flash"
```

### Model Selection Guide

**For most use cases**: `gemini-2.5-flash`
- Very fast
- Often has free tier
- Great quality

**For production**: `gemini-1.5-flash`
- Stable version
- Reliable performance

**For best quality**: `gemini-2.5-pro`
- Advanced reasoning and thinking
- Higher quality, more expensive

### Free Tier

Google AI Studio often provides generous free quotas:
- Check https://ai.google.dev/ for current limits
- Great for testing and personal use

---

## Custom / Self-Hosted

For custom OpenAI-compatible APIs (LM Studio, Ollama, vLLM, etc.)

### Configuration

```python
HEAVY_THINKING_PROVIDER = "custom"
HEAVY_THINKING_API_KEY = "your-api-key"  # or "dummy" if not required
HEAVY_THINKING_BASE_URL = "http://localhost:1234/v1"  # Your API endpoint
HEAVY_THINKING_MODEL = "your-model-name"  # Whatever your API expects
```

### Popular Self-Hosted Solutions

#### LM Studio
```python
HEAVY_THINKING_BASE_URL = "http://localhost:1234/v1"
HEAVY_THINKING_MODEL = "llama-3.1-70b-instruct"  # Whatever model you loaded
```

#### Ollama
```python
HEAVY_THINKING_BASE_URL = "http://localhost:11434/v1"
HEAVY_THINKING_MODEL = "llama3.1:70b"
```

#### vLLM
```python
HEAVY_THINKING_BASE_URL = "http://localhost:8000/v1"
HEAVY_THINKING_MODEL = "meta-llama/Llama-3.1-70B-Instruct"
```

#### text-generation-webui
```python
HEAVY_THINKING_BASE_URL = "http://localhost:5000/v1"
HEAVY_THINKING_MODEL = "model-name"  # Check your installation
```

---

## Model Switching Examples

You can easily switch models to find the best balance for your use case:

### Example 1: Start Cheap, Scale Up

**Phase 1 - Testing**:
```
HEAVY_THINKING_MODEL = "google/gemini-flash-1.5"  # Free tier testing
```

**Phase 2 - Production**:
```
HEAVY_THINKING_MODEL = "anthropic/claude-3.5-haiku"  # Fast & affordable
```

**Phase 3 - Critical Queries**:
```
HEAVY_THINKING_MODEL = "anthropic/claude-3.5-sonnet"  # Best quality
```

### Example 2: Multi-Provider Setup

Keep multiple configurations for different scenarios:

**For quick research**:
```
Provider: openrouter
Model: google/gemini-flash-1.5
Agents: 2
```

**For important work**:
```
Provider: anthropic
Model: claude-3-5-sonnet-20241022
Agents: 4
```

**For critical decisions**:
```
Provider: openai
Model: gpt-4o
Agents: 6
```

---

## Cost Optimization Tips

### 1. Start with Cheap Models
Test with free/cheap models first:
- `google/gemini-flash-1.5` (often free)
- `anthropic/claude-3.5-haiku` (very cheap)
- `openai/gpt-4o-mini` (affordable)

### 2. Use Different Models for Different Agents

Some APIs let you specify per-request models. Future versions of this tool could support:
- Question generation: cheap model
- Main agents: balanced model  
- Synthesis: premium model

### 3. Reduce Agents for Simple Queries
- 2 agents: Simple questions
- 4 agents: Standard queries (recommended)
- 6-8 agents: Complex analysis only

### 4. Monitor Your Usage

Check your API provider's dashboard regularly:
- OpenRouter: https://openrouter.ai/activity
- OpenAI: https://platform.openai.com/usage
- Anthropic: https://console.anthropic.com/
- Google: https://console.cloud.google.com/

---

## Troubleshooting Model Names

### Error: "Model not found"

**Solutions**:
1. Check the exact model name at your provider's docs
2. Verify you have access to that model
3. Try a different model from the same provider

### Error: "Invalid model format"

**Solutions**:
1. OpenRouter requires `provider/model` format
2. Direct APIs use simple names
3. Check if `models/` prefix is needed (Google)

### Error: "Insufficient quota"

**Solutions**:
1. Add credits to your account
2. Switch to a model with free tier
3. Use a different provider

### Testing Model Names

Use this curl command to test if a model name works:

**OpenRouter**:
```bash
curl https://openrouter.ai/api/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -d '{
    "model": "anthropic/claude-3.5-haiku",
    "messages": [{"role": "user", "content": "test"}]
  }'
```

**OpenAI**:
```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": "test"}]
  }'
```

**Google**:
```bash
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key=$GOOGLE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contents":[{"parts":[{"text":"test"}]}]}'
```

---

## Recommended Configurations by Use Case

### For Students (Free/Cheap)
```
Provider: google
Model: models/gemini-2.0-flash-exp
Agents: 2-3
Cost: ~$0 (free tier)
```

### For Developers (Balanced)
```
Provider: openrouter
Model: anthropic/claude-3.5-haiku
Agents: 4
Cost: ~$0.01-0.02 per query
```

### For Businesses (Quality)
```
Provider: anthropic
Model: claude-3-5-sonnet-20241022
Agents: 4-6
Cost: ~$0.15-0.30 per query
```

### For Research (Premium)
```
Provider: openai
Model: gpt-4o
Agents: 6-8
Cost: ~$0.50-1.00 per query
```

---

**Need help choosing a model?** 

1. Start with `anthropic/claude-3.5-haiku` via OpenRouter (great balance)
2. If too expensive, try `google/gemini-flash-1.5` (often free)
3. If need better quality, upgrade to `anthropic/claude-3.5-sonnet`
4. For critical work, use `openai/gpt-4o` or `claude-3-opus`

The model name goes in the `HEAVY_THINKING_MODEL` valve setting in Open WebUI!
