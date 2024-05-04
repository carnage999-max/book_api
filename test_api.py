from fastapi.testclient import TestClient
from api import app
from fastapi import status

import pytest
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from database import engine, SessionLocal, Base


client = TestClient(app=app)

# Clear database tables before each test
@pytest.fixture(autouse=True)
def clear_database():
    Base.metadata.create_all(bind=engine)
    
    connection = engine.connect()
    transaction = connection.begin()

    try:
        # Clear all data from tables
        for table in reversed(Base.metadata.sorted_tables):
            connection.execute(table.delete())

        transaction.commit()

    finally:
        connection.close()


def test_read_books():
    response = client.get('/books/')
    assert response.status_code == status.HTTP_200_OK
    
def test_read_book():
    client.post('/books/', json={"title":"My Book Title I","author": "A man","year": 2016, "isbn": "1112-1123-2234"})
    response = client.get('/books/1')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"id":1, "title":"My Book Title I","author": "A man","year": 2016, "isbn": "1112-1123-2234"}
    
    
def test_create_books():
    response = client.post('/books/', json={"title":"My Book Title II","author": "Creators","year": 2019, "isbn": "0012-1123-2234"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"title":"My Book Title II","author": "Creators","year": 2019, "isbn": "0012-1123-2234"}
    
def test_update_book():
    client.post('/books/', json={"title":"Mind Games","author": "Jacob Fischer","year": 2009, "isbn": "1012-0023-8899"})
    response = client.put('/books/1', json={"title":"Mind Games II","author": "Jacob Fisher","year": 2009, "isbn": "1012-0023-8899"})

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"title":"Mind Games II","author": "Jacob Fisher","year": 2009, "isbn": "1012-0023-8899"}
    
def test_delete_book():
    client.post('/books/', json={"title":"Mind Games","author": "Jacob Fisher","year": 2011, "isbn": "1012-0023-8899"})
    response = client.delete('/books/1')

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"id":1, "title":"Mind Games","author": "Jacob Fisher","year": 2011, "isbn": "1012-0023-8899"}
