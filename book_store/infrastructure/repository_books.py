from typing import List, Optional

from sqlalchemy import delete, insert, select, update
from sqlalchemy.orm import Session

from book_store.core.tables.book_tables import books
from book_store.models.book_models import Book, BookCreate, BookUpdate


def create_book(db: Session, book_create: BookCreate) -> Book:
    book_dict = book_dict = book_create.model_dump()
    stmt = insert(books).values(**book_dict)
    result = db.execute(stmt)
    book_id = result.inserted_primary_key[0]
    db.commit()
    return Book(id=book_id, **book_dict)


def get_books(db: Session) -> List[Book]:
    stmt = select(books)
    result = db.execute(stmt).mappings().all()
    return [Book(**row) for row in result]


def get_book_by_id(db: Session, book_id: int) -> Optional[Book]:
    stmt = select(books).where(books.c.id == book_id)
    result = db.execute(stmt).mappings().first()
    if result:
        return Book(**result)
    return None


def update_book(db: Session, book_id: int, book_update: BookUpdate) -> Optional[Book]:
    existing_book = get_book_by_id(db, book_id)
    if not existing_book:
        return None
    update_data = book_update.model_dump(exclude_unset=True)
    stmt = update(books).where(books.c.id == book_id).values(**update_data)
    db.execute(stmt)
    db.commit()
    return get_book_by_id(db, book_id)


def delete_book(db: Session, book_id: int) -> bool:
    stmt = delete(books).where(books.c.id == book_id)
    db.execute(stmt)
    db.commit()
    return True
