from langchain_core.tools import Tool
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import LLMChain
from agent.llm import llm


prompt = PromptTemplate.from_template(open("prompts/context_judge_prompt.txt").read())
chain = LLMChain(llm=llm, prompt=prompt)
context_presence_tool = Tool.from_function(
        func=chain.run,
        name="ContextPresenceJudge",
        description="Checks if context is present in user input"
    )
