# Installation Guide - Heavy Thinking Tool for Open WebUI

This guide will walk you through installing and configuring the Heavy Thinking tool for Open WebUI.

## Prerequisites

- [Open WebUI](https://github.com/open-webui/open-webui) installed and running
- Admin access to Open WebUI
- API key for at least one supported provider:
  - [OpenRouter](https://openrouter.ai/) (recommended)
  - [OpenAI](https://platform.openai.com/)
  - [Anthropic](https://www.anthropic.com/)
  - [Google AI Studio](https://ai.google.dev/)
  - Or any OpenAI-compatible API

## Installation Methods

### Method 1: Direct File Installation (Recommended)

1. **Download the tool file**
   ```bash
   wget https://raw.githubusercontent.com/YOUR_USERNAME/heavy-thinking-tool-owui/main/heavy_thinking.py
   ```

2. **Copy to Open WebUI tools directory**
   
   The location depends on your Open WebUI installation:

   - **Docker installation**:
     ```bash
     docker cp heavy_thinking.py open-webui:/app/backend/data/tools/
     ```

   - **Python installation**:
     ```bash
     cp heavy_thinking.py /path/to/open-webui/backend/data/tools/
     ```

   - **Manual via UI** (easiest):
     - Open Open WebUI admin panel
     - Navigate to `Workspace` → `Tools`
     - Click `+ Add Tool`
     - Paste the contents of `heavy_thinking.py`
     - Click `Save`

3. **Restart Open WebUI** (if using Docker/Python installation)
   ```bash
   docker restart open-webui
   # or
   systemctl restart open-webui
   ```

### Method 2: Git Clone

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/heavy-thinking-tool-owui.git
   cd heavy-thinking-tool-owui
   ```

2. **Copy to Open WebUI**
   ```bash
   cp heavy_thinking.py /path/to/open-webui/backend/data/tools/
   ```

3. **Restart Open WebUI**

### Method 3: Copy-Paste via Web UI

1. Open the [heavy_thinking.py](./heavy_thinking.py) file
2. Copy all contents
3. In Open WebUI:
   - Go to Admin Panel → Workspace → Tools
   - Click `+ Add Tool`
   - Paste the entire code
   - Give it a name: "Heavy Thinking"
   - Click Save

## Configuration

After installation, configure the tool valves:

### Step 1: Access Tool Settings

1. Go to Open WebUI
2. Open any chat
3. Click the `+` icon or tools menu
4. Find "Heavy Thinking" tool
5. Click settings/configuration icon

### Step 2: Configure Provider

Choose your API provider and configure accordingly:

#### Option A: OpenRouter (Recommended for multi-model access)

```
Provider: openrouter
API Key: sk-or-v1-YOUR_KEY_HERE
Base URL: https://openrouter.ai/api/v1
Model: openai/gpt-4o-mini
```

**Getting an OpenRouter API Key:**
1. Visit https://openrouter.ai/
2. Sign up/Login
3. Go to Keys section
4. Create a new API key
5. Add credits to your account

**Popular OpenRouter Models:**
- `openai/gpt-4o-mini` (cheap, fast)
- `openai/gpt-4o` (high quality)
- `anthropic/claude-3.5-sonnet` (best reasoning)
- `google/gemini-2.0-flash-exp` (fast, free tier)
- `meta-llama/llama-3.1-70b-instruct` (open source)

#### Option B: OpenAI

```
Provider: openai
API Key: sk-YOUR_OPENAI_KEY
Model: gpt-4o-mini
```

**Getting an OpenAI API Key:**
1. Visit https://platform.openai.com/
2. Sign up/Login
3. Go to API Keys
4. Create new secret key

#### Option C: Anthropic

```
Provider: anthropic
API Key: sk-ant-YOUR_KEY
Model: claude-3-5-sonnet-20241022
```

**Getting an Anthropic API Key:**
1. Visit https://www.anthropic.com/
2. Sign up for Claude API access
3. Create API key in console

#### Option D: Google Gemini

```
Provider: google
API Key: YOUR_GOOGLE_AI_KEY
Model: gemini-2.0-flash-exp
```

**Getting a Google AI API Key:**
1. Visit https://ai.google.dev/
2. Sign in with Google account
3. Get API key from AI Studio

#### Option E: Custom OpenAI-Compatible API

```
Provider: custom
API Key: your-custom-key
Base URL: https://your-api.example.com/v1
Model: your-model-name
```

### Step 3: Configure Performance Settings

Adjust these based on your needs:

**For Quick Tests (Cheap & Fast)**
```
Number of Agents: 2
Timeout: 60
Model: gpt-4o-mini (or gemini-flash)
```

**For Production Use (Balanced)**
```
Number of Agents: 4
Timeout: 180
Model: gpt-4o-mini
```

**For Maximum Quality (Expensive)**
```
Number of Agents: 6-8
Timeout: 300
Model: claude-3.5-sonnet or gpt-4o
```

### Step 4: Set Environment Variables (Optional)

Instead of entering API keys in the UI, you can set environment variables:

**Docker**:
```bash
docker run -d \
  -e OPENROUTER_API_KEY="sk-or-v1-..." \
  -e OPENAI_API_KEY="sk-..." \
  -e ANTHROPIC_API_KEY="sk-ant-..." \
  ...
  open-webui
```

**Docker Compose**:
```yaml
services:
  open-webui:
    environment:
      - OPENROUTER_API_KEY=sk-or-v1-...
      - OPENAI_API_KEY=sk-...
      - ANTHROPIC_API_KEY=sk-ant-...
```

**System Environment**:
```bash
export OPENROUTER_API_KEY="sk-or-v1-..."
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."
```

## Verification

Test the installation:

1. **Open a chat in Open WebUI**

2. **Try a simple query**:
   ```
   Use heavy thinking to explain: What is quantum computing?
   ```

3. **Watch for status updates**:
   - "🧠 Generating research questions..."
   - "🔄 Deploying thinking agents..."
   - "✅ Agent 1/4 completed"
   - "✅ Agent 2/4 completed"
   - etc.

4. **Verify response quality**:
   - Should be comprehensive
   - Multiple perspectives
   - Well-structured
   - Synthesized into coherent answer

## Troubleshooting

### Tool doesn't appear in Open WebUI

**Solutions**:
1. Restart Open WebUI completely
2. Check file permissions on `heavy_thinking.py`
3. Check Open WebUI logs for errors
4. Verify file is in correct tools directory

### "API key not configured" error

**Solutions**:
1. Double-check API key is correctly entered
2. Verify provider name is lowercase: `openrouter`, `openai`, etc.
3. Try setting via environment variable
4. Check API key is valid and has credits

### "All thinking agents failed"

**Solutions**:
1. Verify model name is correct for your provider
2. Check API key has sufficient credits
3. Test API key works with a simple curl:
   ```bash
   curl https://openrouter.ai/api/v1/chat/completions \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer $OPENROUTER_API_KEY" \
     -d '{
       "model": "openai/gpt-4o-mini",
       "messages": [{"role": "user", "content": "test"}]
     }'
   ```

### Timeout errors

**Solutions**:
1. Increase `HEAVY_THINKING_TIMEOUT` setting
2. Reduce number of agents
3. Use faster model
4. Check internet connection speed

### High costs

**Solutions**:
1. Reduce number of agents (try 2-3)
2. Use cheaper models (gpt-4o-mini instead of gpt-4o)
3. Use providers with free tiers (Google Gemini Flash)
4. Set usage limits in your API provider dashboard

## Next Steps

- Read [README.md](./README.md) for usage examples
- Check [EXAMPLES.md](./EXAMPLES.md) for advanced use cases
- Join the discussion on GitHub Issues
- Contribute improvements!

## Support

- **GitHub Issues**: Report bugs or request features
- **Open WebUI Discord**: General Open WebUI help
- **Provider Documentation**: API-specific issues

## Updates

To update the tool:

1. **Download latest version**:
   ```bash
   wget https://raw.githubusercontent.com/YOUR_USERNAME/heavy-thinking-tool-owui/main/heavy_thinking.py
   ```

2. **Replace existing file**

3. **Restart Open WebUI**

4. **Test with a simple query**

---

**Installation complete!** 🎉

You're now ready to use heavy thinking mode in Open WebUI. Try asking complex questions and watch multiple AI agents work together to provide comprehensive answers!
