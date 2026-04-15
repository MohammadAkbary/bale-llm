import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """تنظیمات اساسی برنامه"""
    BALE_BOT_TOKEN = os.getenv('BALE_BOT_TOKEN')
    BALE_API_URL = os.getenv('BALE_API_URL', 'https://api.bale.ai')
    PORT = int(os.getenv('PORT', 8000))
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    
    # AI Services Configuration
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    
    # Validate required configurations
    @classmethod
    def validate(cls):
        if not cls.BALE_BOT_TOKEN:
            raise ValueError("BALE_BOT_TOKEN is required")
        if not cls.GOOGLE_API_KEY and not cls.HUGGINGFACE_API_KEY and not cls.OPENAI_API_KEY:
            raise ValueError("At least one AI API key is required")
