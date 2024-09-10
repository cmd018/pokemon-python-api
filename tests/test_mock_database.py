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
    async def test_mock_databases(self, client_test: AsyncClient):
        # generate data
        await Pokemon(
            pokemonId=1,
            name="ivysaur",
            image="http://some/url"
        ).create()

        response = await client_test.get("pokemon")

        assert response.status_code == 200


    @pytest.mark.anyio
    async def test_mock_database(self, client_test: AsyncClient):
        await Admin(
            fullname="admin", email="admin@admin.com", password="admin"
        ).create()

        await Pokemon(
            pokemonId=1,
            name="ivysaur",
            image="http://some/url"
        ).create()

        data = {
            "name": "ivysaur", 
            "pokemonId": 1
        }

        response = await client_test.post("pokemon/verify", data=json.dumps(data))

        assert response.status_code == 200
