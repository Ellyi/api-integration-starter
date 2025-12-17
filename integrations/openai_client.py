import openai
from config import Config

class OpenAIClient:
    """Client for interacting with OpenAI API"""
    
    def __init__(self):
        """Initialize OpenAI client with API key from config"""
        Config.validate()
        self.client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)
    
    def send_message(self, message, model="gpt-4o", max_tokens=1024):
        """
        Send a message to OpenAI and get response
        
        Args:
            message (str): The message to send
            model (str): OpenAI model to use
            max_tokens (int): Maximum tokens in response
            
        Returns:
            str: OpenAI's response text
        """
        try:
            response = self.client.chat.completions.create(
                model=model,
                max_tokens=max_tokens,
                messages=[
                    {"role": "user", "content": message}
                ]
            )
            return response.choices[0].message.content
            
        except openai.APIError as e:
            return f"API Error: {str(e)}"
        except Exception as e:
            return f"Unexpected error: {str(e)}"