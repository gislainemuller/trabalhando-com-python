import sqlite3
def ListarTabelas(cursor, conexao):
     conexao = sqlite3.connect("python.sqlite")
     cursor = conexao.cursor()

     listarTabelas = "SELECT name FROM sqlite_master WHERE type='table';"

     cursor.execute(listarTabelas)

     tabelas = cursor.fetchall()

     if tabelas:
      for tabela in tabelas:
        print("Tabela", tabela[0])

     else: 
      print("nenhuma Tabela encontrada no banco atual")