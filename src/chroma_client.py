import os

import chromadb


def get_client(database_path: str):
    versao = os.getenv("VERSAO")

    if versao.startswith('0.'):
        from chromadb.config import Settings
        return chromadb.Client(Settings(
            chroma_db_impl="duckdb+parquet",
            persist_directory=database_path
        ))
    if versao.startswith('1.'):
        return chromadb.PersistentClient(path=database_path)
    raise ValueError("Versão não suportada")
