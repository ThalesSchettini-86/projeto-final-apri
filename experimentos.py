#Importação de bibliotecas e modularizações
import time, funcoes
#Inicialização da função incluir_experimento()
def incluir_experimento(listacod, listaexp):
    while True: #Validação do código inserido pelo usuário
        try:
            codigo = int(input("Insira o código: "))
            if codigo in listacod:
                print("Código já existente! Tente novamente!")
            else:
                break
        except ValueError: #Tratamento de erro para valores não numéricos
            print("Código inválido! Tente novamente!")

    nome = input("Insira o nome do experimento: ")
    area = input("Insira a area do experimento: ")
    while True: #Validação da data inserida
        try:
            data_inicio = int(input("Insira o data inicio do experimento (AAAAMMDD): "))
            if funcoes.validar_data(data_inicio):
                break
            else:
                print("Data inválida! Tente novamente!")
        except ValueError:
            print("Utilize apenas números!")
    while True: #Validação da data inserida
        try:
            data_fim = int(input("Insira o data fim do experimento (AAAAMMDD): "))
            if funcoes.validar_data(data_fim):
                if data_fim >= data_inicio:
                    break
                else:
                    print("A data final deve ser posterior à data inicial")
            else:
                print("Data inválida! Tente novamente!")
        except ValueError:
            print("Utilize apenas números")
    agencia = input("Insira o nome da agência de fomento: ")
    while True: #Validação do orçamento inserido
        try:
            orcamento = float(input("Digite o orçamento do experimento: "))
            if orcamento <= 0:
                print("Valor inválido! Tente novamente!")
            else:
                break
        except ValueError:
            print("Utilize apenas números!")
    status = input("Digite o status do experimento: ")

    #Criação de lista com informações inseridas
    experimento = [codigo, nome, area, data_inicio, data_fim, agencia, orcamento, status]
    listacod.append(codigo)
    listaexp.append(experimento)
#Inicialização da função excluir_experimento()
def excluir_experimento(lista, dados):
    while True: #Validação do código inserido
        try:
            codigo = int(input("Insira o código do experimento: "))
            #Verificação através da função any() (Retorna True se pelo menos um item satisfazer a condição)
            if any(experimento[0] == codigo for experimento in lista):
                break
            else:
                print("Código não encontrado! Tente novamente!")
        except ValueError:
            print("Use apenas números!")
    for experimento in lista:
        if experimento[0] == codigo:
            dados["participacoes"] = [
                p for p in dados["participacoes"]
                if p["codigo"] != codigo
                #Exclusão das participações através da criação de uma nova lista
            ]
            lista.remove(experimento)
            print("Experimento excluído com sucesso!")
            return True
    print("Experimento não encontrado!")
    return False
#Inicialização da função alterar_experimento()
def alterar_experimento(lista):
    while True: #Validação do código inserido
        try:
            codigo = int(input("Insira o código do experimento: "))
            if any(experimento[0] == codigo for experimento in lista):
                break
            else:
                print("Código não encontrado! Tente novamente!")
        except ValueError:
            print("Use apenas números!")
    for experimento in lista:
        if experimento[0] == codigo:
            print("Experimento encontrado com sucesso!")
            time.sleep(1)
            print("Deixe o espaço em branco para manter o valor atual")
            time.sleep(1)
            nome = input(f"Nome atual: {experimento[1]} \n Insira o novo nome: ")
            area = input(f"Area atual: {experimento[2]} \n Insira a nova área: ")
            data_inicio = input(f"Data de inicio atual: {experimento[3]}\n Insira a data de inicio:  ")
            data_fim = input(f"Data de fim atual: {experimento[4]}\n Insira a data de fim:  ")
            agencia = input(f"Agencia nova: {experimento[5]}\n Insira a agência: ")
            orcamento = input(f"Orçamento atual: {experimento[6]}\n Insira o orçamento atual: ")
            status = input(f"Status atual: {experimento[7]}\n Insira o status atual: ")
            #Criação de variáveis temporárias para fins de validação
            novo_nome = experimento[1] if nome == "" else nome
            nova_area = experimento[2] if area == "" else area
            nova_agencia = experimento[5] if agencia == "" else agencia
            novo_status = experimento[7] if status == "" else status
            try:
                nova_inicio = ( #Criação de variáveis temporárias com operadores ternários
                    experimento[3]
                    if data_inicio == "" #Toma o valor de experimento[3] se a string for vazia
                    else int(data_inicio) #Valida a inserção de dados se a string não for vazia
                )
                nova_fim = (
                    experimento[4]
                    if data_fim == ""
                    else int(data_fim)
                )
            except ValueError:
                print("Digite datas numéricas válidas!")
                return False
            try:
                novo_orcamento = (
                    experimento[6]
                    if orcamento == ""
                    else float(orcamento)
                )
            except ValueError:
                print("Use apenas números!")
                return False
            #Validação de dados
            if not funcoes.validar_data(nova_inicio):
                print("Data inicial inválida!")
                return False
            if not funcoes.validar_data(nova_fim):
                print("Data final inválida!")
                return False
            if nova_inicio > nova_fim:
                print("A data inicial não pode ser posterior à final!")
                return False
            if novo_orcamento <= 0:
                print("O orçamento deve ser maior que 0!")
                return False
            #Atribuição das variáveis verificadas na lista do experimento
            experimento[1] = novo_nome
            experimento[2] = nova_area
            experimento[3] = nova_inicio
            experimento[4] = nova_fim
            experimento[5] = nova_agencia
            experimento[6] = novo_orcamento
            experimento[7] = novo_status
            print("Experimento alterado com sucesso!")
            return True
    print("Experimento não encontrado!")
    return False
#Inicialização da função listar_experimento()
def listar_experimento(lista):
    while True: #Validação do código inserido
        try:
            codigo = int(input("Insira o código do experimento: "))
            if any(experimento[0] == codigo for experimento in lista):
                break
            else:
                print("Código não encontrado! Tente novamente!")
        except ValueError:
            print("Use apenas números!")
    for experimento in lista:
        if experimento[0] == codigo:
            print("\n --------DADOS DO EXPERIMENTO--------")
            print(f"Código: {experimento[0]}")
            print(f"Nome: {experimento[1]}")
            print(f"Area: {experimento[2]}")
            print(f"Data de início: {experimento[3]}")
            print(f"Data de fim: {experimento[4]}")
            print(f"Agencia de fomento: {experimento[5]}")
            print(f"Orçamento: {experimento[6]}")
            print(f"Status atual: {experimento[7]}")
            return
    print("Experimento não encontrado!")
#Inicialização da função listar_todos()
def listar_todos(lista):
    if not lista: #Se lista vazia
        print("Não existem experimentos cadastrados!")
        return

    print("\n--------LISTA DE EXPERIMENTOS--------")
    for experimento in lista:
        print(f"\nCódigo: {experimento[0]}")
        print(f"Nome: {experimento[1]}")
        print(f"Area: {experimento[2]}")
        print(f"Data de início: {experimento[3]}")
        print(f"Data de fim: {experimento[4]}")
        print(f"Agencia de fomento: {experimento[5]}")
        print(f"Orçamento: {experimento[6]}")
        print(f"Status atual: {experimento[7]}")