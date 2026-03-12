from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate

llm =ChatOllama(
    model="qwen3:1.7b"
    temperature=0.9
)


