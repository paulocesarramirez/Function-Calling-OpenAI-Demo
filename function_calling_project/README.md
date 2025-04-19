# Function Calling with OpenAI GPT-4o

This project demonstrates how to use the OpenAI GPT-4o model to call Python functions dynamically. The project includes two functions, `GetDate` and `GetTime`, which return the current date and time, respectively.

## Project Overview

This repository includes two implementations for function calling with GPT-4o:

1. `function_calling.py` - Uses the older OpenAI "functions" parameter approach
2. `function_grok.py` - Uses the newer OpenAI "tools" parameter approach (recommended for new projects)

## Features

- Interact with the GPT-4o model hosted on GitHub Models using Azure API infrastructure
- Dynamically call Python functions based on user prompts
- Handle both function and non-function prompts seamlessly
- Support for calling multiple functions in a single interaction
- Error handling and timeouts for API calls
- Both synchronous function calling implementations (legacy and modern)

## Prerequisites

- Python 3.7 or higher
- A valid GitHub Models API key
- Internet connection

## Setup Instructions

1. Clone this repository or download the project files.
2. Navigate to the project directory:
   ```bash
   cd function_calling_project
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the project directory and add your GitHub Models API key:
   ```env
   GITHUB_MODELS_API_KEY=your_api_key_here
   ```

## Running the Project

### Legacy Implementation (function_calling.py)

1. Run the legacy implementation script:
   ```bash
   python function_calling.py
   ```
2. Interact with the GPT-4o model by typing prompts.
3. To exit, type `exit` or `quit`.

### Modern Implementation (function_grok.py)

1. Run the modern implementation script that uses the updated OpenAI tools approach:
   ```bash
   python function_grok.py
   ```
2. The script will automatically run test prompts defined in the code.

## Example Outputs

### Legacy Implementation (function_calling.py)

- **Input**: "What is the current date?"  
  **Output**: "Today's date is 19/04/2025."

- **Input**: "What time is it right now?"  
  **Output**: "The current time is 14:30:45."

- **Input**: "What is the current date and time?"  
  **Output**: "Today's date is 19/04/2025 and the current time is 14:30:45."

- **Input**: "Tell me a joke."  
  **Output**: "Why don't scientists trust atoms? Because they make up everything!"

### Modern Implementation (function_grok.py)

- **Input**: "What is the current date?"  
  **Output**: "date: 2025-04-19"

- **Input**: "What time is it right now?"  
  **Output**: "time: 14:30:45"

- **Input**: "What is the current date and time?"  
  **Output**: "date: 2025-04-19 and time: 14:30:45"

- **Input**: "Tell me a joke."  
  **Output**: [Direct response from GPT-4o with a joke]

## Implementation Differences

### function_calling.py
- Uses the older OpenAI "functions" parameter
- Returns date in DD/MM/YYYY format
- Interactive command-line interface
- Manual conversation loop implementation

### function_grok.py
- Uses the newer OpenAI "tools" parameter (recommended approach)
- Returns date in YYYY-MM-DD format
- Automated test suite with predefined prompts
- Includes detailed logging and timing information
- Returns structured responses as key-value pairs

## Common Issues and Troubleshooting

- **"None" Responses**: If you're getting "None" responses, check:
  - API key validity
  - API base URL correctness
  - API request format (tools vs functions parameter)
  - Response parsing code logic
  - Network connectivity to the API endpoint

- **Invalid API Key**: Ensure your API key is correct and added to the `.env` file.
- **Connection Issues**: Check your internet connection.
- **Dependency Errors**: Ensure all dependencies are installed using `pip install -r requirements.txt`.
- **API Timeouts**: The code includes a 10-second timeout. For complex prompts, you might need to increase this value.
- **Parameter Format**: Ensure you're using the correct parameter format for your OpenAI API version.

## License

This project is licensed under the MIT License.
