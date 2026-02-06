# Assistente-Educacional-Interativo-com-IA-com-LangChain-Groq

# -*- coding: utf-8 -*-
import sys 
sys.stdout.reconfigure(encoding="utf-8")

from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

tema = input("Digite um tema para a IA explicar: ")

prompt = PromptTemplate(
    input_variables=["tema"],
    template=f"""
Explique o seguinte tema de forma simples para iniciantes:

Tema: {tema}
"""
)

prompt_final = prompt.format(tema=tema)
resposta = llm.invoke(prompt_final)

print("\nResposta da IA: \n")
print(resposta.content)
