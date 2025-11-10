# Personal AI Assistant with Memory and Visual Learning Support

A powerful personal assistant tool designed to help users remember information and support visual learners through interactive AI conversations and automatic visualization generation.

## Features

### 🧠 Memory System
- **Persistent Memory**: Automatically stores all conversations in a local JSON file
- **Context Awareness**: Recalls previous conversations to provide contextual responses
- **Search Functionality**: Search through conversation history by keyword
- **Memory Management**: View memory statistics and clear history when needed

### 🎨 Visual Learning Support
Generate various types of visualizations to enhance understanding:
- **Mind Maps**: Brainstorm and organize ideas around a central concept
- **Concept Maps**: Show relationships between different concepts
- **Flowcharts**: Visualize processes and sequential steps
- **Timelines**: Display chronological events
- **Bar Charts**: Compare values and statistics

### 🤖 AI-Powered Chat
- Powered by OpenAI's GPT-3.5-turbo
- Remembers conversation context
- Specialized in helping visual learners
- Suggests appropriate visualizations for topics

## Installation

### Prerequisites
- Python 3.8 or higher
- OpenAI API key

### Setup Steps

1. **Clone the repository**
```bash
git clone https://github.com/Arpita-314/Personal_AI_AssistantwithMemory.git
cd Personal_AI_AssistantwithMemory
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure API Key**
Create a `.env` file in the project root:
```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

Get your API key from: https://platform.openai.com/api-keys

## Usage

### Starting the Assistant

Run the main application:
```bash
python main.py
```

### Available Commands

| Command | Description |
|---------|-------------|
| `chat` | Chat with the AI assistant (default mode) |
| `search <keyword>` | Search conversation history |
| `memory` | Show memory summary |
| `visualize` | Create visualizations |
| `clear` | Clear conversation memory |
| `help` | Show help message |
| `exit` | Exit the application |

### Example Interactions

**Basic Chat:**
```
You: What are the main types of machine learning?
Assistant: The main types of machine learning are:
1. Supervised Learning - learning from labeled data
2. Unsupervised Learning - finding patterns in unlabeled data
3. Reinforcement Learning - learning through trial and error
Would you like me to create a concept map to visualize these?
```

**Search Memory:**
```
You: search machine learning
[Shows all previous conversations about machine learning]
```

**Create Visualizations:**
```
You: visualize
[Interactive menu appears with visualization options]
```

## Project Structure

```
Personal_AI_AssistantwithMemory/
├── main.py                 # Main application entry point
├── ai_assistant.py         # AI assistant with OpenAI integration
├── memory_manager.py       # Conversation memory management
├── visual_helper.py        # Visualization generation
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## How It Works

### Memory System
The assistant automatically stores every conversation in a JSON file (`conversation_memory.json`). Each entry includes:
- Timestamp
- Role (user/assistant)
- Content
- Optional metadata

This enables:
- Contextual conversations across sessions
- Searchable conversation history
- Learning from past interactions

### Visual Learning
The assistant can generate various types of visualizations using matplotlib:

1. **Mind Maps**: Organize ideas hierarchically around a central concept
2. **Concept Maps**: Show how different concepts relate to each other
3. **Flowcharts**: Break down processes into sequential steps
4. **Timelines**: Visualize events chronologically
5. **Bar Charts**: Compare numerical data visually

All visualizations are saved in the `visualizations/` directory with timestamps.

## Configuration

### Environment Variables

Edit `.env` to customize:

```bash
# OpenAI API Key (required)
OPENAI_API_KEY=your_api_key_here

# Memory settings
MEMORY_FILE=conversation_memory.json
MAX_MEMORY_ITEMS=100
```

### Memory Settings
- `MEMORY_FILE`: Path to the JSON file storing conversations
- `MAX_MEMORY_ITEMS`: Maximum number of conversation entries to keep

## For Visual Learners

This tool is specifically designed to help visual learners:

1. **Automatic Visualization Suggestions**: The AI suggests relevant visualizations for topics
2. **Quick Visual Creation**: Generate diagrams with simple commands
3. **Multiple Formats**: Different visualization types for different learning needs
4. **Save and Review**: All visualizations are saved for later reference

### Best Practices for Visual Learning

- Ask the assistant to create mind maps when brainstorming
- Request concept maps to understand complex relationships
- Use flowcharts to understand processes or algorithms
- Create timelines for historical events or project planning
- Generate bar charts to compare options or track progress

## Examples

### Creating a Mind Map

```python
# The assistant can create a mind map about learning styles:
Central Idea: "Learning"
Branches:
- Visual: Diagrams, Charts, Images, Videos
- Auditory: Lectures, Podcasts, Discussions
- Kinesthetic: Practice, Experiments, Activities
- Reading: Books, Articles, Notes
```

### Creating a Flowchart

```python
# Process flowchart for problem-solving:
Steps:
1. Start
2. Define the problem
3. Gather information
4. Analyze data
5. Develop solution
6. Implement
7. Test and verify
8. Complete
```

## Security Notes

- Never commit your `.env` file or API keys to version control
- The `.gitignore` file is configured to exclude sensitive files
- Keep your OpenAI API key secure and private

## Troubleshooting

### "OPENAI_API_KEY not found"
- Ensure you've created a `.env` file with your API key
- Check that the key is valid and active

### "Module not found" errors
- Run `pip install -r requirements.txt` to install all dependencies

### Visualizations not appearing
- Check the `visualizations/` directory
- Ensure matplotlib is properly installed
- Check for error messages in the console

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- OpenAI for the GPT API
- Matplotlib for visualization capabilities
- Colorama for enhanced terminal output

## Support

For issues, questions, or suggestions, please open an issue on GitHub.