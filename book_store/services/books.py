from typing import List, Optional
from sqlalchemy.orm import Session
from book_store.models.book_models import BookCreate, BookUpdate, Book
from book_store.infrastructure.repository_books import (
    create_book,
    get_books,
    get_book_by_id,
    update_book,
    delete_book,
)


def add_new_book(db: Session, book_create: BookCreate) -> Book:
    return create_book(db, book_create)


def list_all_books(db: Session) -> List[Book]:
    return get_books(db)


def get_book(db: Session, book_id: int) -> Optional[Book]:
    return get_book_by_id(db, book_id)


def modify_book(db: Session, book_id: int, book_update: BookUpdate) -> Optional[Book]:
    return update_book(db, book_id, book_update)


def remove_book(db: Session, book_id: int) -> bool:
    return delete_book(db, book_id)
