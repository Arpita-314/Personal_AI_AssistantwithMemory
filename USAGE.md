# Memory Garden RPG - User Guide

## Getting Started

### First Time Setup

1. **Launch the Application**
   - Run `npm run dev` in your terminal
   - Open `http://localhost:5173` in your browser

2. **Create Your Password**
   - Enter a password (minimum 6 characters)
   - This password encrypts ALL your data
   - ⚠️ **IMPORTANT**: There's no password recovery - remember it!

3. **Enter Your Garden**
   - Click "Unlock Garden" to access the app

## Using Memory Garden RPG

### Planting Thoughts

Simply type anything in the "Plant a thought..." input box and press Enter or click Send. Your thought will:
- Appear in the chat on the left
- Create a node in your garden on the right
- Automatically extract key concepts
- Link related ideas together
- Earn you 20 XP!

**Examples:**
- "I need to finish the project proposal by Friday"
- "Learning React hooks is challenging but exciting"
- "I'm worried about the presentation tomorrow"

### Boss Battles 🗡️

When you type thoughts with stress/anxiety keywords, you'll trigger a **Boss Battle**:
- Words like: worry, anxious, stress, overwhelmed, stuck
- Click "BREAK IT DOWN & DEFEAT" to get actionable steps
- Earn 50 XP for defeating bosses!

**Example:**
Type: "I'm really stressed about this upcoming exam and can't stop worrying"
→ Boss battle triggers! Get AI-powered steps to overcome it.

### Your Memory Garden 🌱

The right panel shows your growing garden:

**Node Colors:**
- 🟢 **Green**: Healthy thoughts (recently added)
- 🟠 **Orange**: Needs care (getting older)
- 🔴 **Red**: Wilting (hasn't been engaged with)

**Node Types:**
- **Larger circles**: Your main thoughts
- **Smaller circles**: Extracted concepts

**Interactions:**
- Click nodes to view details
- Drag nodes to explore connections
- Watch thoughts connect automatically

### Stats & Progress

Top bar shows your progress:

- ⭐ **Level**: Based on XP (100 XP per level)
- 🏆 **Achievements**: Unlocked badges out of 6 total
- ⚡ **Streak**: Days used in a row

### Achievements 🏆

Unlock these badges:
1. 🌱 **First Seed** - Plant your first thought (1 thought)
2. 🌿 **Thought Gardener** - Save 10 thoughts
3. 🧠 **Synapse Builder** - Create 5 connections
4. ⚔️ **Overthinking Slayer** - Defeat your first boss
5. 🔥 **Consistent Thinker** - Use 3 days in a row
6. 👑 **Memory Master** - Reach level 5

When you unlock an achievement, you'll see an animated popup!

## AI Companion Moods

Your AI companion shows different emotions:
- 🤔 **Curious** - Default state, ready to help
- 🎉 **Excited** - Just leveled up!
- 💪 **Supportive** - After you share thoughts
- 💭 **Thoughtful** - Processing deep thoughts
- 🌟 **Celebrating** - Boss defeated!

## Tips & Tricks

### Maximizing Your Garden
1. **Regular Use**: Visit daily to maintain your streak
2. **Diverse Thoughts**: Mix different topics to create rich connections
3. **Reflection**: Click nodes to revisit past thoughts
4. **Boss Battles**: Don't avoid them - they give great insights!

### Privacy & Security
- All data encrypted with AES-GCM
- Nothing stored on servers
- Password never leaves your device
- Data stays in your browser's localStorage

### API Configuration

To enable full AI responses:
1. Get an API key from [Anthropic Console](https://console.anthropic.com/)
2. Create a `.env` file (copy from `.env.example`)
3. Add: `VITE_ANTHROPIC_API_KEY=your_key_here`
4. Restart the dev server

**Note**: The app works without an API key - it just shows friendly error messages.

## Troubleshooting

### "Wrong password" error
- Your password doesn't match the one used to encrypt the data
- If you forgot it, clear your browser's localStorage to start fresh

### AI not responding
- Check if your API key is configured in `.env`
- Verify the API key is valid
- Check browser console for error messages

### Graph not showing
- Make sure you've sent at least one message
- Refresh the page if the SVG doesn't render
- Try resizing the browser window

### Lost my data
- Data is stored locally in your browser
- Clearing browser data will delete everything
- Export feature coming in future updates!

## Keyboard Shortcuts

- **Enter** in password field → Unlock Garden
- **Enter** in chat input → Send message

## Data Management

### Starting Fresh
```javascript
// Open browser console (F12) and run:
localStorage.clear();
location.reload();
```

### Viewing Stored Data
```javascript
// See your encrypted data:
console.log(localStorage.getItem('encrypted-chats'));
```

## Best Practices

1. **Journal Regularly**: Make it a daily habit
2. **Tag Important Thoughts**: Use keywords you'll remember
3. **Review Connections**: Click nodes to see how ideas link
4. **Battle Overthinking**: Don't shy away from boss battles
5. **Backup Important**: Take screenshots of key insights (export coming soon)

## Support

Having issues? Check:
1. Browser console (F12) for error messages
2. README.md for setup instructions
3. GitHub Issues for known problems

---

Happy gardening! 🌱✨ Your thoughts are valuable - nurture them and watch them grow!
