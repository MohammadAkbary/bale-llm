# OpenAI ChatGPT Integration Guide

## 🤖 ChatGPT API Support

Bale LLM Bot now supports OpenAI's ChatGPT API for superior AI responses!

## ⚠️ Important: This is PAID

Unlike Google Gemini and Hugging Face (which are FREE), **OpenAI API requires payment**.

**Cost**: Approximately $0.0005 per request (~$0.30 for 1000 requests)

## 🚀 Quick Setup

### Step 1: Get OpenAI API Key
1. Go to https://platform.openai.com/api-keys
2. Sign up or log in to your account
3. Click "Create new secret key"
4. Copy the key

**⚠️ Important**: 
- Never share your API key
- Your account needs credit ($5 minimum recommended)
- Free trial accounts may have limited access

### Step 2: Add to .env File
```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Step 3: Install Package
```bash
pip install -r requirements.txt
```

The `openai` package is already in requirements.txt

### Step 4: Use in Bot
The bot will automatically use ChatGPT if the key is provided.

## 💰 Pricing

### OpenAI Models

| Model | Cost (per 1K tokens) |
|-------|----------------------|
| gpt-3.5-turbo | $0.0005 input, $0.0015 output |
| gpt-4 | $0.03 input, $0.06 output |
| gpt-4-turbo | $0.01 input, $0.03 output |

For average messages (~100 tokens each):
- **~1000 messages** = $0.50 - $1.50
- **~10000 messages** = $5.00 - $15.00

## 🎯 Quality Comparison

| AI Service | Quality | Speed | Cost | Best For |
|-----------|---------|-------|------|----------|
| Google Gemini | ⭐⭐⭐⭐⭐ | Fast | Free | Good balance |
| Hugging Face | ⭐⭐⭐⭐ | Medium | Free | Unlimited use |
| ChatGPT | ⭐⭐⭐⭐⭐ | Very Fast | Paid | Professional use |

## 🔧 Code Usage

### Automatic Selection
The bot works with any AI provider that has an API key:

```python
# If OPENAI_API_KEY is set, you can manually use it
response = await ai.get_response("Your message", use_service='openai')

# Or use the default (Google by default)
response = await ai.get_response("Your message")  # Uses Google Gemini
```

### Manual Configuration
To change default AI service, edit `main.py`:

```python
# Change this line in main.py (around line 60)
ai_response = asyncio.run(ai.get_response(user_message, 'google'))

# To use ChatGPT instead:
ai_response = asyncio.run(ai.get_response(user_message, 'openai'))
```

## ⚙️ Configuration

### Which Model to Use?

**gpt-3.5-turbo** (Recommended for bots):
- Good quality
- Fast responses
- Cheapest price
```python
model="gpt-3.5-turbo"
```

**gpt-4** (Best quality):
- Superior responses
- More expensive
- Better reasoning
```python
model="gpt-4"
```

### Temperature Setting

Lower temperature = More consistent
Higher temperature = More creative

```python
temperature=0.7  # Current setting (balanced)
temperature=0.0  # More consistent (best for bots)
temperature=1.0  # More creative
```

## 🧪 Testing ChatGPT

```bash
# Test if OpenAI API works
python -c "from openai import OpenAI; print('OpenAI installed!')"
```

## ❌ Troubleshooting

### Error: "API key not valid"
- Check if key is copied correctly
- Make sure `.env` file is in project root
- Restart the bot after changing `.env`

### Error: "Insufficient credit"
- Add credit to OpenAI account
- Go to https://platform.openai.com/account/billing/overview
- Add payment method

### Error: "Rate limit exceeded"
- Wait 60 seconds before next request
- Upgrade to higher tier on OpenAI

### Error: "Model not found"
- Check if you have access to the model
- Some models require higher tier

## 📊 Monitor Usage

To track your API usage:
1. Go to https://platform.openai.com/account/usage
2. See detailed breakdown by model
3. Set spending limits to avoid surprises

## 💡 Money-Saving Tips

### Tip 1: Use Cheaper Model
Use `gpt-3.5-turbo` instead of `gpt-4`
- ~10x cheaper
- Still very good quality

### Tip 2: Set Character Limit
Limit response length to save tokens:
```python
max_tokens=300  # Instead of 500
```

### Tip 3: Use Free Services First
Make Google Gemini/Hugging Face default:
```python
# Use free services, only fallback to ChatGPT
if not use_openai:
    use_service='google'
```

### Tip 4: Cache Responses
Store common responses to save API calls

## 🔄 Fallback Strategy

Recommended approach:
1. Try Google Gemini (free)
2. If fail, try Hugging Face (free)
3. If both fail, optionally try ChatGPT (paid)

```python
try:
    response = await ai.get_response(message, 'google')
    if "error" in response.lower() or len(response) < 10:
        response = await ai.get_response(message, 'huggingface')
except:
    response = "Sorry, all AI services are currently unavailable"
```

## 📚 OpenAI Documentation

- [API Reference](https://platform.openai.com/docs/api-reference)
- [Pricing](https://openai.com/pricing)
- [Usage Counter](https://platform.openai.com/account/usage)
- [API Keys](https://platform.openai.com/api-keys)

## ⚖️ Ethical Usage

- ✅ Use for legitimate purposes
- ✅ Respect rate limits
- ❌ Don't share API keys
- ❌ Don't use for spam
- ❌ Don't resell API access

## 🆘 Support

If you have issues:
1. Check OpenAI status: https://status.openai.com
2. Read OpenAI docs: https://platform.openai.com/docs
3. Check account: https://platform.openai.com/account

---

**Summary**: ChatGPT integration is optional and requires payment, but provides the best AI quality available.
