from fastapi import APIRouter
from users.domain.user import CreateUser
from users.application.service import create_user

router = APIRouter()

@router.post("/users")
def add_user(user:CreateUser):
    return create_user(user)