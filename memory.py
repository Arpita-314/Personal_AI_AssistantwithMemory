"""
Memory system for storing and retrieving past interview questions and solutions
"""
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

class InterviewMemory:
    """Manages storage and retrieval of interview questions and solutions"""
    
    def __init__(self, memory_file: Path):
        self.memory_file = memory_file
        self.memory_data = self._load_memory()
    
    def _load_memory(self) -> Dict:
        """Load memory from file"""
        if self.memory_file.exists():
            try:
                with open(self.memory_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {'questions': [], 'stats': {'total_queries': 0}}
        return {'questions': [], 'stats': {'total_queries': 0}}
    
    def _save_memory(self):
        """Save memory to file"""
        with open(self.memory_file, 'w', encoding='utf-8') as f:
            json.dump(self.memory_data, f, indent=2, ensure_ascii=False)
    
    def add_question(self, question: str, solution: str, hints: List[str], 
                     language: str = 'python', difficulty: str = 'unknown'):
        """Add a new question and solution to memory"""
        entry = {
            'id': len(self.memory_data['questions']) + 1,
            'timestamp': datetime.now().isoformat(),
            'question': question,
            'solution': solution,
            'hints': hints,
            'language': language,
            'difficulty': difficulty
        }
        self.memory_data['questions'].append(entry)
        self.memory_data['stats']['total_queries'] += 1
        self._save_memory()
    
    def search_similar(self, query: str, limit: int = 5) -> List[Dict]:
        """Search for similar questions in memory"""
        # Simple keyword-based search
        query_lower = query.lower()
        results = []
        
        for entry in self.memory_data['questions']:
            question_lower = entry['question'].lower()
            # Calculate simple similarity score based on common words
            query_words = set(query_lower.split())
            question_words = set(question_lower.split())
            common_words = query_words.intersection(question_words)
            
            if common_words:
                score = len(common_words) / max(len(query_words), len(question_words))
                results.append((score, entry))
        
        # Sort by score and return top results
        results.sort(reverse=True, key=lambda x: x[0])
        return [entry for score, entry in results[:limit]]
    
    def get_stats(self) -> Dict:
        """Get memory statistics"""
        return {
            'total_questions': len(self.memory_data['questions']),
            'total_queries': self.memory_data['stats']['total_queries'],
            'languages': self._get_language_stats()
        }
    
    def _get_language_stats(self) -> Dict[str, int]:
        """Get statistics by programming language"""
        stats = {}
        for entry in self.memory_data['questions']:
            lang = entry.get('language', 'unknown')
            stats[lang] = stats.get(lang, 0) + 1
        return stats
    
    def get_recent(self, limit: int = 10) -> List[Dict]:
        """Get recent questions"""
        return self.memory_data['questions'][-limit:]
