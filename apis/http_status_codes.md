# HTTP Status Codes Explained

**Date:** 2026-06-17

## What are Status Codes?

Every API response includes a 3-digit status code that tells you **what happened** with your request.

```
Request → Server processes → Response with status code
```

---

## The 5 Categories

| Range | Category | Meaning |
|-------|----------|---------|
| 1xx | Informational | Request received, processing |
| 2xx | Success | Request worked ✅ |
| 3xx | Redirection | Resource moved |
| 4xx | Client Error | You made a mistake ❌ |
| 5xx | Server Error | Server made a mistake 💥 |

---

## Most Important Codes

### ✅ 2xx — Success

| Code | Name | When |
|------|------|------|
| 200 | OK | GET/PUT succeeded |
| 201 | Created | POST succeeded, resource created |
| 204 | No Content | DELETE succeeded, nothing to return |

### ❌ 4xx — Client Errors (your fault)

| Code | Name | When |
|------|------|------|
| 400 | Bad Request | Invalid data sent |
| 401 | Unauthorized | Missing or invalid API key |
| 403 | Forbidden | Authenticated but no permission |
| 404 | Not Found | Resource doesn't exist |
| 422 | Unprocessable Entity | Validation failed |
| 429 | Too Many Requests | Rate limit exceeded |

### 💥 5xx — Server Errors (their fault)

| Code | Name | When |
|------|------|------|
| 500 | Internal Server Error | Server crashed |
| 502 | Bad Gateway | Upstream server failed |
| 503 | Service Unavailable | Server overloaded/down |

---

## 401 vs 403

```
401 Unauthorized → "Who are you? Show me your API key."
403 Forbidden    → "I know who you are, but you can't do this."
```

---

## Python Example

```python
import requests

response = requests.get("https://api.example.com/users/1")

if response.status_code == 200:
    print("Success!", response.json())
elif response.status_code == 404:
    print("User not found!")
elif response.status_code == 401:
    print("Check your API key!")
elif response.status_code == 500:
    print("Server error — try again later")
```

---

## Key Takeaway

> 2xx = success, 4xx = your mistake, 5xx = their mistake. 401 means unauthenticated, 403 means unauthorized. Always check status codes before using API response data.
