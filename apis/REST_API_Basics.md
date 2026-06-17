# 🌐 REST API Basics

## What is a REST API?

REST stands for **Representational State Transfer**.

A REST API is a type of API that follows a set of rules for communication between clients and servers using HTTP.

REST APIs are the most commonly used APIs on the web.

---

## How REST Works

A client sends an HTTP request to a server.

The server processes the request and returns an HTTP response.

### Example

Request:

```http
GET https://api.example.com/users/1
```

Response:

```json
{
  "id": 1,
  "name": "John",
  "email": "john@example.com"
}
```

---

## Key Principles of REST

### 1. Client-Server Architecture

The client and server are separate.

- Client → Requests data
- Server → Provides data

---

### 2. Stateless Communication

Each request contains all information needed.

The server does not remember previous requests.

---

### 3. Resource-Based URLs

Everything is treated as a resource.

Examples:

```text
/users
/products
/orders
```

---

### 4. Uses HTTP Methods

REST APIs use:

- GET
- POST
- PUT
- DELETE

to perform operations on resources.

---

## REST API Example

### Get all users

```http
GET /users
```

### Get one user

```http
GET /users/1
```

### Create a user

```http
POST /users
```

### Update a user

```http
PUT /users/1
```

### Delete a user

```http
DELETE /users/1
```

---

## Advantages of REST APIs

- Easy to understand
- Scalable
- Lightweight
- Platform independent
- Widely supported

---

## Summary

> REST API is a web API architecture that uses HTTP methods to perform operations on resources.
