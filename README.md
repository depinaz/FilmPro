# FilmPro - Agente de Recomendação de Filmes

Agente inteligente baseado em IA que fornece recomendações personalizadas de filmes usando **Agno**, **Google Gemini**, **OMDB API** e **DuckDuckGo**.

## Setup Rápido

```powershell
# 1. Criar e ativar o ambiente virtual
python -m venv .venv
.venv\Scripts\Activate.ps1

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Configurar variáveis de ambiente
Copy-Item .env.example .env
# Edite o .env com suas chaves

# 4. Executar
python main.py
```

## Variáveis de Ambiente

```env
GOOGLE_API_KEY=sua_chave_google
OMDB_API_KEY=sua_chave_omdb
```

> A chave da OMDB API pode ser obtida gratuitamente em [omdbapi.com](https://www.omdbapi.com/apikey.aspx).

## Estrutura

```
├── main.py              # Ponto de entrada e inicialização do agente
├── requirements.txt     # Dependências
├── models/
│   └── movies.py        # Modelos Pydantic (Movie, Cast, MovieRecommendation)
├── prompts/
│   └── movie_search.py  # Descrição e instruções do agente
└── tools/
    └── omdb.py          # Integração assíncrona com a OMDB API (aiohttp)
```

## Funcionalidades

- Recomendações personalizadas de filmes baseadas nas preferências do usuário
- Busca na web via DuckDuckGo para dados atualizados
- Consulta à OMDB API para metadados detalhados dos filmes
- Saída estruturada em JSON (Pydantic) com 5 a 20 recomendações por consulta
- Informações completas: elenco, diretor, plataformas de streaming, classificação etária e mais
- Respostas em português

## Stack

- **[Agno](https://github.com/agno-agi/agno)** — orquestração do agente
- **Google Gemini-3.8 Flash** — modelo de linguagem
- **aiohttp** — cliente HTTP assíncrono para a OMDB API
- **Pydantic v2** — validação e serialização dos dados
- **DuckDuckGo Search (ddgs)** — busca na web
