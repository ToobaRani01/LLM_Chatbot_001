# Simple Chatbot

Simple Chatbot is a Flask-based web application that provides an interactive AI chat experience using Groq's LLM via LangChain. It features conversation memory, a clean web interface, and easy configuration.

## 🚀 Workflow

The following diagram illustrates the flow of a message through the system:

```mermaid
graph TD
    A["User Input"] --> B["Web Frontend (templates/index.html)"]
    B -->| "POST /chat" | C["Flask Server (app.py)"]
    C --> D["LangChain ConversationChain (llm_config.py)"]
    D --> E["Conversation Memory (ConversationBufferMemory)"]
    D --> F["Groq API (ChatOpenAI model)"]
    F -->| "Response" | D
    D -->| "AI Reply" | C
    C -->| "JSON Response" | B
    B --> G["Display AI Message"]
```

1.  **User Input**: User types a message in the chat interface.
2.  **Flask Route**: The frontend sends the message to the `/chat` endpoint.
3.  **LLM Configuration**: The server uses `llm_config.py` to initialize the LangChain chain.
4.  **Memory**: The system retrieves previous context from the `ConversationBufferMemory`.
5.  **LLM Call**: The message is sent to the Groq API using the `ChatOpenAI` connector.
6.  **Response**: The AI response is returned and displayed to the user.

## 🛠️ Setup Instructions

### 1. Prerequisites
- Python 3.x installed.
- A Groq API Key.

### 2. Create a .env File
To keep your API keys safe, this project uses environment variables. Create a file named `.env` in the root directory of the project and add your Groq API key:

```env
GROK_API_KEY = "your_api_key_here"
```

> [!IMPORTANT]
> Never share your API key or commit your `.env` file to GitHub. The project includes a `.gitignore` to prevent this.

### 3. Install Dependencies
Run the following command to install the required Python libraries:

```bash
pip install -r requirements.txt
```

## 🏃 How to Run the App

1. Start the Flask server by running:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to `http://127.0.0.1:5000`.
3. Start chatting with your AI assistant!

## 📁 Project Structure
- `app.py`: Main Flask application handling routes.
- `llm_config.py`: Configuration for LangChain, LLM, and Memory.
- `templates/`: HTML templates for the web interface.
- `static/`: CSS and JavaScript files.
- `.env`: Environment variables (API keys).
- `.gitignore`: Files and folders to ignore in Git.
- `requirements.txt`: List of dependencies.
