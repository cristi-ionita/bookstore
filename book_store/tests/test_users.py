import pytest
from httpx import AsyncClient
from httpx._transports.asgi import ASGITransport
from book_store.app import app
from book_store.users.domain.database import database

@pytest.mark.asyncio
async def test_user_crud():
    # Conectare la baza de date
    await database.connect()

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # CREATE user
        response = await ac.post("/api/users", json={
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "secret123"
        })
        assert response.status_code == 200
        user = response.json()
        user_id = user["id"]

        # Verificare să nu existe câmpul 'password' în răspuns
        assert "password" not in user

        # GET all users
        response = await ac.get("/api/users")
        assert response.status_code == 200
        users = response.json()
        assert any(u["id"] == user_id for u in users)

        # UPDATE user (modificare username)
        response = await ac.put(f"/api/users/{user_id}", json={
            "username": "updateduser"
        })
        assert response.status_code == 200
        updated_user = response.json()
        assert updated_user["username"] == "updateduser"
        assert "password" not in updated_user

        # DELETE user
        response = await ac.delete(f"/api/users/{user_id}")
        assert response.status_code == 200
        assert response.json() is True

    # Deconectare de la baza de date
    await database.disconnect()