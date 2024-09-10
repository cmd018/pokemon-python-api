import asyncio
import json
from beanie import init_beanie
from fastapi.testclient import TestClient
from httpx import AsyncClient
import pytest

from models.admin import Admin
from models.pokemon import Pokemon
from tests.conftest import mock_no_authentication


class TestMockAuthentication:
    @classmethod
    def setup_class(cls):
        mock_no_authentication()

    @pytest.mark.anyio
    async def test_mock_pokemons(self, client_test: AsyncClient):
        # generate data
        await Pokemon(
            pokemonId=100,
            name="ivysaur",
            image="http://some/url"
        ).create()

        response = await client_test.get("pokemon")

        assert response.status_code == 200


    @pytest.mark.anyio
    async def test_mock_pokemon_verify(self, client_test: AsyncClient):

        await Pokemon(
            pokemonId=101,
            name="ivysaur",
            image="http://some/url"
        ).create()

        data = {
            "name": "ivysaur", 
            "pokemonId": 101
        }

        response = await client_test.post("pokemon/verify", data=json.dumps(data))

        assert response.status_code == 200

    @pytest.mark.anyio
    async def test_mock_pokemon_random(self, client_test: AsyncClient):

        response = await client_test.get("pokemon/random")

        assert response.status_code == 200

    @pytest.mark.anyio
    async def test_mock_pokemon_random_with_id(self, client_test: AsyncClient):

        response = await client_test.get("pokemon/random?id=3")

        assert response.status_code == 200
    
    @pytest.mark.anyio
    async def test_mock_admin_signup(self, client_test: AsyncClient):

        # email already exists
        data = {
            "email": "email@gmail.com",
            "fullname": "Jon Snow",
            "password": "3xt3m#"
        }

        response = await client_test.post("admin", data=json.dumps(data))

        assert response.status_code == 409

    @pytest.mark.anyio
    async def test_mock_admin_login(self, client_test: AsyncClient):

        # email already exists
        data = {
            "password": "3xt3m#",
            "username": "email@gmail.com"
        }

        response = await client_test.post("admin/login", data=json.dumps(data))

        assert response.status_code == 200
