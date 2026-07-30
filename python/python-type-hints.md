# Python Type Hints Properly

**Date:** 2026-07-30

## Why This Gap Existed

Type hints have appeared incidentally in earlier notes — Pydantic
models rely on them, the `TypedDict` used in every LangGraph example
this month is a form of them — but never actually explained on
their own terms. Worth closing that gap directly rather than
continuing to use them without ever having written down what
they actually do.

---

## What Type Hints Actually Are

```python
def add(a: int, b: int) -> int:
    return a + b
```

Type hints are annotations, NOT enforcement. Python does not check
these at runtime by default — calling `add("hello", "world")` runs
fine and returns `"helloworld"`, no error. Hints exist for:

- Editor autocomplete and inline error highlighting
- Static type checkers (mypy, pyright) catching bugs BEFORE running
- Documentation that stays in sync with the actual signature
- Libraries like Pydantic and FastAPI that DO read and enforce
  them at runtime (this is the exception, not the rule)

---

## Basic Syntax

```python
name: str = "Adheethi"
age: int = 22
is_active: bool = True
score: float = 9.5

def greet(name: str) -> str:
    return f"Hello, {name}"

def process(data: list) -> None:  # -> None means no meaningful return value
    print(data)
```

---

## Collection Types

```python
from typing import List, Dict, Tuple, Set, Optional

names: List[str] = ["Adheethi", "John"]
scores: Dict[str, int] = {"Adheethi": 95, "John": 87}
coordinates: Tuple[float, float] = (12.9, 77.6)
unique_ids: Set[int] = {1, 2, 3}

# Python 3.9+ can use built-in types directly (no import needed)
names: list[str] = ["Adheethi", "John"]
scores: dict[str, int] = {"Adheethi": 95}
```

---

## Optional and Union — Values That Might Not Be There

```python
from typing import Optional, Union

def find_user(user_id: int) -> Optional[str]:
    """Optional[str] means: returns a str, OR returns None."""
    if user_id == 1:
        return "Adheethi"
    return None

def parse_value(x: Union[int, str]) -> str:
    """Accepts EITHER an int or a str."""
    return str(x)

# Python 3.10+ shorthand — the | operator instead of Union
def parse_value(x: int | str) -> str:
    return str(x)
```

---

## Where This Has Already Been Used This Month (Without Being Named)

```python
# TypedDict — used in every LangGraph state definition so far
from typing import TypedDict

class AgentState(TypedDict):
    messages: list[str]
    current_agent: str

# Pydantic BaseModel — the entire foundation of FastAPI validation
from pydantic import BaseModel

class CustomerData(BaseModel):
    tenure: int
    monthly_charges: float
```

Both of these rely entirely on type hints to know what shape of
data to expect — Pydantic actually enforces them at runtime
(raising a validation error on mismatch), which is why FastAPI
endpoints reject malformed requests automatically without any
manual `if` checks being written.

---

## Callable and Function Type Hints

```python
from typing import Callable

def apply_twice(func: Callable[[int], int], value: int) -> int:
    return func(func(value))

def double(x: int) -> int:
    return x * 2

apply_twice(double, 5)   # → 20
```

---

## Static Checking — Where Hints Actually Get Enforced

```bash
pip install mypy

# mypy checks a file WITHOUT running it, purely from the hints
mypy my_script.py
```

```python
def add(a: int, b: int) -> int:
    return a + b

add("hello", "world")   # mypy flags this as an error BEFORE runtime,
                          # even though plain Python would happily run it
```

This is the actual practical value for larger codebases — catching
a class of bugs (wrong type passed somewhere) during development,
not after deployment.

---

## Key Takeaway

> Type hints are optional documentation by default — Python itself doesn't enforce them, which is genuinely surprising the first time it's confirmed directly (as above with `add("hello", "world")` running without error). The two places they DO get enforced are static checkers like mypy (catching bugs before runtime) and libraries like Pydantic that read the hints and validate against them at runtime — which is the exact mechanism behind every FastAPI request-validation error seen throughout the Churn API and Interview Simulator work this month.
