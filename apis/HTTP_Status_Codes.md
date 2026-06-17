# 🚦 HTTP Status Codes

HTTP status codes tell us whether a request was successful or failed.

They are returned by the server along with every response.

---

## Status Code Categories

| Range | Meaning |
|---------|---------|
| 1xx | Informational |
| 2xx | Success |
| 3xx | Redirection |
| 4xx | Client Error |
| 5xx | Server Error |

---

## Common Success Codes

### 200 OK

Request completed successfully.

```http
GET /users
```

Response:

```text
200 OK
```

---

### 201 Created

Resource created successfully.

```http
POST /users
```

Response:

```text
201 Created
```

---

## Common Client Error Codes

### 400 Bad Request

The request is invalid.

```text
400 Bad Request
```

---

### 401 Unauthorized

Authentication required.

```text
401 Unauthorized
```

---

### 403 Forbidden

Access denied.

```text
403 Forbidden
```

---

### 404 Not Found

Resource does not exist.

```text
404 Not Found
```

Example:

```http
GET /users/999
```

If user 999 doesn't exist, the server returns:

```text
404 Not Found
```

---

## Common Server Error Codes

### 500 Internal Server Error

Something went wrong on the server.

```text
500 Internal Server Error
```

---

### 503 Service Unavailable

Server is temporarily unavailable.

```text
503 Service Unavailable
```

---

## Quick Reference Table

| Code | Meaning |
|--------|---------|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |
| 503 | Service Unavailable |

---

## Why Status Codes Matter

Status codes help developers:

- Understand API responses
- Debug issues
- Handle errors properly
- Improve application reliability

---

## Summary

> HTTP status codes indicate whether an API request was successful, failed because of the client, or failed because of the server.
