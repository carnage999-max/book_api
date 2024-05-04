import database, models, schemas
from sqlalchemy.orm import Session
from typing import Optional


def get_books(db:Session):
    return db.query(models.Book).all()

def get_single_book(db:Session, book_id:int):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    return book

def create_book(db:Session, book:schemas.BookCreate):
    db_book = models.Book(
        title=book.title,
        author=book.author,
        year=book.year,
        isbn=book.isbn,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_book_by_title(db:Session, title:str):
    return db.query(models.Book).filter(models.Book.title == title).first()

def get_book_by_id(db:Session, book_id:int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def update_book(db: Session, book_id: int, books:schemas.BookUpdate):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book:
        book.title = books.title
        book.author = books.author
        book.year = books.year
        book.isbn = books.isbn
        db.commit()
        return book
    return False

def delete_book(db:Session, book_id:int):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
        return book
    return False
    
