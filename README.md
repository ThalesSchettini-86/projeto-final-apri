# Sistema de Pesquisa Genética

Sistema desenvolvido em Python como projeto final da disciplina de **Algoritmos e Programação I**, com o objetivo de organizar e consultar informações relacionadas a pesquisadores, experimentos e participações em pesquisas genéticas.

## Funcionalidades

- Cadastro e gerenciamento de pesquisadores.
- Cadastro e gerenciamento de experimentos.
- Registro e consulta de participações em experimentos.
- Relatórios de participações por identificador de pesquisador.
- Consulta de experimentos por área de pesquisa.
- Consulta de participações em um intervalo de datas.
- Persistência de dados em arquivos, permitindo manter os registros entre execuções do programa.

## Tecnologias utilizadas

- **Python** — implementação da lógica e das funcionalidades do sistema.
  - Biblioteca JSON — Conversão de dados de dicionário para JSON
  - Biblioteca Pathlib — Obtenção do caminho absoluto dos arquivos
  - Biblioteca Time — Adição de pausas no código com time.sleep()
- **JSON e arquivos de texto** — armazenamento persistente dos dados.

## Estrutura do projeto

| Arquivo                  | Descrição                                                    |
|--------------------------|--------------------------------------------------------------|
| `main.py`                | Ponto de entrada e menu principal do sistema.                |
| `funcoes.py`             | Funções auxiliares e implementação das operações do sistema. |
| `pesquisadores.py`       | Funções relacionadas às ações para pesquisadores             |
| `experimentos.py`        | Funções relacionadas às ações para experimentos              |
| `participacoes.py`       | Funções relacionadas às ações para participações             |
| `relatorios.py`          | Funções relacionadas às pesquisas de dados                   |
| `persistencia.py`        | Funções relacionadas à persistência de dados                 |
| `dados.json`             | Arquivo utilizado para armazenar dados persistentes.         |
| `dados_experimentos.txt` | Arquivo utilizado para armazenar dados de experimentos       |

## Como executar

1. Instale o Python 3, caso ainda não esteja instalado.
2. Clone ou baixe este repositório.
3. Abra a pasta do projeto.
4. Execute o arquivo `main.py` pelo Python ou pelo PyCharm.

## Objetivo acadêmico

Este projeto foi desenvolvido para aplicar os conceitos estudados na disciplina de Algoritmos e Programação I, incluindo estruturas de dados, modularização, funções, manipulação de arquivos e geração de relatórios.

## Autorias e créditos

Projeto acadêmico desenvolvido como atividade final da disciplina de Algoritmos e Programação I.

**Autores:** Thales Schettini de Moraes e Thiago Luiz da Silva.
