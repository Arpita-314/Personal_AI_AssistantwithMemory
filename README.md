# Memory Garden RPG 🌱🧠

An innovative AI-powered personal assistant that gamifies thought organization and mental wellness. Your thoughts become a living garden where you can battle overthinking, level up, and watch your ideas grow and connect.

## Features

### 🎮 RPG Mechanics
- **Level Up System**: Gain XP by saving thoughts and creating connections
- **Achievement System**: Unlock badges for milestones
- **Boss Battles**: Defeat "Overthinking Bosses" by breaking them down into actionable steps
- **Daily Streak Tracking**: Build consistent thinking habits

### 🌳 Memory Garden Visualization
- **Interactive D3 Graph**: Watch your thoughts grow into an interconnected garden
- **Health System**: Nodes show vitality based on engagement
- **Visual Concept Mapping**: See how your ideas connect
- **Drag & Explore**: Interactive force-directed graph

### 🔐 Privacy-First Design
- **End-to-End Encryption**: All data encrypted with AES-GCM
- **Password Protected**: Your key never leaves your device
- **Local Storage**: Data stays in your browser
- **Zero Server Storage**: Complete privacy

### 🤖 AI Companion
- **Claude AI Integration**: Powered by Anthropic's Claude
- **Mood Tracking**: AI shows emotions based on interactions
- **Supportive Responses**: Helps organize and clarify thoughts
- **Overthinking Detection**: Automatically identifies stress patterns

## Setup

### Prerequisites
- Node.js 18+ and npm
- Anthropic API key ([Get one here](https://console.anthropic.com/))

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Arpita-314/Personal_AI_AssistantwithMemory.git
cd Personal_AI_AssistantwithMemory
```

2. Install dependencies:
```bash
npm install
```

3. Configure your API key:
```bash
cp .env.example .env
# Edit .env and add your VITE_ANTHROPIC_API_KEY
```

4. Start the development server:
```bash
npm run dev
```

5. Open your browser to `http://localhost:5173`

## Usage

### First Time Setup
1. Create a password (minimum 6 characters)
2. This password encrypts all your data locally
3. **Important**: Remember this password - it cannot be recovered!

### Planting Thoughts
- Type any thought in the chat input
- Press Enter or click Send
- Watch it appear as a node in your garden
- Concepts are automatically extracted and linked

### Boss Battles
- Thoughts with anxiety/stress keywords trigger boss battles
- Click "BREAK IT DOWN & DEFEAT" to get actionable steps
- Earn 50 XP and unlock achievements

### Managing Your Garden
- Click nodes to view details and health
- Healthy nodes are green, wilting ones are red/orange
- Regular interaction keeps thoughts "watered"

## Technology Stack

- **Frontend**: React 18 + Vite
- **Visualization**: D3.js v7
- **UI Icons**: Lucide React
- **AI**: Anthropic Claude (Sonnet 4)
- **Encryption**: Web Crypto API (AES-GCM)
- **Storage**: Browser LocalStorage

## Project Structure

```
.
├── src/
│   ├── App.jsx                  # Main app with storage polyfill
│   ├── MemoryGardenRPG.jsx     # Core component
│   ├── main.jsx                # React entry point
│   └── index.css               # Global styles
├── public/
│   └── vite.svg                # Favicon
├── .env.example                # Environment template
├── package.json                # Dependencies
├── vite.config.js             # Vite configuration
└── index.html                 # HTML entry point
```

## Security Notes

- All encryption happens client-side
- API key should be kept secure (don't commit .env)
- Consider using environment variables in production
- Data is only stored locally in browser

## Development

### Build for Production
```bash
npm run build
```

### Preview Production Build
```bash
npm run preview
```

## Contributing

Contributions welcome! Please feel free to submit a Pull Request.

## License

MIT License - feel free to use this project however you'd like!

## Acknowledgments

- Built with ❤️ by the community
- AI powered by Anthropic Claude
- Visualization powered by D3.js

---

**Remember**: Your thoughts are valuable. Treat them like a garden - nurture them, connect them, and watch them grow! 🌱✨