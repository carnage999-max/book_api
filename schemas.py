from pydantic import BaseModel
from typing import Optional


class BookBase(BaseModel):
    title: str
    author: str
    year: int
    isbn: str
    
class BookCreate(BookBase):
    class Config:
        orm_mode = True

class BookResponse(BookBase):
    id: int
    class Config:
        orm_mode = True
        
class BookUpdate(BookBase):
    class Config:
        orm_mode = True
