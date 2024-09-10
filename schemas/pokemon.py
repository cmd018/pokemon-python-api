from pydantic import BaseModel, EmailStr
from typing import List, Optional, Any

class VerifyPokemonRequest(BaseModel):
    pokemonId: int
    name: str

    class Collection:
        name = "pokemon"

    class Config:
        json_schema_extra = {
            "example": {
                "pokemonId": 4,
                "name": "charmander",
            }
        }

class Pokemon(BaseModel):
    pokemonId: int
    name: str
    image: str

    class Collection:
        name = "pokemon"

    class Config:
        json_schema_extra = {
            "example": {
                "pokemonId": 4,
                "name": "charmander",
                "image": "http://some/url",
            }
        }

class PokemonsResponse(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: List[Pokemon]

    class Collection:
        name = "pokemon"

    class Config:
        json_schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation successful",
                "data": [
                    {
                        "pokemonId": 4,
                        "name": "charmander",
                        "image": "http://some/url",
                    },
                    {
                        "pokemonId": 4,
                        "name": "charmander",
                        "image": "http://some/url",
                    }
                ],
            }
        }

class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]

    class Config:
        json_schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation successful",
                "data": "Sample data",
            }
        }