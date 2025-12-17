# AI API Integration Starter Kit

A professional, production-ready Python toolkit for integrating Claude, GPT, and other AI APIs into your applications. Built with best practices for security, error handling, and scalability.

## Features

- **Easy-to-use wrappers** for Claude (Anthropic) and OpenAI APIs
- **Environment-based configuration** - Keep API keys secure
- **Built-in error handling** - Graceful failure management
- **Rate limiting** - Prevent hitting API limits
- **Retry logic** - Automatic retry on transient failures
- **Type hints** - Better code completion and error detection
- **Comprehensive examples** - Learn by doing

## Why Use This Starter Kit?

Instead of writing the same API integration code repeatedly, use this battle-tested foundation:

- **Security first**: API keys never in code, proper .gitignore setup
- **Production ready**: Error handling, rate limiting, retry logic included
- **Developer friendly**: Clear documentation, working examples
- **Time saver**: 2-3 hours of setup work done for you
- **Extensible**: Easy to add new AI providers

## Quick Start

### Prerequisites

- Python 3.8 or higher
- API keys for Claude and/or OpenAI

### Installation

1. Clone this repository:
```bash
git clone https://github.com/YourUsername/api-integration-starter.git
cd api-integration-starter
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your API keys
# ANTHROPIC_API_KEY=your_anthropic_key_here
# OPENAI_API_KEY=your_openai_key_here
```

### Basic Usage
```python
from integrations import ClaudeClient, OpenAIClient

# Use Claude
claude = ClaudeClient()
response = claude.send_message("What is Python?")
print(response)

# Use OpenAI
gpt = OpenAIClient()
response = gpt.send_message("What is Python?")
print(response)
```

## Project Structure
```
api-integration-starter/
├── integrations/
│   ├── __init__.py          # Package initialization
│   ├── claude_client.py     # Claude API wrapper
│   ├── openai_client.py     # OpenAI API wrapper
│   └── utils.py             # Rate limiting & retry utilities
├── examples/
│   ├── basic_usage.py       # Simple examples
│   ├── advanced_usage.py    # Rate limiting & error handling
│   └── README.md            # Examples documentation
├── config.py                # Configuration management
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## Configuration

The starter kit uses environment variables for configuration. Copy `.env.example` to `.env` and set your values:
```env
# Required: API Keys
ANTHROPIC_API_KEY=your_anthropic_api_key_here
OPENAI_API_KEY=your_openai_api_key_here

# Optional: Rate Limiting
MAX_REQUESTS_PER_MINUTE=50
```

## Examples

### Basic Claude Integration
```python
from integrations import ClaudeClient

claude = ClaudeClient()
response = claude.send_message(
    "Explain quantum computing in simple terms",
    model="claude-sonnet-4-20250514",
    max_tokens=500
)
print(response)
```

### With Rate Limiting
```python
from integrations import ClaudeClient
from integrations.utils import RateLimiter

@RateLimiter(max_calls=5, time_window=10)
def safe_api_call(client, message):
    return client.send_message(message)

claude = ClaudeClient()
response = safe_api_call(claude, "Hello!")
```

### With Automatic Retry
```python
from integrations import OpenAIClient
from integrations.utils import retry_on_error

@retry_on_error(max_retries=3, delay=2)
def resilient_call(client, message):
    return client.send_message(message)

gpt = OpenAIClient()
response = resilient_call(gpt, "What is AI?")
```

See the `examples/` directory for more detailed usage patterns.

## Advanced Features

### Rate Limiting

Prevent hitting API rate limits with the built-in rate limiter:
```python
from integrations.utils import RateLimiter

# Allow max 10 calls per 60 seconds
@RateLimiter(max_calls=10, time_window=60)
def controlled_api_call(client, message):
    return client.send_message(message)
```

### Automatic Retry

Handle transient failures gracefully:
```python
from integrations.utils import retry_on_error

# Retry up to 5 times with 3-second delays
@retry_on_error(max_retries=5, delay=3)
def resilient_api_call(client, message):
    return client.send_message(message)
```

## Error Handling

All client methods include comprehensive error handling:
```python
claude = ClaudeClient()
response = claude.send_message("Hello")

# Returns either:
# - Successful response text
# - "API Error: [specific error message]"
# - "Unexpected error: [error details]"
```

## Requirements

- Python 3.8+
- anthropic>=0.18.0
- openai>=1.12.0
- python-dotenv>=1.0.0
- requests>=2.31.0

## Security Best Practices

✅ **API keys in .env file only** - Never commit to version control  
✅ **.gitignore configured** - Prevents accidental key exposure  
✅ **Environment validation** - Checks for required keys on startup  
✅ **Error messages sanitized** - No sensitive data in logs  

## Contributing

Contributions welcome! Please feel free to submit a Pull Request.

## License

MIT License - feel free to use this in your projects.

## Author

Built by [Your Name] - [Your Website/GitHub]

## Support

- 📧 Email: your.email@example.com
- 🐙 GitHub: [github.com/YourUsername](https://github.com/YourUsername)
- 💼 LinkedIn: [Your LinkedIn Profile]

---

**Need AI integration for your project? Let's talk!**