# FastAPI Response Models and Status Codes

**Date:** 2026-06-23

## What are Response Models?

Response models define the **shape of data your API returns**. They filter out unwanted fields and document the output automatically.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: str
    password: str          # received from client

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    # password NOT here — never sent back ✅

@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):
    return {"id": 1, "name": user.name, "email": user.email}
```

Even if your function returns extra fields, FastAPI filters them using `response_model`.

---

## Custom Status Codes

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.post("/users", status_code=201)        # 201 Created
def create_user():
    return {"message": "User created"}

@app.delete("/users/{id}", status_code=204) # 204 No Content
def delete_user(id: int):
    return None
```

---

## Returning Different Status Codes Dynamically

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = find_user(user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail=f"User {user_id} not found"
        )

    return user
```

---

## JSONResponse for Custom Responses

```python
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/predict")
def predict():
    return JSONResponse(
        status_code=200,
        content={
            "prediction": "Yes",
            "probability": 0.823,
            "model_version": "v1.0"
        }
    )
```

---

## List Response Models

```python
from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: int
    name: str

@app.get("/users", response_model=List[User])
def get_all_users():
    return [
        {"id": 1, "name": "Adheethi"},
        {"id": 2, "name": "John"}
    ]
```

---

## Common Response Patterns

```python
# Success with data
return {"status": "success", "data": result}

# Created
return JSONResponse(status_code=201, content={"id": new_id})

# Not found
raise HTTPException(status_code=404, detail="Not found")

# Bad request
raise HTTPException(status_code=400, detail="Invalid input")

# Server error
raise HTTPException(status_code=500, detail="Internal error")
```

---

## What I Apply

In my Telecom Churn API — the response model returns only `churn_prediction` and `probability`, never the raw input features or internal model details.

---

## Key Takeaway

> `response_model` filters your output and documents it automatically. Use `status_code` in the decorator for fixed codes and `HTTPException` for dynamic errors. Always separate input and output models — never expose sensitive fields in responses.
