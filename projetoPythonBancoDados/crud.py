import sqlite3

def createTable():
      print('Tabela criada....')

def readTable(conexao, cursor):
            conexao = sqlite3.connect("Python.sqlite")
            cursor = conexao.cursor()

            listarTabelas = "SELECT name FROM sqlite_master WHERE type='table';"

            cursor.execute(listarTabelas)

            tabelas = cursor.fetchall()

            if tabelas:
             for tabela in tabelas:
              print("Tabela", tabela[0])

            else: 
             print("A Tabela não foi encontrada")


def update():
    pass

def deleteTable():
    print("Deletado....")