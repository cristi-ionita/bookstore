from pydantic import BaseModel, Field
from typing import Optional
from sqlalchemy import Table, Column, Integer, String
from .database import metadata


class Book(BaseModel):
    id: Optional[int] = Field(default=None, description="Unique identifier for the book")
    title: str = Field(..., min_length=1, max_length=200, description="Title of the book")
    author: str = Field(..., min_length=1, max_length=100, description="Author of the book")
    year: Optional[int] = Field(None, ge=0, le=2100, description="Publication year of the book")


books = Table(
    "books",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(200)),
    Column("author", String(100)),
    Column("year", Integer, nullable=True),
)
