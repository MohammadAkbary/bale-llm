"""
مثال‌های استفاده ربات Bale LLM
Usage examples for Bale LLM Bot
"""

from database import db
from i18n import i18n

# =====================================================
# مثال 1: ایجاد Admin اولیه
# =====================================================
print("مثال 1: ایجاد Admin اولیه")
print("=" * 40)

# ایجاد Admin
admin_id = "123456789"
if db.add_admin(admin_id):
    print(f"✅ Admin ایجاد شد: {admin_id}")
else:
    print(f"⚠️ Admin قبلاً موجود بود")

print()

# =====================================================
# مثال 2: اضافه کردن کاربران مجاز
# =====================================================
print("مثال 2: اضافه کردن کاربران")
print("=" * 40)

users = ["111111111", "222222222", "333333333"]
for user_id in users:
    if db.add_authorized_user(user_id):
        print(f"✅ کاربر اضافه شد: {user_id}")
    else:
        print(f"⚠️ کاربر موجود است: {user_id}")

print()

# =====================================================
# مثال 3: بررسی سطح دسترسی
# =====================================================
print("مثال 3: بررسی دسترسی")
print("=" * 40)

test_user = "111111111"
print(f"کاربر: {test_user}")
print(f"  - Admin؟ {db.is_admin(test_user)}")
print(f"  - مجاز؟ {db.is_authorized(test_user)}")
print(f"  - مسدود؟ {db.is_blocked(test_user)}")

print()

# =====================================================
# مثال 4: مسدود کردن کاربر
# =====================================================
print("مثال 4: مسدود کردن و فرفع مسدودیت")
print("=" * 40)

block_user = "333333333"
if db.block_user(block_user):
    print(f"✅ کاربر مسدود شد: {block_user}")
    print(f"  - مسدود؟ {db.is_blocked(block_user)}")
    print(f"  - مجاز؟ {db.is_authorized(block_user)}")

print()

# =====================================================
# مثال 5: چند‌زبانی
# =====================================================
print("مثال 5: چند‌زبانی")
print("=" * 40)

user1 = "user_1"
user2 = "user_2"

# تنظیم زبان
i18n.set_language(user1, 'fa')
i18n.set_language(user2, 'en')

# نمایش پیام‌های مختلف
print(f"پیام برای {user1} (فارسی):")
print(f"  {i18n.get_message('welcome', user1)}")

print()
print(f"Message for {user2} (English):")
print(f"  {i18n.get_message('welcome', user2)}")

print()

# =====================================================
# مثال 6: دریافت آمار
# =====================================================
print("مثال 6: آمار سیستم")
print("=" * 40)

stats = db.get_stats()
for key, value in stats.items():
    print(f"  {key}: {value}")

print()

# =====================================================
# مثال 7: لیست کاملی
# =====================================================
print("مثال 7: لیست مدیران و کاربران")
print("=" * 40)

admins = db.get_admins()
users = db.get_authorized_users()

print(f"مدیران ({len(admins)}):")
for admin in admins:
    print(f"  • {admin}")

print()
print(f"کاربران مجاز ({len(users)}):")
for user in users:
    print(f"  • {user}")

print()
print("=" * 40)
print("✅ تمام مثال‌ها انجام شد!")
