from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from book_store.services.books import (
    add_new_book,
    list_all_books,
    get_book,
    modify_book,
    remove_book,
)
from book_store.models.book_models import Book, BookCreate, BookUpdate
from book_store.core.database import get_session

router = APIRouter(tags=["books"])


@router.post("/", response_model=Book)
def create_book(book_create: BookCreate, db: Session = Depends(get_session)):
    return add_new_book(db, book_create)


@router.get("/", response_model=List[Book])
def read_books(db: Session = Depends(get_session)):
    return list_all_books(db)


@router.get("/{book_id}", response_model=Book)
def read_book(book_id: int, db: Session = Depends(get_session)):
    book = get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.put("/{book_id}", response_model=Book)
def update_book(book_id: int, book_update: BookUpdate, db: Session = Depends(get_session)):
    updated_book = modify_book(db, book_id, book_update)
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book


@router.delete("/{book_id}", response_model=dict)
def delete_book(book_id: int, db: Session = Depends(get_session)):
    success = remove_book(db, book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}
