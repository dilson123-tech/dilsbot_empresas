from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from chatbot import gerar_resposta


app = FastAPI()

# Libera o frontend acessar a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # pode restringir depois
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"mensagem": "🤖 API do DilsBot Empresas no ar!"}

@app.post("/chat")
async def chat(request: Request):
    dados = await request.json()
    pergunta = dados.get("mensagem", "")
    resposta = gerar_resposta(pergunta)
    return {"resposta": resposta}
