import os
import tempfile
import shutil

from autogen import ConversableAgent
from autogen.coding import LocalCommandLineCodeExecutor

# Create a temporary directory to store the code files.
temp_dir = tempfile.TemporaryDirectory()

# Create a local command line code executor.
executor = LocalCommandLineCodeExecutor(
    timeout=10,  # Timeout for each code execution in seconds.
    work_dir=temp_dir.name,  # Use the temporary directory to store the code files.
)

# Create an agent with code executor configuration.
code_executor_agent = ConversableAgent(
    "code_executor_agent",
    llm_config=False,  # Turn off LLM for this agent.
    code_execution_config={"executor": executor},  # Use the local command line code executor.
    human_input_mode="ALWAYS",  # Always take human input for this agent for safety.
)

message_with_code_block = """This is a message with code block.
The code block is below:
```python
import numpy as np
import matplotlib.pyplot as plt
x = np.random.randint(0, 100, 100)
y = np.random.randint(0, 100, 100)
plt.scatter(x, y)
plt.savefig('scatter.png')
print('Scatter plot saved to scatter.png')
```
This is the end of the message.
"""

# Generate a reply for the given code.
reply = code_executor_agent.generate_reply(messages=[{"role": "user", "content": message_with_code_block}])
print(reply)

# Show where files are saved
print(f"\n=== File Location Information ===")
print(f"Temporary directory: {temp_dir.name}")
print(f"Files created: {os.listdir(temp_dir.name)}")

# Show full path to the scatter plot
scatter_path = os.path.join(temp_dir.name, 'scatter.png')
if os.path.exists(scatter_path):
    print(f"Scatter plot saved at: {scatter_path}")
    print(f"File size: {os.path.getsize(scatter_path)} bytes")
else:
    print("Scatter plot file not found!")

# Option to copy the file to current directory
import shutil
current_dir_scatter = os.path.join(os.getcwd(), 'scatter.png')
if os.path.exists(scatter_path):
    shutil.copy2(scatter_path, current_dir_scatter)
    print(f"Scatter plot also copied to current directory: {current_dir_scatter}")

print(f"\nTemporary directory object: {temp_dir}")
print("Note: Temporary directory will be automatically cleaned up when the script ends.")
