"""
Setup script for Interview Assistant
"""
import os
import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Check if Python version is adequate"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        print(f"   Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python version: {version.major}.{version.minor}.{version.micro}")
    return True

def check_tesseract():
    """Check if Tesseract OCR is installed"""
    try:
        result = subprocess.run(['tesseract', '--version'], 
                              capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            version = result.stdout.split('\n')[0]
            print(f"✅ Tesseract OCR: {version}")
            return True
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    
    print("⚠️  Tesseract OCR not found")
    print("   Install instructions:")
    if sys.platform == 'win32':
        print("   Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki")
    elif sys.platform == 'darwin':
        print("   macOS: brew install tesseract")
    else:
        print("   Linux: sudo apt-get install tesseract-ocr")
    return False

def install_dependencies():
    """Install Python dependencies"""
    print("\n📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def setup_env_file():
    """Setup .env file if it doesn't exist"""
    env_file = Path('.env')
    env_example = Path('.env.example')
    
    if env_file.exists():
        print("✅ .env file already exists")
        return True
    
    if env_example.exists():
        print("\n📝 Creating .env file...")
        # Copy example to .env
        with open(env_example, 'r') as f:
            content = f.read()
        
        with open(env_file, 'w') as f:
            f.write(content)
        
        print("✅ .env file created")
        print("⚠️  Please edit .env and add your API keys:")
        print("   - OPENAI_API_KEY or ANTHROPIC_API_KEY")
        return True
    
    print("❌ .env.example not found")
    return False

def create_directories():
    """Create necessary directories"""
    print("\n📁 Creating directories...")
    dirs = ['screenshots']
    
    for dir_name in dirs:
        path = Path(dir_name)
        path.mkdir(exist_ok=True)
        print(f"✅ Created {dir_name}/ directory")
    
    return True

def verify_imports():
    """Verify that key modules can be imported"""
    print("\n🔍 Verifying imports...")
    modules = [
        'PIL',
        'pytesseract',
        'pynput',
        'openai',
        'anthropic',
        'pyautogui',
        'cv2',
        'numpy',
        'dotenv'
    ]
    
    failed = []
    for module in modules:
        try:
            __import__(module)
            print(f"✅ {module}")
        except ImportError:
            print(f"❌ {module}")
            failed.append(module)
    
    if failed:
        print(f"\n⚠️  Failed to import: {', '.join(failed)}")
        print("   Try reinstalling dependencies:")
        print("   pip install -r requirements.txt")
        return False
    
    return True

def test_configuration():
    """Test if configuration is valid"""
    print("\n⚙️  Testing configuration...")
    try:
        from config import Config
        Config.validate()
        print("✅ Configuration is valid")
        return True
    except ValueError as e:
        print(f"⚠️  Configuration issue: {e}")
        print("   Please edit .env and add your API keys")
        return False
    except Exception as e:
        print(f"❌ Error testing configuration: {e}")
        return False

def print_next_steps():
    """Print next steps for the user"""
    print("\n" + "="*60)
    print("🎉 Setup Complete!")
    print("="*60)
    print("\n📋 Next Steps:")
    print("\n1. Edit .env file and add your API key:")
    print("   nano .env")
    print("   (Add your OPENAI_API_KEY or ANTHROPIC_API_KEY)")
    print("\n2. Run the application:")
    print("   python interview_assistant.py")
    print("\n3. Read the usage guide:")
    print("   cat USAGE_GUIDE.md")
    print("\n4. Test the hotkeys:")
    print("   Ctrl+Shift+C - Capture and analyze")
    print("   Ctrl+Shift+H - Toggle overlay")
    print("\n⚠️  Important Reminders:")
    print("   - Use ethically and responsibly")
    print("   - For learning and practice only")
    print("   - Don't misrepresent your skills")
    print("="*60 + "\n")

def main():
    """Main setup function"""
    print("="*60)
    print("🚀 Interview Assistant Setup")
    print("="*60 + "\n")
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check Tesseract
    tesseract_ok = check_tesseract()
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Setup .env file
    setup_env_file()
    
    # Create directories
    create_directories()
    
    # Verify imports
    if not verify_imports():
        print("\n⚠️  Some imports failed, but you can try running the application")
    
    # Test configuration
    config_ok = test_configuration()
    
    # Print next steps
    print_next_steps()
    
    # Summary
    if not tesseract_ok:
        print("⚠️  Note: Tesseract OCR is not installed. Screen capture won't work without it.")
    
    if not config_ok:
        print("⚠️  Note: Configuration not complete. Add your API key to .env before running.")

if __name__ == "__main__":
    main()
