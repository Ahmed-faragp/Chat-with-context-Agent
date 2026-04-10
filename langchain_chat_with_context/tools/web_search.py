from tavily import TavilyClient
import os
from dotenv import load_dotenv
from langchain_core.tools import Tool

load_dotenv()
tvly_api_key = os.getenv("tvly_api_key")

tavily_client = TavilyClient(api_key=tvly_api_key)

def web_search(query):
    results = tavily_client.search(query)
    return results

WebSearchTool = Tool.from_function(
    func=web_search,
    name="WebSearch",
    description="Searches the web for relevant information based on the query,Don't use this tool if the question can be answered with the context provided. Use this tool when ContextRelevanceChecker determines that the context is not sufficient to answer the question.   "
)

print(tvly_api_key)