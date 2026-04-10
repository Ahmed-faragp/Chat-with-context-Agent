from langchain_classic.agents import AgentExecutor
from langchain_classic import hub 
from langchain_classic.agents import create_react_agent
from tools.context_judge import context_presence_tool
from langchain_core.prompts import PromptTemplate
from tools.web_search import WebSearchTool
from agent.llm import llm

tools = [
    WebSearchTool,
    context_presence_tool
]

# prompt = hub.pull("hwchase17/react")
prompt = PromptTemplate.from_template(open("prompts/agent_prompt.txt").read())

agent = create_react_agent(
    tools=tools,
    llm=llm,
    prompt=prompt,
    )


agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=tools,
    llm=llm,
    verbose=True,
    handle_parsing_errors=True
)


