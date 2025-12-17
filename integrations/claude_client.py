import anthropic
from config import Config

class ClaudeClient:
    """Client for interacting with Claude API"""
    
    def __init__(self):
        """Initialize Claude client with API key from config"""
        Config.validate()  # Check if API key exists
        self.client = anthropic.Anthropic(api_key=Config.ANTHROPIC_API_KEY)
    
    def send_message(self, message, model="claude-sonnet-4-20250514", max_tokens=1024):
        """
        Send a message to Claude and get response
        
        Args:
            message (str): The message to send
            model (str): Claude model to use
            max_tokens (int): Maximum tokens in response
            
        Returns:
            str: Claude's response text
        """
        try:
            response = self.client.messages.create(
                model=model,
                max_tokens=max_tokens,
                messages=[
                    {"role": "user", "content": message}
                ]
            )
            return response.content[0].text
            
        except anthropic.APIError as e:
            return f"API Error: {str(e)}"
        except Exception as e:
            return f"Unexpected error: {str(e)}"

            