def test_user_crud(client):
    new_user = {
        "username": "testuser",
        "email": "testuser@example.com",
        "full_name": "Test User",
        "password": "securepassword123",
    }
    # CREATE user
    response = client.post("/api/users/", json=new_user)
    assert response.status_code == 200, f"Create failed: {response.text}"
    user = response.json()
    user_id = user.get("id")
    assert user_id is not None, "User ID missing"
    assert user["username"] == new_user["username"]
    assert user["email"] == new_user["email"]
    assert user["full_name"] == new_user["full_name"]

    # GET all users
    response = client.get("/api/users/")
    assert response.status_code == 200, f"Get all failed: {response.text}"
    users = response.json()
    assert any(u["id"] == user_id for u in users), "Created user not in list"

    # GET user by ID
    response = client.get(f"/api/users/{user_id}/")
    assert response.status_code == 200, f"Get by ID failed: {response.text}"
    user_by_id = response.json()
    assert user_by_id["id"] == user_id

    # UPDATE user
    update_data = {"full_name": "Updated User Name"}
    response = client.put(f"/api/users/{user_id}/", json=update_data)
    assert response.status_code == 200, f"Update failed: {response.text}"
    updated_user = response.json()
    assert updated_user["full_name"] == "Updated User Name"
    assert updated_user["username"] == new_user["username"]

    # DELETE user
    response = client.delete(f"/api/users/{user_id}/")
    assert response.status_code == 200, f"Delete failed: {response.text}"
    assert response.json() == {"message": "User deleted successfully"}
    response = client.get(f"/api/users/{user_id}/")
    assert response.status_code == 404, "Deleted user still retrievable"


def test_create_user_invalid_data(client):
    response = client.post("/api/users/", json={"email": "nouser@example.com"})
    assert response.status_code == 422


def test_get_user_not_found(client):
    response = client.get("/api/users/999999/")
    assert response.status_code == 404
