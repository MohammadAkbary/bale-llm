import asyncio
import json
import logging
from flask import Flask, request, jsonify
from config import Config
from bale_handler import BaleHandler
from ai_handler import AIHandler
from database import db
from i18n import i18n
from admin_manager import admin_manager

# تنظیم logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# برنامه Flask
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# مقداردهی handlers
bale = BaleHandler()
ai = AIHandler()

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    دریافت پیام‌های بله از طریق webhook
    پردازش دستورات مدیر و پاسخ‌دهی به کاربران
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"ok": False, "error": "No data received"}), 400
        
        logger.info(f"Webhook received: {json.dumps(data, ensure_ascii=False)}")
        
        # تحلیل پیام
        message_data = bale.handle_webhook(data)
        
        if not message_data or not message_data.get("text"):
            return jsonify({"ok": True}), 200
        
        chat_id = message_data["chat_id"]
        user_id = message_data.get("from_id") or chat_id
        user_message = message_data["text"].strip()
        message_id = message_data["message_id"]
        
        if not chat_id:
            return jsonify({"ok": False, "error": "No chat_id"}), 400
        
        logger.info(f"Message from {user_id}: {user_message}")
        
        # پردازش دستورات مدیر
        admin_response, is_command = admin_manager.process_command(user_id, user_message)
        
        if is_command and admin_response:
            bale.send_message(chat_id, admin_response, message_id)
            return jsonify({"ok": True}), 200
        
        # بررسی دسترسی کاربر
        if db.is_blocked(user_id):
            response = i18n.get_message('restricted', user_id)
            bale.send_message(chat_id, response, message_id)
            logger.warning(f"Blocked user {user_id} tried to access")
            return jsonify({"ok": True}), 200
        
        # بررسی اینکه آیا کاربر مجاز است
        require_approval = db.get_setting('require_approval', True)
        if require_approval and not db.is_authorized(user_id) and not db.is_admin(user_id):
            response = i18n.get_message('restricted', user_id)
            bale.send_message(chat_id, response, message_id)
            logger.info(f"Unauthorized user {user_id} tried to access")
            return jsonify({"ok": True}), 200
        
        # بررسی دستورات رایج
        if user_message == '/help':
            response = i18n.get_message('help', user_id)
            bale.send_message(chat_id, response, message_id)
            return jsonify({"ok": True}), 200
        
        if user_message == '/start':
            response = i18n.get_message('welcome', user_id)
            bale.send_message(chat_id, response, message_id)
            return jsonify({"ok": True}), 200
        
        # ارسال وضعیت تایپ
        bale.send_typing(chat_id)
        
        # درخواست از AI
        ai_response = asyncio.run(ai.get_response(user_message, 'google'))
        
        # محدود کردن طول پیام برای بله (حداکثر 4096 کاراکتر)
        if len(ai_response) > 4096:
            ai_response = ai_response[:4093] + "..."
        
        # ارسال پاسخ
        bale.send_message(chat_id, ai_response, message_id)
        
        logger.info(f"Response sent to {user_id}")
        return jsonify({"ok": True}), 200
        
    except Exception as e:
        logger.error(f"Error in webhook: {str(e)}")
        return jsonify({"ok": False, "error": str(e)}), 500


@app.route('/health', methods=['GET'])
def health():
    """
    بررسی سلامت برنامه
    Keep-alive endpoint برای جلوگیری از خاموش شدن Render
    """
    try:
        bot_info = bale.get_me()
        if "error" not in bot_info:
            return jsonify({"status": "healthy", "bot_info": bot_info}), 200
        else:
            return jsonify({"status": "unhealthy", "error": bot_info.get("error")}), 500
    except Exception as e:
        return jsonify({"status": "unhealthy", "error": str(e)}), 500


@app.route('/ping', methods=['GET'])
def ping():
    """
    Ping endpoint برای keep-alive
    Render suspended apps بعد 15 دقیقه inactivity
    استفاده از UptimeRobot یا service مشابه برای call این endpoint هر 10 دقیقه
    """
    logger.info("🔔 Ping received - Bot is alive!")
    return jsonify({"status": "alive", "timestamp": str(__import__('datetime').datetime.now())}), 200


@app.route('/', methods=['GET'])
def index():
    """
    صفحه اصلی
    """
    return jsonify({
        "name": "Bale LLM Bot",
        "description": "ربات بله با قابلیت AI",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "webhook": "/webhook"
        }
    }), 200


@app.errorhandler(404)
def not_found(error):
    """مدیریت صفحات یافت نشده"""
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(500)
def server_error(error):
    """مدیریت خطاهای داخلی سرور"""
    logger.error(f"Server error: {str(error)}")
    return jsonify({"error": "Internal server error"}), 500


def setup_bot():
    """راه‌اندازی ربات"""
    logger.info("🤖 شروع راه‌اندازی ربات Bale LLM...")
    
    try:
        Config.validate()
        logger.info("✅ تنظیمات بررسی شدند")
        
        # بررسی اینکه آیا Admin اولیه وجود دارد
        if len(db.get_admins()) == 0:
            logger.warning("⚠️ هیچ Admin تعریف نشده است!")
            logger.info("💡 لطفاً یک Admin اولیه ایجاد کنید:")
            logger.info("   از طریق دیتابیس: db.add_admin('YOUR_USER_ID')")
            logger.info("   یا با ویرایش bot_database.json")
        else:
            logger.info(f"✅ Admins تشخیص داده شد: {db.get_admins()}")
        
        stats = db.get_stats()
        logger.info(f"📊 آمار: {stats}")
        
        bot_info = bale.get_me()
        if "error" not in bot_info:
            logger.info(f"✅ ربات متصل شد: {bot_info}")
        else:
            logger.warning(f"⚠️ خطا در دریافت اطلاعات ربات: {bot_info.get('error')}")
        
        logger.info("✅ ربات آماده است!")
    except ValueError as e:
        logger.error(f"❌ خطا در تنظیمات: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"❌ خطا در راه‌اندازی: {str(e)}")
        raise


if __name__ == '__main__':
    try:
        setup_bot()
        port = Config.PORT
        logger.info(f"🚀 سرور روی پورت {port} شروع شد")
        app.run(host='0.0.0.0', port=port, debug=Config.FLASK_DEBUG)
    except Exception as e:
        logger.error(f"خطای جدی: {str(e)}")
        exit(1)
