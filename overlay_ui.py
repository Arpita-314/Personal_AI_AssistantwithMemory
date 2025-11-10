"""
Invisible overlay UI for displaying hints and solutions
"""
import tkinter as tk
from tkinter import ttk, scrolledtext
from typing import Dict, List, Optional

class InvisibleOverlay:
    """Semi-transparent overlay window for displaying interview assistance"""
    
    def __init__(self, width: int, height: int, opacity: float, capture_callback=None):
        self.width = width
        self.height = height
        self.opacity = opacity
        self.visible = False
        self.capture_callback = capture_callback
        
        # Create main window
        self.root = tk.Tk()
        self.root.title("Interview Assistant")
        
        # Configure window properties
        self._setup_window()
        
        # Create UI elements
        self._create_widgets()
        
        # Hide by default
        self.hide()
    
    def _setup_window(self):
        """Setup window properties"""
        # Set window size
        self.root.geometry(f"{self.width}x{self.height}")
        
        # Make window stay on top
        self.root.attributes('-topmost', True)
        
        # Set transparency
        self.root.attributes('-alpha', self.opacity)
        
        # Position in top-right corner
        screen_width = self.root.winfo_screenwidth()
        x_position = screen_width - self.width - 20
        self.root.geometry(f"+{x_position}+20")
        
        # Style
        self.root.configure(bg='#1e1e1e')
    
    def _create_widgets(self):
        """Create UI widgets"""
        # Title bar
        title_frame = tk.Frame(self.root, bg='#2d2d2d', height=30)
        title_frame.pack(fill=tk.X, pady=(0, 5))
        
        title_label = tk.Label(
            title_frame,
            text="🔍 Interview Assistant",
            bg='#2d2d2d',
            fg='#00ff00',
            font=('Arial', 10, 'bold')
        )
        title_label.pack(side=tk.LEFT, padx=10, pady=5)
        
        # Close button
        close_btn = tk.Button(
            title_frame,
            text="✕",
            command=self.hide,
            bg='#2d2d2d',
            fg='#ff0000',
            font=('Arial', 12, 'bold'),
            border=0,
            cursor='hand2'
        )
        close_btn.pack(side=tk.RIGHT, padx=5)
        
        # Notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Hints tab
        self.hints_frame = self._create_hints_tab()
        self.notebook.add(self.hints_frame, text="💡 Hints")
        
        # Solution tab
        self.solution_frame = self._create_solution_tab()
        self.notebook.add(self.solution_frame, text="✅ Solution")
        
        # Memory tab
        self.memory_frame = self._create_memory_tab()
        self.notebook.add(self.memory_frame, text="📚 Memory")
        
        # Control buttons frame
        control_frame = tk.Frame(self.root, bg='#2d2d2d')
        control_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.capture_btn = tk.Button(
            control_frame,
            text="📸 Capture & Analyze",
            bg='#0078d4',
            fg='#ffffff',
            font=('Arial', 9, 'bold'),
            cursor='hand2',
            border=0,
            padx=10,
            pady=5,
            command=self._on_capture_click
        )
        self.capture_btn.pack(fill=tk.X)
        
        # Status bar
        self.status_label = tk.Label(
            self.root,
            text="Ready",
            bg='#2d2d2d',
            fg='#aaaaaa',
            font=('Arial', 8),
            anchor=tk.W
        )
        self.status_label.pack(fill=tk.X, padx=5, pady=2)
    
    def _create_hints_tab(self) -> tk.Frame:
        """Create hints tab"""
        frame = tk.Frame(self.notebook, bg='#1e1e1e')
        
        # Hints display
        self.hints_text = scrolledtext.ScrolledText(
            frame,
            wrap=tk.WORD,
            bg='#2d2d2d',
            fg='#ffffff',
            font=('Consolas', 10),
            height=15
        )
        self.hints_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Buttons
        btn_frame = tk.Frame(frame, bg='#1e1e1e')
        btn_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.reveal_btn = tk.Button(
            btn_frame,
            text="🔓 Reveal Next Hint",
            command=self.reveal_next_hint,
            bg='#0078d4',
            fg='#ffffff',
            font=('Arial', 9),
            cursor='hand2'
        )
        self.reveal_btn.pack(fill=tk.X)
        
        return frame
    
    def _create_solution_tab(self) -> tk.Frame:
        """Create solution tab"""
        frame = tk.Frame(self.notebook, bg='#1e1e1e')
        
        # Solution display
        self.solution_text = scrolledtext.ScrolledText(
            frame,
            wrap=tk.WORD,
            bg='#2d2d2d',
            fg='#ffffff',
            font=('Consolas', 9),
            height=20
        )
        self.solution_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Complexity info
        self.complexity_label = tk.Label(
            frame,
            text="Complexity: Time - O(?), Space - O(?)",
            bg='#1e1e1e',
            fg='#ffa500',
            font=('Arial', 9)
        )
        self.complexity_label.pack(fill=tk.X, padx=5, pady=2)
        
        return frame
    
    def _create_memory_tab(self) -> tk.Frame:
        """Create memory tab"""
        frame = tk.Frame(self.notebook, bg='#1e1e1e')
        
        # Recent questions list
        self.memory_text = scrolledtext.ScrolledText(
            frame,
            wrap=tk.WORD,
            bg='#2d2d2d',
            fg='#ffffff',
            font=('Consolas', 9),
            height=20
        )
        self.memory_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        return frame
    
    def display_analysis(self, analysis: Dict, question: str):
        """Display analysis results"""
        self.current_analysis = analysis
        self.current_hints_revealed = 0
        
        # Clear previous content
        self.hints_text.delete(1.0, tk.END)
        self.solution_text.delete(1.0, tk.END)
        
        # Display question
        self.hints_text.insert(tk.END, f"Question:\n{question}\n\n", 'question')
        self.hints_text.insert(tk.END, "💡 Click 'Reveal Next Hint' to see hints\n", 'info')
        
        # Display solution
        self.solution_text.insert(tk.END, f"Solution:\n\n{analysis['solution']}\n\n")
        self.solution_text.insert(tk.END, f"Explanation:\n{analysis['explanation']}\n")
        
        # Update complexity
        time_comp = analysis['complexity'].get('time', 'O(?)')
        space_comp = analysis['complexity'].get('space', 'O(?)')
        self.complexity_label.config(
            text=f"Complexity: Time - {time_comp}, Space - {space_comp} | Difficulty: {analysis['difficulty']}"
        )
        
        self.show()
    
    def reveal_next_hint(self):
        """Reveal next hint progressively"""
        if not hasattr(self, 'current_analysis'):
            return
        
        hints = self.current_analysis.get('hints', [])
        if self.current_hints_revealed < len(hints):
            hint = hints[self.current_hints_revealed]
            self.hints_text.insert(tk.END, f"\nHint {self.current_hints_revealed + 1}:\n{hint}\n", 'hint')
            self.current_hints_revealed += 1
            
            if self.current_hints_revealed >= len(hints):
                self.reveal_btn.config(state=tk.DISABLED, text="All hints revealed")
        else:
            self.reveal_btn.config(state=tk.DISABLED, text="All hints revealed")
    
    def display_memory(self, memory_entries: List[Dict]):
        """Display memory entries"""
        self.memory_text.delete(1.0, tk.END)
        
        if not memory_entries:
            self.memory_text.insert(tk.END, "No stored questions yet.\n")
            return
        
        for i, entry in enumerate(reversed(memory_entries[-10:]), 1):
            self.memory_text.insert(tk.END, f"\n{i}. [{entry['difficulty']}] {entry['language']}\n", 'header')
            
            # Truncate long questions
            question = entry['question'][:100] + "..." if len(entry['question']) > 100 else entry['question']
            self.memory_text.insert(tk.END, f"{question}\n")
            self.memory_text.insert(tk.END, f"Date: {entry['timestamp'][:10]}\n", 'date')
    
    def update_status(self, message: str):
        """Update status bar"""
        self.status_label.config(text=message)
    
    def show(self):
        """Show the overlay"""
        self.root.deiconify()
        self.visible = True
    
    def hide(self):
        """Hide the overlay"""
        self.root.withdraw()
        self.visible = False
    
    def toggle(self):
        """Toggle overlay visibility"""
        if self.visible:
            self.hide()
        else:
            self.show()
    
    def _on_capture_click(self):
        """Handle capture button click"""
        if self.capture_callback:
            import threading
            threading.Thread(target=self.capture_callback, daemon=True).start()
    
    def run(self):
        """Start the UI event loop"""
        self.root.mainloop()
