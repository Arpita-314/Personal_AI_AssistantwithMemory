"""
Configuration module for the Interview Assistant
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration settings for the interview assistant"""
    
    # API Configuration
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY', '')
    AI_PROVIDER = os.getenv('AI_PROVIDER', 'openai')
    MODEL_NAME = os.getenv('MODEL_NAME', 'gpt-4')
    
    # UI Configuration
    OVERLAY_OPACITY = float(os.getenv('OVERLAY_OPACITY', '0.85'))
    OVERLAY_WIDTH = 400
    OVERLAY_HEIGHT = 600
    
    # Hotkeys
    HOTKEY_CAPTURE = os.getenv('HOTKEY_CAPTURE', '<ctrl>+<shift>+c')
    HOTKEY_TOGGLE = os.getenv('HOTKEY_TOGGLE', '<ctrl>+<shift>+h')
    
    # Storage
    BASE_DIR = Path(__file__).parent
    MEMORY_FILE = BASE_DIR / os.getenv('MEMORY_FILE', 'interview_memory.json')
    SCREENSHOTS_DIR = BASE_DIR / 'screenshots'
    
    # OCR Configuration
    TESSERACT_CMD = os.getenv('TESSERACT_CMD', '/usr/bin/tesseract')
    
    @classmethod
    def validate(cls):
        """Validate configuration"""
        if cls.AI_PROVIDER == 'openai' and not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is required when using OpenAI provider")
        if cls.AI_PROVIDER == 'anthropic' and not cls.ANTHROPIC_API_KEY:
            raise ValueError("ANTHROPIC_API_KEY is required when using Anthropic provider")
        
        # Create necessary directories
        cls.SCREENSHOTS_DIR.mkdir(exist_ok=True)
        
        return True
