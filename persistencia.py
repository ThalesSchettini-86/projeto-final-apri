#Importação de bibliotecas
from pathlib import Path
import json
#Inicialização da função carregar_dados()
def carregar_dados():
    #Definição do caminho absoluto para a abertura e leitura do arquivo
    ARQUIVO = Path(__file__).resolve().parent / "dados.json"
    if not ARQUIVO.exists(): #Se o caminho não existir, cria um dicionário/json vazio
        return {
            "pesquisadores": [],
            "experimentos": [],
            "participacoes": []
        }
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo: #Se o caminho existir, lê o arquivo
        return json.load(arquivo)
#Inicialização da função salvar_dados()
def salvar_dados(dados):
    #Definição do caminho absoluto
    ARQUIVO = Path(__file__).resolve().parent / "dados.json"
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo: #Coloca os dados do dicionário no arquivo json
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
#Inicialização da função carregar_dados_exp()
def carregar_dados_exp():
    #Definição do caminho absoluto
    ARQUIVO = Path(__file__).resolve().parent / "dados_experimentos.txt"
    experimentos = [] #Criação da lista vazia
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo: #Leitura do arquivo
            for linha in arquivo:
                campos = linha.strip().split(";") #Separação dos dados inseridos, antes separados por ;
                campos[0] = int(campos[0])
                campos[3] = int(campos[3])
                campos[4] = int(campos[4])
                campos[6] = float(campos[6])
                experimentos.append(campos) #Reconstrução da lista de dados
    except FileNotFoundError:
        ARQUIVO.touch() #Se o arquivo não existir, cria um de mesmo nome no caminho definido
        return experimentos
    return experimentos
#Inicialização da função salvar_dados_exp()
def salvar_dados_exp(experimentos):
    #Definição de caminho absoluto
    ARQUIVO = Path(__file__).resolve().parent / "dados_experimentos.txt"
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        for experimento in experimentos:
            linha = ";".join(str(campo) for campo in experimento) #Salvamento de dados separados por ;
            arquivo.write(linha + "\n")