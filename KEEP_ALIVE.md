# Keep-Alive Guide - Prevent Bot Sleeping on Render

## ⏰ مشکل: Render Suspension

Render suspends services that are inactive for **15 minutes**. This means if your bot doesn't receive any messages for 15 minutes, it will go to sleep and won't receive new messages.

### Why Web Hooks Need Keep-Alive

Webhooks only work if your service is running. When Render suspends it:

- ❌ Bot won't receive messages
- ❌ Bot won't respond to commands
- ❌ You'll get 503 Service Unavailable

## ✅ Solution: UptimeRobot Monitoring

The best free solution is using **UptimeRobot** to ping your bot every 10 minutes.

### Setup Steps

#### Step 1: Get Your Bot URL

```
https://your-app.onrender.com/ping
```

#### Step 2: Create UptimeRobot Monitor

1. Go to https://uptimerobot.com
2. Sign up (free account)
3. Click "Add New Monitor"
4. Select **HTTP(s)**

#### Step 3: Configure Monitor

```
Monitor Type:       HTTP(s)
URL:               https://your-app.onrender.com/ping
Interval:          Every 10 minutes
Email notifications: (optional)
```

#### Step 4: Activate

Click "Create Monitor" and you're done!

---

## 📊 How It Works

```
Time: 0 min → Bot running ✅
Time: 10 min → UptimeRobot pings /ping endpoint
Time: 15 min → (Would be suspended, but...)
              UptimeRobot pings again ✅
Time: 20 min → UptimeRobot pings again ✅
... (repeats every 10 mins)
```

The ping keeps Render from suspending your service!

---

## 🔄 Alternative Solutions

### Option 1: UptimeRobot (⭐ Recommended)

- **Cost**: Free
- **Reliability**: 99.9% uptime
- **Setup time**: 2 minutes
- **Limitations**: Free tier is limited to 50 monitors

### Option 2: cron-job.org

1. Go to https://cron-job.org
2. Create new cronjob
3. URL: `https://your-app.onrender.com/ping`
4. Interval: Every 10 minutes

- **Cost**: Free
- **Setup time**: 3 minutes

### Option 3: GitHub Actions

Create a workflow to ping your endpoint every 10 minutes

```yaml
name: Keep Alive
on:
  schedule:
    - cron: "*/10 * * * *"
jobs:
  ping:
    runs-on: ubuntu-latest
    steps:
      - name: Ping bot
        run: |
          curl https://your-app.onrender.com/ping
```

### Option 4: AWS Lambda + CloudWatch

Set up a Lambda function triggered every 10 minutes

- **Cost**: Free tier includes 1M requests/month
- **Setup time**: 15 minutes

---

## 🧪 Testing Keep-Alive

### Check if /ping endpoint works

```bash
curl https://your-app.onrender.com/ping
```

Expected response:

```json
{
  "status": "alive",
  "timestamp": "2026-04-15 15:30:45.123456"
}
```

### Monitor on Render Dashboard

1. Go to your Render service
2. Click "Logs"
3. You should see: `🔔 Ping received - Bot is alive!`
4. Every 10 minutes (if using UptimeRobot)

---

## ⚠️ Troubleshooting

### Bot Still Getting Suspended

1. ✅ Verify `/ping` endpoint is working
2. ✅ Check UptimeRobot is sending pings
3. ✅ Look at Render logs for `🔔 Ping received`
4. ✅ Make sure monitor interval is 10 minutes (not 60)

### UptimeRobot Not Working

- Check if URL is correct: `https://your-app.onrender.com/ping`
- Verify Render service is actually deployed
- Check Render logs for errors

### Still Having Issues?

1. Upgrade Render to paid plan ($7/month) for persistent services
2. Use multiple monitoring services as backup
3. Consider switching to dedicated hosting

---

## 💡 Pro Tips

### Tip 1: Monitor Multiple Endpoints

Set up monitors for:

- `/ping` - Keep-alive
- `/health` - Check bot health

### Tip 2: Get Notifications

Enable email notifications in UptimeRobot if bot goes down

### Tip 3: Combine Solutions

Use both UptimeRobot + cron-job.org for redundancy

### Tip 4: Log Activity

Check logs regularly:

```
Render Dashboard → Logs → Search for "Ping received"
```

---

## 📋 Quick Checklist

- [ ] Render service is deployed
- [ ] `/ping` endpoint is working
- [ ] UptimeRobot account created
- [ ] Monitor configured with 10-minute interval
- [ ] Monitor is "Up" (green status)
- [ ] Checked Render logs for pings
- [ ] Bot receives messages consistently

---

## 🚀 Expected Results

**Before Keep-Alive:**

- Bot works first 15 minutes ✅
- Bot sleeps after 15 minutes ❌
- User messages fail ❌

**After Keep-Alive:**

- Bot works 24/7 ✅
- User messages always delivered ✅
- No suspension ✅

---

## 📚 Related Documentation

- [Render Sleep Policy](https://render.com/docs/free)
- [UptimeRobot Docs](https://uptimerobot.com/support/)
- [Webhook Best Practices](https://en.wikipedia.org/wiki/Webhook)

---

## 📞 Still Need Help?

- Check `/health` endpoint for bot status
- Review Render logs for errors
- Test `/ping` manually with curl
- Create an issue on GitHub

**Your bot is now always awake! 🚀**
