from fastapi import FastAPI, Request
from pydantic import BaseModel
from langgraph_config import build_graph

app = FastAPI()
graph = build_graph()

class ChatRequest(BaseModel):
    input: str

@app.post("/chat")
def chat(req: ChatRequest):
    try:
        result = graph.invoke({"input": req.input})
        return {"response": result.get("output") or result}
    except Exception as e:
        return {"error": str(e)}
