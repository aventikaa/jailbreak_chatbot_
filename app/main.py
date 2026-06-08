from fastapi import FastAPI
from pydantic import BaseModel

from vulnerable_bot import vulnerable_chat
from secure_bot import secure_chat

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "AI Security Project Running"}

@app.post("/vulnerable")
def vulnerable_api(request: ChatRequest):

    reply = vulnerable_chat(request.message)

    return {
        "bot": "vulnerable",
        "response": reply
    }

@app.post("/secure")
def secure_api(request: ChatRequest):

    reply = secure_chat(request.message)

    return {
        "bot": "secure",
        "response": reply
    }