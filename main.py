from fastapi import FastAPI
import mysql.connector
from datetime import datetime
from consultas import retorna_geral,retorna_geral_id, delete_id,adiciona_coisa, modifica_nome
from typing import List
from pydantic import BaseModel


conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'gapenna',
    password = '12345'
)

app = FastAPI()

@app.get("/")
async def read_root():
    return retorna_geral()

@app.get("/{item_id}")
async def read_root_id(item_id: int):
    return retorna_geral_id(item_id)

@app.delete("/apagar_{item_id}")
async def read_deleta_id(item_id: int):
    return delete_id(item_id)

@app.post("/adicionar")
async def read_adiciona_id(nome: str, genero: str, cliente: str, cpf: int, status: str):
    return adiciona_coisa(nome, genero, cliente, cpf, status)

@app.put("/modifica_{id}")
async def modifica_nome_id(item_id: int, nome_livro: str):
    return modifica_nome(nome_livro,item_id)