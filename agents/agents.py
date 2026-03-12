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

def main_agent(text:str):
    prompt=main_prompt.format(text=text)
    response=llm.invoke(prompt)
    return response


test_prompt=PromptTemplate.from_template(
"""
You are a validator agent.

Original message:
{text}

Language detection result:
{result}

Check if the analysis is correct.

Return:
Correct or Incorrect. If incorrect, explain why shortly.

"""
)


def test_agent(text:str, result:str):
    prompt=test_prompt.format(text=text, result=result)
    response=llm.invoke(prompt)
    return response
