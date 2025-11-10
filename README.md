# Personal AI Assistant with Memory - Invisible Interview Helper

An invisible, AI-powered coding interview assistant that helps you ace technical interviews with real-time hints and solutions. Similar to Cluely, this tool provides discreet assistance during coding interviews through an intelligent overlay system.

## 🌟 Features

- **🔍 Screen Capture & OCR**: Automatically captures and reads coding questions from your screen
- **🤖 AI-Powered Analysis**: Uses OpenAI or Anthropic models to analyze questions and generate solutions
- **💡 Progressive Hints System**: Get subtle hints that progressively reveal the solution
- **📚 Intelligent Memory**: Remembers past questions and solutions for instant recall
- **👁️ Invisible Overlay**: Semi-transparent, discreet overlay that stays on top
- **⌨️ Hotkey Controls**: Quick keyboard shortcuts for stealth operation
- **🎯 Multiple Languages**: Supports Python, JavaScript, Java, C++, and more
- **📊 Statistics Tracking**: Track your interview preparation progress

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Tesseract OCR installed on your system
- OpenAI API key or Anthropic API key

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Arpita-314/Personal_AI_AssistantwithMemory.git
cd Personal_AI_AssistantwithMemory
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Install Tesseract OCR**

**Ubuntu/Debian:**
```bash
sudo apt-get install tesseract-ocr
```

**MacOS:**
```bash
brew install tesseract
```

**Windows:**
Download and install from: https://github.com/UB-Mannheim/tesseract/wiki

4. **Configure environment variables**
```bash
cp .env.example .env
# Edit .env and add your API keys
```

5. **Run the application**
```bash
python interview_assistant.py
```

## ⚙️ Configuration

Edit the `.env` file to customize your settings:

```bash
# API Keys
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# AI Configuration
AI_PROVIDER=openai  # or 'anthropic'
MODEL_NAME=gpt-4    # or 'gpt-3.5-turbo', 'claude-3-opus-20240229'

# UI Settings
OVERLAY_OPACITY=0.85

# Hotkeys
HOTKEY_CAPTURE=<ctrl>+<shift>+c  # Capture and analyze screen
HOTKEY_TOGGLE=<ctrl>+<shift>+h   # Toggle overlay visibility
```

## 🎮 Usage

### Basic Workflow

1. **Start the application**
   ```bash
   python interview_assistant.py
   ```

2. **During an interview:**
   - Press `Ctrl+Shift+C` to capture the current question on screen
   - The system will analyze it and show the overlay
   - Use the "💡 Hints" tab for progressive hints
   - Check the "✅ Solution" tab for the complete solution
   - View the "📚 Memory" tab to see past questions

3. **Toggle visibility:**
   - Press `Ctrl+Shift+H` to show/hide the overlay
   - The overlay is semi-transparent and stays on top

### Features in Detail

#### Progressive Hints
The system provides three levels of hints:
1. **Subtle hint** - Points you in the right direction
2. **Moderate hint** - Gives more specific guidance
3. **Revealing hint** - Nearly gives away the approach

Click "🔓 Reveal Next Hint" to progressively reveal hints.

#### Memory System
- Automatically stores all analyzed questions
- Searches for similar questions from past sessions
- Provides instant answers for repeated questions
- Tracks statistics by language and difficulty

#### Smart Screen Capture
- Captures entire screen or specific regions
- Uses OCR to extract text from images
- Preprocesses images for better text recognition
- Saves screenshots for later review

## 📁 Project Structure

```
Personal_AI_AssistantwithMemory/
├── interview_assistant.py   # Main application
├── config.py               # Configuration management
├── memory.py               # Memory system for Q&A storage
├── screen_capture.py       # Screen capture and OCR
├── ai_assistant.py         # AI integration (OpenAI/Anthropic)
├── overlay_ui.py           # Invisible overlay UI
├── requirements.txt        # Python dependencies
├── .env.example           # Example environment variables
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## 🔧 Advanced Usage

### Custom Hotkeys

Modify hotkeys in `.env`:
```bash
HOTKEY_CAPTURE=<ctrl>+<alt>+s
HOTKEY_TOGGLE=<ctrl>+<alt>+h
```

### Different AI Models

**For OpenAI:**
```bash
AI_PROVIDER=openai
MODEL_NAME=gpt-4  # or gpt-3.5-turbo
```

**For Anthropic:**
```bash
AI_PROVIDER=anthropic
MODEL_NAME=claude-3-opus-20240229  # or claude-3-sonnet-20240229
```

### Adjusting Overlay Appearance

```bash
OVERLAY_OPACITY=0.85  # 0.0 (transparent) to 1.0 (opaque)
```

Edit `config.py` for more UI customizations:
- `OVERLAY_WIDTH`: Width of overlay window
- `OVERLAY_HEIGHT`: Height of overlay window

## 🛡️ Ethical Considerations

**Important Notice:** This tool is designed for:
- ✅ Personal learning and practice
- ✅ Studying interview patterns
- ✅ Reviewing solutions after attempts
- ✅ Mock interviews and preparation

**NOT intended for:**
- ❌ Cheating in real interviews
- ❌ Misrepresenting your skills
- ❌ Violating interview integrity policies

Using this tool during actual interviews may violate company policies and ethical guidelines. Use responsibly and ethically.

## 🐛 Troubleshooting

### Common Issues

**1. OCR not working:**
- Ensure Tesseract is installed: `tesseract --version`
- Set correct path in `.env`: `TESSERACT_CMD=/usr/bin/tesseract`

**2. API errors:**
- Verify your API key is correct
- Check your API quota/credits
- Ensure internet connectivity

**3. Hotkeys not working:**
- Run with administrator/sudo privileges
- Check for conflicting keyboard shortcuts
- Try different hotkey combinations

**4. Overlay not showing:**
- Press `Ctrl+Shift+H` to toggle
- Check if window is minimized
- Verify tkinter is installed: `python -c "import tkinter"`

## 📊 Statistics

View your progress:
```python
from memory import InterviewMemory
from config import Config

memory = InterviewMemory(Config.MEMORY_FILE)
stats = memory.get_stats()
print(stats)
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is provided as-is for educational purposes. Use responsibly and ethically.

## 🙏 Acknowledgments

- Inspired by coding interview preparation tools
- Built with OpenAI and Anthropic AI models
- Uses Tesseract OCR for text extraction

## ⚠️ Disclaimer

This tool is for educational and practice purposes only. The authors are not responsible for any misuse or violation of interview policies. Always follow ethical guidelines and company policies during actual interviews.