# Docker Compose Basics

**Date:** 2026-06-26

## What is Docker Compose?

Docker Compose lets you **run multiple containers together** with a single command — perfect for apps that need a web server + database + cache all running together.

```
docker-compose up → starts ALL services at once
docker-compose down → stops ALL services
```

---

## docker-compose.yml Example

```yaml
version: "3.8"

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
    depends_on:
      - db

  db:
    image: postgres:14
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

---

## Key Commands

```bash
# Start all services
docker-compose up

# Start in background
docker-compose up -d

# Stop all services
docker-compose down

# View logs
docker-compose logs

# Rebuild after code changes
docker-compose up --build
```

---

## Key Takeaway

> Docker Compose orchestrates multiple containers with one file. Define each service, its image/build, ports, and environment variables. docker-compose up starts everything, docker-compose down stops it all. Essential for apps with databases or multiple services.
