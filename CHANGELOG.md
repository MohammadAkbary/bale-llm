# 📋 خلاصه ویژگی‌های اضافه‌شده

## ✨ نسخه جدید ربات Bale LLM

آپدیت شامل سیستم Admin، چند‌زبانی، و مدیریت کاربران است.

---

## 🎯 ویژگی‌های جدید

### 1️⃣ سیستم Admin و مدیریت دسترسی
- ✅ فقط Admin می‌تواند Admin اضافه/حذف کند
- ✅ Admin می‌تواند کاربران مجاز را مدیریت کند
- ✅ بلاک‌کردن کاربران ممکن است
- ✅ سطح‌های دسترسی: مسدود، غیر مجاز، مجاز، مدیر

دستورات:
```
/add_admin [ID]       # اضافه کردن مدیر
/add_user [ID]        # اضافه کردن کاربر مجاز
/remove_user [ID]     # حذف کاربر
/admin_list           # لیست مدیران
/user_list            # لیست کاربران
```

### 2️⃣ چند‌زبانی (Multi-Language)
- ✅ پشتیبانی فارسی و انگلیسی
- ✅ هر کاربر می‌تواند زبان خود را انتخاب کند
- ✅ تمام پیام‌ها بر اساس زبان کاربر نمایش داده می‌شود

دستور:
```
/lang fa  # فارسی
/lang en  # انگلیسی
```

### 3️⃣ دیتابیس محلی (Local Database)
- ✅ ذخیره Admin و کاربران
- ✅ تنظیمات سیستم
- ✅ بدون نیاز به دیتابیس خارجی

فایل: `bot_database.json`

---

## 📁 فایل‌های جدید ایجاد‌شده

| فایل | توضیح |
|------|-------|
| `database.py` | مدیریت دیتابیس و دسترسی‌ها |
| `i18n.py` | سیستم چند‌زبانی |
| `admin_manager.py` | پردازش دستورات مدیری |
| `setup_admin.py` | اسکریپت ایجاد Admin اولیه |
| `examples.py` | نمونه‌های استفاده |
| `API_REFERENCE.md` | مستندات API کامل |

---

## 🚀 نحوه استفاده

### الف. راه‌اندازی محلی

```bash
# 1. نصب وابستگی‌ها
pip install -r requirements.txt

# 2. تنظیم .env
cp .env.example .env
# توکن‌های خود را اضافه کنید

# 3. ایجاد Admin اولیه
python setup_admin.py

# 4. اجرا
python main.py
```

### ب. استقرار بر Render

```bash
# 1. Push کردن
git push origin main

# 2. در Render:
#    - New Web Service
#    - Repository انتخاب
#    - Environment variables اضافه
#    - Deploy
```

---

## 🔑 دستورات مهم

### کاربران عادی
```
/help    - راهنما
/start   - شروع
/lang    - تغییر زبان
```

### مدیران
```
/admin_list               - لیست مدیران
/add_admin [ID]          - اضافه کردن مدیر
/add_user [ID]           - اضافه کردن کاربر
/remove_user [ID]        - حذف کاربر
/user_list               - لیست کاربران
```

---

## 📊 ساختار دیتابیس

```json
{
  "admins": ["123456789"],
  "authorized_users": ["111222333"],
  "blocked_users": [],
  "settings": {
    "require_approval": true
  }
}
```

---

## 🌍 زبان‌ها

- ✅ **فارسی** (fa) - کامل پشتیبانی‌شده
- ✅ **انگلیسی** (en) - کامل پشتیبانی‌شده

---

## 📚 مستندات

- [README.md](README.md) - معرفی پروژه
- [setup_guide.md](setup_guide.md) - راهنمای کامل
- [API_REFERENCE.md](API_REFERENCE.md) - دستورات و API
- [examples.py](examples.py) - نمونه‌های استفاده

---

## ✅ تست

```bash
# چک کردن تنظیمات
python check_setup.py

# نمونه‌های استفاده
python examples.py
```

---

## 🎉 تمام!

ربات شما حالا:
- ✅ چندزبانی است
- ✅ سیستم admin دارد
- ✅ کاربران را با precision مدیریت می‌کند
- ✅ برای Render آماده است

**لطفاً Admin اولیه را ایجاد کنید:**
```bash
python setup_admin.py
```

سپس `python main.py` را اجرا کنید!

---

**نسخه**: 1.1.0\
**تاریخ**: April 15, 2026\
**وضعیت**: ✅ محصول والی
