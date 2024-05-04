from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from fastapi import Body
from typing import List, Optional
from models import Book
from uuid import uuid4
import database, models, schemas, crud
from sqlalchemy.orm import Session
from database import SessionLocal, engine

app = FastAPI()
router = APIRouter()

models.Base.metadata.create_all(bind=engine)
not_found_message = "Book not found"
#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/')
async def home():
    return JSONResponse({"message": "Home is under development"})

#Get information about all the books in the database
@router.get('/books/', response_model=list[schemas.BookResponse])
async def get_books(db: Session=Depends(get_db)):
    books = crud.get_books(db)
    return books

#Get information about a single book
@router.get('/books/{book_id}', response_model=schemas.BookResponse)
async def get_single_book(book_id:int, db:Session=Depends(get_db)):
    db_book = crud.get_single_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail=not_found_message)
    return db_book

#Create a new book
@router.post('/books/', response_model=schemas.BookCreate)
async def create_book(book: schemas.BookCreate, db: Session=Depends(get_db)):
    db_book = crud.get_book_by_title(db, title=book.title)
    if db_book: 
        raise HTTPException(status_code=404, detail="Book already exists")
    return crud.create_book(db=db, book=book)

@router.put('/books/{book_id}', response_model=schemas.BookUpdate)
async def update_books(book_id:int, books:schemas.BookUpdate, db: Session=Depends(get_db)):
    book = crud.get_book_by_id(db=db, book_id=book_id)
    if book is None:
        raise HTTPException(status_code=404, detail=not_found_message)
    if not crud.update_book(db, book_id, books):
           raise HTTPException(status_code=404, detail="Failed to update book")
    return book

@router.delete('/books/{book_id}')
async def delete_book(book_id:int, db: Session=Depends(get_db)):
    book = crud.get_book_by_id(db=db, book_id=book_id)
    if book is None:
        raise HTTPException(status_code=404, detail=not_found_message)
    if not crud.delete_book(db, book_id):
        raise HTTPException(status_code=404, detail="Failed to delete book")
    return book

app.include_router(router)