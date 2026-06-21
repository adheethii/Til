# FastAPI Basics

**Date:** 2026-06-21

## What is FastAPI?

FastAPI is a modern Python framework for building APIs — fast to code, fast to run, and automatically generates documentation.

```
Flask/Django → older, slower, manual docs
FastAPI      → modern, async, auto docs ✅
```

---

## Why FastAPI?

| Feature | FastAPI |
|---------|---------|
| Speed | One of the fastest Python frameworks |
| Auto docs | Swagger UI generated automatically |
| Type hints | Uses Python type hints for validation |
| Async | Built-in async/await support |
| Easy | Less code than Flask for same result |

---

## Installation

```bash
pip install fastapi uvicorn
```

`uvicorn` is the server that runs your FastAPI app.

---

## Your First API

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from FastAPI!"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": "Adheethi"}
```

Run it:
```bash
uvicorn main:app --reload
```

Visit: `http://localhost:8000`
Auto docs: `http://localhost:8000/docs`

---

## Path Parameters vs Query Parameters

```python
# Path parameter — part of the URL
@app.get("/users/{user_id}")
def get_user(user_id: int):       # /users/1
    return {"id": user_id}

# Query parameter — after ?
@app.get("/users")
def get_users(page: int = 1, limit: int = 10):   # /users?page=2&limit=5
    return {"page": page, "limit": limit}
```

---

## POST Request with Body

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str
    age: int

@app.post("/users")
def create_user(user: User):
    return {"message": "User created", "user": user}
```

FastAPI automatically validates the request body using the Pydantic model.

---

## All HTTP Methods

```python
@app.get("/users/{id}")      # Read
@app.post("/users")          # Create
@app.put("/users/{id}")      # Full update
@app.patch("/users/{id}")    # Partial update
@app.delete("/users/{id}")   # Delete
```

---

## Auto Documentation

FastAPI generates two docs automatically:
- `http://localhost:8000/docs` → Swagger UI (interactive)
- `http://localhost:8000/redoc` → ReDoc (clean)

No extra code needed — it reads your type hints and generates everything.

---

## Key Takeaway

> FastAPI is the go-to framework for building ML model APIs in Python. Type hints do double duty — they validate inputs AND generate documentation automatically. `uvicorn main:app --reload` is your development command.
