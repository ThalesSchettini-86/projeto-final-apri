#Importação de biblioteca
from datetime import datetime
#Inicialização da função menu()
def menu():
    print("***************************")
    print("1- Submenu de Pesquisador")
    print("2- Submenu de Experimento")
    print("3- Submenu de Participação")
    print("4- Submenu de Relatórios")
    print("5- Sair")
    print("***************************")
    while True: #Validação da opção inserida pelo usuário
        try:
            selecao = int(input("Insira o número da opção que deseja: "))
            if selecao > 5 or selecao < 1:
                print("Opção inválida! Tente novamente.")
            else:
                break
        except ValueError: #Tratamento de erro para valores não numéricos
            print("Opção inválida! Tente novamente.")
    return selecao
#Inicialização da função submenu()
def submenu():
    print("***************************")
    print("1- Listar todos")
    print("2- Listar um")
    print("3- Incluir")
    print("4- Alterar")
    print("5- Excluir")
    print("6- Salvar alterações")
    print("7- Sair")
    print("***************************")
    while True: #Validação da opção inserida
        try:
            subselecao = int(input("Insira o número da opção que deseja: "))
            if subselecao > 7 or subselecao < 1:
                print("Opção inválida! Tente novamente.")
            else:
                break
        except ValueError:
            print("Opção inválida! Tente novamente.")
    return subselecao
#Inicialização da função submenu_relatorios()
def submenu_relatorios():
    print("***************************")
    print("1- Mostrar participações de um pesquisador")
    print("2- Listar experimentos de uma área")
    print("3- Participações em um período de tempo")
    print("4- Sair")
    print("***************************")
    while True: #Validação da opção inserida
        try:
            subselecao = int(input("Insira o número da opção que deseja: "))
            if subselecao > 4 or subselecao < 1:
                print("Opção inválida! Tente novamente.")
            else:
                break
        except ValueError:
            print("Opção inválida! Tente novamente.")
    return subselecao
#Inicialização da função validar_data()
def validar_data(data):
    try:
        #Validação da data inserida pelo usuário
        datetime.strptime(str(data), "%Y%m%d")
        return True
    except ValueError: #Tratamento de erro para valores não numéricos
        return False