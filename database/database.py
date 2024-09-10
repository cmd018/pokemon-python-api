from typing import List, Union

from beanie import PydanticObjectId
from beanie.operators import In


from models.admin import Admin
from models.pokemon import Pokemon

admin_collection = Admin
pokemon_collection = Pokemon


async def add_admin(new_admin: Admin) -> Admin:
    admin = await new_admin.create()
    return admin



async def retrieve_pokemons() -> List[Pokemon]:
    pokemons = await pokemon_collection.all().to_list()
    return pokemons


async def load_pokemons_db(pokemons: List[Pokemon]) -> List[Pokemon]:
    new_pokemons = await pokemon_collection.insert_many(pokemons)
    return new_pokemons

    
async def retrieve_pokemon(pokemonId: int) -> Pokemon:
    pokemon = await pokemon_collection.find_one(Pokemon.pokemonId == pokemonId)
    if pokemon:
        return pokemon

async def retrieve_random_pokemons(pokemonIds: List[int]) -> Pokemon:
    pokemons = await pokemon_collection.find(
        In(pokemon_collection.pokemonId, pokemonIds)
    ).to_list()
    if pokemons:
        return pokemons
