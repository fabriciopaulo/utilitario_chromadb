# Utilitário Chroma DB

Esse é uma pequena aplicação CLI para lidar com operações rápidas de suporte em bancos de dados Chroma DB.

## Features

- Leitura de dados de um banco Chroma DB;
- Criação, chunk e embedding de texto com gravação no Chroma DB.

## Requisitos

- Python 3.11+
- Projeto GCP com API VertexAI habilitada.

## Como utilizar

- Clonar o repositório;
- Renomear o arquivo `.env.example` para `.env`;
- Preencher os valores das variáveis:
    - `PROJECT` = Projeto do GCP que tem a API VertexAI habilitada;
    - `LOCATION` = Região do GCP onde o projeto está;
    - `GOOGLE_APPLICATION_CREDENTIALS` = Path do arquivo JSON com as suas credenciais ou da SA com acesso ao VertexAO.
    - `VERSAO` = É preenchida automaticamente após a seleção da versão na execução do `setup.py`
- Executar `python -m setup`;
- Executar `python -m main`;
- Selecionar a versão do Chroma DB que pretende utilizar;
- Seguir os menus.

## Notas

Versões suportadas do Chroma DB:

- `0.3.6+`
- `1.3.X+`
- `1.4.X+`

---
© 2026 - Dioleti™ Brasil