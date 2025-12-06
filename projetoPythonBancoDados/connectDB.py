import sqlite3

conexao = sqlite3.connect("python.sqlite")
cursor = conexao.cursor()

comandoSQL = '''
CREATE TABLE IF NOT EXISTS tabelas (
id INTEGER,
nome TEXT NOT NULL
)
'''

cursor.execute (comandoSQL)
conexao.commit()
conexao.close()