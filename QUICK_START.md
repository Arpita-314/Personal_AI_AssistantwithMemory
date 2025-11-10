# Quick Start Guide

Get up and running with the Interview Assistant in 5 minutes!

## Prerequisites

- Python 3.8+
- Tesseract OCR
- OpenAI or Anthropic API key

## Installation (3 steps)

### 1. Install Tesseract OCR

**macOS:**
```bash
brew install tesseract
```

**Ubuntu/Debian:**
```bash
sudo apt-get install tesseract-ocr
```

**Windows:**
Download from: https://github.com/UB-Mannheim/tesseract/wiki

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API Key

```bash
cp .env.example .env
nano .env  # Add your API key
```

Edit `.env`:
```bash
OPENAI_API_KEY=sk-your-key-here
AI_PROVIDER=openai
MODEL_NAME=gpt-4
```

## Usage

### Start the Application

```bash
python interview_assistant.py
```

### During Interview

1. **Capture question**: Press `Ctrl+Shift+C` (or click "📸 Capture & Analyze" button)
2. **View hints**: Click "💡 Hints" tab, then "🔓 Reveal Next Hint"
3. **See solution**: Click "✅ Solution" tab
4. **Hide overlay**: Press `Ctrl+Shift+H` or click ✕

## Features at a Glance

| Feature | Description |
|---------|-------------|
| 📸 Screen Capture | Automatically captures visible questions |
| 🔍 OCR | Extracts text from screen |
| 🤖 AI Analysis | Generates hints and solutions |
| 💡 Progressive Hints | 3 levels of hints |
| 📚 Memory | Stores past questions |
| 👁️ Invisible Overlay | Semi-transparent UI |
| ⌨️ Hotkeys | Quick keyboard shortcuts |

## Hotkeys

- `Ctrl+Shift+C` - Capture and analyze
- `Ctrl+Shift+H` - Toggle overlay visibility

## Tips

✅ **Do:**
- Practice with mock interviews first
- Try solving problems yourself first
- Use hints progressively
- Learn from the explanations

❌ **Don't:**
- Use in actual interviews without permission
- Copy solutions blindly
- Misrepresent your skills

## Troubleshooting

**No text detected?**
- Zoom in on the question
- Ensure good contrast
- Try capturing again

**API error?**
- Check your API key in `.env`
- Verify you have credits
- Check internet connection

**Hotkeys not working?**
- Use the manual "📸 Capture & Analyze" button
- Try running with admin/sudo privileges

## Need Help?

- Read the full [README.md](README.md)
- Check the [USAGE_GUIDE.md](USAGE_GUIDE.md)
- Run tests: `python simple_test.py`

## Example Workflow

```
1. Start: python interview_assistant.py
2. Open coding question in browser
3. Press Ctrl+Shift+C
4. Wait 2-3 seconds
5. Read Hint 1 (subtle)
6. Try to solve
7. If stuck, reveal Hint 2
8. Check solution if needed
9. Press Ctrl+Shift+H to hide
```

## Safety & Ethics

⚠️ **Important:** This tool is for learning and practice only. Using it during actual interviews may violate policies and is considered unethical. Use responsibly!

---

**Ready?** Run `python interview_assistant.py` and start practicing! 🚀
