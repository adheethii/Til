# Calling APIs with Python requests Library

**Date:** 2026-06-19

## Installation

```bash
pip install requests
```

---

## Basic GET Request

```python
import requests

response = requests.get("https://api.example.com/users")

print(response.status_code)   # 200
print(response.json())        # parsed JSON data
```

---

## Full Request Anatomy

```python
import requests

response = requests.get(
    url="https://api.example.com/users",          # endpoint
    params={"page": 1, "limit": 10},              # query parameters
    headers={"Authorization": "Bearer token123"}  # headers
)
```

URL with params becomes:
```
https://api.example.com/users?page=1&limit=10
```

---

## All HTTP Methods

```python
import requests

BASE_URL = "https://api.example.com"
HEADERS = {"Authorization": "Bearer your_token"}

# GET — read
response = requests.get(f"{BASE_URL}/users/1", headers=HEADERS)

# POST — create
response = requests.post(f"{BASE_URL}/users",
    json={"name": "Adheethi", "role": "ML Engineer"},
    headers=HEADERS)

# PUT — full update
response = requests.put(f"{BASE_URL}/users/1",
    json={"name": "Adheethi K", "role": "AI Engineer"},
    headers=HEADERS)

# PATCH — partial update
response = requests.patch(f"{BASE_URL}/users/1",
    json={"role": "AI Engineer"},
    headers=HEADERS)

# DELETE — remove
response = requests.delete(f"{BASE_URL}/users/1", headers=HEADERS)
```

---

## Response Object

```python
response = requests.get("https://api.example.com/users/1")

response.status_code    # 200
response.json()         # parsed JSON as Python dict
response.text           # raw response as string
response.headers        # response headers
response.url            # final URL called
response.ok             # True if status 200-299
```

---

## Error Handling

```python
import requests

try:
    response = requests.get("https://api.example.com/users/1", timeout=5)
    response.raise_for_status()   # raises exception for 4xx/5xx
    data = response.json()
    print(data)

except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")         # 404, 401, etc.
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.ConnectionError:
    print("Connection failed")
```

---

## Real Example — Calling a Public API

```python
import requests

# OpenWeatherMap API (free)
API_KEY = "your_api_key"
city = "Kochi"

response = requests.get(
    "https://api.openweathermap.org/data/2.5/weather",
    params={"q": city, "appid": API_KEY, "units": "metric"}
)

if response.ok:
    data = response.json()
    print(f"Temperature in {city}: {data['main']['temp']}°C")
    print(f"Condition: {data['weather'][0]['description']}")
```

---

## Key Takeaway

> `requests` is the standard Python library for calling APIs. Use `params=` for query strings, `json=` for request body, `headers=` for auth. Always check `status_code` and handle errors with `raise_for_status()` or try/except.
