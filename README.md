# FilmPro - Agente de Recomendação de Filmes

Agente inteligente baseado em IA que fornece recomendações personalizadas de filmes usando **Agno** e **Google Gemini**.

## Setup Rápido 

```powershell
# 1. Criar e ativar o ambiente virtual
python -m venv .venv
.venv\Scripts\Activate.ps1

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Configurar a chave da API no arquivo .env
Set-Content .env 'GEMINI_API_KEY="sua_chave_aqui"'

# 4. Executar
python main.py
```

## Estrutura

```
├── main.py              # Agente principal
├── prompts/movie_search.py  # Prompts e instruções
└── requirements.txt     # Dependências
```

## Funcionalidades

- 🎬 Recomendações personalizadas de filmes
- 🔍 Busca integrada na web
- 📋 Respostas em Markdown formatado
- 🌍 Suporte a múltiplos critérios (gênero, classificação, idioma)
- 🇧🇷 Respostas em português