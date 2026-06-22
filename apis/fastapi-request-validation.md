# FastAPI Request Validation

**Date:** 2026-06-22

## What is Request Validation?

Request validation ensures that incoming data is correct **before** your code processes it. FastAPI + Pydantic handle this automatically.

```
Client sends request → FastAPI validates → ✅ Process OR ❌ Return 422
```

---

## Automatic Validation

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float
    quantity: int

@app.post("/products")
def create_product(product: Product):
    return product

# ✅ Valid request:
# {"name": "Laptop", "price": 999.99, "quantity": 5}

# ❌ Invalid — price is a string:
# {"name": "Laptop", "price": "expensive", "quantity": 5}
# → 422 Unprocessable Entity (automatic, no extra code!)
```

---

## Field Validation with Pydantic

```python
from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(ge=0, le=120)          # ge=greater than or equal, le=less than or equal
    price: float = Field(gt=0)              # gt=greater than
    email: EmailStr                         # validates email format
    username: str = Field(pattern=r"^\w+$") # regex pattern
```

---

## Field Constraints Reference

| Constraint | Meaning | Example |
|------------|---------|---------|
| `min_length` | Minimum string length | `Field(min_length=2)` |
| `max_length` | Maximum string length | `Field(max_length=100)` |
| `ge` | Greater than or equal | `Field(ge=0)` |
| `le` | Less than or equal | `Field(le=100)` |
| `gt` | Greater than | `Field(gt=0)` |
| `lt` | Less than | `Field(lt=1000)` |
| `pattern` | Regex pattern | `Field(pattern=r"^\w+$")` |

---

## Query Parameter Validation

```python
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/users")
def get_users(
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=10, ge=1, le=100),
    search: str = Query(default=None, min_length=3)
):
    return {"page": page, "limit": limit, "search": search}
```

---

## Path Parameter Validation

```python
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int = Path(ge=1)):    # ID must be positive
    return {"user_id": user_id}
```

---

## Custom Validators

```python
from pydantic import BaseModel, validator

class ChurnPrediction(BaseModel):
    tenure: int
    monthly_charges: float
    contract_type: str

    @validator("contract_type")
    def validate_contract(cls, v):
        allowed = ["Month-to-month", "One year", "Two year"]
        if v not in allowed:
            raise ValueError(f"contract_type must be one of {allowed}")
        return v

    @validator("tenure")
    def validate_tenure(cls, v):
        if v < 0:
            raise ValueError("tenure cannot be negative")
        return v
```

---

## Validation Error Response

When validation fails, FastAPI returns a clear error:

```json
{
  "detail": [
    {
      "loc": ["body", "age"],
      "msg": "ensure this value is greater than or equal to 0",
      "type": "value_error.number.not_ge"
    }
  ]
}
```

---

## What I Apply

This pattern is exactly how I'll deploy my [Telecom Customer Churn](https://github.com/adheethii/Telecom-customer-churn) model — strict input validation ensures only valid customer data reaches the ML model.

---

## Key Takeaway

> FastAPI validation is free — just define your Pydantic model with `Field` constraints and FastAPI handles the rest. Use `Query()` for query params, `Path()` for path params, and `@validator` for custom business logic validation.
