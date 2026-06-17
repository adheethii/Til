# 🔧 HTTP Methods Explained

HTTP methods define the action a client wants to perform on a resource.

---

## 1. GET

Used to retrieve data from the server.

### Example

```http
GET /users
```

### Response

```json
[
  {
    "id": 1,
    "name": "John"
  }
]
```

### Characteristics

- Read-only
- Does not modify data

---

## 2. POST

Used to create new data.

### Example

```http
POST /users
```

Request Body:

```json
{
  "name": "John",
  "email": "john@example.com"
}
```

### Result

A new user is created.

---

## 3. PUT

Used to update existing data.

### Example

```http
PUT /users/1
```

Request Body:

```json
{
  "name": "John Smith",
  "email": "johnsmith@example.com"
}
```

### Result

User information is updated.

---

## 4. DELETE

Used to remove data.

### Example

```http
DELETE /users/1
```

### Result

User is deleted from the database.

---

## CRUD Operations Mapping

| Operation | HTTP Method |
|------------|------------|
| Create | POST |
| Read | GET |
| Update | PUT |
| Delete | DELETE |

CRUD = Create, Read, Update, Delete

---

## Quick Comparison

| Method | Purpose |
|----------|----------|
| GET | Retrieve data |
| POST | Create data |
| PUT | Update data |
| DELETE | Remove data |

---

## Summary

> HTTP methods define what action should be performed on a resource in a REST API.
