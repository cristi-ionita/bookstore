from fastapi import APIRouter, HTTPException
from book_store.users.application.service import (
    create_user, get_users, get_user_by_id, update_user, delete_user,
    create_book, get_books, get_book_by_id, update_book, delete_book
)
from book_store.users.domain.user import UserCreate
from book_store.users.domain.user import User, UserUpdate
from book_store.users.domain.book import BookCreate, BookUpdate, Book
from typing import List

router = APIRouter()

"""USERS"""


@router.post("/users", response_model=User)
async def create(user: UserCreate):
    return await create_user(user)


@router.get("/users", response_model=List[User])
async def read_users():
    return await get_users()


@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    user = await get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/users/{user_id}", response_model=User)
async def update_user_endpoint(user_id: int, user_update: UserUpdate):
    updated_user = await update_user(user_id, user_update)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


@router.delete("/users/{user_id}", response_model=bool)
async def delete_user_endpoint(user_id: int):
    deleted = await delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return True



"""BOOKS"""


@router.post("/books", response_model=Book)
async def create_book_endpoint(book: BookCreate):
    return await create_book(book)


@router.get("/books", response_model=List[Book])
async def read_books():
    return await get_books()

@router.get("/books/{book_id}", response_model=Book)
async def read_book(book_id: int):
    book = await get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.put("/books/{book_id}", response_model=Book)
async def update_book_endpoint(book_id: int, book_update: BookUpdate):
    updated_book = await update_book(book_id, book_update)
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book

@router.delete("/books/{book_id}", response_model=dict)
async def delete_book_endpoint(book_id: int):
    deleted = await delete_book(book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"detail": "Book deleted"}
