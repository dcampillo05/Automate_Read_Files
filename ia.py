from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()

def textAnalytic(text: str) -> str:
    """
     Envia o texto para o modelo OpenAI e retorna a resposta da IA.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente que analisa relatórios de campanha e dá um resumo útil."},
            {"role": "user", "content": text},  
        ],
    )
    return



