from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing import Optional


class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    full_name: str = Field(..., min_length=3, max_length=100)
    model_config = ConfigDict(from_attributes=True)


class UserCreate(UserBase):
    password: str = Field(..., min_length=6)
    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    password: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)


class User(UserBase):
    id: Optional[int] = None
    model_config = ConfigDict(from_attributes=True)


class MessageResponse(BaseModel):
    detail: str
    model_config = ConfigDict(from_attributes=True)
