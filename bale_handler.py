import requests
import json
from typing import Dict, Optional
from config import Config

class BaleHandler:
    """مدیریت ارتباط با API بله"""
    
    def __init__(self):
        self.token = Config.BALE_BOT_TOKEN
        self.api_url = Config.BALE_API_URL
        self.base_url = f"{self.api_url}/v1"
    
    def send_message(self, chat_id: str, text: str, reply_to_message_id: Optional[str] = None) -> Dict:
        """
        ارسال پیام به چت
        
        Args:
            chat_id: شناسه چت
            text: متن پیام
            reply_to_message_id: شناسه پیام جوابی
        
        Returns:
            نتیجه درخواست
        """
        try:
            url = f"{self.base_url}/messages/send"
            headers = {
                "Content-Type": "application/json",
                "X-Bale-Token": self.token
            }
            payload = {
                "chat_id": chat_id,
                "text": text
            }
            
            if reply_to_message_id:
                payload["reply_to_message_id"] = reply_to_message_id
            
            response = requests.post(url, headers=headers, json=payload, timeout=30)
            return response.json()
        except Exception as e:
            return {"error": str(e)}
    
    def send_typing(self, chat_id: str) -> Dict:
        """ارسال وضعیت تایپ کردن"""
        try:
            url = f"{self.base_url}/chats/actions"
            headers = {
                "Content-Type": "application/json",
                "X-Bale-Token": self.token
            }
            payload = {
                "chat_id": chat_id,
                "action": "typing"
            }
            response = requests.post(url, headers=headers, json=payload, timeout=30)
            return response.json()
        except Exception as e:
            return {"error": str(e)}
    
    def get_me(self) -> Dict:
        """دریافت اطلاعات ربات"""
        try:
            url = f"{self.base_url}/users/me"
            headers = {"X-Bale-Token": self.token}
            response = requests.get(url, headers=headers, timeout=30)
            return response.json()
        except Exception as e:
            return {"error": str(e)}
    
    def handle_webhook(self, data: Dict) -> Optional[Dict]:
        """
        پردازش webhook از بله
        
        Args:
            data: داده‌های webhook
        
        Returns:
            جزئیات پیام
        """
        try:
            if "message" in data:
                message = data["message"]
                return {
                    "chat_id": message.get("chat", {}).get("id"),
                    "text": message.get("text"),
                    "message_id": message.get("message_id"),
                    "from_id": message.get("from", {}).get("id")
                }
            return None
        except Exception as e:
            print(f"خطا در تحلیل webhook: {str(e)}")
            return None
