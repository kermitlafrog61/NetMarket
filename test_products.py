import pytest
from httpx import AsyncClient

from main import app


@pytest.mark.asyncio
async def test_list():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/products/")
    assert response.status_code == 200
