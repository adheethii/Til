# Python Decorators

**Date:** 2026-06-26

## What is a Decorator?

A decorator wraps another function to add extra behavior — without modifying the original code.

```python
@decorator
def my_function():
    pass

# Same as:
my_function = decorator(my_function)
```

---

## Simple Decorator

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Before
# Hello!
# After
```

---

## Practical Examples

```python
import time

# Timer decorator
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time()-start:.2f}s")
        return result
    return wrapper

@timer
def train_model():
    time.sleep(2)
    return "done"

train_model()  # → train_model took 2.00s
```

---

## FastAPI Uses Decorators

```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/users")      # ← decorator that registers route
def get_users():
    return {"users": []}
```

---

## Built-in Decorators

```python
class MyClass:
    @staticmethod    # no self needed
    def helper(): return "help"

    @classmethod     # receives class
    def create(cls): return cls()

    @property        # access like attribute
    def name(self): return self._name
```

---

## Key Takeaway

> Decorators wrap functions to add behavior without changing their code. Pattern: outer function receives func → inner wrapper adds behavior → returns wrapper. FastAPI routes, timing, logging, caching — all use decorators.
