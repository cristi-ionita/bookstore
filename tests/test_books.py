import pytest
from fastapi.testclient import TestClient
from book_store.app import app
from book_store.core.database import engine, Base

client = TestClient(app)


@pytest.fixture(scope="module", autouse=True)
def setup_db():
    # Creează tabelele înainte de teste
    Base.metadata.create_all(bind=engine)
    yield
    # Șterge tabelele după teste
    Base.metadata.drop_all(bind=engine)


def test_book_crud():
    # === CREATE book ===
    new_book = {"title": "1984", "author": "George Orwell", "year": 1949}
    response = client.post("/api/books/", json=new_book)
    assert response.status_code == 200, f"Create failed: {response.text}"
    book = response.json()
    book_id = book.get("id")
    assert book_id is not None, "Book ID missing"
    assert book["title"] == new_book["title"]
    assert book["author"] == new_book["author"]
    assert book["year"] == new_book["year"]

    # === GET all books ===
    response = client.get("/api/books/")
    assert response.status_code == 200, f"Get all failed: {response.text}"
    books = response.json()
    assert any(b["id"] == book_id for b in books), "Created book not in list"

    # === UPDATE book ===
    update_data = {"title": "Animal Farm"}
    response = client.put(f"/api/books/{book_id}/", json=update_data)
    assert response.status_code == 200, f"Update failed: {response.text}"
    updated_book = response.json()
    assert updated_book["title"] == "Animal Farm"
    assert updated_book["author"] == new_book["author"]  # unchanged
    assert updated_book["year"] == new_book["year"]  # unchanged

    # === DELETE book ===
    response = client.delete(f"/api/books/{book_id}/")
    assert response.status_code == 200, f"Delete failed: {response.text}"
    assert response.json() == {"detail": "Book deleted"}

    # === VERIFY delete ===
    response = client.get(f"/api/books/{book_id}/")
    assert response.status_code == 404, "Deleted book still retrievable"


def test_create_book_invalid_data():
    # Lipsește titlul
    response = client.post("/api/books/", json={"author": "Author"})
    assert response.status_code == 422  # validation error


def test_get_book_not_found():
    response = client.get("/api/books/999999/")
    assert response.status_code == 404
