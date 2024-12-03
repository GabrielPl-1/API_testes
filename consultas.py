import pandas as pd
import mysql.connector
from datetime import datetime

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'gapenna',
    password = '12345'
)

def retorna_geral():
    query = "SELECT * FROM biblioteca.tb_livros"
    df = pd.read_sql(query,con = conexao)
    return df.to_dict(orient='records')

def retorna_geral_id(id):
    query = f"SELECT * FROM biblioteca.tb_livros where id = {id}"
    df = pd.read_sql(query,con = conexao)
    return df.to_dict(orient='records')[0]

def delete_id(id):
    query = "delete FROM biblioteca.tb_livros where id = %s"
    cursor = conexao.cursor()
    cursor.execute(query,(id,))
    conexao.commit()
    return {"message":f"{id} deletado com sucesso"}

def adiciona_coisa(nome,genero,cliente,cpf,status):
    sql = "insert into biblioteca.tb_livros(nome_livro,categoria_livro,data_compra,nome_cliente,cpf_cliente,status_pedido) values (%s,%s,%s,%s,%s,%s)"
    cursor = conexao.cursor()
    data = datetime.now().strftime('%Y-%m-%d')
    cursor.execute(sql,[nome,genero,data,cliente,cpf,status])
    conexao.commit()
    return {"message":"adicionado com sucesso"}


def modifica_nome(nome,id):
    sql = "Update biblioteca.tb_livros set nome_livro = %s where id = %s"
    cursor = conexao.cursor()
    cursor.execute(sql,[nome,id])
    conexao.commit()
    return {"message":"Update feito com sucesso"}

modifica_nome('Tio patinhas', 6)