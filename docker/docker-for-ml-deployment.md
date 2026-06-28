# Docker for ML Model Deployment

**Date:** 2026-06-28

## Why Docker for ML?

ML deployments have unique challenges — specific Python versions, GPU drivers, heavy libraries. Docker solves all of this.

```
Data Scientist's laptop → Docker image → Any server → Same results ✅
```

---

## Complete ML API Docker Setup

### main.py (FastAPI + ML model)

```python
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI(title="Churn Prediction API")

# Load model at startup
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

class CustomerData(BaseModel):
    tenure: int
    monthly_charges: float
    total_charges: float

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict")
def predict(data: CustomerData):
    features = np.array([[data.tenure, data.monthly_charges, data.total_charges]])
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]
    return {
        "churn": bool(prediction),
        "probability": round(float(probability), 3)
    }
```

### requirements.txt

```
fastapi
uvicorn
scikit-learn
pandas
numpy
pydantic
```

### Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app and model
COPY main.py .
COPY model.pkl .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Build, Run and Test

```bash
# Build
docker build -t churn-api:v1 .

# Run
docker run -d -p 8000:8000 --name churn churn-api:v1

# Test
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"tenure": 24, "monthly_charges": 65.5, "total_charges": 1572.0}'

# Check logs
docker logs churn

# Stop
docker stop churn
```

---

## Multi-stage Build (Smaller Image)

```dockerfile
# Stage 1 — build
FROM python:3.10 AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Stage 2 — runtime (smaller)
FROM python:3.10-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY main.py model.pkl .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## What I'll Build

Deploying my [Telecom Customer Churn](https://github.com/adheethii/Telecom-customer-churn) model as a Dockerized FastAPI app — fully portable and deployable to any cloud platform with one command.

---

## Key Takeaway

> Docker + FastAPI is the standard way to deploy ML models in production. Copy requirements.txt before your code for better layer caching. Use multi-stage builds to reduce image size. Always add a /health endpoint for monitoring.
