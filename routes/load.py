from fastapi import APIRouter, Body
from typing import Optional

import requests

from database.database import *
from models.pokemon import Pokemon
from schemas.load import LoadPokemonResponse
from typing import List


router = APIRouter()

@router.get("/", response_description="Pokemons loaded", response_model=LoadPokemonResponse)
async def load_pokemons():

    response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=50")
    json_object = response.json()["results"]

    count = 0
    list = []
    for pokemon in json_object:
        count += 1
        list.append(Pokemon(
            pokemonId=count,  
            name=pokemon["name"], 
            image= f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/{count}.svg"))
        
    await load_pokemons_db(list)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Pokemons data loaded successfully",
        "data": "Pokemons loaded",
    }




