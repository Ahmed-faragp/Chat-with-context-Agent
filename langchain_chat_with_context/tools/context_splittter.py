from langchain_core.tools import Tool
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import LLMChain
from agent.llm import llm


prompt = PromptTemplate.from_template(open("prompts/context_splitter_prompt.txt").read())
chain = LLMChain(llm=llm, prompt=prompt)
context_splitter_tool = Tool.from_function(
        func=chain.run,
        name="ContextSplitter",
        description="Separate background context from the actual question so the LLM gets both cleanly."
    )