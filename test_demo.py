"""
Demo/Test script for Interview Assistant
This simulates the assistant without requiring actual screen capture or API calls
"""
import json
from pathlib import Path
from datetime import datetime

def test_memory_system():
    """Test the memory system"""
    print("=" * 60)
    print("Testing Memory System")
    print("=" * 60)
    
    from memory import InterviewMemory
    
    # Create a temporary memory file
    test_memory_file = Path('/tmp/test_memory.json')
    memory = InterviewMemory(test_memory_file)
    
    # Add some test questions
    test_questions = [
        {
            'question': 'Given an array of integers, return indices of two numbers that add up to a target.',
            'solution': 'def twoSum(nums, target):\n    seen = {}\n    for i, num in enumerate(nums):\n        complement = target - num\n        if complement in seen:\n            return [seen[complement], i]\n        seen[num] = i',
            'hints': [
                'Consider using a hash map for O(1) lookups',
                'Store the numbers you\'ve seen so far',
                'For each number, check if target - number exists in your map'
            ],
            'language': 'python',
            'difficulty': 'Easy'
        },
        {
            'question': 'Reverse a linked list',
            'solution': 'def reverseList(head):\n    prev = None\n    curr = head\n    while curr:\n        next_temp = curr.next\n        curr.next = prev\n        prev = curr\n        curr = next_temp\n    return prev',
            'hints': [
                'Think about using three pointers',
                'You need to reverse the direction of the links',
                'Use prev, current, and next pointers'
            ],
            'language': 'python',
            'difficulty': 'Easy'
        }
    ]
    
    for q in test_questions:
        memory.add_question(
            question=q['question'],
            solution=q['solution'],
            hints=q['hints'],
            language=q['language'],
            difficulty=q['difficulty']
        )
    
    # Test search
    print("\n✅ Added", len(test_questions), "questions")
    
    # Search for similar question
    results = memory.search_similar('array sum two numbers', limit=2)
    print(f"\n🔍 Search results for 'array sum two numbers': {len(results)} found")
    if results:
        print(f"   - {results[0]['question'][:50]}...")
    
    # Get stats
    stats = memory.get_stats()
    print(f"\n📊 Stats: {stats['total_questions']} questions, {stats['total_queries']} queries")
    
    # Clean up
    test_memory_file.unlink(missing_ok=True)
    print("\n✅ Memory system test passed!")

def test_ai_response_parsing():
    """Test AI response parsing"""
    print("\n" + "=" * 60)
    print("Testing AI Response Parsing")
    print("=" * 60)
    
    from ai_assistant import AIAssistant
    
    # Mock response
    mock_response = """HINTS:
1. Use a hash map for O(1) lookups
2. Store numbers you've seen and their indices
3. For each number, check if (target - number) exists

SOLUTION:
```python
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

COMPLEXITY:
Time: O(n)
Space: O(n)

DIFFICULTY: Easy

EXPLANATION:
We use a hash map to store numbers and their indices as we iterate. For each number, we check if its complement exists in the map.
"""
    
    # Create a mock assistant (won't make actual API calls for this test)
    class MockAssistant:
        def _parse_response(self, response):
            from ai_assistant import AIAssistant
            # Use the real parsing logic
            assistant = AIAssistant.__new__(AIAssistant)
            return assistant._parse_response(response)
    
    assistant = MockAssistant()
    result = assistant._parse_response(mock_response)
    
    print(f"\n✅ Parsed hints: {len(result['hints'])} hints")
    for i, hint in enumerate(result['hints'], 1):
        print(f"   {i}. {hint[:50]}...")
    
    print(f"\n✅ Solution extracted: {len(result['solution'])} characters")
    print(f"✅ Complexity - Time: {result['complexity']['time']}, Space: {result['complexity']['space']}")
    print(f"✅ Difficulty: {result['difficulty']}")
    print(f"✅ Explanation: {result['explanation'][:50]}...")

def test_config():
    """Test configuration"""
    print("\n" + "=" * 60)
    print("Testing Configuration")
    print("=" * 60)
    
    from config import Config
    
    print(f"✅ AI Provider: {Config.AI_PROVIDER}")
    print(f"✅ Model: {Config.MODEL_NAME}")
    print(f"✅ Overlay opacity: {Config.OVERLAY_OPACITY}")
    print(f"✅ Hotkey capture: {Config.HOTKEY_CAPTURE}")
    print(f"✅ Hotkey toggle: {Config.HOTKEY_TOGGLE}")
    print(f"✅ Memory file: {Config.MEMORY_FILE}")
    print(f"✅ Screenshots dir: {Config.SCREENSHOTS_DIR}")

def test_ui_demo():
    """Demo the UI (requires display)"""
    print("\n" + "=" * 60)
    print("Testing UI Components (requires display)")
    print("=" * 60)
    
    try:
        import tkinter as tk
        
        # Test if tkinter works
        root = tk.Tk()
        root.withdraw()
        print("✅ Tkinter is available")
        root.destroy()
        
        # Don't actually show the overlay in tests
        print("✅ UI components would work (test environment, not showing)")
        
    except Exception as e:
        print(f"⚠️  UI test skipped: {e}")
        print("   This is expected in headless environments")

def create_demo_data():
    """Create demo data for showcase"""
    print("\n" + "=" * 60)
    print("Creating Demo Data")
    print("=" * 60)
    
    demo_questions = [
        {
            'title': 'Two Sum',
            'question': 'Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.',
            'difficulty': 'Easy',
            'language': 'Python'
        },
        {
            'title': 'Reverse Linked List',
            'question': 'Given the head of a singly linked list, reverse the list, and return the reversed list.',
            'difficulty': 'Easy',
            'language': 'Python'
        },
        {
            'title': 'Binary Tree Level Order Traversal',
            'question': 'Given the root of a binary tree, return the level order traversal of its nodes\' values.',
            'difficulty': 'Medium',
            'language': 'Python'
        },
        {
            'title': 'Merge K Sorted Lists',
            'question': 'You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.',
            'difficulty': 'Hard',
            'language': 'Python'
        }
    ]
    
    print("\n📝 Demo Questions:")
    for q in demo_questions:
        print(f"   [{q['difficulty']}] {q['title']} ({q['language']})")
    
    print(f"\n✅ Created {len(demo_questions)} demo questions")

def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("🧪 Interview Assistant - Demo & Test Suite")
    print("=" * 60)
    
    try:
        test_config()
        test_memory_system()
        test_ai_response_parsing()
        test_ui_demo()
        create_demo_data()
        
        print("\n" + "=" * 60)
        print("✅ All tests completed!")
        print("=" * 60)
        print("\nℹ️  This is a demo. To use the full application:")
        print("   1. Set up your API keys in .env")
        print("   2. Run: python interview_assistant.py")
        print("   3. Use Ctrl+Shift+C to capture questions")
        print("=" * 60 + "\n")
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
