from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    author: str = Field(..., min_length=1, max_length=100)
    year: int = Field(..., ge=0)
    model_config = ConfigDict(from_attributes=True)


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None
    model_config = ConfigDict(from_attributes=True)


class Book(BookBase):
    id: Optional[int] = None
    model_config = ConfigDict(from_attributes=True)
