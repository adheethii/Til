# Handling API Errors Gracefully

**Date:** 2026-06-20

## Why Error Handling Matters

APIs fail — networks drop, servers crash, rate limits hit. Without error handling your app crashes. With it, your app stays stable and gives useful feedback.

```
No error handling → App crashes on first API failure
Good error handling → App catches it, logs it, recovers gracefully
```

---

## Common API Errors

| Error | Cause | Fix |
|-------|-------|-----|
| 400 Bad Request | Wrong data sent | Check request format |
| 401 Unauthorized | Missing/invalid token | Check API key |
| 403 Forbidden | No permission | Check account access |
| 404 Not Found | Wrong URL or ID | Check endpoint |
| 429 Too Many Requests | Rate limit hit | Add delay, retry |
| 500 Server Error | API is broken | Retry later |
| Timeout | Network too slow | Increase timeout |
| ConnectionError | No internet | Check connection |

---

## Basic Error Handling

```python
import requests

response = requests.get("https://api.example.com/users/1")

# Method 1 — Check status code manually
if response.status_code == 200:
    data = response.json()
elif response.status_code == 404:
    print("User not found")
elif response.status_code == 401:
    print("Invalid API key")
else:
    print(f"Error: {response.status_code}")
```

---

## raise_for_status()

Automatically raises an exception for any 4xx or 5xx response:

```python
import requests

response = requests.get("https://api.example.com/users/1")

try:
    response.raise_for_status()   # raises HTTPError for 4xx/5xx
    data = response.json()
    print(data)
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
```

---

## Full Error Handling Pattern

```python
import requests
import time

def call_api(url, headers=None, retries=3):
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as e:
            if response.status_code == 429:
                # Rate limited — wait and retry
                print(f"Rate limited. Waiting 5 seconds...")
                time.sleep(5)
            elif response.status_code >= 500:
                # Server error — retry
                print(f"Server error. Attempt {attempt + 1}/{retries}")
                time.sleep(2)
            else:
                # Client error — don't retry
                print(f"Client error: {e}")
                return None

        except requests.exceptions.Timeout:
            print(f"Timeout. Attempt {attempt + 1}/{retries}")
            time.sleep(2)

        except requests.exceptions.ConnectionError:
            print("No internet connection")
            return None

    print("All retries failed")
    return None
```

---

## Handling Rate Limits (429)

```python
import requests
import time

def get_with_retry(url, headers):
    while True:
        response = requests.get(url, headers=headers)

        if response.status_code == 429:
            retry_after = int(response.headers.get("Retry-After", 5))
            print(f"Rate limited. Waiting {retry_after}s...")
            time.sleep(retry_after)
        else:
            return response
```

---

## Key Takeaway

> Always wrap API calls in try/except. Use `raise_for_status()` to catch HTTP errors automatically. For 429 rate limits — wait and retry. For 5xx server errors — retry with backoff. For 4xx client errors — fix your request, don't retry.
