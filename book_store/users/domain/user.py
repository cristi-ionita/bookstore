from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from sqlalchemy import Table, Column, Integer, String
from .database import metadata


class User(BaseModel):
    id: Optional[int] = Field(default=None, description="Unique identifier for the user")
    username: str = Field(..., min_length=3, max_length=50, description="Username of the user")
    email: EmailStr = Field(..., description="User's email address")
    password: str = Field(..., min_length=6, description="Hashed password of the user")


users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(50), unique=True, index=True),
    Column("email", String(255), unique=True, index=True),
    Column("password", String(255)),
)
