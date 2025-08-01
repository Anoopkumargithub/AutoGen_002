import os
from dotenv import load_dotenv
from autogen import ConversableAgent

load_dotenv()  # Load environment variables from .env file

agent = ConversableAgent(
    "chatbot",
    llm_config={
        "config_list": [{
            "model": "llama-3.1-8b-instant",
            "api_key": os.environ.get("GROQ_API_KEY"),
            "base_url": "https://api.groq.com/openai/v1"
        }]
    },
    code_execution_config=False,  # Turn off code execution, by default it is off.
    function_map=None,  # No registered functions, by default it is None.
    human_input_mode="NEVER",  # Never ask for human input.
)

reply = agent.generate_reply(messages=[{"content": "Tell me a joke.", "role": "user"}])
print(reply)