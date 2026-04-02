import os
import subprocess

from dotenv import load_dotenv

from src.menu import selecao_versao


def update_env_var(key: str, value: str, env_path: str = ".env"):
    lines = []
    found = False

    if os.path.exists(env_path):
        with open(env_path, "r") as f:
            for line in f:
                if line.startswith(f"{key}="):
                    lines.append(f"{key}={value}\n")
                    found = True
                else:
                    lines.append(line)

    if not found:
        lines.append(f"{key}={value}\n")

    with open(env_path, "w") as f:
        f.writelines(lines)


if __name__ == '__main__':
    versao = selecao_versao()

    update_env_var("VERSAO", versao)

    requirements = {
        "0.3+": [
            'chromadb~=0.3.6',
            'pydantic==1.10.13',
            'duckdb==0.7.1',
            'langchain==0.1.16',
            'langchain-community==0.0.34',
            'langchain-google-vertexai==0.1.0',
            'google-cloud-aiplatform==1.49.0',
            'python-dotenv==1.0.1'
        ],
        "1.3+": [
            'chromadb==1.3.0',
            'duckdb==0.9.2',
            'uvicorn==0.23.2',
            'langchain==0.1.16',
            'langchain-community==0.0.34',
            'langchain-google-vertexai==0.1.0',
            'google-cloud-aiplatform==1.49.0',
            'python-dotenv==1.0.1'
        ],
        "1.4+": [
            'chromadb~=1.4.0',
            'pydantic~=2.6.4',
            'pydantic-core~=2.16.3',
            'uvicorn~=0.29.0',
            'fastapi~=0.110.0',
            'typing_extensions~=4.10.0',
            'langchain~=0.1.16',
            'langchain-community~=0.0.34',
            'langchain-google-vertexai~=0.1.0',
            'google-cloud-aiplatform~=1.49.0',
            'python-dotenv~=1.0.1'
        ],
    }

    for pkg in requirements[versao]:
        subprocess.run(["pip", "install", pkg])

    load_dotenv()
    print(f'Versão selecionada: {os.getenv("VERSAO")}')
