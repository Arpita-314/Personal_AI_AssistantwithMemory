# Usage Guide - Personal AI Assistant with Memory

This guide provides detailed instructions on how to use the Personal AI Assistant effectively.

## Quick Start

### 1. Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Create .env file with your API key
cp .env.example .env
# Edit .env and add your OpenAI API key
```

### 2. Run the Assistant

```bash
python main.py
```

### 3. Try the Examples (No API Key Required)

```bash
python examples.py
```

## Commands Reference

### Chat Commands

| Command | Usage | Description |
|---------|-------|-------------|
| `help` | `help` | Display available commands |
| `exit` / `quit` | `exit` | Exit the application |
| Regular text | `What is Python?` | Chat with the AI assistant |

### Memory Commands

| Command | Usage | Description |
|---------|-------|-------------|
| `memory` | `memory` | Show memory statistics |
| `search` | `search machine learning` | Search conversation history |
| `clear` | `clear` | Clear all conversation memory |

### Visualization Commands

| Command | Usage | Description |
|---------|-------|-------------|
| `visualize` | `visualize` | Open visualization menu |

## Use Cases

### For Students

**Taking Notes**
- Chat with the assistant about topics you're learning
- The conversation is automatically saved as notes
- Search previous conversations when reviewing

**Visual Learning**
- Request mind maps to organize study topics
- Create concept maps to understand relationships
- Use flowcharts to understand processes
- Generate timelines for historical events

**Example:**
```
You: Explain the water cycle
Assistant: [Provides explanation]
You: visualize
[Select: Flowchart]
[A flowchart of the water cycle is created]
```

### For Professionals

**Project Planning**
- Brainstorm ideas with the AI
- Create mind maps for project structure
- Generate flowcharts for workflows
- Track progress with timelines

**Knowledge Management**
- Store important information in conversations
- Search for specific topics later
- Build a personal knowledge base

### For Visual Learners

**Understanding Complex Topics**
1. Ask the AI to explain a complex topic
2. Request a visualization (mind map, concept map)
3. Review the visual representation
4. Ask follow-up questions
5. The conversation is saved for later review

**Example:**
```
You: What are the main components of a computer?
Assistant: [Explains CPU, RAM, Storage, etc.]
You: visualize
[Select: Concept Map]
[A concept map showing computer components is created]
You: Tell me more about RAM
[Conversation continues with context]
```

## Visualization Types Explained

### 1. Mind Maps
**Best for:** Brainstorming, organizing ideas around a central concept

**Structure:**
- Central idea in the middle
- Main branches radiating outward
- Sub-topics connected to branches

**Use when:**
- Planning a project
- Brainstorming solutions
- Organizing thoughts
- Learning new topics

### 2. Concept Maps
**Best for:** Showing relationships between different concepts

**Structure:**
- Multiple concepts
- Lines showing connections
- Hierarchical or network layout

**Use when:**
- Understanding how ideas relate
- Learning connected topics
- Mapping knowledge domains
- Studying complex subjects

### 3. Flowcharts
**Best for:** Sequential processes, algorithms, decision trees

**Structure:**
- Steps in sequence
- Arrows showing flow
- Top to bottom layout

**Use when:**
- Understanding processes
- Learning algorithms
- Following procedures
- Planning workflows

### 4. Timelines
**Best for:** Chronological events, project schedules

**Structure:**
- Linear timeline
- Events marked with dates
- Left to right progression

**Use when:**
- Tracking historical events
- Planning project milestones
- Understanding sequences
- Organizing schedules

### 5. Bar Charts
**Best for:** Comparing quantities, showing statistics

**Structure:**
- Categories on X-axis
- Values on Y-axis
- Colored bars for each category

**Use when:**
- Comparing options
- Tracking progress
- Visualizing statistics
- Analyzing data

## Advanced Tips

### Maximizing Memory Features

1. **Be Specific in Searches**
   ```
   search "neural networks"  # Better than just "neural"
   ```

2. **Regular Memory Checks**
   ```
   memory  # Check how many conversations are stored
   ```

3. **Clear When Needed**
   - Clear memory when switching topics
   - Start fresh for new projects

### Getting Better AI Responses

1. **Provide Context**
   - The AI remembers previous conversations
   - Build on previous discussions
   
2. **Ask for Visualizations**
   ```
   "Can you create a mind map of programming languages?"
   "Show me a flowchart for the software development process"
   ```

3. **Request Clarifications**
   - Don't hesitate to ask follow-up questions
   - Request examples or more details

### Organizing Your Visualizations

The assistant saves all visualizations in the `visualizations/` directory with timestamps. You can:

1. **Organize by Project**
   - Move visualization files to project folders
   - Rename files with descriptive names

2. **Review Later**
   - Keep visualizations for study materials
   - Use them in presentations
   - Share with others

3. **Create Collections**
   - Group related visualizations
   - Build a visual knowledge base

## Troubleshooting

### Common Issues

**"OPENAI_API_KEY not found"**
- Solution: Create `.env` file with your API key
- Check: Make sure `.env` is in the same directory as `main.py`

**"Module not found"**
- Solution: Run `pip install -r requirements.txt`
- Check: Make sure you're in the correct directory

**Visualizations not creating**
- Solution: Check the `visualizations/` directory
- Check: Look for error messages in the console
- Try: Run `examples.py` to test without API key

**Assistant not remembering context**
- Check: Memory is enabled (default)
- Solution: Don't use `clear` unless intentionally resetting
- Note: Memory is limited to recent messages

## Best Practices

### For Daily Use

1. **Start with a Goal**
   - Know what you want to accomplish
   - Ask focused questions

2. **Use Memory Effectively**
   - Build on previous conversations
   - Search when you forget something

3. **Request Visuals**
   - Ask for visualizations when learning
   - Use appropriate visualization types

4. **Review and Organize**
   - Periodically review saved conversations
   - Organize visualization files
   - Clear memory when switching contexts

### For Learning

1. **Break Down Topics**
   - Start with overview questions
   - Drill down into details
   - Request visualizations for complex parts

2. **Connect Ideas**
   - Use concept maps to see relationships
   - Build on previous knowledge
   - Ask comparative questions

3. **Practice Recall**
   - Search for topics you've discussed
   - Test your understanding
   - Ask the AI to quiz you

### For Projects

1. **Plan with Mind Maps**
   - Start with project goals
   - Branch out features and tasks
   - Visualize project structure

2. **Document Decisions**
   - Store important discussions
   - Record reasoning for choices
   - Search when revisiting topics

3. **Track Progress**
   - Use timelines for milestones
   - Create bar charts for metrics
   - Update visualizations as needed

## Example Workflows

### Learning a New Programming Language

```
1. You: "I want to learn Python. Where should I start?"
2. Assistant: [Provides learning path]
3. You: "visualize"
4. [Create flowchart of learning steps]
5. You: "Tell me more about Python data types"
6. [Continue conversation...]
7. You: "search data types"
8. [Review previous discussion]
```

### Planning a Project

```
1. You: "Help me plan a web application project"
2. Assistant: [Discusses components]
3. You: "visualize"
4. [Create mind map of project structure]
5. You: "What technologies should I use?"
6. [Discussion continues with context]
7. You: "Create a timeline for development"
8. [Generate project timeline]
```

### Studying for Exams

```
1. You: "Explain cellular respiration"
2. Assistant: [Explains the process]
3. You: "visualize"
4. [Create flowchart of the process]
5. You: "What's the difference between aerobic and anaerobic?"
6. [Detailed explanation]
7. [Later] You: "search respiration"
8. [Review all related conversations]
```

## Privacy and Security

- All conversations stored locally in JSON
- API key stored in `.env` file
- Add `.env` to `.gitignore` (already configured)
- No data sent to external services except OpenAI API
- You control when to clear memory

## Support

For issues or questions:
1. Check this guide first
2. Review the README.md
3. Run `examples.py` to verify setup
4. Check GitHub issues
5. Open a new issue with details

---

Happy learning with your Personal AI Assistant! 🧠✨
