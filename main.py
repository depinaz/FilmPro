import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.websearch import WebSearchTools

from models.movies import MovieRecommendation
from prompts import *
from tools.omdb import search_movie


movie_recommendation_agent = Agent(
    name="FilmPro",
    tools=[WebSearchTools(backend="duckduckgo"), search_movie],
    model=Gemini(id="gemini-3.8-flash", api_key=os.getenv("GOOGLE_API_KEY")),
    description=description,
    instructions=instructions,
    markdown=True,
    add_datetime_to_context=True,
    output_schema=MovieRecommendation,
    debug_mode=True,
    debug_level=1,
)

async def recommendations():
    result = await movie_recommendation_agent.arun(
        "Estou procurando filmes similares ao Star Wars. "
        "Gosto de filmes de ação.",
        stream=False,
    )

    if result and result.content:
        if isinstance(result.content, MovieRecommendation):
            pretty_json_output = result.content.model_dump_json(indent=2)
            print(pretty_json_output)
        elif isinstance(result.content, str):
            try:
                data = MovieRecommendation.model_validate_json(result.content)
                print(data.model_dump_json(indent=2))
            except Exception:
                print(result.content)
        else:
            print(result.content)

    return result


if __name__ == "__main__":
    asyncio.run(recommendations())