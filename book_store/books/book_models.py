from pydantic import BaseModel, Field
from typing import Optional


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
