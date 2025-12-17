"""
Basic usage examples for AI API Integration Starter Kit
"""

import sys
import os

# Add parent directory to path so we can import our modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from integrations import ClaudeClient, OpenAIClient

def claude_example():
    """Example using Claude API"""
    print("\n=== Claude Example ===")
    
    try:
        # Create client
        claude = ClaudeClient()
        
        # Send message
        response = claude.send_message("What is Python in one sentence?")
        
        print(f"Claude: {response}")
        
    except Exception as e:
        print(f"Error: {e}")


def openai_example():
    """Example using OpenAI API"""
    print("\n=== OpenAI Example ===")
    
    try:
        # Create client
        gpt = OpenAIClient()
        
        # Send message
        response = gpt.send_message("What is Python in one sentence?")
        
        print(f"GPT: {response}")
        
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("AI API Integration Starter Kit - Basic Examples")
    print("=" * 50)
    
    # Run examples
    claude_example()
    openai_example()