from langchain_core.tools import Tool
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import LLMChain
from agent.llm import llm


prompt = PromptTemplate.from_template(open("prompts/context_relevance_checker_prompt.txt").read())
chain = LLMChain(llm=llm, prompt=prompt)
context_relevance_tool = Tool.from_function(
        func=chain.run,
        name="ContextRelevanceChecker",
        description="MANDATORY TOOL. Use this whenever ContextPresenceJudge finds any info. Do not skip this tool. It determines if you need to use WebSearch."
    )
