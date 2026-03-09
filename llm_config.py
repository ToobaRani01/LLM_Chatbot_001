# import libraries 

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
# remove warnings 
import warnings
warnings.filterwarnings("ignore")

# Load environment variables from .env file
load_dotenv()

# Set up API keys
Grok_API_KEY = os.environ.get("Grok_API_KEY")

# Grok API endpoint
BASE_url="https://api.groq.com/openai/v1"

# Initialize the language model
llm = ChatOpenAI(
    model = "openai/gpt-oss-120b",
    api_key = Grok_API_KEY,
    base_url = BASE_url,
    temperature = 0.3,
)

