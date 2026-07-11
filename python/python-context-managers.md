# Python Context Managers

**Date:** 2026-07-11

## What is a Context Manager?

A context manager handles **setup and cleanup** automatically using the `with` statement — most commonly seen with file handling.

```python
# You've been using this all along!
with open("file.txt") as f:
    data = f.read()
# file automatically closed here, even if an error occurs
```

---

## Why Context Managers Matter

```
❌ Without context manager:
f = open("file.txt")
data = f.read()
f.close()   # forgotten if error occurs above! 💥

✅ With context manager:
with open("file.txt") as f:
    data = f.read()
# always closed, even on exception ✅
```

---

## Creating a Class-based Context Manager

```python
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        print(f"Connecting to {self.db_name}...")
        self.connection = f"Connection to {self.db_name}"
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Closing connection to {self.db_name}")
        # cleanup code here
        return False   # False = don't suppress exceptions

with DatabaseConnection("mydb") as conn:
    print(f"Using: {conn}")
# Connecting to mydb...
# Using: Connection to mydb
# Closing connection to mydb
```

---

## Function-based Context Manager (Cleaner)

```python
from contextlib import contextmanager

@contextmanager
def timer(name):
    import time
    start = time.time()
    print(f"Starting {name}...")
    yield                          # code inside 'with' runs here
    elapsed = time.time() - start
    print(f"{name} took {elapsed:.2f}s")

with timer("Model Training"):
    train_model()   # your code here
# Starting Model Training...
# (training happens)
# Model Training took 45.32s
```

---

## Practical ML Examples

```python
from contextlib import contextmanager

@contextmanager
def suppress_warnings():
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        yield

@contextmanager
def model_evaluation_mode(model):
    """Switch model to eval mode, then back to train mode"""
    model.eval()
    yield
    model.train()

with model_evaluation_mode(model):
    predictions = model(X_test)   # model in eval mode here
# model automatically back in train mode after
```

---

## Multiple Context Managers

```python
with open("input.csv") as infile, open("output.csv", "w") as outfile:
    data = infile.read()
    outfile.write(process(data))
```

---

## Key Takeaway

> Context managers guarantee cleanup happens — even if an error occurs. Use `with open()` for files always. The `@contextmanager` decorator is the cleanest way to create custom ones — just `yield` where the "with" block code should execute. Essential for resources like files, connections, and locks.
