#Importação de biblioteca
import time
#Inicialização da função incluir_pesquisadr()
def incluir_pesquisador(lista, dados):
    while True: #Validação do CPF inserido pelo usuário
        try:
            cpf = int(input("Insira o CPF (apenas números): "))
            if cpf in lista:
                print("CPF já existente! Tente novamente!")
            else:
                lista.append(cpf)
                break
        except ValueError: #Tratamento de erro para valores não numéricos
            print("CPF inválido! Tente novamente!")
    #Leitura dos valores de cadastro
    nome = input("Insira o nome do pesquisador: ")
    area = input("Insira o área de especialização: ")
    instituicao = input("Insira a instituição do pesquisador: ")
    email = input("Insira o E-Mail do pesquisador: ")
    pais = input("Insira o país de origem do pesquisador: ")
    titulacao = input("Insira o grau acadêmico do pesquisador: ")

    pesquisador = { #Criação de dicionário com as informações inseridas
        "cpf" : cpf,
        "nome" : nome,
        "area" : area,
        "instituicao" : instituicao,
        "email" : email,
        "pais" : pais,
        "titulacao" : titulacao,
    }

    dados["pesquisadores"].append(pesquisador) #Adição ao dicionário para o armazenamento no arquivo json
#Inicialização da função excluir_pesquisador()
def excluir_pesquisador(lista, dados):
    while True: #Validação do CPF inserido
        try:
            cpf = int(input("Insira o CPF do pesquisador: "))
            if cpf in lista:
                break
            else:
                print("CPF não encontrado! Tente novamente!")
        except ValueError:
            print("Use apenas números!")
    for pesquisador in dados["pesquisadores"]:
        if pesquisador["cpf"] == cpf:
            dados["participacoes"] = [
                p for p in dados["participacoes"]
                if p["cpf"] != cpf
                #Exclusão das participações através da criação de uma nova lista
            ]
            dados["pesquisadores"].remove(pesquisador)
            print("Pesquisador excluído com sucesso!")
            return True
    print("Pesquisador não encontrado!")
    return False
#Inicialização da função alterar_pesquisador()
def alterar_pesquisador(lista, dados):
    while True: #Validação do CPF inserido
        try:
            cpf = int(input("Insira o CPF do pesquisador: "))
            if cpf in lista:
                break
            else:
                print("CPF não encontrado! Tente novamente!")
        except ValueError:
            print("Utilize apenas números!")
    for pesquisador in dados["pesquisadores"]:
        if pesquisador["cpf"] == cpf:
            print("Pesquisador encontrado!")
            time.sleep(1)
            print("Deixe o espaço em branco para manter o valor atual")
            time.sleep(1)
            nome = input(f"Nome atual: {pesquisador['nome']} \n Insira o novo nome: ")
            area = input(f"Área atual: {pesquisador['area']} \n Insira a nova área: ")
            instituicao = input(f"Instituição atual: {pesquisador['instituicao']} \n Insira a nova instituição: ")
            email = input(f"E-Mail atual: {pesquisador['email']} \n Insira o novo E-Mail: ")
            pais = input(f"País atual: {pesquisador['pais']} \n Insira o novo país: ")
            titulacao = input(f"Titulação atual: {pesquisador['titulacao']} \n Insira a nova titulação: ")
            if nome != "":
                pesquisador["nome"] = nome
            if area != "":
                pesquisador["area"] = area
            if instituicao != "":
                pesquisador["instituicao"] = instituicao
            if email != "":
                pesquisador["email"] = email
            if pais != "":
                pesquisador["pais"] = pais
            if titulacao != "":
                pesquisador["titulacao"] = titulacao
            print("Pesquisador alterado com sucesso!")
            return True
    print("Pesquisador não encontrado!")
    return False
#Inicialização da função listar_pesquisador()
def listar_pesquisador(lista, dados):
    while True: #Validação do CPF inserido
        try:
            cpf = int(input("Insira o CPF do pesquisador: "))
            if cpf in lista:
                break
            else:
                print("CPF não encontrado! Tente novamente!")
        except ValueError:
            print("Utilize apenas números!")
    for pesquisador in dados["pesquisadores"]: #Iteração do dicionário e busca do pesquisador
        if pesquisador["cpf"] == cpf:
            print("\n --------DADOS DO PESQUISADOR--------")
            # cpf, nome, area, instituicao, email, pais, titulacao
            print(f"CPF: {pesquisador['cpf']}")
            print(f"Nome: {pesquisador['nome']}")
            print(f"Área: {pesquisador['area']}")
            print(f"Instituição: {pesquisador['instituicao']}")
            print(f"Email: {pesquisador['email']}")
            print(f"Pais: {pesquisador['pais']}")
            print(f"Titulação: {pesquisador['titulacao']}")
            return
    print("Pesquisador não encontrado!")
#Inicialização da função listar_todos()
def listar_todos(dados):
    if not dados["pesquisadores"]: #Dicionário com listas vazias
        print("Não há pesquisadores cadastrados!")
        return

    print("\n--------LISTA DE PESQUISADORES--------")
    for pesquisador in dados["pesquisadores"]:
        print(f"\nCPF: {pesquisador['cpf']}")
        print(f"Nome: {pesquisador['nome']}")
        print(f"Área: {pesquisador['area']}")
        print(f"Instituição: {pesquisador['instituicao']}")
        print(f"Email: {pesquisador['email']}")
        print(f"Pais: {pesquisador['pais']}")
        print(f"Titulação: {pesquisador['titulacao']}")