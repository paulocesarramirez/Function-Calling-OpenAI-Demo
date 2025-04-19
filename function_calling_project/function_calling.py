import os
import openai
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
openai.api_key = os.getenv("GITHUB_MODELS_API_KEY")
openai.api_base = "https://models.inference.ai.azure.com"

# Define functions

def GetDate():
    """Returns the current date in DD/MM/YYYY format."""
    return datetime.now().strftime("%d/%m/%Y")

def GetTime():
    """Returns the current time in HH:MM:SS format."""
    return datetime.now().strftime("%H:%M:%S")

# Function registry
function_registry = {
    "GetDate": GetDate,
    "GetTime": GetTime
}

def process_user_input(prompt):
    """Processes user input and interacts with GPT-4o."""
    try:
        # Send user prompt to GPT-4o
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            temperature=0.5,
            max_tokens=200,
            messages=[{"role": "user", "content": prompt}],
            functions=[
                {"name": "GetDate", "description": "Returns the current date.", "parameters": {}},
                {"name": "GetTime", "description": "Returns the current time.", "parameters": {}}
            ],
            request_timeout=10  # Timeout in seconds
        )
        # Print the API response for debugging
        print("API Response:", response)

        # Check if the response contains choices and if there are any choices available
        if not response["choices"]:
            return "Error: No response from GPT-4o."

        # Check if GPT-4o wants to call a function
        if response["choices"][0]["message"].get("function_call"):
            function_calls = []
            while response["choices"][0]["message"].get("function_call"):
                function_name = response["choices"][0]["message"]["function_call"]["name"]
                if function_name in function_registry:
                    # Call the function and get the result
                    function_result = function_registry[function_name]()
                    function_calls.append({
                        "name": function_name,
                        "content": function_result
                    })

                    # Send the function result back to GPT-4o
                    response = openai.ChatCompletion.create(
                        model="gpt-4o",
                        messages=[
                            {"role": "user", "content": prompt},
                            *[
                                {"role": "function", "name": call["name"], "content": call["content"]}
                                for call in function_calls
                            ]
                        ],
                        functions=[
                            {"name": "GetDate", "description": "Returns the current date.", "parameters": {}},
                            {"name": "GetTime", "description": "Returns the current time.", "parameters": {}}
                        ]
                    )
                else:
                    return f"Error: Function '{function_name}' not found."

            # Return GPT-4o's final response
            return response["choices"][0]["message"]["content"]
        else:
            # Return GPT-4o's direct response
            return response["choices"][0]["message"]["content"]

    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        print("GPT-4o:", process_user_input(user_input))
