# REST API Basics

**Date:** 2026-06-16

## What is REST?

**REST = Representational State Transfer**

REST is an architectural style for building APIs. A REST API uses HTTP to communicate and follows a set of principles that make it simple, scalable, and stateless.

---

## Core REST Principles

| Principle | Meaning |
|-----------|---------|
| Stateless | Each request is independent — server stores no session |
| Client-Server | Frontend and backend are separate |
| Uniform Interface | Consistent URL structure and methods |
| Resource-Based | Everything is a resource with its own URL |

---

## Resources and URLs

In REST, everything is a **resource** — and each resource has a unique URL.

```
https://api.example.com/users          → all users
https://api.example.com/users/1        → user with ID 1
https://api.example.com/users/1/posts  → posts by user 1
```

**URL naming rules:**
```
✅ /users          (plural nouns)
✅ /users/1        (resource ID)
✅ /users/1/posts  (nested resource)

❌ /getUsers       (no verbs)
❌ /user           (not plural)
❌ /Users          (not uppercase)
```

---

## REST vs Non-REST

```
❌ Non-REST (old style):
/getUser?id=1
/createUser
/deleteUser?id=1

✅ REST:
GET    /users/1    → get user
POST   /users      → create user
DELETE /users/1    → delete user
```

---

## Request Structure

```
Method  URL                Headers          Body
GET     /api/users/1       Authorization:   (none)
                           Bearer token123
```

## Response Structure

```json
{
  "status": 200,
  "data": {
    "id": 1,
    "name": "Adheethi",
    "email": "adheethii@gmail.com"
  }
}
```

---

## Key Takeaway

> REST APIs are resource-based — URLs represent things (nouns), HTTP methods represent actions (verbs). Keep URLs clean, plural, and lowercase. Each request is stateless and self-contained.
