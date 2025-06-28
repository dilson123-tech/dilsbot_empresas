import os
from openai import OpenAI
from pydantic import BaseModel
from fastapi import FastAPI

# Só carrega o .env se estiver rodando localmente
if os.getenv("RAILWAY_ENVIRONMENT") is None:
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except:
        pass

# Inicializa o cliente OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

class Mensagem(BaseModel):
    mensagem: str

@app.post("/pergunta")
async def responder(mensagem: Mensagem):
    try:
        resposta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Você é um assistente profissional que responde perguntas de empresas sobre o serviço oferecido."
                },
                {"role": "user", "content": mensagem.mensagem}
            ]
        )
        return {"resposta": resposta.choices[0].message.content}
    except Exception as e:
        return {"erro": str(e)}
