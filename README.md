# LangGraph Chatbot

LangGraph Chatbot is a FastAPI-based chatbot with memory that assists users in interacting with API endpoints effectively. The chatbot is designed to help users perform actions like creating and retrieving messages while ensuring a smooth and guided experience. Additionally, the project includes a Streamlit application for an interactive front-end interface.

## Features

- **FastAPI Back-End:** A robust API server built with FastAPI for handling chat-related operations.
- **Streamlit Front-End:** An intuitive web interface powered by Streamlit to interact with the chatbot.
- **Memory-Powered Chatbot:** Maintains conversation context to offer a more natural and effective user experience.
- **Integrated Tools:** Supports various API calls, including:
  - `read_root`
  - `create_message`
  - `read_messages`
  - `read_message`
- **Dynamic Assistance:** Ensures the user is guided towards effective use of the available API tools while responding to non-tool-related queries naturally.

## Installation

### Prerequisites
- Python 3.11 or higher
- A virtual environment (recommended)

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/langgraph-chatbot.git
    cd langgraph-chatbot
    ```

2. Set up the virtual environment:
    ```bash
    python -m pip install uv
    uv sync
    ```

3. Configure environment variables:
    - Duplicate `.env_example` and rename it to `.env`.
    - Fill in the required environment variables.

## Usage

### Running Streamlit (Front-End)
Start the Streamlit app to interact with the chatbot visually:
```bash
uv run streamlit run chat.py --server.port 8501
```
Access the application in your browser at `http://localhost:8501`.

### Running FastAPI (Back-End)
Start the FastAPI server to handle API requests:
```bash
cd app
uv run fastapi run main:app --host 0.0.0.0
```
Access the API documentation at `http://127.0.0.1:8000/docs`.

## Prompt and Chatbot Objective

The chatbot operates with the following objective:

```
Assist the user to use the API call tools for read_root, create_message, read_messages, and read_message.
If there is missing information to use a tool, prompt the user to provide it.
If the user discusses other topics, redirect them to the main goal: helping with API calls.
For messages that don't require tools, respond naturally without invoking them.
Return API responses to the user in a well-formatted and user-friendly manner.
```

## Project Structure

## Project Structure

```
langgraph-chatbot/
├── .venv/                    # Virtual environment directory
├── app/
│   ├── db/                   # Database-related scripts
│   ├── notebooks/            # Jupyter notebooks for experiments
│   ├── routers/              # FastAPI routers for API endpoints
│   ├── schemas/              # Pydantic models
│   ├── utils.py              # Utility functions for the app
│   └── main.py               # FastAPI entry point
├── chatbot/
│   ├── agent.py              # Agent logic for chatbot operations
│   ├── api_tools.py          # Tools for API integrations
│   └── chat.py               # Core chatbot logic
├── .env                      # Environment variables file
├── .env_example              # Example of environment variables file
├── .gitignore                # Git ignore file
├── .python-version           # Python version file
├── pyproject.toml            # Project dependencies and metadata
├── README.md                 # Project documentation
└── uv.lock                   # Dependency lock file for `uvicorn`
```


## Dependencies

The project uses the following libraries:

- `duckduckgo-search` - For implementing search capabilities.
- `fastapi[standard]` - Core framework for API development.
- `isort` - Python import sorter for cleaner code.
- `langchain` & `langgraph` - To implement and manage the chatbot memory and processing.
- `python-dotenv` - To manage environment variables.
- `sqlalchemy` - Database ORM for efficient data handling.
- `streamlit` - For creating the interactive web app.
- `uvicorn` - ASGI server for running FastAPI apps.

## Future Improvements

- Add more tools to expand chatbot functionality.
- Enhance conversation context and memory handling.
- Improve the Streamlit interface for better user experience.
