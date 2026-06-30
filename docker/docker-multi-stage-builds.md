# Docker Multi-Stage Builds

**Date:** 2026-06-30

## What are Multi-Stage Builds?

Multi-stage builds use multiple FROM statements in one Dockerfile — each stage can copy artifacts from the previous one, resulting in a much smaller final image.

```
Stage 1 (builder): Install all dependencies, compile code
Stage 2 (runtime): Copy only what's needed to run
Result: Small, lean production image ✅
```

---

## Why it Matters

```bash
# Without multi-stage (all dev tools included)
docker image ls my-api
# → SIZE: 1.2GB 😱

# With multi-stage (only runtime deps)
docker image ls my-api-optimized
# → SIZE: 180MB ✅
```

---

## Basic Multi-Stage Dockerfile

```dockerfile
# ── Stage 1: Builder ──────────────────────────
FROM python:3.10 AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# ── Stage 2: Runtime ──────────────────────────
FROM python:3.10-slim

WORKDIR /app

# Copy only installed packages from builder
COPY --from=builder /root/.local /root/.local

# Copy app files
COPY main.py .
COPY model.pkl .

# Make sure scripts in .local are usable
ENV PATH=/root/.local/bin:$PATH

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## ML-Specific Multi-Stage Build

```dockerfile
# Stage 1 — Train model
FROM python:3.10 AS trainer

WORKDIR /app
COPY requirements.txt train.py data.csv ./
RUN pip install -r requirements.txt
RUN python train.py    # generates model.pkl

# Stage 2 — Serve model
FROM python:3.10-slim AS server

WORKDIR /app
COPY requirements-serve.txt .
RUN pip install -r requirements-serve.txt

COPY --from=trainer /app/model.pkl .
COPY main.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Key Commands

```bash
# Build specific stage only
docker build --target builder -t my-app-builder .

# Build final image
docker build -t my-app-optimized .

# Compare sizes
docker images | grep my-app
```

---

## Key Takeaway

> Multi-stage builds separate the build environment from the runtime environment — you get all tools for building but only what's needed for running. Essential for production ML deployments where image size and security matter. Use python:3.10-slim for runtime — much smaller than python:3.10.
