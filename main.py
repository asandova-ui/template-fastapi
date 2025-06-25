from fastapi import FastAPI
from openai import OpenAI
from pydantic import BaseModel

app = FastAPI()
client = OpenAI()

class Msg(BaseModel):
    q: str

@app.get("/")
async def root():
    return {"status": "ok", "message": "Template-FastAPI up and running!"}

@app.post("/chat")
async def chat(msg: Msg):
    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": msg.q}],
    )
    return {"answer": r.choices[0].message.content}
