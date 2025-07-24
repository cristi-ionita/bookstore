from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from sqlalchemy import Table, Column, Integer, String
from .database import metadata

""" Modele Pydantic """

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr

class UserCreate(UserBase):
    password: str = Field(..., min_length=6)

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

class User(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

""" Tabela SQLAlchemy """

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(50), unique=True, index=True),
    Column("email", String(255), unique=True, index=True),
    Column("password", String(255)),
)