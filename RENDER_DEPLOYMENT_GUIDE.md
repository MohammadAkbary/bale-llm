# 🚀 Complete Render Deployment Guide

> Deploy Bale LLM Bot on Render in 5 minutes - **Completely FREE!**

<div align="center">
  <img src="https://img.shields.io/badge/Platform-Render-46E3B7?style=for-the-badge&logo=render" alt="Render">
  <img src="https://img.shields.io/badge/Cost-Free-green?style=for-the-badge" alt="Free">
  <img src="https://img.shields.io/badge/Setup%20Time-5%20mins-blue?style=for-the-badge" alt="5 mins">
  <img src="https://img.shields.io/badge/Python-3.11+-3776ab?style=for-the-badge&logo=python" alt="Python">
</div>

---

## 📖 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Step 1: Prepare Your Code](#step-1-prepare-your-code)
3. [Step 2: Create Render Account](#step-2-create-render-account)
4. [Step 3: Deploy on Render](#step-3-deploy-on-render)
5. [Step 4: Configure Bale Webhook](#step-4-configure-bale-webhook)
6. [Step 5: Setup Keep-Alive](#step-5-setup-keep-alive)
7. [Step 6: Verify Deployment](#step-6-verify-deployment)
8. [Maintenance & Monitoring](#maintenance--monitoring)
9. [Troubleshooting](#troubleshooting)
10. [Security Best Practices](#security-best-practices)

---

## 📋 Prerequisites

Before you start, make sure you have:

| Item | Status | Notes |
|------|--------|-------|
| ✅ Git | Required | [Download](https://git-scm.com) |
| ✅ GitHub Account | Required | [Create Free Account](https://github.com/signup) |
| ✅ Bale Bot Token | Required | From [@BaleBot](https://bale.ai) |
| ✅ AI API Key | Required | Google, Hugging Face, or DeepSeek (all FREE) |
| ✅ User ID | Required | From [@userinfobot in Bale](https://bale.ai) |
| ✅ Render Account | Required | [Create Free Account](https://render.com) |

### Get Your Required Credentials

#### 🤖 **Bale Bot Token** (5 mins)
1. Open Bale app or go to [bale.ai](https://bale.ai)
2. Search for **@BaleBot** or **@BotFather**
3. Send `/newbot` command
4. Follow the instructions and save your token

#### 🔑 **AI API Keys** (Choose ONE - All Free!)

**Option 1: Google Gemini (⭐ Recommended)**
- Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
- Click "Get API Key"
- Create a new key
- Copy and save it

**Option 2: Hugging Face**
- Sign up at [huggingface.co](https://huggingface.co)
- Create API token in Settings → Access Tokens
- Use as `HUGGINGFACE_API_KEY`

**Option 3: DeepSeek**
- Go to [DeepSeek Platform](https://platform.deepseek.com)
- Create API key
- Use as `DEEPSEEK_API_KEY`

#### 👤 **Your Bale User ID** (2 mins)
1. Open Bale app
2. Search for **@userinfobot**
3. Send any message
4. It will show your `me.id` - copy this number

---

## Step 1: Prepare Your Code

### 1.1 Create GitHub Repository

1. Go to [GitHub.com](https://github.com)
2. Click **"+"** → **"New repository"**
3. Fill in details:
   ```
   Repository name: bale-llm-bot
   Description: AI-powered Bale messenger bot
   Visibility: Public
   ```
4. Click **"Create repository"**
3. Name it `bale-llm` (or any name you prefer)
4. Choose **Public** (for easy deployment)
5. Click **Create repository**

### Step 2: Clone Locally

```bash
cd your-projects-folder
git clone https://github.com/MohammadAkbary/bale-llm.git
cd bale-llm
```

### Step 3: Add Your Repository as Remote

```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/bale-llm.git
git branch -M main
```

### Step 4: Create `.env.example`

This is required for Render to know what environment variables are needed:

```bash
# Create file named .env.example
```

Add this content to `.env.example`:

```env
# Bale Bot Configuration
BALE_BOT_TOKEN=your_token_here
BALE_API_URL=https://api.bale.ai
PORT=10000

# AI Provider Keys (choose at least one)
GOOGLE_API_KEY=your_key_here
HUGGINGFACE_API_KEY=your_key_here
DEEPSEEK_API_KEY=your_key_here

# Optional
FLASK_DEBUG=False
```

### Step 5: Verify Procfile

Ensure `Procfile` exists with:

```
web: gunicorn main:app
```

### Step 6: Verify render.yaml

Ensure `render.yaml` contains:

```yaml
services:
  - type: web
    name: bale-llm-bot
    env: python
    startCommand: gunicorn main:app
    buildCommand: pip install -r requirements.txt
    plan: free
    envVars:
      - key: PYTHON_VERSION
        value: 3.11
```

### Step 7: Push to GitHub

```bash
git add .
git commit -m "Initial commit - Ready for Render deployment"
git push origin main
```

---

## 🔐 Create Render Account

### Step 1: Sign Up

1. Visit [render.com](https://render.com)
2. Click **Sign up**
3. Choose **Sign up with GitHub**
4. Grant permissions to GitHub
5. Accept terms and verify email

### Step 2: Authorize GitHub

1. In Render dashboard, go to **Dashboard**
2. Click **New +** icon
3. Select **Web Service**
4. Click **Connect a repository**
5. Search for `bale-llm` repository
6. Click **Connect**

---

## 🎯 Deploy on Render

### Step 1: Create Web Service

1. In Render dashboard, click **New + → Web Service**
2. Select your `bale-llm` repository
3. Click **Connect**

### Step 2: Configure Service

Fill in the configuration form:

| Field | Value | Notes |
|-------|-------|-------|
| **Name** | `bale-llm-bot` | Must be unique |
| **Environment** | `Python` | Select from dropdown |
| **Region** | Your nearest | Reduces latency |
| **Runtime** | `Python 3.11` | Latest stable |
| **Build Command** | `pip install -r requirements.txt` | Auto-detected |
| **Start Command** | `gunicorn main:app` | Important! |
| **Plan** | **Free** or **Starter** | Free is fine |

### Step 3: Add Environment Variables

⚠️ **IMPORTANT**: Don't commit `.env` file to GitHub!

1. Scroll down to **Environment**
2. Click **Add Environment Variable**
3. Add each variable:

```
BALE_BOT_TOKEN = your_bot_token_here
DEEPSEEK_API_KEY = your_deepseek_key (recommended)
```

Or:

```
BALE_BOT_TOKEN = your_bot_token_here
GOOGLE_API_KEY = your_google_key
```

Or:

```
BALE_BOT_TOKEN = your_bot_token_here
HUGGINGFACE_API_KEY = your_huggingface_key
```

### Step 4: Advanced Settings (Optional)

Leave defaults unless you know what you're doing:

- **Auto-Deploy**: Toggle ON (recommended)
- **Notification Email**: Your email
- **Docker Command**: Leave blank

### Step 5: Deploy

1. Click **Create Web Service**
2. Watch the deployment logs scroll by
3. Wait for **"Live"** status (usually 2-5 minutes)

**That's it!** Your bot is now deployed! 🎉

---

## 🔌 Configure Bale Webhook

After deployment completes, configure the webhook:

### Step 1: Get Your URL

1. In Render dashboard, go to your service
2. Look for **URL** near the top
3. It should be: `https://bale-llm-bot.onrender.com`

### Step 2: Open Bale Bot Settings

1. Open Bale messenger
2. Contact your bot
3. Send `/admin` command
4. Navigate to **Settings**

### Step 3: Add Webhook URL

In Bale bot settings, set webhook to:

```
https://bale-llm-bot.onrender.com/webhook
```

(Replace `bale-llm-bot` with your actual service name)

### Step 4: Verify Connection

Send a test message to your bot. You should get a response within seconds! ✅

---

## ✅ Verify Deployment

### Test 1: Check Service Status

```bash
curl -I https://your-service.onrender.com
# Should return 200 or 302
```

### Test 2: Test Webhook

```bash
curl -X POST https://your-service.onrender.com/webhook \
  -H "Content-Type: application/json" \
  -d '{"test": "data"}'
```

### Test 3: Send Message

1. Open Bale messenger
2. Send a message to your bot
3. Wait for response
4. If no response, check logs

### Check Deployment Logs

1. In Render dashboard, click your service
2. Go to **Logs** tab
3. Look for errors or warnings
4. Common issues:
   - `ModuleNotFoundError`: Missing dependency in `requirements.txt`
   - `BALE_BOT_TOKEN is required`: Missing environment variable
   - `Connection refused`: Application not listening on correct port

---

## 📊 Maintenance & Monitoring

### Monitor Service Health

1. **Dashboard View**: Shows uptime and memory usage
2. **Logs**: Real-time application logs
3. **Metrics**: CPU, memory, and network usage

### View Logs

```
Render Dashboard → Your Service → Logs
```

### Redeploy (If Code Changed)

```bash
git add .
git commit -m "Update code"
git push origin main
```

**Automatic redeploy** happens if you enabled Auto-Deploy ✅

### Manual Redeploy

1. Go to your service
2. Click **Manual Deploy → Deploy latest commit**

### Scale Service (Paid)

- **Free Plan**: One shared instance (~512MB RAM)
- **Starter Plan**: 0.5 CPU, 512MB RAM ($12/month)
- **Standard Plan**: 1 CPU, 2GB RAM ($40/month)

---

## 🐛 Troubleshooting

### Problem: "Build Failed"

**Symptoms**: Deployment fails at build step

**Solutions**:
1. Check `requirements.txt` syntax
2. Ensure all dependencies are available on PyPI
3. Check Python version compatibility
4. View build logs in Render dashboard

```bash
# Test locally
pip install -r requirements.txt
```

### Problem: "Internal Server Error" (500)

**Symptoms**: Bot doesn't respond

**Solutions**:
1. Check environment variables are set
2. Verify `BALE_BOT_TOKEN` is correct
3. Check application logs:
   ```
   Render → Logs tab
   ```
4. Re-setup admin:
   ```bash
   python setup_admin.py
   ```

### Problem: "Connection Refused" (Connection failed)

**Symptoms**: Can't reach the webhook

**Solutions**:
1. Verify URL in Bale bot settings
2. Check service is running (status should be "Live")
3. Wait 30 seconds after deployment
4. Try pinging the service:
   ```
   curl https://your-service.onrender.com
   ```

### Problem: "Invalid API Key"

**Symptoms**: `Authentication failed` errors

**Solutions**:
1. Verify key format (check for extra spaces)
2. Regenerate key from provider dashboard
3. Ensure key isn't expired
4. Use correct key for correct provider

### Problem: Environment Variables Not Loading

**Solutions**:
1. Redeploy after adding variables
2. Check variable names are exact (case-sensitive)
3. Remove leading/trailing spaces
4. Verify in logs that variables are loaded

**Command to verify**:
```bash
# In Render shell
echo $BALE_BOT_TOKEN
```

### Free Tier Limitations

**Render Free Tier**:
- ❌ Spins down after 15 minutes of inactivity
- ❌ ~1GB total storage
- ✅ No cost
- ✅ Good for testing

**Workaround**: Upgrade to Starter Plan ($1-12/month)

---

## 🔧 Advanced Configuration

### Custom Domain

1. Get a free domain from [Freenom](https://www.freenom.com)
2. In Render dashboard: **Settings → Custom Domains**
3. Add your domain
4. Configure DNS records

### Health Checks

Render can monitor your service:

1. Go to **Settings**
2. Enable **HTTP Health Check**
3. Path: `/` (or your health endpoint)
4. Interval: 5 minutes

### Automatic Scaling

Not available on free tier, but:
- Starter ($12/month) and above get scaling

### Persistent Data

Use environment variables or cloud database:

- **SQLite** (local, not persistent)
- **PostgreSQL** (Render offers add-on)
- **MongoDB** (Atlas has free tier)

### Environment Variables Security

**Best Practices**:
- ❌ Never commit `.env` to Git
- ✅ Use Render's built-in secrets
- ✅ Use different keys for different environments
- ✅ Rotate keys periodically

### Performance Optimization

```python
# In Flask config
SEND_FILE_MAX_AGE_DEFAULT = 31536000
```

---

## ❓ FAQ

### Q: Can I use the free tier?
**A**: Yes! Free tier is perfect for testing and development.

### Q: Will my bot go to sleep?
**A**: Yes, after 15 minutes of inactivity on free tier. Upgrade to prevent this.

### Q: How do I update my bot?
**A**: Just push to GitHub, and Render redeploys automatically.

### Q: Where are logs stored?
**A**: In Render dashboard → Logs tab. They persist for 1 hour.

### Q: Can I run background jobs?
**A**: Yes, but need to implement cron jobs or scheduled tasks.

### Q: How much does it cost?
**A**: 
- **Free**: $0 (with limitations)
- **Starter**: $7/month
- **Standard**: $40/month

### Q: Can I use a database?
**A**: Yes, add PostgreSQL to your service (free tier available).

### Q: How do I monitor my bot?
**A**: 
- Render Dashboard
- Logs
- Email alerts
- Third-party monitoring (Sentry, DataDog)

### Q: What if deployment fails?
**A**: Check logs, fix errors, push to Git, redeploy.

---

## 🚀 Quick Commands Reference

```bash
# Test locally before deploying
python main.py

# Check syntax errors
python -m py_compile *.py

# Install dependencies
pip install -r requirements.txt

# Setup admin
python setup_admin.py

# Deploy to GitHub
git add .
git commit -m "New features"
git push origin main

# Check service URL
curl -I https://your-service.onrender.com

# View environment variables
# (in Render dashboard)
```

---

## 📞 Getting Help

- **Render Docs**: https://render.com/docs
- **Python Docs**: https://python.org
- **Flask Docs**: https://flask.palletsprojects.com
- **GitHub Discussions**: [Project Discussion]
- **Issues**: Report bugs on GitHub

---

## 🎯 Next Steps

After successful deployment:

1. ✅ Test bot responses
2. ✅ Configure admin account
3. ✅ Add AI API keys
4. ✅ Monitor logs regularly
5. ✅ Set up alerts for errors
6. ✅ Plan database backup strategy
7. ✅ Consider upgrading to paid tier

---

## 📝 Deployment Checklist

- [ ] `requirements.txt` updated
- [ ] `Procfile` exists and correct
- [ ] `.env.example` created
- [ ] `.gitignore` includes `.env`
- [ ] Code pushed to GitHub
- [ ] Render account created
- [ ] Service connected to GitHub
- [ ] Environment variables added
- [ ] Deployment completed successfully
- [ ] Webhook configured in Bale
- [ ] Bot responding to messages
- [ ] Logs checked for errors
- [ ] Monitoring enabled
- [ ] Documentation updated

---

<div align="center">
  <p><strong>🎉 Your bot is now live! Celebrate! 🎉</strong></p>
  <p>
    <a href="https://render.com">Render</a> •
    <a href="https://bale.ai">Bale</a> •
    <a href="README.md">Back to README</a>
  </p>
</div>

---

**Last Updated**: April 2026
**Version**: 1.0
**Status**: ✅ Production Ready
