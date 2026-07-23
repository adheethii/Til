# Docker Networking for Microservices

**Date:** 2026-07-23

## Beyond a Single Container

Earlier Docker networking notes covered basic container-to-container
communication. This note goes further — how multiple SERVICES
(API, database, cache) discover and talk to each other reliably.

```
Single container:  one app, done
Microservices:     API + DB + cache + queue, all need to find
                    and talk to each other correctly
```

---

## The Core Idea — Docker's Built-in DNS

```
Inside a Docker network, containers reach each other using their
SERVICE NAME as a hostname — Docker resolves this automatically,
no manual IP management needed.
```

```yaml
# docker-compose.yml
services:
  api:
    build: .
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
      - REDIS_URL=redis://cache:6379
    depends_on:
      - db
      - cache

  db:
    image: postgres:14

  cache:
    image: redis:7
```

Here, `db` and `cache` in the connection strings are NOT IP
addresses — they're the service names, and Docker's internal DNS
resolves them to the right container automatically.

---

## depends_on — Startup Order, Not Readiness

```
depends_on ensures containers START in the right order, but
it does NOT wait for the database to be fully READY to accept
connections — a common source of confusing early-startup errors.
```

```yaml
services:
  api:
    depends_on:
      db:
        condition: service_healthy   # waits for actual readiness

  db:
    image: postgres:14
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user"]
      interval: 5s
      timeout: 3s
      retries: 5
```

---

## Network Isolation Between Service Groups

```yaml
services:
  api:
    networks:
      - frontend-net
      - backend-net

  db:
    networks:
      - backend-net   # NOT on frontend-net — unreachable from
                        # outside, only 'api' can talk to it

networks:
  frontend-net:
  backend-net:
```

This means even if the `api` container is exposed publicly, the
`db` container is only reachable from other containers on
`backend-net` — a real isolation boundary, not just convention.

---

## Communicating with the Outside World

```yaml
services:
  api:
    ports:
      - "8000:8000"   # host:container — exposed OUTSIDE Docker

  db:
    # no 'ports' — only reachable INSIDE the Docker network,
    # never directly from the host machine or internet
```

Only `api` is reachable from outside; `db` and `cache` are
intentionally invisible to the outside world — a basic but
important security default.

---

## Debugging Network Issues

```bash
# See all networks
docker network ls

# Inspect a specific network — see which containers are attached
docker network inspect my-network

# Test connectivity FROM one container TO another
docker exec -it api-container ping db

# Check DNS resolution inside a container
docker exec -it api-container nslookup db
```

---

## Common Gotcha — localhost Doesn't Mean What You Think

```
❌ Inside container 'api', trying to reach the database with:
   DATABASE_URL=postgresql://user:pass@localhost:5432/mydb

'localhost' inside a container refers to THAT CONTAINER ITSELF,
not the host machine and not other containers.

✅ Correct: use the service name
   DATABASE_URL=postgresql://user:pass@db:5432/mydb
```

---

## Key Takeaway

> Docker Compose services communicate using service names as hostnames — Docker's internal DNS handles the resolution, no manual IP tracking needed. `depends_on` controls start ORDER, not readiness — use healthchecks for real readiness waiting. Keep databases off any network exposed outside Docker, and never expect `localhost` inside a container to reach another container.
