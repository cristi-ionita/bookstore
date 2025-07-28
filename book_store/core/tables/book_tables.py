from sqlalchemy import Table, Column, Integer, String
from book_store.core.database import metadata

books = Table(
    "books",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(100), nullable=False),
    Column("author", String(100), nullable=False),
    Column("year", Integer, nullable=False),
)
