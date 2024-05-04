from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional

from sqlalchemy import Column, Integer, String
from database import Base


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True, index=True)
    author = Column(String)
    year = Column(Integer)
    isbn = Column(String)
    