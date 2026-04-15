"""
مدیریت دستورات مدیر و کاربران
Admin command management
"""

from database import db
from i18n import i18n
from typing import Tuple, Optional

class AdminManager:
    """مدیریت دستورات مدیر"""
    
    @staticmethod
    def process_command(user_id: str, message: str) -> Tuple[str, bool]:
        """
        پردازش دستورات مدیر
        
        Args:
            user_id: شناسه کاربر
            message: پیام/دستور
        
        Returns:
            (پاسخ، آیا دستور بود یا خیر)
        """
        message = message.strip()
        
        # دستورات عمومی
        if message == '/help':
            return (i18n.get_message('help', user_id), True)
        
        elif message == '/lang':
            current_lang = i18n.get_language(user_id)
            response = f"زبان فعلی: {current_lang}\nWritten at:\nفارسی: /lang fa\nEnglish: /lang en"
            return (response, True)
        
        elif message.startswith('/lang '):
            lang = message.split()[-1]
            if i18n.set_language(user_id, lang):
                return (i18n.get_message('lang_changed', user_id, lang='فارسی' if lang == 'fa' else 'English'), True)
            return (i18n.get_message('error', user_id), True)
        
        # دستورات مدیران
        if not db.is_admin(user_id):
            return ('', False)
        
        if message == '/admin_list':
            admins = db.get_admins()
            if not admins:
                return (i18n.get_message('admin_list_empty', user_id), True)
            admin_list = '\n'.join([f"• {admin}" for admin in admins])
            return (i18n.get_message('admin_list', user_id, admin_list), True)
        
        elif message == '/add_admin':
            return (i18n.get_message('enter_user_id', user_id), True)
        
        elif message.startswith('/add_admin '):
            new_admin_id = message.split()[-1]
            if not new_admin_id.isdigit():
                return (i18n.get_message('invalid_user_id', user_id), True)
            
            if db.add_admin(new_admin_id):
                return (i18n.get_message('admin_added', user_id, new_admin_id), True)
            return (i18n.get_message('user_already_added', user_id), True)
        
        elif message == '/add_user':
            return (i18n.get_message('enter_user_id', user_id), True)
        
        elif message.startswith('/add_user '):
            new_user_id = message.split()[-1]
            if not new_user_id.isdigit():
                return (i18n.get_message('invalid_user_id', user_id), True)
            
            if db.add_authorized_user(new_user_id):
                return (i18n.get_message('user_added', user_id, new_user_id), True)
            return (i18n.get_message('user_already_added', user_id), True)
        
        elif message == '/remove_user':
            return (i18n.get_message('enter_user_id', user_id), True)
        
        elif message.startswith('/remove_user '):
            target_user_id = message.split()[-1]
            if not target_user_id.isdigit():
                return (i18n.get_message('invalid_user_id', user_id), True)
            
            if db.remove_authorized_user(target_user_id):
                return (i18n.get_message('user_removed', user_id, target_user_id), True)
            return (i18n.get_message('user_not_found', user_id), True)
        
        elif message == '/user_list':
            users = db.get_authorized_users()
            if not users:
                return (i18n.get_message('user_list_empty', user_id), True)
            user_list = '\n'.join([f"• {user}" for user in users])
            return (i18n.get_message('user_list', user_id, user_list), True)
        
        elif message.startswith('/'):
            return (i18n.get_message('invalid_command', user_id), True)
        
        return ('', False)

# Initialize globally
admin_manager = AdminManager()
