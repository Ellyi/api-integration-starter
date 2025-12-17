"""
Advanced usage examples with rate limiting and retry logic
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from integrations import ClaudeClient
from integrations.utils import RateLimiter, retry_on_error


# Apply rate limiter: max 5 calls per 10 seconds
@RateLimiter(max_calls=5, time_window=10)
@retry_on_error(max_retries=3, delay=2)
def rate_limited_call(client, message):
    """Make a rate-limited API call with retry logic"""
    return client.send_message(message)


def advanced_example():
    """Example with rate limiting and error handling"""
    print("\n=== Advanced Example: Rate Limiting ===")
    
    try:
        claude = ClaudeClient()
        
        # Make 7 calls (will trigger rate limit after 5th)
        for i in range(7):
            print(f"\nCall {i+1}:")
            response = rate_limited_call(claude, f"Count to {i+1}")
            print(f"Response: {response[:50]}...")  # First 50 chars
            
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("AI API Integration Starter Kit - Advanced Examples")
    print("=" * 50)
    
    advanced_example()