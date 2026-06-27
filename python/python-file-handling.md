# Python File Handling

**Date:** 2026-06-27

## Reading and Writing Files

```python
# Write to file
with open("output.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("Second line\n")

# Read entire file
with open("output.txt", "r") as f:
    content = f.read()
    print(content)

# Read line by line
with open("output.txt", "r") as f:
    for line in f:
        print(line.strip())

# Append to file
with open("output.txt", "a") as f:
    f.write("Appended line\n")
```

---

## File Modes

| Mode | Meaning |
|------|---------|
| `r` | Read (default) |
| `w` | Write (overwrites) |
| `a` | Append |
| `rb` | Read binary |
| `wb` | Write binary |

---

## Working with CSV

```python
import csv

# Write CSV
with open("data.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "score"])
    writer.writeheader()
    writer.writerow({"name": "Adheethi", "age": 22, "score": 95})

# Read CSV
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["score"])
```

---

## Working with JSON

```python
import json

data = {"name": "Adheethi", "skills": ["Python", "ML"]}

# Write JSON
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Read JSON
with open("data.json", "r") as f:
    loaded = json.load(f)
    print(loaded["name"])
```

---

## Working with Paths (pathlib)

```python
from pathlib import Path

# Create path
path = Path("data/models/model.pkl")

# Check if exists
if path.exists():
    print("File found")

# Create directory
path.parent.mkdir(parents=True, exist_ok=True)

# List files
for file in Path("data/").glob("*.csv"):
    print(file.name)
```

---

## Saving ML Models

```python
import pickle

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

# Load model
with open("model.pkl", "rb") as f:
    loaded_model = pickle.load(f)
```

---

## Key Takeaway

> Always use `with open()` — it automatically closes the file even if an error occurs. Use `pathlib.Path` for cross-platform file paths. For ML projects: save models with pickle, data with CSV/JSON, and always check if paths exist before reading.
