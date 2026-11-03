#Importação de modularizações
import funcoes
#Inicialização da função participacoes_por_pesquisador()
def participacoes_por_pesquisador(lista, dados):
    while True: #Validação do CPF inserido pelo usuário
        try:
            cpf = int(input("Insira o CPF do pesquisador: "))
            if cpf in lista:
                break
            else:
                print("CPF não encontrado! Tente novamente!")
        except ValueError: #Tratamento de erro para valores não numéricos
            print("Use apenas números!")
    encontrou = False
    print("\n--------PARTICIPAÇÕES DO PESQUISADOR--------")
    for participacao in dados["participacoes"]:
        if participacao["cpf"] == cpf:
            print(f"\nCPF: {participacao['cpf']}")
            print(f"Código: {participacao['codigo']}")
            print(f"Função: {participacao['funcao']}")
            print(f"Carga horária: {participacao['carga_horaria']}")
            print(f"Resultado: {participacao['resultado']}")
            print(f"Data: {participacao['data']}")
            encontrou = True
    if not encontrou:
        print("Nenhuma participação encontrada para este pesquisador.")
#Inicialização da função experimentos_por_area()
def experimentos_por_area(lista):
    area = input("Insira a área do experimento: ")
    encontrou = False
    print("\n--------EXPERIMENTOS POR ÁREA--------")
    for experimento in lista:
        if experimento[2].capitalize() == area.capitalize():
            print(f"\nCódigo: {experimento[0]}")
            print(f"Nome: {experimento[1]}")
            print(f"Area: {experimento[2]}")
            print(f"Data de início: {experimento[3]}")
            print(f"Data de fim: {experimento[4]}")
            print(f"Agencia de fomento: {experimento[5]}")
            print(f"Orçamento: {experimento[6]}")
            print(f"Status atual: {experimento[7]}")
            encontrou = True
    if not encontrou:
        print("Nenhum experimento encontrado nessa área.")
#Inicialização da função participacoes_entre_datas()
def participacoes_entre_datas(dados):
    while True: #Verificação da data inserida
        try:
            data_inicio = int(input("Insira a data de inicio (AAAAMMDD): "))
            if funcoes.validar_data(data_inicio):
                break
            else:
                print("Data inválida! Tente novamente!")
        except ValueError:
            print("Use apenas números!")
    while True: #Verificação da data inserida
        try:
            data_fim = int(input("Insira a data de fim (AAAAMMDD): "))
            if funcoes.validar_data(data_fim):
                break
            else:
                print("Data inválida! Tente novamente!")
        except ValueError:
            print("Use apenas números!")
    if data_inicio > data_fim:
        print("Erro!")
        print("A data inicial deve ser anterior à data final")
        return
    encontrou = False
    print(f"\n--------PARTICIPAÇÕES ENTRE {data_inicio} E {data_fim}--------")
    for participacao in dados["participacoes"]:
        data = int(participacao["data"])
        if data_inicio <= data <= data_fim:
            print(f"\nCPF: {participacao['cpf']}")
            print(f"Código: {participacao['codigo']}")
            print(f"Função: {participacao['funcao']}")
            print(f"Carga horária: {participacao['carga_horaria']}")
            print(f"Resultado: {participacao['resultado']}")
            print(f"Data: {participacao['data']}")
            encontrou = True
    if not encontrou:
        print("Não foram encontradas participações neste período.")