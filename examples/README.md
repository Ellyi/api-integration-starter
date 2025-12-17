# Examples

This folder contains usage examples for the AI API Integration Starter Kit.

## Files

- `basic_usage.py` - Simple examples showing how to use Claude and OpenAI clients
- `advanced_usage.py` - Advanced examples with rate limiting and error handling

## Setup

Before running examples, make sure you have:

1. Created a `.env` file with your API keys (copy from `.env.example`)
2. Installed dependencies: `pip install -r requirements.txt`

## Running Examples
```bash
# Basic usage
python examples/basic_usage.py

# Advanced usage
python examples/advanced_usage.py
```

## Notes

- Examples require valid API keys in `.env` file
- Advanced example demonstrates rate limiting (5 calls per 10 seconds)
- All examples include error handling