from fastapi import HTTPException
from users.domain.user import CreateUser


def create_user(user_data:CreateUser):
    return {"message":f"User {user_data.username} created"}