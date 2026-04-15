# راهنمای راه‌اندازی ربات Bale LLM

## نیازمندی‌ها
- Python 3.8+
- حساب Bale Bot
- کلید API برای یکی از سرویس‌های AI رایگان

## مراحل راه‌اندازی محلی

### 1. Clone کردن پروژه
```bash
git clone https://github.com/yourusername/bale-llm.git
cd bale-llm
```

### 2. ایجاد Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. نصب وابستگی‌ها
```bash
pip install -r requirements.txt
```

### 4. تنظیم متغیرهای محیطی
```bash
# کپی کردن فایل نمونه
cp .env.example .env

# ویرایش فایل .env و اضافه کردن توکن‌های خود
```

### 5. اطلاعات مورد نیاز برای .env

#### برای Bale Bot:
1. به [@BaleBot](https://t.me/balebot) یا سایت رسمی بله مراجعه کنید
2. یک ربات جدید بسازید و توکن را کپی کنید

#### برای Google Gemini (رایگان):
1. به https://ai.google.dev بروید
2. دکمه "Get API Key" را کلیک کنید
3. کلید API را کپی کنید

#### برای Hugging Face (رایگان):
1. به https://huggingface.co بروید
2. ثبت‌نام کنید یا وارد شوید
3. در Settings > Access Tokens کلید جدید ایجاد کنید

### 6. اجرای محلی
```bash
python main.py
```

### ⚠️ مهم: تنظیم Admin اولیه
ربات نیاز به یک Admin اولیه دارد. پس از اولین اجرا:

```bash
python setup_admin.py
```

سپس شناسه کاربر خود را وارد کنید (می‌توانید از @userinfobot در Bale آن را دریافت کنید)

## استقرار بر روی Render

### 1. آماده‌سازی

```bash
git add .
git commit -m "Initial commit"
git push origin main
```

### 2. ایجاد سرویس روی Render
1. به https://render.com بروید
2. "New +" کلیک کنید و "Web Service" انتخاب کنید
3. Repository خود را انتخاب کنید
4. تنظیمات:
   - **Name**: bale-llm-bot
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn main:app`

### 3. تنظیم Environment Variables
1. در Render dashboard، به سرویس خود بروید
2. به "Environment" بروید
3. متغیرهای زیر را اضافه کنید:
   - `BALE_BOT_TOKEN`: توکن بله شما
   - `GOOGLE_API_KEY`: کلید Google Gemini
   - `HUGGINGFACE_API_KEY`: کلید Hugging Face
   - `PORT`: 8000

### 4. تنظیم Webhook
1. URL سرویس Render خود (شبیه: `https://your-app.onrender.com`) را کپی کنید
2. این URL را به عنوان Webhook در تنظیمات Bale Bot خود قرار دهید
3. Webhook باید به `/webhook` اشاره کند: `https://your-app.onrender.com/webhook`

### 5. ⏰ تنظیم Keep-Alive (مهم!)
Render سرویس‌های رایگان را بعد از 15 دقیقه inactivity suspend می‌کند.

**راه‌حل**: از UptimeRobot استفاده کنید:
1. به https://uptimerobot.com بروید
2. اکاونت رایگان بسازید
3. Add Monitor:
   - Type: HTTP(s)
   - URL: `https://your-app.onrender.com/ping`
   - Interval: Every 10 minutes

[📖 دستورالعمل کامل Keep-Alive](KEEP_ALIVE.md)

### 6. ایجاد Admin
برای ایجاد Admin در محیط Render:
```bash
# اگر از Shell استفاده می‌کنید (Render dashboard)
python setup_admin.py
```

یا دستی فایل `bot_database.json` را ویرایش کنید.

## ساختار فایل‌ها

```
bale-llm/
├── main.py              # 🎯 فایل اصلی برنامه
├── config.py            # ⚙️ تنظیمات
├── bale_handler.py      # 📨 مدیریت API Bale
├── ai_handler.py        # 🤖 مدیریت API های AI
├── database.py          # 💾 مدیریت دیتابیس (Admin, کاربران)
├── i18n.py              # 🌍 چند‌زبانی (فارسی، انگلیسی)
├── admin_manager.py     # 👨‍💼 مدیریت دستورات مدیر
├── setup_admin.py       # 🔧 تنظیم Admin اولیه
├── requirements.txt     # 📦 وابستگی‌های Python
├── .env.example         # 📄 نمونه متغیرهای محیطی
├── Procfile             # ☁️ برای استقرار
├── render.yaml          # 🎨 تنظیمات Render
├── render.json          # 📋 تنظیمات جایگزین Render
├── check_setup.py       # ✅ بررسی تنظیمات
├── .gitignore           # 🚫 فایل‌های نادیده
└── README.md            # 📖 مستندات
```

## دستورات مدیر (Admin Commands)

### دستورات عمومی
```bash
/help           # نمایش راهنما
/start          # شروع مجدد
/lang fa        # تغییر زبان به فارسی
/lang en        # تغییر زبان به انگلیسی
```

### دستورات مدیران (Admin Only)
```bash
/admin_list                    # نمایش لیست مدیران
/add_admin [USER_ID]           # اضافه کردن مدیر جدید
/add_user [USER_ID]            # اضافه کردن کاربر مجاز
/remove_user [USER_ID]         # حذف کاربر مجاز
/user_list                     # نمایش لیست کاربران مجاز
```

### مثال استفاده
```
/add_admin 123456789
/add_user 987654321
/remove_user 987654321
```

## چند‌زبانی (Multi-Language Support)

### زبان‌های پشتیبانی‌شده
- ✅ **فارسی** (Farsi/Persian) - کد: `fa`
- ✅ **انگلیسی** (English) - کد: `en`

### تغییر زبان
کاربران می‌توانند با دستور `/lang` زبان را تغییر دهند:
```bash
/lang fa  # برای فارسی
/lang en  # برای انگلیسی
```

**نکته**: تمام پیام‌ها (شامل پاسخ‌های AI و دستورات مدیر) بر اساس زبان انتخاب‌شده کاربر نمایش داده می‌شود.

## سیستم تأیید و دسترسی

### سطح‌های دسترسی
| سطح | علامت | توضیح |
|-----|-------|-------|
| مسدود (Blocked) | ❌ | کاربر قطعاً نمی‌تواند استفاده کند |
| بدون دسترسی | ❌ | کاربران غریب نمی‌توانند (پیش‌فرض) |
| کاربر مجاز | ✅ | کاربر می‌تواند از ربات استفاده کند |
| مدیر (Admin) | 👨‍💼 | دسترسی مدیریتی کامل |

### تنظیمات دسترسی

**پیش‌فرض**: فقط کاربران مجاز و مدیران می‌توانند استفاده کنند

```python
# در database.py
require_approval = True  # تأیید مورد نیاز است
```

برای اجازه به کاربران جدید:
```bash
/add_user [USER_ID]
```

### ریست کردن دسترسی‌ها
اگر دسترسی‌ها مختل شد:
1. فایل `bot_database.json` را حذف کنید
2. `python setup_admin.py` را دوباره اجرا کنید
3. Admin جدید را تنظیم کنید

## API های رایگان موجود

### Google Gemini
- **مزایا**: کیفیت خوب، تعداد درخواست‌های بیشتر
- **محدودیت**: تقریباً 60 درخواست در دقیقه
- **سایت**: https://ai.google.dev

### Hugging Face
- **مزایا**: مدل‌های متعدد و متنوع
- **محدودیت**: سرعت محدود در تیار رایگان
- **سایت**: https://huggingface.co

## مشکل‌زدایی

### مشکل: "BALE_BOT_TOKEN not found"
- توکن را در فایل `.env` بررسی کنید
- مطمئن شوید کپی‌پیست صحیح انجام شده

### مشکل: "API rate limit exceeded"
- صبر کنید و دوباره امتحان کنید
- مدل متفاوتی را امتحan کنید

### مشکل: "Connection timeout"
- اتصال اینترنت را بررسی کنید
- Firewall را بررسی کنید

## مراجع

- [Bale Bot Documentation](https://balebot.ir)
- [Google Generative AI](https://ai.google.dev)
- [Hugging Face](https://huggingface.co)
- [Render Documentation](https://render.com/docs)

## لایسنس

MIT

## نویسندگان

یوسرنیمی که پروژه را شروع کرد
