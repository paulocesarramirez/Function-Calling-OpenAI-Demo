import os
import json
import time
from datetime import datetime
import openai
from dotenv import load_dotenv
import requests  # For handling API timeouts

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
openai.api_key = os.getenv("GITHUB_MODELS_API_KEY")
openai.api_base = "https://models.inference.ai.azure.com"

# Define functions
def GetDate():
    """Get the current date in YYYY-MM-DD format."""
    return {"date": datetime.now().strftime("%Y-%m-%d")}

def GetTime():
    """Get the current time in HH:MM:SS format (24-hour)."""
    return {"time": datetime.now().strftime("%H:%M:%S")}

# Function registry (maps function names to actual functions)
function_registry = {
    "GetDate": GetDate,
    "GetTime": GetTime
}

# Tool schema for GPT-4o
tools = [
    {
        "type": "function",
        "function": {
            "name": "GetDate",
            "description": "Get the current date in YYYY-MM-DD format.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "GetTime",
            "description": "Get the current time in HH:MM:SS format (24-hour).",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    }
]

def process_user_input(prompt):
    """
    Process the user's prompt, call GPT-4o, and handle function calls.
    """
    try:
        # Step 1: Send prompt to GPT-4o with tool schema (with timeout)
        start_time = time.time()
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": prompt}
            ],
            tools=tools,
            tool_choice="auto",
            timeout=10  # Set a 10-second timeout for the API call
        )
        print(f"API response time: {time.time() - start_time:.2f} seconds")
        
        # Step 2: Get the message from the response
        message = response.choices[0].message
        print(f"Message structure: content={message.content}, tool_calls={getattr(message, 'tool_calls', None)}")

        # Step 3: Process tool calls if present
        function_results = []
        if hasattr(message, 'tool_calls') and message.tool_calls:
            for tool_call in message.tool_calls:
                function_name = tool_call.function.name
                try:
                    arguments = json.loads(tool_call.function.arguments or "{}")
                except json.JSONDecodeError as e:
                    print(f"Error parsing arguments for {function_name}: {e}")
                    function_results.append({"error": f"Invalid arguments for {function_name}"})
                    continue

                if function_name in function_registry:
                    function = function_registry[function_name]
                    try:
                        result = function(**arguments)
                        function_results.append(result)
                        print(f"Function {function_name} called. Result: {result}")
                    except Exception as e:
                        print(f"Error executing {function_name}: {e}")
                        function_results.append({"error": f"Function {function_name} failed: {str(e)}"})
                else:
                    print(f"Function {function_name} not found.")
                    function_results.append({"error": f"Function {function_name} not found."})

            # Combine results for multiple function calls
            if function_results:
                combined_results = " and ".join(
                    [f"{key}: {value}" for result in function_results for key, value in result.items()]
                )
                return combined_results
            else:
                return "No valid function results."

        # Step 4: Return direct response content if no tool calls
        if message.content:
            return message.content
        return "No response content available."

    except requests.exceptions.Timeout:
        print(f"Error: API call timed out for prompt: {prompt}")
        return "Error: API call timed out."
    except Exception as e:
        print(f"Error processing prompt '{prompt}': {str(e)}")
        return f"Error: {str(e)}"

# Test the system
prompts = [
    "What is the current date?",
    "What time is it right now?",
    "What is the current date and time?",
    "Tell me a joke."
]

for prompt in prompts:
    print(f"\nPrompt: {prompt}")
    response = process_user_input(prompt)
    print(f"Response: {response}")