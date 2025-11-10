"""
Main Interview Assistant Application
"""
import threading
from pynput import keyboard
from typing import Optional
import time

from config import Config
from memory import InterviewMemory
from screen_capture import ScreenCapture
from ai_assistant import AIAssistant
from overlay_ui import InvisibleOverlay

class InterviewAssistant:
    """Main application class that coordinates all components"""
    
    def __init__(self):
        """Initialize the interview assistant"""
        print("🚀 Initializing Interview Assistant...")
        
        # Validate configuration
        try:
            Config.validate()
        except ValueError as e:
            print(f"❌ Configuration error: {e}")
            print("Please check your .env file and ensure API keys are set.")
            raise
        
        # Initialize components
        self.memory = InterviewMemory(Config.MEMORY_FILE)
        self.screen_capture = ScreenCapture(Config.SCREENSHOTS_DIR, Config.TESSERACT_CMD)
        self.ai_assistant = AIAssistant(
            provider=Config.AI_PROVIDER,
            api_key=Config.OPENAI_API_KEY if Config.AI_PROVIDER == 'openai' else Config.ANTHROPIC_API_KEY,
            model=Config.MODEL_NAME
        )
        self.overlay = InvisibleOverlay(
            width=Config.OVERLAY_WIDTH,
            height=Config.OVERLAY_HEIGHT,
            opacity=Config.OVERLAY_OPACITY
        )
        
        # State
        self.processing = False
        self.last_question = ""
        
        print("✅ Interview Assistant initialized successfully!")
        print(f"📊 Memory: {len(self.memory.memory_data['questions'])} questions stored")
        print(f"🤖 AI Provider: {Config.AI_PROVIDER.upper()}")
        print(f"\n⌨️  Hotkeys:")
        print(f"   Capture & Analyze: {Config.HOTKEY_CAPTURE}")
        print(f"   Toggle Overlay: {Config.HOTKEY_TOGGLE}")
    
    def capture_and_analyze(self):
        """Capture screen and analyze the coding question"""
        if self.processing:
            print("⏳ Already processing a request...")
            return
        
        self.processing = True
        self.overlay.update_status("📸 Capturing screen...")
        
        try:
            # Capture screen and extract text
            print("📸 Capturing screen...")
            text, screenshot_path = self.screen_capture.capture_and_extract(save=True)
            
            if not text or len(text.strip()) < 20:
                print("⚠️  No meaningful text detected on screen")
                self.overlay.update_status("⚠️  No text detected")
                return
            
            print(f"📝 Extracted {len(text)} characters")
            print(f"💾 Screenshot saved: {screenshot_path}")
            
            # Check if similar question exists in memory
            self.overlay.update_status("🔍 Searching memory...")
            similar = self.memory.search_similar(text, limit=1)
            
            if similar and similar[0]['question'][:100] in text[:100]:
                print("📚 Found similar question in memory!")
                self.overlay.display_analysis(similar[0], text)
                self.overlay.display_memory(self.memory.get_recent())
                self.overlay.update_status("✅ Loaded from memory")
                return
            
            # Analyze with AI
            self.overlay.update_status("🤖 Analyzing with AI...")
            print("🤖 Analyzing question with AI...")
            analysis = self.ai_assistant.analyze_question(text)
            
            # Store in memory
            self.memory.add_question(
                question=text,
                solution=analysis['solution'],
                hints=analysis['hints'],
                difficulty=analysis['difficulty']
            )
            
            # Display results
            self.overlay.display_analysis(analysis, text)
            self.overlay.display_memory(self.memory.get_recent())
            self.overlay.update_status("✅ Analysis complete")
            
            print("✅ Analysis complete!")
            
        except Exception as e:
            error_msg = f"❌ Error: {str(e)}"
            print(error_msg)
            self.overlay.update_status(error_msg)
        
        finally:
            self.processing = False
    
    def toggle_overlay(self):
        """Toggle overlay visibility"""
        self.overlay.toggle()
        status = "visible" if self.overlay.visible else "hidden"
        print(f"👁️  Overlay {status}")
    
    def _setup_hotkeys(self):
        """Setup global hotkeys"""
        def on_activate_capture():
            print("\n🎯 Capture hotkey activated!")
            threading.Thread(target=self.capture_and_analyze, daemon=True).start()
        
        def on_activate_toggle():
            print("\n👁️  Toggle hotkey activated!")
            self.toggle_overlay()
        
        # Parse hotkey strings (simple implementation)
        # For production, use proper hotkey parsing
        try:
            # Setup keyboard listener
            def on_press(key):
                try:
                    # Check for Ctrl+Shift+C (capture)
                    if (hasattr(key, 'char') and key.char == 'c' and 
                        keyboard.Controller().pressed(keyboard.Key.ctrl) and
                        keyboard.Controller().pressed(keyboard.Key.shift)):
                        on_activate_capture()
                    # Check for Ctrl+Shift+H (toggle)
                    elif (hasattr(key, 'char') and key.char == 'h' and 
                          keyboard.Controller().pressed(keyboard.Key.ctrl) and
                          keyboard.Controller().pressed(keyboard.Key.shift)):
                        on_activate_toggle()
                except AttributeError:
                    pass
            
            # Start keyboard listener in background thread
            listener = keyboard.Listener(on_press=on_press)
            listener.daemon = True
            listener.start()
            
        except Exception as e:
            print(f"⚠️  Could not setup hotkeys: {e}")
            print("You can still use the overlay manually")
    
    def show_stats(self):
        """Show memory statistics"""
        stats = self.memory.get_stats()
        print("\n📊 Statistics:")
        print(f"   Total questions: {stats['total_questions']}")
        print(f"   Total queries: {stats['total_queries']}")
        print(f"   Languages: {stats['languages']}")
    
    def run(self):
        """Run the application"""
        print("\n🎬 Starting Interview Assistant...")
        print("The overlay is hidden by default. Use hotkeys to interact.\n")
        
        # Setup hotkeys
        self._setup_hotkeys()
        
        # Display initial memory
        self.overlay.display_memory(self.memory.get_recent())
        
        # Show stats
        self.show_stats()
        
        # Run UI (this blocks)
        try:
            self.overlay.run()
        except KeyboardInterrupt:
            print("\n👋 Shutting down...")

def main():
    """Main entry point"""
    try:
        app = InterviewAssistant()
        app.run()
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
