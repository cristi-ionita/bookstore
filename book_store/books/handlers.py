from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from book_store.books.services import (
    create_book,
    get_books,
    get_book_by_id,
    update_book,
    delete_book,
)
from book_store.books.book_models import Book, BookCreate, BookUpdate
from book_store.core.database import get_db

router = APIRouter()


@router.post("/", response_model=Book)
def create_book_endpoint(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book)


@router.get("/", response_model=List[Book])
def read_books(db: Session = Depends(get_db)):
    return get_books(db)


@router.get("/{book_id}", response_model=Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.put("/{book_id}", response_model=Book)
def update_book_endpoint(
    book_id: int, book_update: BookUpdate, db: Session = Depends(get_db)
):
    updated_book = update_book(db, book_id, book_update)
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book


@router.delete("/{book_id}", response_model=dict)
def delete_book_endpoint(book_id: int, db: Session = Depends(get_db)):
    deleted = delete_book(db, book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"detail": "Book deleted"}
