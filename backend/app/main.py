from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Liberar CORS pra testes externos tipo ReqBin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/pergunta")
async def responder(request: Request):
    body = await request.json()
    mensagem = body.get("mensagem")

    # Resposta fake só pra teste
    return {"resposta": f"Recebi sua mensagem: {mensagem}"}
