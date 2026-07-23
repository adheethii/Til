# Load Balancing and Caching Basics

**Date:** 2026-07-23

## Why These Two Topics Together

Load balancing and caching are the two most common answers to
"how do you make this handle more traffic?" in system design
interviews — one distributes work, the other avoids redoing it.

```
Load balancing → spread REQUESTS across multiple servers
Caching        → avoid REPEATING expensive work at all
```

---

## Load Balancing

### The Problem It Solves

```
1 server, 10,000 requests/second → server falls over 💥
Many servers + load balancer → traffic spread evenly → survives
```

### Common Load Balancing Algorithms

```
Round Robin:
  Request 1 → Server A
  Request 2 → Server B
  Request 3 → Server C
  Request 4 → Server A (cycle repeats)
  Simple, but ignores server load/capacity differences

Least Connections:
  Send each new request to whichever server currently has
  the FEWEST active connections — adapts to uneven load

Weighted Round Robin:
  Server A (powerful) gets 3 requests for every 1 sent to
  Server B (weaker) — accounts for different server capacities

IP Hash:
  Route based on a hash of the client's IP — same client
  consistently reaches the same server (useful for session
  affinity / "sticky sessions")
```

### Where Load Balancers Sit

```
                    ┌─────────────┐
Client requests →   │Load Balancer│
                    └──────┬──────┘
              ┌────────────┼────────────┐
              ↓            ↓            ↓
          Server A     Server B     Server C
```

### Health Checks

```
Load balancers continuously ping each server (e.g. GET /health).
If a server stops responding correctly, it's automatically
removed from rotation until it recovers — this is exactly why
main.py in a deployed API should always expose a /health endpoint.
```

---

## Caching

### The Problem It Solves

```
Without cache: every request recomputes/refetches from scratch
               (expensive DB query, slow model inference, etc.)

With cache: first request does the work and STORES the result;
            subsequent identical requests get the stored result
            instantly
```

### Where to Cache

```
Client-side:    browser cache (static assets, images)
CDN:            cached content served from servers near the user
Application:    in-memory cache (Redis, Memcached) for computed
                results, DB query results, session data
Database:       query result caching, indexed lookups
```

### Cache Eviction Policies

```
LRU (Least Recently Used):
  Evict whatever hasn't been accessed in the longest time
  — the most common default policy

LFU (Least Frequently Used):
  Evict whatever has been accessed the FEWEST times overall

TTL (Time To Live):
  Evict automatically after a fixed duration, regardless
  of usage — good for data that goes stale (weather, prices)
```

### Simple Caching Example

```python
import redis
import json

cache = redis.Redis(host='localhost', port=6379)

def get_user_recommendations(user_id):
    cache_key = f"recommendations:{user_id}"

    # Check cache first
    cached = cache.get(cache_key)
    if cached:
        return json.loads(cached)

    # Cache miss — do the expensive work
    recommendations = compute_recommendations(user_id)  # slow

    # Store in cache with 1 hour expiry
    cache.setex(cache_key, 3600, json.dumps(recommendations))

    return recommendations
```

---

## Cache Invalidation — "The Hard Part"

```
The classic quote: "There are only two hard things in Computer
Science: cache invalidation and naming things."

Problem: if the underlying data changes, the cache becomes STALE
and serves outdated results.

Common strategies:
- TTL (accept some staleness, auto-expires)
- Write-through (update cache immediately when data changes)
- Explicit invalidation (delete cache key when related data updates)
```

---

## How This Connects to My Own Work

```
Load balancing: directly relevant to deploying the Telecom Churn
                FastAPI app at scale — multiple container instances
                behind a load balancer, each exposing /health

Caching: relevant to my Agentic RAG project — the FAISS index
         itself IS a form of caching (avoiding re-embedding
         documents on every query); could add a query-result
         cache for frequently asked questions
```

---

## Key Takeaway

> Load balancing distributes REQUESTS across servers (round robin, least connections, health checks); caching avoids REPEATING expensive work (Redis, TTL, LRU eviction). Cache invalidation — knowing WHEN to clear stale data — is usually the harder problem in practice, not the caching mechanism itself.
