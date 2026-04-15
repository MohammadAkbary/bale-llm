#!/usr/bin/env python3
"""
اسکریپت راه‌اندازی برای تست محلی
"""

import os
import sys
from pathlib import Path

def check_env_file():
    """بررسی وجود فایل .env"""
    if not Path('.env').exists():
        print("❌ فایل .env وجود ندارد!")
        print("💡 لطفاً فایل .env.example را کپی کن و به .env تغیر نام بده")
        return False
    return True

def check_python_version():
    """بررسی نسخه Python"""
    if sys.version_info < (3, 8):
        print(f"❌ نسخه Python {sys.version_info.major}.{sys.version_info.minor} کافی نیست")
        print("💡 لطفاً Python 3.8 یا بالاتر را نصب کن")
        return False
    return True

def check_requirements():
    """بررسی نصب requirements"""
    try:
        import flask
        import requests
        print("✅ تمام وابستگی‌ها نصب شده‌اند")
        return True
    except ImportError as e:
        print(f"❌ {e} نصب نشده")
        print("💡 دستور 'pip install -r requirements.txt' را اجرا کن")
        return False

def main():
    print("=" * 50)
    print("🔍 بررسی تنظیمات Bale LLM Bot...")
    print("=" * 50)
    
    checks = [
        ("Python Version", check_python_version()),
        ("Environment File", check_env_file()),
        ("Requirements", check_requirements()),
    ]
    
    all_passed = all(check[1] for check in checks)
    
    print("\n" + "=" * 50)
    if all_passed:
        print("✅ تمام بررسی‌ها موفق!")
        print("🚀 می‌توانید 'python main.py' را اجرا کنید")
    else:
        print("❌ برخی بررسی‌ها ناموفق بود")
        print("💡 لطفاً مشکل‌ها را حل کن")
        sys.exit(1)
    print("=" * 50)

if __name__ == '__main__':
    main()
