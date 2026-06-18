# HTTP Methods Explained (GET, POST, PUT, DELETE)

**Date:** 2026-06-17

## What are HTTP Methods?

HTTP methods (also called verbs) tell the server **what action to perform** on a resource.

```
Method + URL = Complete instruction
GET /users/1  → "Give me user 1"
DELETE /users/1 → "Delete user 1"
```

---

## The 4 Main Methods

### GET — Read
Retrieve data. Never modifies anything.
```
GET /users          → get all users
GET /users/1        → get user with ID 1

Response: 200 OK + data
```

### POST — Create
Send data to create a new resource.
```
POST /users
Body: { "name": "Adheethi", "email": "adheethii@gmail.com" }

Response: 201 Created + new resource
```

### PUT — Update (Full)
Replace an entire resource with new data.
```
PUT /users/1
Body: { "name": "Adheethi K", "email": "adheethii@gmail.com" }

Response: 200 OK + updated resource
```

### DELETE — Delete
Remove a resource.
```
DELETE /users/1

Response: 204 No Content
```

---

## PATCH vs PUT

| | PUT | PATCH |
|--|-----|-------|
| Updates | Entire resource | Only specified fields |
| Body | All fields required | Only changed fields |

```
PATCH /users/1
Body: { "name": "Adheethi K" }  ← only update name
```

---

## Quick Reference

| Method | Action | Request Body | Success Code |
|--------|--------|--------------|--------------|
| GET | Read | None | 200 OK |
| POST | Create | Yes | 201 Created |
| PUT | Full Update | Yes | 200 OK |
| PATCH | Partial Update | Yes | 200 OK |
| DELETE | Delete | None | 204 No Content |

---

## Python Example

```python
import requests

# GET
response = requests.get("https://api.example.com/users/1")

# POST
response = requests.post("https://api.example.com/users",
    json={"name": "Adheethi", "email": "adheethii@gmail.com"})

# PUT
response = requests.put("https://api.example.com/users/1",
    json={"name": "Adheethi K", "email": "adheethii@gmail.com"})

# DELETE
response = requests.delete("https://api.example.com/users/1")
```

---

## Key Takeaway

> GET reads, POST creates, PUT replaces, DELETE removes. PATCH is like PUT but only updates what you specify. Methods + URLs together form the complete language of REST APIs.
