"""
Quick test to verify all components work
"""

from config import Config
from integrations import ClaudeClient, OpenAIClient

def test_setup():
    """Test that everything is configured correctly"""
    print("Testing API Integration Starter Kit...\n")
    
    # Test 1: Config
    print("✅ Config module loads")
    
    # Test 2: Claude Client
    try:
        claude = ClaudeClient()
        print("✅ ClaudeClient initializes")
    except ValueError as e:
        print(f"⚠️  ClaudeClient needs API key: {e}")
    except Exception as e:
        print(f"❌ ClaudeClient error: {e}")
    
    # Test 3: OpenAI Client
    try:
        gpt = OpenAIClient()
        print("✅ OpenAIClient initializes")
    except ValueError as e:
        print(f"⚠️  OpenAIClient needs API key: {e}")
    except Exception as e:
        print(f"❌ OpenAIClient error: {e}")
    
    print("\n🎉 All tests complete!")
    print("Next step: Add real API keys to .env file")

if __name__ == "__main__":
    test_setup()