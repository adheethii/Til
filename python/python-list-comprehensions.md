# Python List Comprehensions and Generator Expressions

**Date:** 2026-06-25

## What are List Comprehensions?

List comprehensions are a concise, readable way to create lists in Python — replacing multi-line for loops with a single line.

```python
# Traditional for loop
squares = []
for x in range(10):
    squares.append(x ** 2)

# List comprehension — same result, one line
squares = [x ** 2 for x in range(10)]
```

---

## Syntax

```python
[expression for item in iterable if condition]
```

---

## Examples

```python
# Basic
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]
# → [2, 4, 6, 8, 10]

# With condition
evens = [x for x in range(20) if x % 2 == 0]
# → [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# String manipulation
names = ["adheethi", "john", "alice"]
upper = [name.upper() for name in names]
# → ["ADHEETHI", "JOHN", "ALICE"]

# From a DataFrame column
import pandas as pd
df = pd.DataFrame({"score": [45, 72, 88, 91, 55]})
passed = [s for s in df["score"] if s >= 60]
# → [72, 88, 91]
```

---

## Dictionary Comprehensions

```python
# Square of numbers as dict
squares = {x: x**2 for x in range(5)}
# → {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Flip a dictionary
original = {"a": 1, "b": 2, "c": 3}
flipped = {v: k for k, v in original.items()}
# → {1: "a", 2: "b", 3: "c"}
```

---

## Generator Expressions

Like list comprehensions but **lazy** — generates values one at a time, uses less memory:

```python
# List comprehension — creates full list in memory
squares_list = [x**2 for x in range(1000000)]

# Generator — generates one at a time
squares_gen = (x**2 for x in range(1000000))

# Use with sum, max, min — no full list needed
total = sum(x**2 for x in range(1000000))
```

---

## When to Use Each

| | List Comprehension | Generator |
|--|-------------------|-----------|
| Memory | Stores all items | One at a time |
| Speed | Fast for small data | Better for large data |
| Reusable | ✅ Yes | ❌ Once only |
| Use when | Need the full list | Just iterating once |

---

## Key Takeaway

> List comprehensions make Python code cleaner and more Pythonic. Use them instead of for loops when building lists. Use generator expressions when you only need to iterate once or are working with large data — they save memory significantly.
