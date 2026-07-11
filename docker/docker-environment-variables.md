# Docker Environment Variables

**Date:** 2026-07-11

## Why Environment Variables in Docker?

Environment variables let you configure containers **without changing code** — different values for dev, staging, production.

```
Same Docker image + different env vars = different behavior
```

---

## Setting Environment Variables

### In Dockerfile

```dockerfile
FROM python:3.10-slim

ENV APP_ENV=production
ENV MODEL_PATH=/app/models/model.pkl
ENV LOG_LEVEL=info

COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
```

### At Runtime (docker run)

```bash
# Single variable
docker run -e API_KEY=secret123 my-api

# Multiple variables
docker run \
  -e API_KEY=secret123 \
  -e MODEL_VERSION=v2 \
  -e DEBUG=false \
  my-api

# From a file
docker run --env-file .env my-api
```

### In docker-compose.yml

```yaml
services:
  api:
    build: .
    environment:
      - API_KEY=secret123
      - MODEL_VERSION=v2
      - DEBUG=false
    env_file:
      - .env
```

---

## Reading Env Vars in Python

```python
import os

api_key = os.getenv("API_KEY")
model_version = os.getenv("MODEL_VERSION", "v1")  # default if not set
debug = os.getenv("DEBUG", "false").lower() == "true"

print(f"Running model {model_version}, debug={debug}")
```

---

## .env File Pattern

```bash
# .env file (never commit this!)
API_KEY=sk-abc123secretkey
MODEL_VERSION=v2
DEBUG=false
DATABASE_URL=postgresql://user:pass@db:5432/mydb
```

```python
# main.py — load .env locally, Docker uses --env-file
from dotenv import load_dotenv
import os

load_dotenv()   # only needed for local dev, not inside container

api_key = os.getenv("API_KEY")
```

---

## Never Hardcode Secrets

```dockerfile
# ❌ NEVER do this
ENV API_KEY=sk-abc123secretkey

# ✅ Instead, pass at runtime
# docker run -e API_KEY=$API_KEY my-api
```

---

## Different Environments Pattern

```bash
# Development
docker run --env-file .env.dev my-api

# Production
docker run --env-file .env.prod my-api
```

```
.env.dev:
  DEBUG=true
  LOG_LEVEL=debug

.env.prod:
  DEBUG=false
  LOG_LEVEL=error
```

---

## Key Takeaway

> Environment variables separate configuration from code — same Docker image works across dev/staging/prod. Never hardcode secrets in Dockerfile with ENV — pass them at runtime with `-e` or `--env-file`. Always add `.env` to `.gitignore` — never commit secrets to Git.
