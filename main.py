from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()
client = OpenAI()

class Msg(BaseModel):
    q: str

@app.post("/chat")
async def chat(msg: Msg):
    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": msg.q}],
    )
    return {"a": r.choices[0].message.content}



