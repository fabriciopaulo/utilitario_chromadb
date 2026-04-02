from pathlib import Path

from google.cloud import aiplatform
from langchain_google_vertexai import VertexAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter

from src import menu
from src.chroma_client import get_client


def read_database():
    from src.menu import menu_principal
    root_dir = Path(__file__).resolve().parent.parent

    database_path, collection_name, dimensions, qt_results = menu.leitura(root_dir)

    client = get_client(database_path)
    collection = client.get_collection(collection_name, embedding_function=None)

    results = collection.query(
        query_embeddings=[[0.0] * dimensions],
        n_results=qt_results
    )

    print(results)
    menu_principal()


def load_data(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def chunk_text(text):
    splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separator="\n"
    )
    return splitter.split_text(text)


def create_database():
    from src.menu import menu_principal
    root_dir = Path(__file__).resolve().parent.parent

    sa_file, project, location, file_content, output_dir, collection_name = menu.criacao(root_dir)

    aiplatform.init(project=project, location=location)

    text = load_data(file_content)
    chunks = chunk_text(text)

    embeddings = VertexAIEmbeddings(
        model_name="text-embedding-large-exp-03-07",
        project=project,
        location=location
    )

    client = get_client(output_dir)

    collection = client.get_or_create_collection(
        name=collection_name,
        metadata={"hnsw:space": "cosine"}
    )

    ids = [f"chunk_{i}" for i in range(len(chunks))]
    vectors = embeddings.embed_documents(chunks)

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=vectors
    )

    print(f"[OK] Chroma DB persistido em {output_dir}")
    menu_principal()
