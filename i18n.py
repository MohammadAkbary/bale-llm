"""
مدیریت زبان‌های مختلف برای ربات
Multi-language support for the bot
"""

LANGUAGES = {
    'fa': 'فارسی',
    'en': 'English'
}

MESSAGES = {
    'fa': {
        # عمومی
        'welcome': 'سلام! من ربات هوشمند بله هستم 🤖\nچطور می‌تونم کمکت کنم؟',
        'help': '''
سلام👋 من می‌تونم:
✅ جواب از سوال‌های شما
✅ کمک در نوشتن و ترجمه
✅ توضیح مفاهیم پیچیده

دستورات مدیر:
/help - راهنمایی
/admin_list - لیست مدیران
/add_admin - اضافه کردن مدیر (فقط مدیر)
/add_user - اضافه کردن کاربر (فقط مدیر)
/remove_user - حذف کاربر (فقط مدیر)
/lang - تغییر زبان
''',
        'error': '❌ خطایی رخ داد',
        'unauthorized': '❌ شما دسترسی به این عملیات ندارید',
        'admin_only': '🔒 این دستور فقط برای مدیران است',
        'user_not_found': '❌ کاربر یافت نشد',
        'user_already_added': '⚠️ این کاربر قبلاً اضافه شده',
        'admin_added': '✅ مدیر جدید اضافه شد: {}',
        'user_added': '✅ کاربر جدید اضافه شد: {}',
        'user_removed': '✅ کاربر حذف شد: {}',
        'admin_list_empty': '📋 درحال حاضر مدیری وجود ندارد',
        'admin_list': '📋 لیست مدیران:\n{}',
        'user_list_empty': '📋 درحال حاضر کاربری وجود ندارد',
        'user_list': '📋 لیست کاربران مجاز:\n{}',
        'invalid_command': '❌ دستور نامشناخت. /help برای کمک',
        'lang_changed': '✅ زبان به {} تغییر کرد',
        'enter_user_id': 'لطفاً شناسه کاربر را وارد کنید:',
        'invalid_user_id': '❌ شناسه کاربر نامعتبر',
        'restricted': '❌ شما دسترسی به این ربات ندارید. لطفاً با مدیران تماس بگیرید',
        'processing': '⏳ درحال پردازش...',
    },
    'en': {
        # عمومی
        'welcome': 'Hello! I\'m an intelligent Bale bot 🤖\nHow can I help you?',
        'help': '''
Hi there 👋 I can:
✅ Answer your questions
✅ Help with writing and translation
✅ Explain complex concepts

Admin Commands:
/help - Get help
/admin_list - List admins
/add_admin - Add admin (admin only)
/add_user - Add user (admin only)
/remove_user - Remove user (admin only)
/lang - Change language
''',
        'error': '❌ An error occurred',
        'unauthorized': '❌ You do not have access to this operation',
        'admin_only': '🔒 This command is for admins only',
        'user_not_found': '❌ User not found',
        'user_already_added': '⚠️ This user has already been added',
        'admin_added': '✅ New admin added: {}',
        'user_added': '✅ New user added: {}',
        'user_removed': '✅ User removed: {}',
        'admin_list_empty': '📋 No admins currently',
        'admin_list': '📋 Admin List:\n{}',
        'user_list_empty': '📋 No authorized users currently',
        'user_list': '📋 Authorized Users:\n{}',
        'invalid_command': '❌ Unknown command. /help for assistance',
        'lang_changed': '✅ Language changed to {}',
        'enter_user_id': 'Please enter the user ID:',
        'invalid_user_id': '❌ Invalid user ID',
        'restricted': '❌ You do not have access to this bot. Please contact admins',
        'processing': '⏳ Processing...',
    }
}

class I18n:
    """مدیریت زبان‌ها"""
    
    def __init__(self):
        self.user_languages = {}  # {user_id: language_code}
    
    def get_message(self, key: str, user_id: str = None, **kwargs) -> str:
        """
        دریافت پیام به زبان کاربر
        
        Args:
            key: کلید پیام
            user_id: شناسه کاربر
            **kwargs: متغیرهای برای format
        
        Returns:
            پیام ترجمه‌شده
        """
        lang = self.user_languages.get(user_id, 'fa')
        message = MESSAGES.get(lang, MESSAGES['fa']).get(key, key)
        
        try:
            return message.format(**kwargs) if kwargs else message
        except (KeyError, IndexError):
            return message
    
    def set_language(self, user_id: str, language: str) -> bool:
        """تعیین زبان کاربر"""
        if language in LANGUAGES:
            self.user_languages[user_id] = language
            return True
        return False
    
    def get_language(self, user_id: str) -> str:
        """دریافت زبان کاربر"""
        return self.user_languages.get(user_id, 'fa')

# Initialize globally
i18n = I18n()
