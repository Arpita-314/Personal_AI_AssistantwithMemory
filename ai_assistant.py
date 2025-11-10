"""
AI Assistant Module
Handles interactions with OpenAI API and integrates memory and visual features.
"""

import os
from typing import List, Dict, Optional
from openai import OpenAI
from memory_manager import MemoryManager
from visual_helper import VisualHelper


class AIAssistant:
    """AI-powered personal assistant with memory and visual learning support."""
    
    def __init__(self, api_key: Optional[str] = None, memory_manager: Optional[MemoryManager] = None,
                 visual_helper: Optional[VisualHelper] = None):
        """
        Initialize the AI Assistant.
        
        Args:
            api_key: OpenAI API key (if None, uses OPENAI_API_KEY env var)
            memory_manager: MemoryManager instance
            visual_helper: VisualHelper instance
        """
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OpenAI API key not provided. Set OPENAI_API_KEY environment variable.")
        
        self.client = OpenAI(api_key=self.api_key)
        self.memory_manager = memory_manager or MemoryManager()
        self.visual_helper = visual_helper or VisualHelper()
        
        self.system_prompt = """You are a helpful personal AI assistant with memory capabilities and a focus on visual learning.
        
Your capabilities include:
1. Remembering previous conversations and context
2. Helping visual learners by creating diagrams, mind maps, concept maps, and flowcharts
3. Organizing information in structured, visual ways
4. Breaking down complex topics into visual representations

When users ask for visual aids, suggest appropriate visualizations:
- Concept maps for related ideas
- Mind maps for brainstorming
- Flowcharts for processes and steps
- Timelines for chronological events
- Bar charts for comparisons

Be concise, friendly, and focused on helping users learn and remember information effectively."""
    
    def chat(self, user_message: str, include_context: bool = True) -> str:
        """
        Chat with the AI assistant.
        
        Args:
            user_message: User's message
            include_context: Whether to include conversation history
            
        Returns:
            Assistant's response
        """
        # Store user message in memory
        self.memory_manager.add_memory("user", user_message)
        
        # Prepare messages for API
        messages = [{"role": "system", "content": self.system_prompt}]
        
        if include_context:
            # Add recent conversation context
            context = self.memory_manager.get_conversation_context(max_messages=10)
            messages.extend(context)
        else:
            messages.append({"role": "user", "content": user_message})
        
        try:
            # Call OpenAI API
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=500,
                temperature=0.7
            )
            
            assistant_message = response.choices[0].message.content
            
            # Store assistant response in memory
            self.memory_manager.add_memory("assistant", assistant_message)
            
            return assistant_message
            
        except Exception as e:
            error_msg = f"Error communicating with AI: {str(e)}"
            return error_msg
    
    def search_memory(self, keyword: str) -> List[Dict]:
        """
        Search conversation memory for a keyword.
        
        Args:
            keyword: Keyword to search for
            
        Returns:
            List of matching memory entries
        """
        return self.memory_manager.search_memories(keyword)
    
    def get_memory_summary(self) -> str:
        """Get a summary of stored memories."""
        return self.memory_manager.get_summary()
    
    def create_visualization(self, viz_type: str, data: Dict, title: str = "") -> str:
        """
        Create a visualization based on type and data.
        
        Args:
            viz_type: Type of visualization (concept_map, mind_map, flowchart, timeline, bar_chart)
            data: Data for the visualization
            title: Title for the visualization
            
        Returns:
            Path to the saved visualization or error message
        """
        try:
            if viz_type == "concept_map":
                return self.visual_helper.create_concept_map(data, title or "Concept Map")
            elif viz_type == "mind_map":
                central_idea = data.get('central_idea', 'Main Idea')
                branches = data.get('branches', {})
                return self.visual_helper.create_mind_map(central_idea, branches, title or "Mind Map")
            elif viz_type == "flowchart":
                steps = data.get('steps', [])
                return self.visual_helper.create_flowchart(steps, title or "Process Flowchart")
            elif viz_type == "timeline":
                events = data.get('events', [])
                return self.visual_helper.create_timeline(events, title or "Timeline")
            elif viz_type == "bar_chart":
                chart_data = data.get('data', {})
                xlabel = data.get('xlabel', 'Categories')
                ylabel = data.get('ylabel', 'Values')
                return self.visual_helper.create_bar_chart(chart_data, title or "Bar Chart", xlabel, ylabel)
            else:
                return f"Unknown visualization type: {viz_type}"
        except Exception as e:
            return f"Error creating visualization: {str(e)}"
