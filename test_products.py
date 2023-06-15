import pytest
from httpx import AsyncClient

from main import app


@pytest.mark.asyncio
async def test_list():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/products/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        body = {
            'title': 'test',
            'description': 'test',
            'price': 100
        }
        response = await ac.post("/products/", json=body)
    assert response.json()['title'] == body['title']
    assert response.json()['description'] == body['description']
    assert response.json()['price'] == body['price']
    assert response.status_code == 201


@pytest.mark.asyncio
async def test_update():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        body = {
            'title': 'test',
            'description': 'test',
            'price': 100
        }
        response = await ac.patch(f"/products//", json=body)
    assert response.json()['title'] == body['title']
    assert response.json()['description'] == body['description']
    assert response.json()['price'] == body['price']
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_delete():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        body = {
            'title': 'test',
            'description': 'test',
            'price': 100
        }
        response_create = await ac.post("/products/", json=body)
        id = response_create.json()['id']
        response_delete = await ac.delete(f"/products/{id}/")
    assert response_delete.status_code == 204
