import time
from functools import wraps

class RateLimiter:
    """Simple rate limiter to prevent hitting API limits"""
    
    def __init__(self, max_calls, time_window):
        """
        Initialize rate limiter
        
        Args:
            max_calls (int): Maximum number of calls allowed
            time_window (int): Time window in seconds
        """
        self.max_calls = max_calls
        self.time_window = time_window
        self.calls = []
    
    def __call__(self, func):
        """Decorator to rate limit a function"""
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            
            # Remove old calls outside time window
            self.calls = [call_time for call_time in self.calls 
                         if now - call_time < self.time_window]
            
            # Check if we're at limit
            if len(self.calls) >= self.max_calls:
                sleep_time = self.time_window - (now - self.calls[0])
                if sleep_time > 0:
                    print(f"Rate limit reached. Waiting {sleep_time:.2f} seconds...")
                    time.sleep(sleep_time)
                    self.calls = []
            
            # Record this call
            self.calls.append(time.time())
            
            # Execute the function
            return func(*args, **kwargs)
        
        return wrapper


def retry_on_error(max_retries=3, delay=1):
    """
    Decorator to retry a function if it fails
    
    Args:
        max_retries (int): Maximum number of retry attempts
        delay (int): Seconds to wait between retries
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise e
                    print(f"Attempt {attempt + 1} failed. Retrying in {delay}s...")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator