from pydantic import BaseModel
from typing import Any, List, Optional


class LoadPokemonResponse(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]

    class Collection:
        name = "load"

    class Config:
        json_schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation successful",
                "data": [{
                "pokemonId": 4,
                "name": "charmander",
                "image": "https://url/to/image"
                },{
                    "pokemonId": 5,
                    "name": "pickachu",
                    "image": "https://url/to/image5"
                }],
            }
        }
