from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserBase(BaseModel):
    """Datele de bază pentru un utilizator (fără parolă)"""

    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr


class UserCreate(UserBase):
    """Date necesare pentru crearea unui utilizator"""

    password: str = Field(..., min_length=6)


class UserUpdate(BaseModel):
    """Date opționale pentru actualizarea unui utilizator"""

    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=6)


class User(UserBase):
    """Modelul complet al utilizatorului, inclusiv ID"""

    id: Optional[int] = None

    model_config = {"from_attributes": True}


class MessageResponse(BaseModel):
    detail: str
