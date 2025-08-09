def test_book_crud(client):
    # TODO: what exactly you are trying to test here? CRUD operations on books?
    # if so lets split this into multiple tests
    new_book = {"title": "1984", "author": "George Orwell", "year": 1949}
    response = client.post("/api/books/", json=new_book)
    assert response.status_code == 200, f"Create failed: {response.text}"
    book = response.json()
    book_id = book.get("id")
    assert book_id is not None, "Book ID missing"
    assert book["title"] == new_book["title"]
    assert book["author"] == new_book["author"]
    assert book["year"] == new_book["year"]

    response = client.get("/api/books/")
    assert response.status_code == 200, f"Get all failed: {response.text}"
    books = response.json()
    assert any(b["id"] == book_id for b in books), "Created book not in list"

    update_data = {"title": "Animal Farm"}
    response = client.put(f"/api/books/{book_id}/", json=update_data)
    assert response.status_code == 200, f"Update failed: {response.text}"
    updated_book = response.json()
    assert updated_book["title"] == "Animal Farm"
    assert updated_book["author"] == new_book["author"]
    assert updated_book["year"] == new_book["year"]

    response = client.delete(f"/api/books/{book_id}/")
    assert response.status_code == 200, f"Delete failed: {response.text}"
    assert response.json() == {"message": "Book deleted successfully"}

    response = client.get(f"/api/books/{book_id}/")
    assert response.status_code == 404, "Deleted book still retrievable"


def test_create_book_invalid_data(client):
    response = client.post("/api/books/", json={"author": "Author"})
    assert response.status_code == 422


def test_get_book_not_found(client):
    response = client.get("/api/books/999999/")
    assert response.status_code == 404
