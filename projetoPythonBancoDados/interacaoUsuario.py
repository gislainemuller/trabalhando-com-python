from time import sleep
import sqlite3
from connectDB import ListarTabelas

def menu_interacao():
    
    loop = True

    while loop != False:
        continuarSistema = int(input(f"Deseja continuar no sistema?\n (1) para Continuar e (2) para Sair: "))

        if continuarSistema == 1:
            print("Continuando com o sistema")
            print("Verificando se existe tabelas no sistema")
            conexao = sqlite3.connect("python.sqlite")
            cursor = conexao.cursor()

            ListarTabelas(cursor, conexao)
          
            criaTabela = int(input(f"Deseja criar uma tabela?\nDigite (1)-Sim e (2)-Não: "))
            if criaTabela == 1:
                print("Processando a criação das tabelas...")
            
            elif criaTabela == 2:
                print("Tudo bem, nenhuma tabela adicional será criada.")
            
            else:
                print("Opção inválida! Tente novamente.")

            excluirTabela = int(input(f"Deseja deletar uma tabela?\nDigite 1 para Sim e 2 para Não: "))

            if excluirTabela == 1:
                print("Deletando tabelas...")
            
            elif excluirTabela == 2:
                print("Ok, não será deletado nenhuma tabela!")
            
            else:
                print("Opção inválida! Tente novamente.")


            loop = True



        elif continuarSistema == 2:

            for animacao in range(20):
                sleep(0.1)
                print("*")
                
            print("Você Saiu do sistema !")

            loop = False



        else:
            print("Opção inválida. Tente novamente.")
            loop = True