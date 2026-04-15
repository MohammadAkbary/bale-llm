import requests
import json
from config import Config

class AIHandler:
    """مدیریت تعامل با services هوش مصنوعی رایگان"""
    
    def __init__(self):
        self.google_key = Config.GOOGLE_API_KEY
        self.huggingface_key = Config.HUGGINGFACE_API_KEY
        self.deepseek_key = Config.DEEPSEEK_API_KEY
    
    async def get_response(self, user_message: str, use_service: str = 'google') -> str:
        """
        دریافت پاسخ از AI
        
        Args:
            user_message: پیام کاربر
            use_service: سرویس مورد نظر ('google', 'huggingface' یا 'deepseek')
        
        Returns:
            پاسخ هوش مصنوعی
        """
        try:
            if use_service.lower() == 'google':
                return await self._get_google_response(user_message)
            elif use_service.lower() == 'huggingface':
                return await self._get_huggingface_response(user_message)
            elif use_service.lower() == 'deepseek':
                return await self._get_deepseek_response(user_message)
            else:
                return "سرویس نامشخص"
        except Exception as e:
            return f"خطا در دریافت پاسخ: {str(e)}"
    
    async def _get_google_response(self, user_message: str) -> str:
        """استفاده از Google Gemini API (رایگان)"""
        try:
            import google.generativeai as genai
            genai.configure(api_key=self.google_key)
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(user_message)
            return response.text
        except ImportError:
            return "کتابخانه Google Generative AI نصب نشده"
        except Exception as e:
            return f"خطا در Google API: {str(e)}"
    
    async def _get_huggingface_response(self, user_message: str) -> str:
        """استفاده از Hugging Face API (رایگان)"""
        try:
            api_url = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
            headers = {"Authorization": f"Bearer {self.huggingface_key}"}
            payload = {
                "inputs": user_message,
                "parameters": {"max_length": 500}
            }
            response = requests.post(api_url, headers=headers, json=payload, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    return result[0].get('generated_text', 'پاسخی دریافت نشد')
                return str(result)
            else:
                return f"خطا از سرور: {response.status_code}"
        except Exception as e:
            return f"خطا در Hugging Face API: {str(e)}"
    
    async def _get_deepseek_response(self, user_message: str) -> str:
        """استفاده از DeepSeek API (رایگان)"""
        try:
            api_url = "https://api.deepseek.com/chat/completions"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.deepseek_key}"
            }
            payload = {
                "model": "deepseek-chat",
                "messages": [
                    {
                        "role": "user",
                        "content": user_message
                    }
                ],
                "temperature": 0.7,
                "max_tokens": 1000
            }
            
            response = requests.post(api_url, headers=headers, json=payload, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                if "choices" in result and len(result["choices"]) > 0:
                    return result["choices"][0]["message"]["content"]
                else:
                    return "پاسخی دریافت نشد"
            else:
                return f"خطا از سرور DeepSeek: {response.status_code}"
        except Exception as e:
            return f"خطا در DeepSeek API: {str(e)}"
