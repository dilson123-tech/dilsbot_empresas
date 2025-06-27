# chatbot.py

import os
from openai import OpenAI
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do .env
load_dotenv()

# Configura o cliente da OpenAI com a nova lib (v1.0+)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gerar_resposta(pergunta: str) -> str:
    try:
        resposta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente que ajuda empresas com soluções em IA."},
                {"role": "user", "content": pergunta}
            ]
        )
        return resposta.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Erro ao gerar resposta: {str(e)}"
