# Python Error Handling (try/except)

**Date:** 2026-06-26

## What is Error Handling?

Error handling prevents your program from crashing when something goes wrong — instead you catch the error and respond gracefully.

```python
# Without error handling → crashes
result = 10 / 0    # ZeroDivisionError: division by zero 💥

# With error handling → controlled response
try:
    result = 10 / 0
except ZeroDivisionError:
    result = 0
    print("Cannot divide by zero")
```

---

## Basic try/except

```python
try:
    # Code that might fail
    number = int(input("Enter a number: "))
    result = 100 / number
    print(f"Result: {result}")

except ValueError:
    print("Please enter a valid number")

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

## else and finally

```python
try:
    file = open("data.csv")
    data = file.read()

except FileNotFoundError:
    print("File not found!")

else:
    # Runs only if no exception occurred
    print(f"File loaded: {len(data)} characters")

finally:
    # Always runs — good for cleanup
    file.close()
    print("File closed")
```

---

## Common Python Exceptions

| Exception | When |
|-----------|------|
| `ValueError` | Wrong value type |
| `TypeError` | Wrong data type |
| `KeyError` | Dict key doesn't exist |
| `IndexError` | List index out of range |
| `FileNotFoundError` | File doesn't exist |
| `ZeroDivisionError` | Division by zero |
| `AttributeError` | Object has no attribute |

---

## Custom Exceptions

```python
class InvalidAgeError(Exception):
    pass

def set_age(age):
    if age < 0 or age > 150:
        raise InvalidAgeError(f"Invalid age: {age}")
    return age

try:
    set_age(-5)
except InvalidAgeError as e:
    print(f"Error: {e}")
```

---

## Error Handling in ML Code

```python
import pickle
import numpy as np

def load_model(path):
    try:
        with open(path, "rb") as f:
            model = pickle.load(f)
        return model
    except FileNotFoundError:
        print(f"Model file not found: {path}")
        return None
    except Exception as e:
        print(f"Failed to load model: {e}")
        return None

def predict(model, features):
    if model is None:
        return {"error": "Model not loaded"}
    try:
        prediction = model.predict([features])
        return {"prediction": int(prediction[0])}
    except Exception as e:
        return {"error": str(e)}
```

---

## Key Takeaway

> Always handle errors in production code — especially file operations, API calls, and model predictions. Use specific exceptions (FileNotFoundError) rather than bare except. Use finally for cleanup. Custom exceptions make your code more readable and debuggable.
