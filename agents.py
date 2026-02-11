from strands import Agent

agent = Agent()

from strands.models.ollama import OllamaModel
from strands_tools import http_request
# Create an Ollama model instance
ollama_model = OllamaModel(
    host="http://localhost:11434",  # Ollama server address
    model_id="glm-4.6:cloud"               # Specify which model to use
)

system_prompt= "You are respectful agent."\
"you can use free api "
# Create an agent using the Ollama model
agent = Agent(model=ollama_model,system_prompt=system_prompt,tools=[http_request])

# Use the agent
user_input= input("You:")
agent(user_input) # Prints model output to stdout by default