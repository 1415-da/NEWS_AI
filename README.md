# NEWS_AI - AI-Powered News Research and Writing Crew

A CrewAI-powered system that uses Google Gemini models to research and write news articles about trending topics.

## Setup Instructions

### Configuration

Edit the `config.py` file in the root directory and replace the placeholder values with your actual API keys:

```python
# Google API Key for Gemini models
GOOGLE_API_KEY = "your_actual_google_api_key_here"

# Serper API Key for web search functionality
SERPER_API_KEY = "your_actual_serper_api_key_here"
```

### Getting API Keys

#### Google API Key
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the key and paste it in the `config.py` file

#### Serper API Key (for web search)
1. Go to [Serper.dev](https://serper.dev/)
2. Sign up and get your API key
3. Copy the key and paste it in the `config.py` file

### Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the crew:
```bash
python crewgooglegemini/crew.py
```

### Troubleshooting

If you encounter authentication errors:
1. Make sure your `GOOGLE_API_KEY` is set correctly in the `config.py` file
2. Ensure you have installed all dependencies from `requirements.txt`
3. The model name format has been updated to work with CrewAI's LiteLLM integration
4. Make sure your API keys are valid and have the necessary permissions

## Project Structure

```
NEWS_AI/
├── crewgooglegemini/
│   ├── agents.py      # AI agents configuration
│   ├── crew.py        # Main crew execution
│   ├── tasks.py       # Task definitions
│   └── tools.py       # Web search tools
├── config.py          # API key configuration
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## Features

- **AI Research Agent**: Uncovers groundbreaking technologies and trends
- **AI Writer Agent**: Creates compelling news articles
- **Web Search Integration**: Uses Serper.dev for real-time information
- **Google Gemini Integration**: Powered by Google's latest AI models
- **Sequential Processing**: Agents work together to research and write