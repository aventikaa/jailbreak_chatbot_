from fastapi import FastAPI
from pydantic import BaseModel

from app.vulnerable_bot import vulnerable_chat
from app.secure_bot import secure_chat

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "AI Security Project Running"}

@app.post("/vulnerable")
def vulnerable_api(req: ChatRequest):
    return {
        "bot": "vulnerable",
        "response": vulnerable_chat(req.message)
    }

@app.post("/secure")
def secure_api(req: ChatRequest):
    return {
        "bot": "secure",
        "response": secure_chat(req.message)
    }