import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.websearch import WebSearchTools

from prompts import *

load_dotenv()

movie_recommendation_agent = Agent(
    name="FilmPro",
    tools=[WebSearchTools(backend="duckduckgo")],
    model=Gemini(id="gemini-3.8-flash", api_key=os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")),
    description=description,
    instructions=instructions,
    markdown=True,
    add_datetime_to_context=True,
)

if __name__ == "__main__":
    movie_recommendation_agent.print_response(
        input="Procuro filmes similares ao Matrix, gosto dos filmes de ficção científica com ação, efeitos visuais e história filosófica.",
        stream=True, 
    )