# Architecture Overview

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   Interview Assistant                        │
│                  (interview_assistant.py)                    │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              Main Application Loop                    │  │
│  │  - Coordinate all components                         │  │
│  │  - Handle user interactions                          │  │
│  │  - Manage application lifecycle                      │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   Screen     │    │   Overlay    │    │   Memory     │
│   Capture    │    │      UI      │    │   System     │
│ (screen_     │    │  (overlay_   │    │  (memory.py) │
│  capture.py) │    │    ui.py)    │    │              │
└──────────────┘    └──────────────┘    └──────────────┘
        │                   │                   │
        │                   │                   │
        ▼                   ▼                   ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  Tesseract   │    │   Tkinter    │    │     JSON     │
│     OCR      │    │   Widgets    │    │   Storage    │
└──────────────┘    └──────────────┘    └──────────────┘
        │
        │
        ▼
┌─────────────────────────────────────────────────────────┐
│                   AI Assistant                           │
│                 (ai_assistant.py)                        │
│                                                          │
│  ┌────────────────────┐      ┌────────────────────┐   │
│  │   OpenAI API       │      │   Anthropic API    │   │
│  │   - GPT-4          │  OR  │   - Claude 3       │   │
│  │   - GPT-3.5        │      │   - Claude 2       │   │
│  └────────────────────┘      └────────────────────┘   │
└─────────────────────────────────────────────────────────┘
        │
        │
        ▼
┌─────────────────────────────────────────────────────────┐
│                   Configuration                          │
│                    (config.py)                           │
│                                                          │
│  - API keys and settings                                │
│  - Environment variables                                │
│  - System configuration                                 │
└─────────────────────────────────────────────────────────┘
```

## Component Breakdown

### 1. Main Application (`interview_assistant.py`)
**Purpose:** Orchestrates all components and manages application lifecycle

**Responsibilities:**
- Initialize all components
- Setup global hotkeys (optional)
- Handle capture and analyze workflow
- Coordinate between UI, AI, and memory
- Manage application state

**Key Methods:**
- `capture_and_analyze()` - Main workflow for capturing and analyzing questions
- `toggle_overlay()` - Show/hide the overlay
- `_setup_hotkeys()` - Configure keyboard shortcuts

### 2. Screen Capture (`screen_capture.py`)
**Purpose:** Capture screen content and extract text

**Responsibilities:**
- Take screenshots of entire screen or regions
- Apply image preprocessing for better OCR
- Extract text using Tesseract OCR
- Save screenshots to disk

**Key Methods:**
- `capture_screen()` - Take screenshot
- `extract_text()` - OCR text extraction
- `_preprocess_image()` - Improve image quality

**Dependencies:**
- PyAutoGUI (screen capture)
- Pillow (image processing)
- OpenCV (preprocessing)
- Tesseract (OCR)

### 3. AI Assistant (`ai_assistant.py`)
**Purpose:** Interact with AI models to analyze questions

**Responsibilities:**
- Send questions to AI models
- Parse AI responses
- Generate progressive hints
- Extract solutions and complexity

**Supported Providers:**
- OpenAI (GPT-4, GPT-3.5-turbo)
- Anthropic (Claude 3, Claude 2)

**Key Methods:**
- `analyze_question()` - Full analysis with hints and solution
- `get_quick_hint()` - Single hint generation
- `_parse_response()` - Extract structured data from AI response

### 4. Overlay UI (`overlay_ui.py`)
**Purpose:** Display hints and solutions in a semi-transparent overlay

**Responsibilities:**
- Create semi-transparent window
- Display hints progressively
- Show solutions and explanations
- Display memory/history
- Handle user interactions

**Features:**
- 3 tabs: Hints, Solution, Memory
- Progressive hint revelation
- Complexity information
- Draggable window
- Adjustable opacity

**Key Methods:**
- `display_analysis()` - Show analysis results
- `reveal_next_hint()` - Progressive hint system
- `display_memory()` - Show past questions
- `toggle()` - Show/hide overlay

### 5. Memory System (`memory.py`)
**Purpose:** Store and retrieve past questions and solutions

**Responsibilities:**
- Persist Q&A to JSON file
- Search for similar questions
- Track statistics
- Manage history

**Storage Format:**
```json
{
  "questions": [
    {
      "id": 1,
      "timestamp": "2024-11-10T12:00:00",
      "question": "...",
      "solution": "...",
      "hints": ["...", "...", "..."],
      "language": "python",
      "difficulty": "Medium"
    }
  ],
  "stats": {
    "total_queries": 10
  }
}
```

**Key Methods:**
- `add_question()` - Store new question
- `search_similar()` - Find related questions
- `get_stats()` - Usage statistics
- `get_recent()` - Recent history

### 6. Configuration (`config.py`)
**Purpose:** Manage all configuration and settings

**Configuration Sources:**
1. Environment variables (`.env` file)
2. Default values
3. Runtime overrides

**Key Settings:**
- `OPENAI_API_KEY` / `ANTHROPIC_API_KEY`
- `AI_PROVIDER` (openai/anthropic)
- `MODEL_NAME` (gpt-4, claude-3-opus, etc.)
- `OVERLAY_OPACITY` (0.0 - 1.0)
- `HOTKEY_CAPTURE` / `HOTKEY_TOGGLE`
- `MEMORY_FILE` path
- `SCREENSHOTS_DIR` path

## Data Flow

### Capture and Analyze Workflow

```
1. User triggers capture (Ctrl+Shift+C or button click)
                │
                ▼
