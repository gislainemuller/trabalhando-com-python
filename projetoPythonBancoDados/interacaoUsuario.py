from time import sleep
from crud import readTable, createTable, deleteTable
import sqlite3

def menu_interacao():
    
    loop = True

    while loop != False:
        continuarSistema = input("Deseja continuar ou sair\nDigite 1 para Continuar e 2 para Sair: ")

        if continuarSistema == "1":
            print("Bem vindo ao nosso sistema!")
            print("Verificando se existem tabelas no banco...\n")
            
            conexao = sqlite3.connect("Python.sqlite")
            cursor = conexao.cursor()

            readTable(conexao, cursor)


            criarTabela = input("Deseja criar uma tabela?\nDigite 1 para Sim e 2 para Não: ")

            createTable()

            if criarTabela == "1":
                nomeTabela = input("Digite o nome da tabela que pretende criar: ")
                print(f"Tabela '{nomeTabela}' criada com sucesso!\n")

            elif criarTabela == "2":
                print("A tabela não foi criada!\n")

            else:
                print("Opção inválida!\n")

            deletarTabela = input("Você deseja excluir uma tabela?\nDigite 1 para Sim e 2 para Não: ")

            deleteTable()

            if deletarTabela == "1":
                print("Exclusão da tabela realizada com sucesso")

            elif deletarTabela == "2":
                print("A tabela não foi removida!\n")

            else:
                print("Opção inválida!\n")

            loop = True  


        elif continuarSistema == "2":

            for animacao in range(8):
                sleep(0.1)
                print("*")

            print("A sessão foi encerrada")
            loop = False


        else:
            print("Forneça uma opção válida!\n")
            loop = True