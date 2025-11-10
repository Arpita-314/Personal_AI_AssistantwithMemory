# Detailed Usage Guide

## Table of Contents
1. [First Time Setup](#first-time-setup)
2. [Starting the Application](#starting-the-application)
3. [Using During Interviews](#using-during-interviews)
4. [Understanding the Interface](#understanding-the-interface)
5. [Tips and Best Practices](#tips-and-best-practices)
6. [Troubleshooting](#troubleshooting)

## First Time Setup

### Step 1: Install Dependencies

Make sure you have Python 3.8+ installed:
```bash
python --version
```

Install required packages:
```bash
pip install -r requirements.txt
```

### Step 2: Install Tesseract OCR

**Windows:**
1. Download from: https://github.com/UB-Mannheim/tesseract/wiki
2. Install to default location
3. Add to PATH or set in `.env`: `TESSERACT_CMD=C:\\Program Files\\Tesseract-OCR\\tesseract.exe`

**macOS:**
```bash
brew install tesseract
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

### Step 3: Get API Keys

**Option A: OpenAI (Recommended)**
1. Go to https://platform.openai.com/api-keys
2. Create a new API key
3. Copy the key

**Option B: Anthropic**
1. Go to https://console.anthropic.com/
2. Get your API key
3. Copy the key

### Step 4: Configure Environment

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` with your favorite editor:
```bash
nano .env  # or vim, code, notepad, etc.
```

3. Add your API key:
```bash
OPENAI_API_KEY=sk-...your-key-here
AI_PROVIDER=openai
MODEL_NAME=gpt-4
```

### Step 5: Test Installation

Run a quick test:
```bash
python -c "from config import Config; Config.validate(); print('✅ Configuration valid!')"
```

## Starting the Application

### Basic Start

```bash
python interview_assistant.py
```

You should see:
```
🚀 Initializing Interview Assistant...
✅ Interview Assistant initialized successfully!
📊 Memory: 0 questions stored
🤖 AI Provider: OPENAI

⌨️  Hotkeys:
   Capture & Analyze: <ctrl>+<shift>+c
   Toggle Overlay: <ctrl>+<shift>+h

🎬 Starting Interview Assistant...
```

### Running in Background

**Linux/macOS:**
```bash
nohup python interview_assistant.py &
```

**Windows:**
Use `pythonw` instead of `python`:
```bash
pythonw interview_assistant.py
```

## Using During Interviews

### Typical Workflow

1. **Before Interview:**
   - Start the application
   - Verify the overlay is working (Ctrl+Shift+H)
   - Position windows appropriately

2. **When Question Appears:**
   - Make sure the coding question is visible on screen
   - Press `Ctrl+Shift+C` to capture
   - Wait 2-3 seconds for analysis
   - Overlay appears automatically

3. **Getting Hints:**
   - Start with the "💡 Hints" tab
   - Click "🔓 Reveal Next Hint" for first subtle hint
   - Click again for more revealing hints
   - Only check solution as last resort

4. **Hiding Overlay:**
   - Press `Ctrl+Shift+H` to hide
   - Press again to show

### Screen Capture Tips

**What works best:**
- Clean, high-contrast text
- Full questions visible on screen
- Minimized background noise
- Standard fonts and sizes

**What doesn't work well:**
- Very small text (< 10pt)
- Handwritten text
- Complex formatting
- Images of code (screenshots)

### Discrete Usage

1. **Position overlay wisely:**
   - Top-right corner (default)
   - On secondary monitor if available
   - Adjust opacity in `.env`

2. **Use keyboard shortcuts:**
   - Avoid mouse clicks on overlay
   - Memorize hotkeys
   - Practice beforehand

3. **Quick glances:**
   - Read hints quickly
   - Hide immediately
   - Don't stare at overlay

## Understanding the Interface

### The Overlay Window

#### Title Bar
- 🔍 **Interview Assistant** - Application title
- **✕** - Close/hide button

#### Tab 1: 💡 Hints
- Shows the captured question
- Progressive hint reveal system
- "🔓 Reveal Next Hint" button
- Three levels of hints

#### Tab 2: ✅ Solution
- Complete code solution
- Explanation of approach
- Time and space complexity
- Programming language

#### Tab 3: 📚 Memory
- Recent questions (last 10)
- Difficulty level
- Programming language
- Timestamp

#### Status Bar
- Shows current operation status
- "Ready" when idle
- "📸 Capturing..." during capture
- "🤖 Analyzing..." during AI processing

### Understanding Hints

**Level 1 - Subtle:**
- General problem-solving direction
- High-level approach
- Pattern recognition

Example: "Consider using a hash map for O(1) lookups"

**Level 2 - Moderate:**
- More specific guidance
- Algorithm suggestions
- Data structure hints

Example: "Use two pointers, one starting at each end of the array"

**Level 3 - Revealing:**
- Detailed approach
- Nearly complete solution outline
- Edge cases to consider

Example: "Initialize left=0, right=n-1. While left<right, check if sum equals target..."

## Tips and Best Practices

### For Learning

1. **Always try first:**
   - Attempt the problem yourself
   - Only use hints when stuck
   - Challenge yourself

2. **Understand, don't copy:**
   - Read explanations carefully
   - Implement in your own style
   - Add comments to understand

3. **Review later:**
   - Check Memory tab
   - Review past solutions
   - Identify patterns

### For Interviews

1. **Practice beforehand:**
   - Test the system
   - Familiarize with hotkeys
   - Verify everything works

2. **Be subtle:**
   - Use minimal hints
   - Hide overlay frequently
   - Don't rely completely on it

3. **Stay ethical:**
   - Use for learning only
   - Don't misrepresent skills
   - Follow company policies

### Optimizing Performance

1. **API costs:**
   - Use gpt-3.5-turbo for practice (cheaper)
   - Use gpt-4 for important sessions
   - Monitor API usage

2. **Memory management:**
   - Review and clean old entries
   - Export important solutions
   - Backup memory file

3. **Screen capture:**
   - Ensure good lighting
   - Use clear fonts
   - Maximize question window

## Troubleshooting

### Issue: "No text detected"

**Causes:**
- Text too small
- Poor contrast
- Wrong screen captured

**Solutions:**
- Zoom in on question
- Increase font size
- Ensure question is visible
- Try capturing again

### Issue: "API Error"

**Causes:**
- Invalid API key
- No credits/quota
- Network issues

**Solutions:**
```bash
# Test API key
python -c "from ai_assistant import AIAssistant; ai = AIAssistant('openai', 'your-key', 'gpt-3.5-turbo'); print(ai.get_quick_hint('test'))"
```

### Issue: Hotkeys Not Working

**Solutions:**
1. Run with elevated privileges:
   ```bash
   sudo python interview_assistant.py  # Linux/macOS
   ```

2. Change hotkey combinations in `.env`

3. Check for conflicts with other apps

### Issue: Overlay Not Visible

**Solutions:**
1. Press `Ctrl+Shift+H` to toggle
2. Check if minimized to taskbar
3. Restart application
4. Verify tkinter:
   ```bash
   python -c "import tkinter; print('✅ tkinter works')"
   ```

### Issue: Poor OCR Accuracy

**Solutions:**
1. Update Tesseract:
   ```bash
   tesseract --version  # Should be 4.0+
   ```

2. Use better quality display
3. Increase text size
4. Clean background

### Getting Help

If issues persist:
1. Check GitHub Issues
2. Review logs (if enabled)
3. Test individual components
4. Reinstall dependencies

## Advanced Customization

### Custom Hotkeys

Edit `.env`:
```bash
# Single key
HOTKEY_CAPTURE=<f9>

# Combinations
HOTKEY_CAPTURE=<ctrl>+<alt>+c
HOTKEY_TOGGLE=<ctrl>+<alt>+h
```

### Overlay Position

Edit `overlay_ui.py`:
```python
# Top-left corner
x_position = 20
self.root.geometry(f"+{x_position}+20")

# Bottom-right corner
x_position = screen_width - self.width - 20
y_position = screen_height - self.height - 20
self.root.geometry(f"+{x_position}+{y_position}")
```

### Multiple Monitors

The overlay appears on the primary monitor by default. To use on secondary:
```python
# In overlay_ui.py, modify _setup_window()
# Add offset for second monitor
x_position = 1920 + 20  # Assuming first monitor is 1920px wide
```

## Practice Exercises

### Exercise 1: Setup Test
1. Start the application
2. Open a coding question in browser
3. Capture with Ctrl+Shift+C
4. Verify hints appear

### Exercise 2: Hotkey Speed Test
1. Practice hiding/showing quickly
2. Time yourself
3. Aim for < 1 second response

### Exercise 3: Hint Effectiveness
1. Try solving with only Level 1 hint
2. If stuck, use Level 2
3. Track which problems need more hints

### Exercise 4: Memory Review
1. Do 5 practice problems
2. Review Memory tab
3. Identify patterns in your mistakes

## Best Practices Summary

✅ **Do:**
- Use for learning and practice
- Try problems yourself first
- Understand solutions thoroughly
- Keep API keys secure
- Test before important use
- Review and learn from memory

❌ **Don't:**
- Misrepresent your abilities
- Copy solutions blindly
- Violate interview policies
- Share API keys
- Rely completely on hints
- Use without understanding

## Keyboard Shortcuts Quick Reference

| Action | Shortcut |
|--------|----------|
| Capture & Analyze | Ctrl+Shift+C |
| Toggle Overlay | Ctrl+Shift+H |
| Close Overlay | Click ✕ |
| Reveal Next Hint | Click button |
| Switch Tabs | Click tab name |

---

**Remember:** This tool is for learning. Real skill comes from understanding, not memorization. Use it to learn patterns and improve your problem-solving abilities.
