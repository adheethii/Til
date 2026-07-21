# Python Asyncio Basics

**Date:** 2026-07-21

## What is Asyncio?

Asyncio lets Python handle many I/O-bound tasks (network requests, file
reads, API calls) concurrently — without needing multiple threads/processes.

```
Synchronous:  Task A (wait 2s) → Task B (wait 2s) → Task C (wait 2s)
              Total: 6 seconds

Asynchronous: Task A, B, C all start waiting AT THE SAME TIME
              Total: ~2 seconds (limited by the slowest one)
```

---

## When Asyncio Helps (and When It Doesn't)

```
✅ Good for I/O-bound work:
- Calling multiple APIs
- Reading multiple files
- Database queries
- Web scraping many pages

❌ Doesn't help CPU-bound work:
- Heavy computation (use multiprocessing instead)
- Training an ML model (CPU-bound, asyncio won't speed this up)
```

---

## Basic Syntax — async/await

```python
import asyncio

async def fetch_data(name, delay):
    print(f"Starting {name}...")
    await asyncio.sleep(delay)   # simulates a network call
    print(f"Finished {name}!")
    return f"{name} result"

async def main():
    result = await fetch_data("Task A", 2)
    print(result)

asyncio.run(main())
```

---

## Running Tasks Concurrently

```python
import asyncio

async def fetch_data(name, delay):
    await asyncio.sleep(delay)
    return f"{name} done"

async def main():
    # Sequential — takes 2+3+1 = 6 seconds total
    r1 = await fetch_data("A", 2)
    r2 = await fetch_data("B", 3)
    r3 = await fetch_data("C", 1)

    # Concurrent — takes ~3 seconds (the slowest task)
    results = await asyncio.gather(
        fetch_data("A", 2),
        fetch_data("B", 3),
        fetch_data("C", 1)
    )
    print(results)

asyncio.run(main())
```

---

## Practical Example — Calling Multiple APIs

```python
import asyncio
import httpx

async def fetch_url(client, url):
    response = await client.get(url)
    return response.status_code

async def check_apis():
    urls = [
        "https://api1.example.com/health",
        "https://api2.example.com/health",
        "https://api3.example.com/health",
    ]

    async with httpx.AsyncClient() as client:
        # All 3 requests fire concurrently, not one after another
        results = await asyncio.gather(*[fetch_url(client, url) for url in urls])

    return results

status_codes = asyncio.run(check_apis())
```

---

## Asyncio in FastAPI

```python
from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/combined-data")
async def get_combined_data():
    async with httpx.AsyncClient() as client:
        # Fetch from two services concurrently instead of sequentially
        weather_task = client.get("https://weather-api.com/current")
        news_task = client.get("https://news-api.com/latest")

        weather_resp, news_resp = await asyncio.gather(weather_task, news_task)

    return {
        "weather": weather_resp.json(),
        "news": news_resp.json()
    }
```

FastAPI is built on asyncio — using `async def` for route handlers that
call external services lets FastAPI handle other requests while waiting.

---

## Common Gotcha — Mixing Sync and Async

```python
# ❌ Wrong — blocks the entire event loop
async def bad_example():
    import time
    time.sleep(5)   # BLOCKS everything, defeats the purpose of async!

# ✅ Correct — yields control back to the event loop
async def good_example():
    await asyncio.sleep(5)   # non-blocking
```

---

## Key Takeaway

> Asyncio speeds up I/O-bound work (API calls, network requests) by running tasks concurrently instead of waiting for each one sequentially — but does nothing for CPU-bound work like model training. `asyncio.gather()` is the key tool for running multiple async tasks at once. FastAPI's async routes are especially valuable when a single request needs to call multiple external services.
