# DeepSeek API Integration

## 🚀 DeepSeek Support Added

DeepSeek is now integrated as a free AI provider. It's completely free and requires no credit card!

## 📋 Available AI Providers

| Provider | Free? | Quality | Speed | Link |
|----------|-------|---------|-------|------|
| Google Gemini | ✅ | ⭐⭐⭐⭐⭐ | Fast | [ai.google.dev](https://ai.google.dev) |
| Hugging Face | ✅ | ⭐⭐⭐⭐ | Medium | [huggingface.co](https://huggingface.co) |
| **DeepSeek** | ✅ | ⭐⭐⭐⭐⭐ | Fast | [deepseek.com](https://www.deepseek.com) |

## 🔑 Get DeepSeek API Key

### Step 1: Sign Up
1. Go to https://www.deepseek.com
2. Click "Sign Up" (or use your GitHub account)
3. Create a free account

### Step 2: Get API Key
1. Go to https://platform.deepseek.com/api_keys
2. Click "Create new API key"
3. Copy the key

### Step 3: Add to .env
```bash
DEEPSEEK_API_KEY=sk_live_xxxxxxxxxxxxxxxxxxxxx
```

## 💻 Usage

### In Python Code
```python
# Using DeepSeek
response = await ai_handler.get_response("Hello!", use_service='deepseek')

# Or use the default
response = await ai_handler.get_response("Hello!")  # Uses Google by default
```

### How the Bot Chooses AI Provider

The bot tries providers in this order:
1. **Google Gemini** (if GOOGLE_API_KEY is set)
2. **Hugging Face** (if HUGGINGFACE_API_KEY is set)
3. **DeepSeek** (if DEEPSEEK_API_KEY is set)

You can also specify which one to use:
```python
use_service='deepseek'     # Use DeepSeek
use_service='google'       # Use Google
use_service='huggingface'  # Use Hugging Face
```

## ✨ Features

- ✅ **Completely Free** - No credit card required
- ✅ **High Quality** - Advanced reasoning capabilities
- ✅ **Fast** - Quick response times
- ✅ **Reliable** - Good uptime
- ✅ **OpenAI Compatible** - Standard API format

## 📊 DeepSeek Model

DeepSeek uses **deepseek-chat** model which is:
- Latest generation AI model
- Great for general conversations
- Good for code generation
- Efficient token usage

## 🔄 API Format

DeepSeek uses OpenAI-compatible API format:

```python
payload = {
    "model": "deepseek-chat",
    "messages": [
        {
            "role": "user",
            "content": "Your message here"
        }
    ],
    "temperature": 0.7,      # Creativity (0-1)
    "max_tokens": 1000       # Response length limit
}
```

## 🧪 Testing DeepSeek

### Manual Test
```bash
python -m py_compile ai_handler.py  # Check syntax

# Or run the bot and send a message
python main.py
```

### Check API Key Works
```bash
curl -X POST "https://api.deepseek.com/chat/completions" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "Hello"}],
    "max_tokens": 100
  }'
```

## ⚠️ Important Notes

1. **API Key Security**: Never commit your API key to GitHub
2. **Rate Limits**: DeepSeek has rate limits on free tier
3. **Token Usage**: Each request uses tokens (part of your free quota)
4. **Backup Providers**: If DeepSeek fails, bot will try Google Gemini

## 🆓 Free Tier Details

- **Monthly Tokens**: Generous free allowance
- **RPM Limit**: Requests per minute (usually sufficient for bots)
- **No Credit Card**: Completely free to try

[More info on DeepSeek docs](https://docs.deepseek.com)

## 🐛 Troubleshooting

### "Invalid API Key" Error
```
Solution: Double-check your API key from https://platform.deepseek.com/api_keys
```

### "Rate limit exceeded" 
```
Solution: Wait a few minutes, or switch to Google Gemini
```

### "Connection timeout"
```
Solution: Check your internet connection
            Retry after a few seconds
```

## 📚 Updated Files

These files were updated to support DeepSeek:

- ✅ `requirements.txt` - Added openai library
- ✅ `.env.example` - Added DEEPSEEK_API_KEY
- ✅ `config.py` - Added DEEPSEEK_API_KEY config
- ✅ `ai_handler.py` - Added _get_deepseek_response method

## 🎯 Best Practices

1. **Use Multiple Providers**: Set keys for all three providers as backup
2. **Error Handling**: Bot automatically falls back if one provider fails
3. **Cost Monitoring**: All three are free, no cost concerns
4. **Performance**: Pick the fastest provider for your needs

## 💡 Pro Tips

1. **Test Different Providers**
   ```
   /help deepseek      # See if this works
   ```

2. **Monitor API Usage**
   - Check your DeepSeek dashboard for usage stats

3. **Combine Providers**
   - Use different providers for different use cases

---

**Enjoy free AI-powered responses! 🚀**
