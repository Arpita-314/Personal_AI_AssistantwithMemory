"""
Memory Manager Module
Handles storing and retrieving conversation history and user notes.
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional


class MemoryManager:
    """Manages conversation memory and user notes."""
    
    def __init__(self, memory_file: str = "conversation_memory.json", max_items: int = 100):
        """
        Initialize the Memory Manager.
        
        Args:
            memory_file: Path to the JSON file storing memories
            max_items: Maximum number of memory items to retain
        """
        self.memory_file = memory_file
        self.max_items = max_items
        self.memories = self._load_memories()
    
    def _load_memories(self) -> List[Dict]:
        """Load memories from file."""
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return []
        return []
    
    def _save_memories(self) -> None:
        """Save memories to file."""
        try:
            with open(self.memory_file, 'w', encoding='utf-8') as f:
                json.dump(self.memories, f, indent=2, ensure_ascii=False)
        except IOError as e:
            print(f"Error saving memories: {e}")
    
    def add_memory(self, role: str, content: str, metadata: Optional[Dict] = None) -> None:
        """
        Add a new memory entry.
        
        Args:
            role: The role (user, assistant, system)
            content: The content of the memory
            metadata: Optional metadata dictionary
        """
        memory_entry = {
            "timestamp": datetime.now().isoformat(),
            "role": role,
            "content": content,
            "metadata": metadata or {}
        }
        
        self.memories.append(memory_entry)
        
        # Keep only the most recent items
        if len(self.memories) > self.max_items:
            self.memories = self.memories[-self.max_items:]
        
        self._save_memories()
    
    def get_recent_memories(self, count: int = 10) -> List[Dict]:
        """
        Get the most recent memories.
        
        Args:
            count: Number of recent memories to retrieve
            
        Returns:
            List of memory dictionaries
        """
        return self.memories[-count:]
    
    def search_memories(self, keyword: str) -> List[Dict]:
        """
        Search memories by keyword.
        
        Args:
            keyword: Keyword to search for
            
        Returns:
            List of matching memory dictionaries
        """
        keyword_lower = keyword.lower()
        return [
            memory for memory in self.memories
            if keyword_lower in memory['content'].lower()
        ]
    
    def get_conversation_context(self, max_messages: int = 10) -> List[Dict]:
        """
        Get recent conversation context for AI assistant.
        
        Args:
            max_messages: Maximum number of messages to include
            
        Returns:
            List of message dictionaries formatted for OpenAI API
        """
        recent = self.get_recent_memories(max_messages)
        return [
            {"role": mem["role"], "content": mem["content"]}
            for mem in recent
        ]
    
    def clear_memories(self) -> None:
        """Clear all memories."""
        self.memories = []
        self._save_memories()
    
    def get_summary(self) -> str:
        """Get a summary of stored memories."""
        if not self.memories:
            return "No memories stored yet."
        
        total = len(self.memories)
        oldest = self.memories[0]['timestamp']
        newest = self.memories[-1]['timestamp']
        
        return f"Total memories: {total}\nOldest: {oldest}\nNewest: {newest}"
