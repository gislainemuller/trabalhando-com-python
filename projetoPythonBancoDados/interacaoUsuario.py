from time import sleep
from crud import readTable, createTable, deleteTable, InsertSql
import sqlite3

def menu_interacao():
    
    loop = True

    while loop != False:
        continuarSistema = input("Deseja continuar ou sair\nDigite 1 para Continuar e 2 para Sair: ")

        if continuarSistema == "1":
            print("Bem vindo ao nosso sistema!")
            print("Verificando se existem tabelas no banco...\n")
            
            conexao = sqlite3.connect("python.sqlite")
            cursor = conexao.cursor()

            readTable(conexao, cursor)


            criarTabela = input("Deseja criar uma tabela?\nDigite 1 para Sim e 2 para Não: ")

            if criarTabela == "1":
                nomeTabela = input("Qual o nome da tabela que deseja criar? ")
                createTable(conexao, cursor)

            elif criarTabela == "2":
                print("A tabela não foi criada!\n")

            else:
                print("Opção inválida!\n")

            print("Inserindo dados iniciais automaticamente...\n")
            InsertSql(conexao, cursor)

            deletarTabela = input("Deseja deletar uma tabela?\nDigite 1 para Sim e 2 para Não: ")

            if deletarTabela == "1":
                deleteTable(cursor, conexao)

            elif deletarTabela == "2":
                print("A Tabela não foi deletada!\n")

            else:
                print("Opção inválida!\n")

            loop = True  


        elif continuarSistema == "2":

            for animacao in range(8):
                sleep(0.2)
                print("*")

            print("Você saiu do sistema.")
            loop = False


        else:
            print("Informe uma opção válida!\n")
            loop = True