from langgraph.graph import StateGraph, START , END
from typing import TypedDict
from agents.agents import main_agent, test_agent

class AgentState(TypedDict):
    text:str
    result:str
    validation:str


def run_main_agent(state: AgentState)->AgentState:
    result= main_agent(state["text"])
    return {
        "result":result
    }


