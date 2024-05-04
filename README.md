# Books API documentation
>
> Swagger documentation is available at `<host_name>/docs`
>
## Table of Contents

## Introduction

- [Overview](#overview)

## Usage

- [Getting Started](#getting-started)
- [Examples](#examples)

---

## Introduction

### Overview

### Model

> Model : `Book`

#### Attributes

- `id : int`
- `title : str`
- `author: str`
- `year : int`
- `isbn : str`

### Endpoints

- `GET /books/`
- `GET /books/{book_id}`
- `POST /books/`
- `PUT /books/{book_id}`
- `DELETE /books/{book_id}`

---

## Installation

### Requirements
>
> Complete API requirements can be found in [requirements.txt](https://github.com/carnage999-max/book_api/blob/main/requirements.txt)

---

### Getting Started
>
> Clone project from git repo

`git clone https://github.com/carnage999-max/book_api.git`

> Install dependencies

`pip install -r requirements.txt`

> Start `uvicorn` server

`uvicorn api:app --reload`

### Examples

#### Example GET request

`GET /books/`

#### Response (HTTP 200)

`[
    {
    "id":1,
    "title": "Book 1",
    "author": "First Author",
    "year": 1999,
    "isbn": "1234-5678-900"
    },
    {
    "id":1,
    "title": "Book 2",
    "author": "Second Author",
    "year": 1998,
    "isbn": "1044-5678-900"
    }
]`

#### Example GET request

`GET /books/{book_id}`

#### Response (HTTP 200)

`{
    "id":1,
    "title": "Book 1",
    "author": "First Author",
    "year": 1999,
    "isbn": "1234-5678-900"
    },`

#### Example POST request

`POST /books/`

#### Response (HTTP 200)

`{
    "id":1,
    "title": "Book 1",
    "author": "First Author",
    "year": 1999,
    "isbn": "1234-5678-900"
}`

#### Response (HTTP 400)
`
    {
        "detail": "Book already exists"
    }
`
