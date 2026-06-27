# Dockerizing a FastAPI App

**Date:** 2026-06-27

## Why Dockerize?

Packaging your FastAPI ML app in Docker means it runs identically everywhere — your laptop, a server, or any cloud platform.

```
Without Docker → "works on my machine" 😅
With Docker    → works everywhere ✅
```

---

## Project Structure

```
my_fastapi_app/
├── main.py
├── model.pkl
├── requirements.txt
├── Dockerfile
└── .dockerignore
```

---

## Dockerfile

```dockerfile
# Use official Python slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies first (caching layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Expose port
EXPOSE 8000

# Start the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## .dockerignore

```
__pycache__/
*.pyc
.env
.git
*.md
venv/
```

Keeps your image small — don't copy unnecessary files.

---

## Build and Run

```bash
# Build the image
docker build -t churn-api .

# Run the container
docker run -p 8000:8000 churn-api

# Run with environment variables
docker run -p 8000:8000 -e API_KEY=secret churn-api

# Run in background
docker run -d -p 8000:8000 churn-api
```

---

## Test Your Dockerized API

```python
import requests

response = requests.post(
    "http://localhost:8000/predict",
    json={"tenure": 24, "monthly_charges": 65.5}
)
print(response.json())
```

---

## Push to Docker Hub

```bash
# Login
docker login

# Tag your image
docker tag churn-api yourusername/churn-api:v1

# Push
docker push yourusername/churn-api:v1
```

---

## What I'll Build

Dockerizing my [Telecom Customer Churn](https://github.com/adheethii/Telecom-customer-churn) FastAPI app — making it deployable anywhere with a single `docker run` command.

---

## Key Takeaway

> Dockerizing a FastAPI app is 3 steps: write a Dockerfile, build the image, run the container. Always copy requirements.txt first for better layer caching. Use .dockerignore to keep image size small.
