from sqlalchemy import Column, Integer, String, Table

from book_store.core.database import metadata

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(50), unique=True, nullable=False),
    Column("email", String(100), unique=True, nullable=False),
    Column("password", String(128), nullable=False),
    Column("full_name", String, nullable=False),
)
