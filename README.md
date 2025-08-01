# AutoGen AI Agents Project

This project demonstrates the use of Microsoft AutoGen framework with Groq's Llama 3.1 model to create conversational AI agents with different roles and capabilities.

## Overview

The project includes several examples of AI agents:
- **Basic chatbot** - Simple conversational agent
- **Role-based conversation** - Multi-agent system with student-teacher interaction
- **Guardrail system** - Content verification and safety checking

## Features

- 🤖 Multi-agent conversations using AutoGen
- 🦙 Integration with Groq's Llama 3.1-8B-Instant model
- 🛡️ Built-in content verification and safety guardrails
- 📚 Educational content generation and review
- ⚡ Fast inference with Groq API
- 🔧 Configurable agent roles and behaviors

## Prerequisites

- Python 3.8+
- Groq API key
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd AutoGen_002
```

2. Create and activate a virtual environment:
```bash
python -m venv autogen002
source autogen002/bin/activate  # On Linux/Mac
# or
autogen002\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_groq_api_key_here
```

## Project Structure

```
AutoGen_002/
├── sample.py              # Basic OpenAI example (for reference)
├── sample_GROQ.py         # Basic Groq integration example
├── Role_conversable.py    # Multi-agent role-based conversation
├── requirements.txt       # Python dependencies
├── pyproject.toml        # Project configuration
├── .env                  # Environment variables (create this)
├── README.md             # Project documentation
└── autogen002/           # Virtual environment directory
```

## Usage

### Basic Groq Agent Example

Run the basic chatbot example:
```bash
python sample_GROQ.py
```

This demonstrates a simple agent that tells jokes using the Groq API.

### Multi-Agent Role-Based Conversation

Run the educational conversation example:
```bash
python Role_conversable.py
```

This example features:
- **Joe** (Student) - Asks questions about Agentic AI
- **Cathy** (Teacher) - Provides educational explanations
- **Guards** (Reviewer) - Verifies content quality and safety

### Expected Output

The role-based conversation will show:
1. Joe asking Cathy to teach about Agentic AI
2. Cathy providing comprehensive explanations
3. Guards reviewing the educational content for accuracy and safety

## Configuration

### Agent Roles

Each agent is configured with specific roles:

- **Student Agent (Joe)**: Curious learner asking questions
- **Teacher Agent (Cathy)**: Knowledgeable assistant providing explanations
- **Guardian Agent (Guards)**: Content reviewer ensuring quality and safety

### Model Configuration

All agents use the same Groq configuration:
```python
llm_config={
    "config_list": [{
        "model": "llama-3.1-8b-instant",
        "api_key": os.environ.get("GROQ_API_KEY"),
        "base_url": "https://api.groq.com/openai/v1",
        "price": [0.00005, 0.00008]  # Custom pricing to avoid warnings
    }]
}
```

## Key Features Explained

### Warning Suppression
The project includes logging configuration to suppress AutoGen cost tracking warnings:
```python
import logging
logging.getLogger("autogen.oai.client").setLevel(logging.ERROR)
```

### Custom Pricing
Custom pricing is configured to avoid model not found warnings:
```python
"price": [0.00005, 0.00008]  # [prompt_price_per_1k, completion_price_per_1k]
```

### Conversation Flow
- Maximum turns are limited to prevent infinite conversations
- Human input is disabled (`human_input_mode="NEVER"`)
- Agents respond automatically based on their system messages

## Troubleshooting

### Common Issues

1. **API Key Error**: Ensure your `.env` file contains a valid `GROQ_API_KEY`
2. **Import Errors**: Make sure all dependencies are installed via `pip install -r requirements.txt`
3. **Virtual Environment**: Ensure the virtual environment is activated before running scripts

### Debug Mode

To see more detailed output, you can modify the logging level:
```python
logging.getLogger("autogen.oai.client").setLevel(logging.DEBUG)
```

## Dependencies

Main dependencies include:
- `autogen` - Microsoft AutoGen framework
- `python-dotenv` - Environment variable management
- `groq` - Groq API client (if used directly)

See `requirements.txt` for complete dependency list.

## API Usage

This project uses the Groq API which offers:
- Fast inference with Llama models
- Competitive pricing
- OpenAI-compatible API format

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

[Add your license information here]

## Acknowledgments

- Microsoft AutoGen framework
- Groq for fast AI inference
- Meta's Llama 3.1 model

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review AutoGen documentation
3. Check Groq API documentation
4. Open an issue in this repository

---

**Note**: This project is for educational and demonstration purposes. Always review AI-generated content for accuracy and appropriateness in production use cases.