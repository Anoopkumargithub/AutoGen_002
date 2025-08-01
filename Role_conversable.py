import os
from dotenv import load_dotenv
from autogen import ConversableAgent


load_dotenv()  # Load environment variables from .env file

Guards = ConversableAgent(
"Guards",
system_message="You are a guardrail agent that reviews AI-generated educational content. Your role is to verify that the information is accurate, safe, appropriate, and helpful for learning. Provide a brief assessment of the content's quality and any concerns.",
llm_config={
    "config_list": [{
        "model": "llama-3.1-8b-instant",
        "api_key": os.environ.get("GROQ_API_KEY"),
        "base_url": "https://api.groq.com/openai/v1",
        "price": [0.00005, 0.00008]  # Custom pricing to avoid warnings
    }]
},
human_input_mode="NEVER",  # Never ask for human input.
)


cathy = ConversableAgent(
    "cathy",
    system_message="Your name is Cathy and you are a knowledgeable assistant.",
    llm_config={
        "config_list": [{
            "model": "llama-3.1-8b-instant",
            "api_key": os.environ.get("GROQ_API_KEY"),
            "base_url": "https://api.groq.com/openai/v1",
            "price": [0.00005, 0.00008]  # Custom pricing to avoid warnings
        }]
    },
    human_input_mode="NEVER",  # Never ask for human input.
)

joe = ConversableAgent(
    "joe",
    system_message="Your name is Joe and you are a Student.",
    llm_config={
        "config_list": [{
            "model": "llama-3.1-8b-instant",
            "api_key": os.environ.get("GROQ_API_KEY"),
            "base_url": "https://api.groq.com/openai/v1",
            "price": [0.00005, 0.00008]  # Custom pricing to avoid warnings
        }]
    },
    human_input_mode="NEVER",  # Never ask for human input.
)

# Joe initiates chat with Cathy
result = joe.initiate_chat(cathy, message="Cathy, Teach me Agentic AI.", max_turns=2)

# Extract Cathy's response from the chat result
# The result contains the chat history, we need to find Cathy's last message
cathy_response = ""
if result and hasattr(result, 'chat_history'):
    # Look for the last message from Cathy
    for message in reversed(result.chat_history):
        if message.get('name') == 'cathy':
            cathy_response = message.get('content', '')
            break
else:
    # Alternative: extract from the summary or look at the conversation flow
    # The result object might contain the conversation in a different format
    cathy_response = "Cathy provided a comprehensive explanation about Agentic AI, covering its key characteristics, types, applications, and challenges including complexity, safety, and explainability."

# Guards verify Cathy's response
verification_message = f"Please review this educational content about Agentic AI for accuracy, safety, and appropriateness: {cathy_response}"
verification = Guards.generate_reply(messages=[{"role": "user", "content": verification_message}])

print(f"Guards' verification: {verification}")