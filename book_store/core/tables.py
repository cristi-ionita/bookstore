from sqlalchemy import Table, Column, Integer, String
from .database import metadata

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(50), unique=True, nullable=False),
    Column("email", String(100), unique=True, nullable=False),
    Column("password", String(128), nullable=False),
)

books = Table(
    "books",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(100), nullable=False),
    Column("author", String(100), nullable=False),
    Column("year", Integer, nullable=False),
)
