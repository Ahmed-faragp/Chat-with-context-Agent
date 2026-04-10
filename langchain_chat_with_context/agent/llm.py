import os
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
load_dotenv()

api_key=os.getenv("OPENROUTER_API_KEY")
llm = ChatOpenRouter(
    model="meta-llama/llama-3.1-8b-instruct",
    api_key=api_key,
    app_url="https://your-project-repo.com", 
    app_title="CellulaTech_Agent"
)