2. ScreenCapture.capture_screen()
                │
                ▼
3. ScreenCapture.extract_text() [OCR]
                │
                ▼
4. Memory.search_similar() [Check cache]
                │
        ┌───────┴───────┐
        │               │
        ▼               ▼
   Found in        Not found
   memory          in memory
        │               │
        │               ▼
        │    5. AIAssistant.analyze_question()
        │               │
        │               ▼
        │    6. Memory.add_question()
        │               │
        └───────┬───────┘
                │
                ▼
7. Overlay.display_analysis()
                │
                ▼
8. User interacts with hints/solution
```

### Progressive Hints System

```
Question received
        │
        ▼
AI generates 3 hints:
  1. Subtle (algorithm category)
  2. Moderate (specific approach)
  3. Revealing (implementation details)
        │
        ▼
User reveals progressively:
  Click 1 → Show Hint 1
  Click 2 → Show Hint 2
  Click 3 → Show Hint 3
        │
        ▼
User checks solution (if needed)
```

## Technology Stack

### Core Technologies
- **Language:** Python 3.8+
- **UI Framework:** Tkinter (built-in)
- **Image Processing:** Pillow, OpenCV
- **OCR:** Tesseract
- **AI APIs:** OpenAI, Anthropic

### Key Libraries

| Library | Purpose |
|---------|---------|
| pillow | Image capture and manipulation |
| pytesseract | OCR text extraction |
| pynput | Global hotkeys (optional) |
| openai | OpenAI API client |
| anthropic | Anthropic API client |
| pyautogui | Screen capture |
| opencv-python | Image preprocessing |
| numpy | Array operations |
| python-dotenv | Environment configuration |

## Design Patterns

### 1. Dependency Injection
Components receive dependencies via constructor:
```python
overlay = InvisibleOverlay(width, height, opacity, capture_callback)
```

### 2. Observer Pattern
UI updates via callbacks:
```python
self.overlay.update_status("Analyzing...")
```

### 3. Strategy Pattern
Multiple AI providers with same interface:
```python
if provider == 'openai':
    return self._call_openai(prompt)
else:
    return self._call_anthropic(prompt)
```

### 4. Singleton Configuration
Global config accessed via class:
```python
Config.API_KEY
Config.MODEL_NAME
```

## Security Considerations

### API Keys
- Stored in `.env` file (not committed)
- Loaded via python-dotenv
- Never logged or displayed

### Screenshots
- Saved locally only
- Configurable storage location
- Can be disabled

### Network
- HTTPS only for API calls
- No data sent to third parties
- AI providers' data policies apply

## Extension Points

### Adding New AI Provider

1. Add provider check in `ai_assistant.py`:
```python
elif self.provider == 'newprovider':
    self.client = NewProviderClient(api_key=api_key)
```

2. Implement provider-specific call:
```python
def _call_newprovider(self, prompt: str) -> str:
    # Implementation
```

3. Update config and documentation

### Adding New Feature Tab

1. In `overlay_ui.py`, add new tab:
```python
self.new_frame = self._create_new_tab()
self.notebook.add(self.new_frame, text="🆕 New")
```

2. Implement tab creation:
```python
def _create_new_tab(self) -> tk.Frame:
    # Implementation
```

### Custom Hotkeys

Modify `interview_assistant.py` hotkey setup or use library like `keyboard` for more complex shortcuts.

## Performance Considerations

### Optimization Points

1. **OCR Processing**
   - Image preprocessing improves accuracy
   - Can be slow for large images
   - Consider caching results

2. **AI API Calls**
   - Network latency (1-5 seconds)
   - API rate limits apply
   - Memory cache helps avoid repeated calls

3. **UI Responsiveness**
   - Heavy operations run in background threads
   - UI updates via event loop
   - Non-blocking capture

### Scaling Considerations

- Memory file grows with usage (consider rotation)
- Screenshot storage can fill disk
- API costs scale with usage

## Testing Strategy

### Unit Tests
- Individual component testing
- Mock external dependencies
- Test data validation

### Integration Tests
- Component interaction
- End-to-end workflows
- Error handling

### Manual Testing
- UI functionality
- Hotkey responsiveness
- Cross-platform compatibility

## Deployment

### Packaging Options

1. **Simple Distribution**
   ```bash
   zip -r interview-assistant.zip .
   ```

2. **Python Package**
   ```bash
   python setup.py install
   ```

3. **Executable (PyInstaller)**
   ```bash
   pyinstaller --onefile interview_assistant.py
   ```

## Future Enhancements

### Potential Features
- [ ] Voice input for questions
- [ ] Multiple language support for UI
- [ ] Code syntax highlighting
- [ ] Export to PDF/Markdown
- [ ] Cloud sync for memory
- [ ] Browser extension integration
- [ ] Real-time collaboration
- [ ] Video recording of solutions
- [ ] Integration with LeetCode/HackerRank
- [ ] Custom AI model fine-tuning

### Platform Support
- [x] Linux
- [x] macOS
- [x] Windows
- [ ] Mobile (iOS/Android)
- [ ] Web version

---

*Last Updated: 2024-11-10*
