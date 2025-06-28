from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Mensagem(BaseModel):
    mensagem: str

@app.post("/pergunta")
async def responder(mensagem: Mensagem):
    return {"recebido": mensagem.mensagem}

if __name__ == "__main__":
    uvicorn.run("teste:app", host="127.0.0.1", port=8000, reload=True)
