#!/usr/bin/env python3
"""
Personal AI Assistant with Memory and Visual Learning Support
Main application entry point
"""

import os
import sys
from dotenv import load_dotenv
from colorama import init, Fore, Style
from ai_assistant import AIAssistant
from memory_manager import MemoryManager
from visual_helper import VisualHelper


# Initialize colorama for cross-platform colored terminal output
init(autoreset=True)


def print_banner():
    """Print application banner."""
    banner = f"""
{Fore.CYAN}╔═══════════════════════════════════════════════════════════╗
║  Personal AI Assistant with Memory & Visual Learning      ║
║  Type 'help' for commands, 'exit' to quit                ║
╚═══════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(banner)


def print_help():
    """Print help information."""
    help_text = f"""
{Fore.YELLOW}Available Commands:{Style.RESET_ALL}
  {Fore.GREEN}chat{Style.RESET_ALL} - Chat with the AI assistant (default mode)
  {Fore.GREEN}search <keyword>{Style.RESET_ALL} - Search conversation history
  {Fore.GREEN}memory{Style.RESET_ALL} - Show memory summary
  {Fore.GREEN}visualize{Style.RESET_ALL} - Create visualizations
  {Fore.GREEN}clear{Style.RESET_ALL} - Clear conversation memory
  {Fore.GREEN}help{Style.RESET_ALL} - Show this help message
  {Fore.GREEN}exit{Style.RESET_ALL} - Exit the application

{Fore.YELLOW}Visualization Types:{Style.RESET_ALL}
  - Mind Map: For brainstorming and organizing ideas
  - Concept Map: For showing relationships between concepts
  - Flowchart: For processes and sequential steps
  - Timeline: For chronological events
  - Bar Chart: For comparing values

{Fore.YELLOW}Tips for Visual Learners:{Style.RESET_ALL}
  - Ask the AI to create visualizations for complex topics
  - Request mind maps to organize your thoughts
  - Use flowcharts to understand processes
  - Create concept maps to connect related ideas
