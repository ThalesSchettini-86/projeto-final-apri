#Importação de bibliotecas e modularizações
import time, funcoes
#Inicialização da função incluir_participacao()
def incluir_participacao(lista_cpf, lista_codigo, dados):
    #Verificação de dados inseridos pelo usuário
    while True:
        try:
            cpf = int(input("Insira o CPF do pesquisador: "))
            if cpf not in lista_cpf:
                print("CPF não existente! Cadastre o pesquisador e tente novamente!")
                return False
            else:
                break
        except ValueError: #Tratamento de erro para valores não numéricos
            print("CPF inválido! Tente novamente!")
    while True:
        try:
            codigo = int(input("Insira o código do experimento: "))
            if codigo not in lista_codigo:
                print("Código não existente! Cadastre o experimento e tente novamente!")
                return False
            else:
                break
        except ValueError:
            print("Código inválido! Tente novamente!")

    funcao = input("Insira a função do pesquisador: ")
    while True: #Validação da carga horária inserida
        try:
            carga_horaria = int(input("Insira a carga horária: "))
            if carga_horaria > 0:
                break
            print("A carga horária deve ser maior que 0!")
        except ValueError:
            print("Digite apenas números!")

    resultado = input("Insira o resultado do experimento: ")
    while True: #Validação da data inserida
        try:
            data = int(input("Insira a data do experimento (AAAAMMDD): "))
            if funcoes.validar_data(data):
                break
            else:
                print("Data inválida! Tente novamente!")
        except ValueError:
            print("Digite apenas números!")
    participacao = { #Criação do dicionário com as informações inseridas e validadas
        "cpf" : cpf,
        "codigo" : codigo,
        "funcao": funcao,
        "carga_horaria" : carga_horaria,
        "resultado" : resultado,
        "data" : data,
    }
    dados["participacoes"].append(participacao) #Adição das informações no dicionário usado no arquivo json
    print("Participação cadastrada com sucesso!")
    return True
#Inicialização da função excluir_participação()
def excluir_participacao(lista_cpf, lista_codigo, dados):
    #Validação de dados inseridos
    while True:
        try:
            cpf = int(input("Insira o CPF do pesquisador: "))
            if cpf not in lista_cpf:
                print("CPF não existente! Cadastre o pesquisador e tente novamente!")
                return False
            else:
                break
        except ValueError:
            print("CPF inválido! Tente novamente!")
    while True:
        try:
            codigo = int(input("Insira o código do experimento: "))
            if codigo not in lista_codigo:
                print("Código não existente! Cadastre o experimento e tente novamente!")
                return False
            else:
                break
        except ValueError:
            print("Código inválido! Tente novamente!")
    for participacao in dados["participacoes"]:
        if participacao["cpf"] == cpf and participacao["codigo"] == codigo:
            dados["participacoes"].remove(participacao)
            print("Participação excluída com sucesso!")
            return True
    print("Perticipação não encontrada!")
    return False
#Inicialização da função alterar_participacao()
def alterar_participacao(lista_cpf, lista_codigo, dados):
    #Validação dos dados inseridos
    while True:
        try:
            cpf = int(input("Insira o CPF do pesquisador: "))
            if cpf not in lista_cpf:
                print("CPF não existente! Cadastre o pesquisador e tente novamente!")
                return False
            else:
                break
        except ValueError:
            print("CPF inválido! Tente novamente!")
    while True:
        try:
            codigo = int(input("Insira o código do experimento: "))
            if codigo not in lista_codigo:
                print("Código não existente! Cadastre o experimento e tente novamente!")
                return False
            else:
                break
        except ValueError:
            print("Código inválido! Tente novamente!")
    for participacao in dados["participacoes"]:
        if participacao["cpf"] == cpf and participacao["codigo"] == codigo:
            print("Participação encontrada!")
            time.sleep(1)
            print("Deixe o espaço em branco para manter o valor atual")
            time.sleep(1) #funcao, carga_horaria, resultado, data
            funcao = input(f"Função atual: {participacao['funcao']} \n Insira a nova função: ")
            carga_horaria = input(f"Carga horária atual: {participacao['carga_horaria']} \n Insira a nova carga horária: ")
            resultado = input(f"Resultado atual: {participacao['resultado']} \n Insira o novo resultado: ")
            data = input(f"Data atual: {participacao['data']} \n Insira a nova data (AAAAMMDD): ")
            nova_carga = participacao["carga_horaria"]
            nova_data = participacao["data"]
            if carga_horaria != "":
                try: #Validação da carga horária inserida
                    nova_carga = int(carga_horaria)
                    if nova_carga <= 0:
                        print("A carga horária deve ser positiva!")
                        return False
                except ValueError:
                    print("Carga horária inválida!")
                    return False
            if data != "":
                try: #Validação da data inserida
                    nova_data = int(data)
                    if not funcoes.validar_data(nova_data):
                        print("Data inválida!")
                        return False
                except ValueError:
                    print("Digite uma data numérica válida!")
                    return False
            #Atribuição das variáveis verificadas
            participacao["carga_horaria"] = nova_carga
            participacao["data"] = nova_data
            if resultado != "":
                participacao["resultado"] = resultado
            if funcao != "":
                participacao["funcao"] = funcao
            print("Participação alterada com sucesso!")
            return True
    print("Participação não encontrada!")
    return False
#Inicialização da função listar_participacao()
def listar_participacao(lista_cpf, lista_codigo, dados):
    while True: #Validação de dados inseridos
        try:
            cpf = int(input("Insira o CPF do pesquisador: "))
            if cpf not in lista_cpf:
                print("CPF não existente! Cadastre o pesquisador e tente novamente!")
                return False
            else:
                break
        except ValueError:
            print("CPF inválido! Tente novamente!")
    while True:
        try:
            codigo = int(input("Insira o código do experimento: "))
            if codigo not in lista_codigo:
                print("Código não existente! Cadastre o experimento e tente novamente!")
                return False
            else:
                break
        except ValueError:
            print("Código inválido! Tente novamente!")
    for participacao in dados["participacoes"]:
        if participacao["cpf"] == cpf and participacao["codigo"] == codigo:
            print("\n --------DADOS DA PARTICIPAÇÃO--------")
            print(f"CPF: {participacao['cpf']}")
            print(f"Código: {participacao['codigo']}")
            print(f"Função: {participacao['funcao']}")
            print(f"Carga horária: {participacao['carga_horaria']}")
            print(f"Resultado: {participacao['resultado']}")
            print(f"Data: {participacao['data']}")
            return
    print("Partcipação não encontrada!")
    return False
#Inicialização da função listar_todos()
def listar_todos(dados):
    if not dados["participacoes"]: #Se dicionário vazio
        print("Não há participações cadastradas!")
        return

    print("\n--------LISTA DE PARTICIPAÇÕES--------")
    for participacao in dados["participacoes"]:
        print(f"\nCPF: {participacao['cpf']}")
        print(f"Código: {participacao['codigo']}")
        print(f"Função: {participacao['funcao']}")
        print(f"Carga horária: {participacao['carga_horaria']}")
        print(f"Resultado: {participacao['resultado']}")
        print(f"Data: {participacao['data']}")