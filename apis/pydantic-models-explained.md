# Pydantic Models Explained

**Date:** 2026-06-22

## What is Pydantic?

Pydantic is a Python library for **data validation using type hints**. FastAPI uses it automatically to validate all request and response data.

```
You define the shape of data → Pydantic validates it → FastAPI enforces it
```

---

## Basic Model

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str
    is_active: bool = True    # default value
```

---

## How FastAPI Uses It

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: str

@app.post("/users")
def create_user(user: User):
    return {"message": f"Created user {user.name}", "data": user}
```

FastAPI automatically:
- Reads the request body as JSON
- Validates each field against the model
- Returns `422 Unprocessable Entity` if validation fails
- Generates docs from the model

---

## Optional Fields

```python
from pydantic import BaseModel
from typing import Optional

class UserUpdate(BaseModel):
    name: Optional[str] = None      # not required
    age: Optional[int] = None       # not required
    email: Optional[str] = None     # not required
```

Useful for PATCH endpoints where only some fields are updated.

---

## Nested Models

```python
from pydantic import BaseModel
from typing import List

class Address(BaseModel):
    city: str
    state: str

class User(BaseModel):
    name: str
    age: int
    address: Address              # nested model
    skills: List[str] = []        # list of strings
```

```json
{
  "name": "Adheethi",
  "age": 22,
  "address": {"city": "Kochi", "state": "Kerala"},
  "skills": ["Python", "ML", "LangChain"]
}
```

---

## Input vs Output Models

Best practice — separate models for input and output:

```python
class UserCreate(BaseModel):      # input — what client sends
    name: str
    email: str
    password: str                 # received but never sent back

class UserResponse(BaseModel):    # output — what API returns
    id: int
    name: str
    email: str
    # password NOT included ✅

@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):
    # save to DB, return without password
    return {"id": 1, "name": user.name, "email": user.email}
```

---

## Accessing Model Data

```python
user = User(name="Adheethi", age=22, email="adheethii@gmail.com")

user.name          # "Adheethi"
user.age           # 22
user.dict()        # {"name": "Adheethi", "age": 22, "email": "..."}
user.json()        # '{"name": "Adheethi", "age": 22, "email": "..."}'
```

---

## Key Takeaway

> Pydantic models are the backbone of FastAPI. They define the shape of your data, validate it automatically, and generate API documentation. Always use separate input/output models to avoid accidentally exposing sensitive fields like passwords.
