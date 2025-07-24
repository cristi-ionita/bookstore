from pydantic import BaseModel, Field
from typing import Optional
from sqlalchemy import Table, Column, Integer, String
from .database import metadata

"""Modele Pydantic"""
class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    author: str = Field(..., min_length=1, max_length=100)
    year: int = Field(..., ge=0)


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None


class Book(BookBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


"""Tabela SQLAlchemy"""

books = Table(
    "books",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(100), nullable=False),
    Column("author", String(100), nullable=False),
    Column("year", Integer, nullable=False),
)
