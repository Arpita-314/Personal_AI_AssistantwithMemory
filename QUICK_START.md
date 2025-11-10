# Quick Start Guide

Get started with the Personal AI Assistant in 3 easy steps!

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- openai (AI conversations)
- python-dotenv (configuration)
- colorama (colored output)
- matplotlib (visualizations)
- pillow (image processing)
- numpy (numerical operations)

## Step 2: Configure Your API Key

### Get an OpenAI API Key
1. Visit https://platform.openai.com/api-keys
2. Sign up or log in
3. Create a new API key
4. Copy the key

### Set Up Your Environment
```bash
# Copy the example configuration
cp .env.example .env

# Edit .env and add your API key
# Replace 'your_openai_api_key_here' with your actual key
```

Your `.env` file should look like:
```
OPENAI_API_KEY=sk-...your-actual-key-here...
MEMORY_FILE=conversation_memory.json
MAX_MEMORY_ITEMS=100
```

## Step 3: Run the Assistant

### Try the Examples First (No API Key Needed)
```bash
python examples.py
```
This demonstrates:
- ✓ Memory system
- ✓ 5 types of visualizations
- ✓ All core features

### Start the Full Assistant
```bash
python main.py
```

## Your First Conversation

```
You: help
[See available commands]

You: What is machine learning?
Assistant: [Explains machine learning...]

You: visualize
[Create a concept map about ML]

You: search machine
[Find previous ML discussions]
```

## Common Commands

| What you want | Command |
|--------------|---------|
| Chat with AI | Just type normally |
| Get help | `help` |
| Create visuals | `visualize` |
| Search history | `search <keyword>` |
| View memory stats | `memory` |
| Clear history | `clear` |
| Exit | `exit` or `quit` |

## Visualization Types

Try each visualization type from the menu:

1. **Mind Map** - Organize ideas around a central concept
2. **Concept Map** - Show relationships between concepts
3. **Flowchart** - Visualize step-by-step processes
4. **Timeline** - Display events chronologically
5. **Bar Chart** - Compare values visually

All visualizations are saved in the `visualizations/` folder!

## Tips for Success

### For Learning
- Ask the AI to explain topics
- Request visualizations for complex subjects
- Use search to review previous lessons
- Build a personal knowledge base

### For Projects
- Brainstorm with mind maps
- Plan workflows with flowcharts
- Track progress with timelines
- Compare options with bar charts

### For Memory
- The AI remembers your conversations
- Context builds across sessions
- Search anytime to recall information
- Clear memory when switching topics

## Troubleshooting

### "OPENAI_API_KEY not found"
✓ Create `.env` file  
✓ Add your API key  
✓ Check the file is in the same directory as `main.py`

### "Module not found"
✓ Run `pip install -r requirements.txt`  
✓ Make sure you're using Python 3.8+

### Can't see visualizations
✓ Check the `visualizations/` folder  
✓ Try running `examples.py` first  
✓ Look for error messages

## What's Next?

1. **Read the full documentation**
   - `README.md` - Overview and features
   - `USAGE_GUIDE.md` - Detailed usage instructions

2. **Customize your experience**
   - Edit `.env` to change memory limits
   - Organize your visualizations
   - Build your personal knowledge base

3. **Explore features**
   - Try all visualization types
   - Search your conversation history
   - Build on previous conversations
   - Create your own workflows

## Need More Help?

- Check `README.md` for detailed feature descriptions
- Read `USAGE_GUIDE.md` for examples and workflows
- Run `examples.py` to see demos without API key
- Open an issue on GitHub for support

---

**Ready to start?** Run `python main.py` and type `help`! 🚀
