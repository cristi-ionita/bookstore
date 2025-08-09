from sqlalchemy import Column, Integer, String, Table

from book_store.core.database import metadata

books = Table(
    "books",
    metadata,
    Column("id", Integer, primary_key=True),  # TODO: lets use UUID instead of Integer for id
    Column("title", String(100), nullable=False),
    Column("author", String(100), nullable=False),
    Column("year", Integer, nullable=False),
)
