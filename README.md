# 🚀 Smart Context-Aware LangChain Agent

An intelligent chatbot built with **LangChain** and **ReAct Agents** that doesn't just answer questions—it evaluates them. This agent autonomously determines if it has enough information, searches the web for missing context, and validates data relevance before providing a grounded response.

## 🧠 Overview
Unlike traditional chatbots that may hallucinate when information is lacking, this system implements a **Reasoning and Acting (ReAct)** loop. The agent mimics human logic to ensure every answer is backed by verified context.

### The Agentic Workflow:
1.  **🕵️ Judge:** "Did the user provide enough background info?"
2.  **🌐 Search:** "If not, let me fetch the latest data from the web."
3.  **🎯 Validate:** "Is this information actually relevant to the question?"
4.  **✂️ Process:** "Let me split the background facts from the core query."
5.  **🤖 Answer:** "Generate a response using the processed context."

## 🧰 Core Tools
The agent's intelligence is powered by four modular **LangChain Tools**:

| Tool | Role |
| :--- | :--- |
| **Context Presence Judge** | Uses an LLM to detect if background info is provided. |
| **Web Search Tool** | Connects to Tavily API  to retrieve missing data. |
| **Context Relevance Checker** | Filters out "noise" to ensure context matches the user's intent. |
| **Context Splitter** | Separates raw input into structured `Context` and `Question` blocks. |

## 🛠️ Tech Stack
* **Framework:** [LangChain](https://www.langchain.com/)
* **LLM:** [Ollama](https://ollama.ai/) (Running Llama 3)
* **Search API:** [Tavily AI](https://tavily.com/)
* **UI:** Streamlit
* **Language:** Python 3.10+

## 📂 Project Structure
```text
langchain_chat_with_context/
├── tools/                # Python files for each LangChain tool
├── agent/                # Agent initialization and ReAct logic
├── prompts/              # System prompt templates (.txt)
└── main.py               # Application entry point

🚀 Installation & Setup
1. Clone the repository
Bash
git clone [https://github.com/your-username/smart-context-agent.git](https://github.com/your-username/smart-context-agent.git)
cd smart-context-agent
2. Install dependencies
Bash
pip install langchain langchain-community python-dotenv ollama requests
3. Configure your LLM using openrouter




🧪 Use Case Example
User Input: "Tell me how attention mechanisms are used."

Agent Logic: Detects missing context.

Action: Executes WebSearchTool for "Attention mechanisms in deep learning."

Validation: RelevanceChecker confirms the search results match the NLP topic.

Final Output: A detailed, technical response based on real-time retrieved data.

