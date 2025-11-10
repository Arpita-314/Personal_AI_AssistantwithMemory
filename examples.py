#!/usr/bin/env python3
"""
Example usage of the Personal AI Assistant
Demonstrates key features without requiring OpenAI API
"""

from memory_manager import MemoryManager
from visual_helper import VisualHelper
from datetime import datetime


def demo_memory_system():
    """Demonstrate the memory system."""
    print("=" * 60)
    print("DEMO: Memory System")
    print("=" * 60)
    
    memory = MemoryManager(memory_file="demo_memory.json", max_items=50)
    
    # Add some example memories
    print("\n1. Adding memories...")
    memory.add_memory("user", "What is machine learning?")
    memory.add_memory("assistant", "Machine learning is a subset of AI that enables systems to learn from data.")
    memory.add_memory("user", "Can you explain neural networks?")
    memory.add_memory("assistant", "Neural networks are computing systems inspired by biological neural networks.")
    
    print("✓ Added 4 conversation entries")
    
    # Get recent memories
    print("\n2. Retrieving recent memories...")
    recent = memory.get_recent_memories(3)
    for mem in recent:
        print(f"   [{mem['role']}] {mem['content'][:50]}...")
    
    # Search memories
    print("\n3. Searching for 'neural'...")
    results = memory.search_memories("neural")
    print(f"   Found {len(results)} matching entries")
    
    # Get summary
    print("\n4. Memory summary:")
    print("   " + memory.get_summary().replace("\n", "\n   "))
    
    print("\n✓ Memory system demo complete!")
    return memory


def demo_visualizations():
    """Demonstrate visualization generation."""
    print("\n" + "=" * 60)
    print("DEMO: Visual Learning Features")
    print("=" * 60)
    
    visual = VisualHelper(output_dir="demo_visualizations")
    created_files = []
    
    # 1. Mind Map
    print("\n1. Creating Mind Map...")
    mind_map_data = {
        'central_idea': 'AI Assistant',
        'branches': {
            'Memory': ['Store conversations', 'Context aware', 'Search history'],
            'Visual': ['Mind maps', 'Charts', 'Diagrams'],
            'AI': ['GPT-3.5', 'Natural language', 'Smart responses'],
            'Features': ['Easy to use', 'Helpful', 'Educational']
        }
    }
    filepath = visual.create_mind_map(
        mind_map_data['central_idea'],
        mind_map_data['branches'],
        'AI Assistant Features'
    )
    if filepath:
        created_files.append(filepath)
        print(f"   ✓ Created: {filepath}")
    
    # 2. Concept Map
    print("\n2. Creating Concept Map...")
    concept_data = {
        'Programming': ['Python', 'JavaScript', 'SQL'],
        'Data Science': ['Machine Learning', 'Statistics', 'Visualization'],
        'Web Dev': ['Frontend', 'Backend', 'APIs']
    }
    filepath = visual.create_concept_map(concept_data, 'Tech Skills Concept Map')
    if filepath:
        created_files.append(filepath)
        print(f"   ✓ Created: {filepath}")
    
    # 3. Flowchart
    print("\n3. Creating Flowchart...")
    steps = [
        'Open Assistant',
        'Type your question',
        'Receive AI response',
        'Request visualization if needed',
        'Save to memory',
        'Continue conversation'
    ]
    filepath = visual.create_flowchart(steps, 'Using the AI Assistant')
    if filepath:
        created_files.append(filepath)
        print(f"   ✓ Created: {filepath}")
    
    # 4. Timeline
    print("\n4. Creating Timeline...")
    events = [
        {'date': 'Week 1', 'description': 'Learn basics'},
        {'date': 'Week 2', 'description': 'Practice daily'},
        {'date': 'Week 3', 'description': 'Build projects'},
        {'date': 'Week 4', 'description': 'Advanced topics'},
        {'date': 'Week 5', 'description': 'Master skill'}
    ]
    filepath = visual.create_timeline(events, 'Learning Journey Timeline')
    if filepath:
        created_files.append(filepath)
        print(f"   ✓ Created: {filepath}")
    
    # 5. Bar Chart
    print("\n5. Creating Bar Chart...")
    chart_data = {
        'Monday': 5,
        'Tuesday': 7,
        'Wednesday': 6,
        'Thursday': 8,
        'Friday': 9,
        'Saturday': 4,
        'Sunday': 3
    }
    filepath = visual.create_bar_chart(
        chart_data,
        'Weekly Study Hours',
        'Day of Week',
        'Hours Studied'
    )
    if filepath:
        created_files.append(filepath)
        print(f"   ✓ Created: {filepath}")
    
    print(f"\n✓ Created {len(created_files)} visualizations!")
    print(f"✓ Check the 'demo_visualizations' directory")
    
    return created_files


def main():
    """Run all demos."""
    print("\n" + "=" * 60)
    print("Personal AI Assistant - Feature Demonstrations")
    print("=" * 60)
    
    try:
        # Demo memory system
        memory = demo_memory_system()
        
        # Demo visualizations
        files = demo_visualizations()
        
        # Summary
        print("\n" + "=" * 60)
        print("DEMO COMPLETE")
        print("=" * 60)
        print(f"\n✓ Memory system: Working")
        print(f"✓ Visualizations: {len(files)} created")
        print("\nThese demos show the core features without requiring an API key.")
        print("Run 'python main.py' with your OpenAI API key for the full experience!")
        
    except Exception as e:
        print(f"\n✗ Error during demo: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
