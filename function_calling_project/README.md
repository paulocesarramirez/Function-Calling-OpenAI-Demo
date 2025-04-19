# Function Calling with OpenAI GPT-4o

This project demonstrates how to use the OpenAI GPT-4o model to call Python functions dynamically. The project includes two functions, `GetDate` and `GetTime`, which return the current date and time, respectively.

## Updated Features

- Interact with the GPT-4o model hosted on GitHub Models.
- Dynamically call Python functions based on user prompts.
- Handle both function and non-function prompts seamlessly.
- **NEW**: Support for calling multiple functions in a single interaction, such as retrieving both the current date and time.

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

1. Run the main script:
   ```bash
   python function_calling.py
   ```
2. Interact with the GPT-4o model by typing prompts. Example prompts:
   - "What is the current date?"
   - "What time is it right now?"
   - "Tell me a joke."
3. To exit, type `exit` or `quit`.

## Example Outputs

- **Input**: "What is the current date?"
  **Output**: "Today's date is 16/04/2025."

- **Input**: "What time is it right now?"
  **Output**: "The current time is 14:30:45."

- **Input**: "What is the current date and time?"
  **Output**: "Today's date is 16/04/2025 and the current time is 14:30:45."

- **Input**: "Tell me a joke."
  **Output**: "Why don't scientists trust atoms? Because they make up everything!"

## Troubleshooting

- **Invalid API Key**: Ensure your API key is correct and added to the `.env` file.
- **Connection Issues**: Check your internet connection.
- **Dependency Errors**: Ensure all dependencies are installed using `pip install -r requirements.txt`.

## License

This project is licensed under the MIT License.
