# Docker Basics

**Date:** 2026-06-26

## What is Docker?

Docker is a tool that packages your application and all its dependencies into a **container** — a lightweight, portable unit that runs the same way on any machine.

```
Your app + Python + libraries + config = Docker Container
Runs identically on: your laptop, server, cloud ✅
```

---

## Why Docker?

```
❌ Without Docker:
"It works on my machine but not on the server"
→ Different Python versions, missing libraries, wrong OS

✅ With Docker:
Same container runs everywhere — guaranteed
```

---

## Key Concepts

| Concept | Meaning |
|---------|---------|
| Image | Blueprint for a container (like a class) |
| Container | Running instance of an image (like an object) |
| Dockerfile | Instructions to build an image |
| Docker Hub | Registry to share images (like GitHub for containers) |

---

## Basic Dockerfile for FastAPI

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Common Commands

```bash
# Build image
docker build -t my-api .

# Run container
docker run -p 8000:8000 my-api

# List running containers
docker ps

# Stop container
docker stop <container_id>

# List images
docker images

# Remove image
docker rmi my-api
```

---

## Port Mapping

```bash
docker run -p 8000:8000 my-api
#           ↑host  ↑container
```

Maps port 8000 on your machine to port 8000 inside the container.

---

## Key Takeaway

> Docker solves the "works on my machine" problem by packaging everything your app needs into one container. A Dockerfile is just a recipe — FROM sets the base, COPY adds your files, RUN installs dependencies, CMD starts your app.
