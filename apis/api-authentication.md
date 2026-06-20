# API Authentication (API Keys, Bearer Tokens)

**Date:** 2026-06-18

## What is API Authentication?

Authentication proves **who you are** to an API. Without it, anyone could call your API and abuse it.

```
Without auth → API rejects request (401 Unauthorized)
With auth    → API processes request ✅
```

---

## Types of Authentication

| Type | How | Common Use |
|------|-----|------------|
| API Key | Pass a key in header or URL | Simple public APIs |
| Bearer Token | Pass a token in Authorization header | Most modern APIs |
| Basic Auth | Username + password (base64 encoded) | Legacy systems |
| OAuth 2.0 | Token-based with login flow | Google, GitHub login |

---

## 1. API Key Authentication

The simplest method — just pass your key:

```python
import requests

# Option 1 — In query parameters (less secure)
response = requests.get(
    "https://api.openweathermap.org/data/2.5/weather",
    params={"q": "Kochi", "appid": "your_api_key"}
)

# Option 2 — In headers (more secure ✅)
response = requests.get(
    "https://api.example.com/data",
    headers={"X-API-Key": "your_api_key"}
)
```

---

## 2. Bearer Token Authentication

Most common in modern APIs:

```python
import requests

token = "your_bearer_token"

response = requests.get(
    "https://api.example.com/users",
    headers={"Authorization": f"Bearer {token}"}
)
```

The word `Bearer` is required — it tells the API what type of token you're sending.

---

## 3. Basic Authentication

```python
import requests

response = requests.get(
    "https://api.example.com/data",
    auth=("username", "password")   # requests handles encoding
)
```

---

## Storing API Keys Safely

**Never hardcode keys in your code!**

```python
# ❌ Bad — exposed in code
API_KEY = "sk-abc123secretkey"

# ✅ Good — stored in .env file
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

response = requests.get(
    "https://api.example.com/data",
    headers={"Authorization": f"Bearer {API_KEY}"}
)
```

---

## 401 vs 403

```
401 Unauthorized → No token / invalid token
403 Forbidden    → Valid token but no permission for this resource
```

---

## Key Takeaway

> Always use headers for authentication — not URL params. Store keys in `.env` files, never in code. Bearer tokens are the most common pattern in modern APIs — format is always `Authorization: Bearer <token>`.
