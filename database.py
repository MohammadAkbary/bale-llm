"""
مدیریت دیتابیس کاربران و مدیران
User and admin management database
"""

import json
import os
from typing import List, Dict, Optional
from datetime import datetime

DATABASE_FILE = 'bot_database.json'

class Database:
    """مدیریت دیتابیس محلی"""
    
    def __init__(self, db_file: str = DATABASE_FILE):
        self.db_file = db_file
        self.data = self._load_database()
    
    def _load_database(self) -> Dict:
        """بارگذاری دیتابیس"""
        if os.path.exists(self.db_file):
            try:
                with open(self.db_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"خطا در بارگذاری دیتابیس: {e}")
                return self._create_default_db()
        return self._create_default_db()
    
    def _create_default_db(self) -> Dict:
        """ایجاد دیتابیس پیش‌فرض"""
        return {
            'admins': [],
            'authorized_users': [],
            'blocked_users': [],
            'settings': {
                'require_approval': True,
                'auto_add_users': False
            }
        }
    
    def _save_database(self) -> bool:
        """ذخیره دیتابیس"""
        try:
            with open(self.db_file, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"خطا در ذخیره دیتابیس: {e}")
            return False
    
    # Admin Management
    def add_admin(self, user_id: str) -> bool:
        """اضافه کردن مدیر"""
        if user_id not in self.data['admins']:
            self.data['admins'].append(user_id)
            # مدیر خودکار کاربر مجاز هم می‌شود
            self.add_authorized_user(user_id)
            return self._save_database()
        return False
    
    def remove_admin(self, user_id: str) -> bool:
        """حذف مدیر"""
        if user_id in self.data['admins']:
            self.data['admins'].remove(user_id)
            return self._save_database()
        return False
    
    def is_admin(self, user_id: str) -> bool:
        """بررسی اینکه کاربر مدیر است یا خیر"""
        return str(user_id) in [str(uid) for uid in self.data['admins']]
    
    def get_admins(self) -> List[str]:
        """دریافت لیست مدیران"""
        return self.data['admins']
    
    # User Management
    def add_authorized_user(self, user_id: str) -> bool:
        """اضافه کردن کاربر مجاز"""
        if user_id not in self.data['authorized_users']:
            self.data['authorized_users'].append(user_id)
            return self._save_database()
        return False
    
    def remove_authorized_user(self, user_id: str) -> bool:
        """حذف کاربر مجاز"""
        if user_id in self.data['authorized_users']:
            self.data['authorized_users'].remove(user_id)
            return self._save_database()
        return False
    
    def is_authorized(self, user_id: str) -> bool:
        """بررسی اینکه کاربر مجاز است یا خیر"""
        user_id_str = str(user_id)
        return any(str(uid) == user_id_str for uid in self.data['authorized_users'])
    
    def get_authorized_users(self) -> List[str]:
        """دریافت لیست کاربران مجاز"""
        return self.data['authorized_users']
    
    # Block Management
    def block_user(self, user_id: str) -> bool:
        """مسدود کردن کاربر"""
        if user_id not in self.data['blocked_users']:
            self.data['blocked_users'].append(user_id)
            # حذف از کاربران مجاز
            self.remove_authorized_user(user_id)
            return self._save_database()
        return False
    
    def unblock_user(self, user_id: str) -> bool:
        """فرفع مسدودیت کاربر"""
        if user_id in self.data['blocked_users']:
            self.data['blocked_users'].remove(user_id)
            return self._save_database()
        return False
    
    def is_blocked(self, user_id: str) -> bool:
        """بررسی اینکه کاربر مسدود است یا خیر"""
        return str(user_id) in [str(uid) for uid in self.data['blocked_users']]
    
    # Settings
    def get_setting(self, key: str, default=None):
        """دریافت تنظیمات"""
        return self.data['settings'].get(key, default)
    
    def set_setting(self, key: str, value) -> bool:
        """تنظیم مقدار"""
        self.data['settings'][key] = value
        return self._save_database()
    
    def get_stats(self) -> Dict:
        """دریافت آمار"""
        return {
            'total_admins': len(self.data['admins']),
            'total_authorized_users': len(self.data['authorized_users']),
            'total_blocked_users': len(self.data['blocked_users']),
        }

# Initialize globally
db = Database()
