from fastapi import APIRouter, Body
from typing import Optional

import random

from database.database import *
from models.pokemon import Pokemon
from schemas.pokemon import PokemonsResponse, VerifyPokemonRequest, Response
from typing import List


router = APIRouter()

@router.get("/", response_description="Get all pokemons", response_model=PokemonsResponse)
async def get_pokemons():

    pokemons = await retrieve_pokemons()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Pokemons data retrieved successfully",
        "data": pokemons,
    }

@router.get("/random", response_description="Gets a random pokemon", response_model=Response)
async def get_random_pokemon_data(id: int = 0):

    id_passed = False

    randomIds = random.sample(range(1,50),4)
    if id > 0 and id < 51:
        randomIds[0] = id
        id_passed = True
    pokemons = await retrieve_random_pokemons(randomIds)
    decoyNames = []

    if pokemons:

        for pokemon in pokemons:
            decoyNames.append(pokemon.name)

        random.shuffle(decoyNames)

        response = {
            "pokemonId": pokemons[0].pokemonId,
            "image": pokemons[0].image,
            "decoyNames":  decoyNames
        }

        if id_passed:
            pokemon = next(p for p in pokemons if p.pokemonId == id)
            response = {
                "pokemonId": pokemon.pokemonId,
                "image": pokemon.image,
                "decoyNames":  decoyNames
            }

        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Pokemons data retrieved successfully",
            "data": response
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Pokemons doesn't exist",
    }

@router.post("/verify", response_model=Response)
async def verify_pokemon(req: VerifyPokemonRequest = Body(...)):
    pokemon = await retrieve_pokemon(req.pokemonId)
    if pokemon:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Pokemon with ID: {} found".format(req.pokemonId),
            "data": {
                "name": pokemon.name,
                "image": pokemon.image,
                "correct": req.name == pokemon.name
            },
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. Pokemon with ID: {} not found".format(req.pokemonId),
        "data": False,
    }





