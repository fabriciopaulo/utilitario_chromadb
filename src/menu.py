import os
from pathlib import Path

from src.operations import read_database, create_database


def menu_principal():
    print("* ================================================================================= *")
    print(' Utilitário Chroma DB')
    print("* ================================================================================= *\n")
    print("Selecione a função desejada:")
    print("[1] Ler um banco local Chroma DB")
    print("[2] Criar/escrever um banco local Chroma DB")
    try:
        selected = int(input())
        if selected == 1:
            read_database()
        elif selected == 2:
            create_database()
        else:
            raise ValueError("Opção inválida!")
    except ValueError:
        print("Opção inválida!")
        return menu_principal()


def selecao_versao():
    print("Escolha a versão do Chroma DB:")
    print("[1] 0.3+")
    print("[2] 1.3+")
    print("[3] 1.4+")
    try:
        selected = int(input())
        if selected == 1:
            return "0.3+"
        elif selected == 2:
            return "1.3+"
        elif selected == 3:
            return "1.4+"
        else:
            raise ValueError('Opção invalida!')
    except ValueError:
        print("Versão inválida, escolha uma versão na lista")
        return selecao_versao()


def criacao(root_dir: Path):
    sa_file = input("Digite o caminho (Path) do arquiv JSON com a chave da Service Account:\n")
    project = input("Digite o projeto onde está a API do VertexAI para geração dos Embeddings:\n")
    location = input("Digite a região do projeto onde está habilitada a API VertexAI:\n")
    collection_name = input("Digite a coleção a ser criada (Ou deixe em branco para ler default):\n")
    file_content = input("Digite o path do arquivo de dados:\n")
    output_dir = input(
        "Digite o local onde deseja salvar os arquivos do banco (Ou deixe em branco para usar o padrão):\m")

    if not sa_file:
        sa_file = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

    if not output_dir:
        output_dir = f"{root_dir}/output/{os.getenv('VERSAO')}"

    if not file_content:
        file_content = f"{root_dir}/input/data.txt"

    if not project:
        project = os.getenv('PROJECT')

    if not location:
        location = os.getenv('LOCATION')

    if not collection_name:
        collection_name = 'default'

    return sa_file, project, location, file_content, output_dir, collection_name


def leitura(root_dir: Path):
    database_path = input(
        "Digite o local dos arquivos do banco de dados (Ou deixe em branco para ler do local padrão):\n")
    collection_name = input("Digite a coleção a ser lida (Ou deixe em branco para ler default):\n")
    dimensions = input("Digite a dimensão dos embeddings (Ou deixe em branco para o valor padrão 3072):\n")
    qt_results = input("Digite quantos registros deseja ler (Ou deixe em branco para ler 3 registros):\n")

    if not database_path:
        database_path = f"{root_dir}/output/{os.getenv('VERSAO')}"

    if not collection_name:
        collection_name = 'default'

    if not dimensions:
        dimensions = 3072
    else:
        dimensions = int(dimensions)

    if not qt_results:
        qt_results = 3
    else:
        qt_results = int(qt_results)

    return database_path, collection_name, dimensions, qt_results
