"""
A quickstart project from langchain's 
docs: https://python.langchain.com/en/latest/getting_started/getting_started.html
"""

from langchain.llms import OpenAI
llm = OpenAI()
TEXT = "What would be a good company name for a company that makes colorful socks?"
print(llm(TEXT))
