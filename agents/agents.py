from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate

llm=ChatOllama(
    model="qwen3:1.7b", 
    temperature=0
)


main_prompt=PromptTemplate.from_template(
    """
You are a language decetion agent.

Your job is to detect which language each word belongs to.

Sentence:{text}

Return format:
word -> language

"""
)



