#Importações de bibliotecas e modularizações
import funcoes, pesquisadores, experimentos, participacoes, relatorios, persistencia, time

#Criação da função main()
def main():
    #Carregamento de dados
    dados = persistencia.carregar_dados()
    experimentos_li = persistencia.carregar_dados_exp()
    lista_CPF = [
        p["cpf"] for p in dados["pesquisadores"]
        #Carregamento das listas de CPF e de Códigos (linha 13:15)
    ]
    lista_codigo = [
        e[0] for e in experimentos_li
    ]
    print("Bem-vindo ao Sistema de Pesquisa Genética!")
    print()
    time.sleep(3)
    selecao_menu = funcoes.menu() #Inicialização do menu principal
    while selecao_menu != 5:
        match selecao_menu:
            case 1: #Submenu Pesquisadores
                sub = funcoes.submenu()
                match sub:
                    case 1:
                        pesquisadores.listar_todos(dados)
                    case 2:
                        pesquisadores.listar_pesquisador(lista_CPF, dados)
                    case 3:
                        pesquisadores.incluir_pesquisador(lista_CPF, dados)
                    case 4:
                        pesquisadores.alterar_pesquisador(lista_CPF, dados)
                    case 5:
                        print("Excluindo o pesquisador, suas participações também serão excluídas!")
                        time.sleep(1)
                        while True:
                            esc = input("Deseja excluir mesmo assim? [S/N]").upper()
                            if esc == "S" or esc == "N":
                                break
                            else:
                                print("Escolha inválida! Tente novamente!")
                        if esc == "S":
                            if pesquisadores.excluir_pesquisador(lista_CPF, dados):
                                lista_CPF = [
                                    p["cpf"] for p in dados["pesquisadores"]
                                    #Atualização da lista de CPF após a exclusão
                                ]
                    case 6:
                        persistencia.salvar_dados(dados)
                        print("Dados salvos com sucesso!")
                    case 7:
                        persistencia.salvar_dados(dados)
                        selecao_menu = funcoes.menu() 
            case 2: #Submenu Experimentos
                sub = funcoes.submenu()
                match sub:
                    case 1:
                        experimentos.listar_todos(experimentos_li)
                    case 2:
                        experimentos.listar_experimento(experimentos_li)
                    case 3:
                        experimentos.incluir_experimento(lista_codigo, experimentos_li)
                    case 4:
                        experimentos.alterar_experimento(experimentos_li)
                    case 5:
                        print("Excluindo o experimento, suas participações relacionadas também serão excluídas!")
                        time.sleep(1)
                        while True:
                            esc = input("Deseja excluir mesmo assim? [S/N]").upper()
                            if esc == "S" or esc == "N":
                                break
                            else:
                                print("Escolha inválida! Tente novamente!")
                        if esc == "S":
                            if experimentos.excluir_experimento(experimentos_li, dados):
                                lista_codigo = [
                                    e[0] for e in experimentos_li
                                    #Atualização da lista de Códigos após a exclusão
                                ]
                    case 6:
                        persistencia.salvar_dados(dados)
                        persistencia.salvar_dados_exp(experimentos_li)
                        print("Dados salvos com sucesso!")
                    case 7:
                        persistencia.salvar_dados(dados)
                        persistencia.salvar_dados_exp(experimentos_li)
                        selecao_menu = funcoes.menu()
            case 3: #Submenu Participações
                sub = funcoes.submenu()
                match sub:
                    case 1:
                        participacoes.listar_todos(dados)
                    case 2:
                        participacoes.listar_participacao(lista_CPF, lista_codigo, dados)
                    case 3:
                        participacoes.incluir_participacao(lista_CPF, lista_codigo, dados)
                    case 4:
                        participacoes.alterar_participacao(lista_CPF, lista_codigo, dados)
                    case 5:
                        participacoes.excluir_participacao(lista_CPF, lista_codigo, dados)
                    case 6:
                        persistencia.salvar_dados(dados)
                        print("Dados salvos com sucesso!")
                    case 7:
                        persistencia.salvar_dados(dados)
                        selecao_menu = funcoes.menu()
            case 4: #Submenu Relatórios
                sub = funcoes.submenu_relatorios()
                match sub:
                    case 1:
                        relatorios.participacoes_por_pesquisador(lista_CPF, dados)
                    case 2:
                        relatorios.experimentos_por_area(experimentos_li)
                    case 3:
                        relatorios.participacoes_entre_datas(dados)
                    case 4:
                        selecao_menu = funcoes.menu()
            case 5: #Sair
                break
main()