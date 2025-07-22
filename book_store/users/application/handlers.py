from fastapi import APIRouter
from book_store.users.application.service import create_user, get_users
from book_store.users.domain.user import User
from typing import List

router = APIRouter()


@router.post("/users")
async def create(user: User):
    return await create_user(user)


@router.get("/users", response_model=List[User])
async def read_users():
    return await get_users()
