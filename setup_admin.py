"""
اسکریپت ایجاد Admin اولیه
Initial admin setup script
"""

from database import db
import sys

def create_initial_admin():
    """ایجاد Admin اولیه"""
    print("=" * 50)
    print("🔐 ایجاد Admin اولیه برای ربات Bale LLM")
    print("=" * 50)
    
    # بررسی اینکه آیا Admin تعریف شده است
    if len(db.get_admins()) > 0:
        print("⚠️ Admin(s) قبلاً تعریف شده‌اند:")
        for admin in db.get_admins():
            print(f"   • {admin}")
        return
    
    print("\n💡 شناسه کاربر (User ID) خود را وارد کنید:")
    print("   (می‌توانید از @userinfobot در Bale آن را دریافت کنید)")
    print()
    
    user_id = input("User ID: ").strip()
    
    if not user_id.isdigit():
        print("❌ شناسه کاربر معتبر نیست")
        return
    
    try:
        if db.add_admin(user_id):
            print(f"\n✅ Admin با موفقیت ایجاد شد!")
            print(f"👤 Admin ID: {user_id}")
            print("\n📋 آمار:")
            stats = db.get_stats()
            for key, value in stats.items():
                print(f"   {key}: {value}")
        else:
            print("❌ خطایی رخ داد")
    except Exception as e:
        print(f"❌ خطا: {str(e)}")

if __name__ == '__main__':
    create_initial_admin()
