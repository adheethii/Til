# JSON Request and Response Format

**Date:** 2026-06-19

## What is JSON?

**JSON = JavaScript Object Notation**

JSON is the standard format for sending and receiving data in APIs. It's lightweight, human-readable, and works with every programming language.

```json
{
  "name": "Adheethi",
  "age": 22,
  "skills": ["Python", "ML", "LangChain"],
  "active": true
}
```

---

## JSON Data Types

| Type | Example |
|------|---------|
| String | `"Adheethi"` |
| Number | `22` or `3.14` |
| Boolean | `true` or `false` |
| Array | `["Python", "ML"]` |
| Object | `{"city": "Kochi"}` |
| Null | `null` |

---

## JSON in API Requests

When sending data to an API (POST/PUT), you send JSON in the request body:

```python
import requests

# Sending JSON in request body
response = requests.post(
    "https://api.example.com/users",
    json={                          # ← Python dict, auto-converted to JSON
        "name": "Adheethi",
        "email": "adheethii@gmail.com",
        "role": "ML Engineer"
    },
    headers={"Authorization": "Bearer your_api_key"}
)
```

---

## JSON in API Responses

When the API responds, it sends JSON back:

```python
response = requests.get("https://api.example.com/users/1")

# Parse JSON response
data = response.json()             # ← converts JSON to Python dict

print(data["name"])                # → "Adheethi"
print(data["skills"][0])           # → "Python"
```

---

## Nested JSON

APIs often return complex nested structures:

```json
{
  "user": {
    "id": 1,
    "name": "Adheethi",
    "address": {
      "city": "Kochi",
      "state": "Kerala"
    },
    "projects": [
      {"name": "Agentic RAG", "status": "completed"},
      {"name": "MediCore", "status": "completed"}
    ]
  }
}
```

```python
data = response.json()
city = data["user"]["address"]["city"]          # → "Kochi"
first_project = data["user"]["projects"][0]["name"]  # → "Agentic RAG"
```

---

## JSON vs Python Dict

| | Python Dict | JSON |
|--|-------------|------|
| Keys | Any type | Strings only |
| True/False | `True`, `False` | `true`, `false` |
| None | `None` | `null` |
| Format | Python syntax | Text string |

```python
import json

# Python dict → JSON string
json_string = json.dumps({"name": "Adheethi", "active": True})
# → '{"name": "Adheethi", "active": true}'

# JSON string → Python dict
python_dict = json.loads('{"name": "Adheethi", "active": true}')
# → {"name": "Adheethi", "active": True}
```

---

## Key Takeaway

> JSON is the universal language of APIs. It's just a text format that represents structured data. In Python, `requests` handles JSON automatically — use `json=` for sending and `.json()` for receiving.
