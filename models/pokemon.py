
from typing import Optional, Any

import pymongo
from beanie import Document, Indexed
from pydantic import BaseModel

class Pokemon(Document):
    pokemonId: int
    name: str
    image: str

    class Config:
        json_schema_extra = {
            "example": {
                "pokemonId": 1,
                "name": "bulbasaur",
                "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/1.svg",
            }
        }

    class Settings:
        name = "pokemon"
        use_cache = True