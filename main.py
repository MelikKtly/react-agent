from fastapi import FastAPI
from pydantic import BaseModel
from graph import build_graph

app = FastAPI()

graph= build_graph()


class Message(BaseModel):
    text:str


@app.post("/detect_language")
def detect_language(message: Message):
    result= graph.invoke({
        "text":message.text
    })
    return {
        "input": message.text,
        "analysis": result["result"],
        "validation": result["validation"]
    }