"""
    print(help_text)


def visualize_menu(assistant: AIAssistant):
    """Interactive visualization menu."""
    print(f"\n{Fore.CYAN}Choose a visualization type:{Style.RESET_ALL}")
    print("1. Mind Map")
    print("2. Concept Map")
    print("3. Flowchart")
    print("4. Timeline")
    print("5. Bar Chart")
    print("0. Cancel")
    
    choice = input(f"\n{Fore.YELLOW}Enter your choice (0-5): {Style.RESET_ALL}").strip()
    
    if choice == '0':
        return
    
    # Example visualizations
    if choice == '1':
        print("\nCreating a sample Mind Map...")
        data = {
            'central_idea': 'Learning',
            'branches': {
                'Visual': ['Diagrams', 'Charts', 'Images', 'Videos'],
                'Auditory': ['Lectures', 'Podcasts', 'Discussions'],
                'Kinesthetic': ['Practice', 'Experiments', 'Activities'],
                'Reading': ['Books', 'Articles', 'Notes']
            }
        }
        filepath = assistant.create_visualization('mind_map', data, 'Learning Styles Mind Map')
        
    elif choice == '2':
        print("\nCreating a sample Concept Map...")
        data = {
            'AI': ['Machine Learning', 'Neural Networks', 'NLP'],
            'Machine Learning': ['Supervised', 'Unsupervised', 'Reinforcement'],
            'Applications': ['Computer Vision', 'Speech Recognition', 'Chatbots']
        }
        filepath = assistant.create_visualization('concept_map', data, 'AI Concepts')
        
    elif choice == '3':
        print("\nCreating a sample Flowchart...")
        data = {
            'steps': [
                'Start',
                'Define the problem',
                'Gather information',
                'Analyze data',
                'Develop solution',
                'Implement',
                'Test and verify',
                'Complete'
            ]
        }
        filepath = assistant.create_visualization('flowchart', data, 'Problem Solving Process')
        
    elif choice == '4':
        print("\nCreating a sample Timeline...")
        data = {
            'events': [
                {'date': '2020-01', 'description': 'Started learning Python'},
                {'date': '2020-06', 'description': 'Built first web app'},
                {'date': '2021-03', 'description': 'Learned machine learning'},
                {'date': '2021-09', 'description': 'Created AI project'},
                {'date': '2022-05', 'description': 'Advanced to deep learning'}
            ]
        }
        filepath = assistant.create_visualization('timeline', data, 'Learning Journey')
        
    elif choice == '5':
        print("\nCreating a sample Bar Chart...")
        data = {
            'data': {
                'Python': 85,
                'JavaScript': 70,
                'SQL': 75,
                'Machine Learning': 65,
                'Web Dev': 80
            },
            'xlabel': 'Skills',
            'ylabel': 'Proficiency (%)'
        }
        filepath = assistant.create_visualization('bar_chart', data, 'Skill Levels')
    
    else:
        print(f"{Fore.RED}Invalid choice!{Style.RESET_ALL}")
        return
    
    if filepath and os.path.exists(filepath):
        print(f"{Fore.GREEN}✓ Visualization saved to: {filepath}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}✗ Error creating visualization{Style.RESET_ALL}")


def main():
    """Main application loop."""
    # Load environment variables
    load_dotenv()
    
    # Check for API key
    if not os.getenv('OPENAI_API_KEY'):
        print(f"{Fore.RED}Error: OPENAI_API_KEY not found in environment variables.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Please create a .env file with your OpenAI API key.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}See .env.example for reference.{Style.RESET_ALL}")
        sys.exit(1)
    
    # Initialize components
    try:
        memory_manager = MemoryManager()
        visual_helper = VisualHelper()
        assistant = AIAssistant(memory_manager=memory_manager, visual_helper=visual_helper)
    except Exception as e:
        print(f"{Fore.RED}Error initializing assistant: {e}{Style.RESET_ALL}")
        sys.exit(1)
    
    print_banner()
    print(f"{Fore.GREEN}Assistant initialized successfully!{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Start chatting or type 'help' for available commands.{Style.RESET_ALL}\n")
    
    # Main interaction loop
    while True:
        try:
            user_input = input(f"{Fore.BLUE}You: {Style.RESET_ALL}").strip()
            
            if not user_input:
                continue
            
            # Parse commands
            if user_input.lower() == 'exit' or user_input.lower() == 'quit':
                print(f"\n{Fore.CYAN}Goodbye! Your conversation has been saved.{Style.RESET_ALL}")
                break
            
            elif user_input.lower() == 'help':
                print_help()
            
            elif user_input.lower() == 'memory':
                summary = assistant.get_memory_summary()
                print(f"\n{Fore.CYAN}Memory Summary:{Style.RESET_ALL}")
                print(summary)
                print()
            
            elif user_input.lower().startswith('search '):
                keyword = user_input[7:].strip()
                results = assistant.search_memory(keyword)
                print(f"\n{Fore.CYAN}Search Results for '{keyword}':{Style.RESET_ALL}")
                if results:
                    for i, memory in enumerate(results[-5:], 1):  # Show last 5 matches
                        print(f"\n{i}. [{memory['role']}] {memory['timestamp']}")
                        print(f"   {memory['content'][:200]}...")
                else:
                    print("No results found.")
                print()
            
            elif user_input.lower() == 'clear':
                confirm = input(f"{Fore.YELLOW}Are you sure you want to clear all memories? (yes/no): {Style.RESET_ALL}").lower()
                if confirm == 'yes':
                    assistant.memory_manager.clear_memories()
                    print(f"{Fore.GREEN}✓ Memory cleared!{Style.RESET_ALL}\n")
                else:
                    print(f"{Fore.YELLOW}Cancelled.{Style.RESET_ALL}\n")
            
            elif user_input.lower() == 'visualize':
                visualize_menu(assistant)
            
            else:
                # Regular chat
                print(f"\n{Fore.MAGENTA}Assistant: {Style.RESET_ALL}", end='')
                response = assistant.chat(user_input)
                print(response)
                print()
        
        except KeyboardInterrupt:
            print(f"\n\n{Fore.CYAN}Interrupted. Type 'exit' to quit.{Style.RESET_ALL}\n")
        except Exception as e:
            print(f"\n{Fore.RED}Error: {e}{Style.RESET_ALL}\n")


if __name__ == "__main__":
    main()
