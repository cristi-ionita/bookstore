import pytest
from fastapi.testclient import TestClient
from book_store.app import app
from book_store.core.database import engine, Base

client = TestClient(app)


# TODO: lets move fixtures into the conftest module like pytest propagates
@pytest.fixture(scope="module", autouse=True)
def setup_db():
    # Creează tabelele înainte de teste
    Base.metadata.create_all(bind=engine)
    yield
    # Șterge tabelele după teste
    Base.metadata.drop_all(bind=engine)


def test_user_crud():
    # === CREATE user ===
    new_user = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "secret123",
    }
    response = client.post("/api/users/", json=new_user)
    assert response.status_code == 200, f"Create failed: {response.text}"
    user = response.json()
    user_id = user.get("id")
    assert user_id is not None, "User ID missing from response"
    assert user["username"] == new_user["username"]
    assert user["email"] == new_user["email"]
    assert "password" not in user, "Password should not be exposed"

    # === GET all users ===
    response = client.get("/api/users/")
    assert response.status_code == 200, f"List users failed: {response.text}"
    users = response.json()
    assert any(u["id"] == user_id for u in users), "Created user not found in list"

    # === UPDATE user ===
    updated_data = {"username": "updateduser"}
    response = client.put(f"/api/users/{user_id}/", json=updated_data)
    assert response.status_code == 200, f"Update failed: {response.text}"
    updated_user = response.json()
    assert updated_user["username"] == "updateduser"
    assert updated_user["email"] == new_user["email"]
    assert "password" not in updated_user

    # === DELETE user ===
    response = client.delete(f"/api/users/{user_id}/")
    assert response.status_code == 200, f"Delete failed: {response.text}"
    assert response.json() == {"detail": "User deleted"}

    # === VERIFY delete ===
    response = client.get(f"/api/users/{user_id}/")
    assert response.status_code == 404, "Deleted user still retrievable"


def test_create_user_invalid_data():
    # Email invalid (fără @)
    response = client.post(
        "/api/users/",
        json={"username": "baduser", "email": "bademail", "password": "secret123"},
    )
    assert response.status_code == 422


def test_get_user_not_found():
    response = client.get("/api/users/999999/")
    assert response.status_code == 404


def test_update_user_invalid_data():
    # Creează un user temporar
    response = client.post(
        "/api/users/",
        json={
            "username": "tempuser",
            "email": "tempuser@example.com",
            "password": "secret123",
        },
    )
    user = response.json()
    user_id = user["id"]

    # Update cu email invalid
    response = client.put(f"/api/users/{user_id}/", json={"email": "not-an-email"})
    assert response.status_code == 422

    # Șterge user-ul temporar
    client.delete(f"/api/users/{user_id}/")
