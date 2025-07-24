import pytest
from httpx import AsyncClient
from book_store.app import app
from book_store.users.domain.database import database
from httpx._transports.asgi import ASGITransport

@pytest.mark.asyncio
async def test_book_crud():
    await database.connect()

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Create book
        response = await ac.post("/api/books", json={
            "title": "1984",
            "author": "George Orwell",
            "year": 1949
        })
        assert response.status_code == 200
        book = response.json()
        book_id = book["id"]

        # Get all books
        response = await ac.get("/api/books")
        assert response.status_code == 200
        assert any(b["id"] == book_id for b in response.json())

        # Update book
        response = await ac.put(f"/api/books/{book_id}", json={
            "title": "Animal Farm"
        })
        assert response.status_code == 200
        updated_book = response.json()
        assert updated_book["title"] == "Animal Farm"

        # Delete book
        response = await ac.delete(f"/api/books/{book_id}")
        assert response.status_code == 200
        assert response.json() == {"detail": "Book deleted"}
    await database.disconnect()