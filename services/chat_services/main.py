from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "Chatbot Microservice Running"}

@app.post("/chat")
def chat(req: ChatRequest):
    user_message = req.message.lower()

    # Simple rule-based fallback (no AI yet)
    if "hello" in user_message or "hi" in user_message:
        return {"response": "Hello! How can I assist you with your health today?"}

    if "appointment" in user_message:
        return {"response": "Sure! Who do you want to book an appointment with?"}

    if "predict" in user_message or "risk" in user_message:
        return {"response": "You can check your disease risk in the Prediction section."}

    # Default response
    return {"response": "I'm here to help! Ask me anything about your health or appointments."}
