# Creating Your First FastAPI Endpoint

**Date:** 2026-06-21

## What is an Endpoint?

An endpoint is a specific URL in your API that performs a specific action.

```
GET  /predict     → run ML model prediction
POST /upload      → upload a file
GET  /health      → check if API is running
```

---

## Project Structure

```
my_api/
├── main.py          ← FastAPI app
├── model.py         ← ML model loading
├── requirements.txt
└── .env             ← API keys, secrets
```

---

## Building a Real ML Prediction Endpoint

```python
# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI(title="Churn Prediction API")

# Load model on startup
model = pickle.load(open("model.pkl", "rb"))

# Define input schema
class CustomerData(BaseModel):
    tenure: int
    monthly_charges: float
    total_charges: float
    contract_type: str

# Define output schema
class PredictionResult(BaseModel):
    churn_prediction: str
    probability: float

@app.get("/")
def home():
    return {"status": "running", "model": "Churn Predictor v1"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/predict", response_model=PredictionResult)
def predict(data: CustomerData):
    # Prepare features
    features = np.array([[
        data.tenure,
        data.monthly_charges,
        data.total_charges
    ]])

    # Predict
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    return {
        "churn_prediction": "Yes" if prediction == 1 else "No",
        "probability": round(float(probability), 3)
    }
```

---

## Testing Your Endpoint

**Option 1 — Swagger UI (easiest)**
Go to `http://localhost:8000/docs` → click `/predict` → Try it out → Execute

**Option 2 — Python requests**
```python
import requests

response = requests.post(
    "http://localhost:8000/predict",
    json={
        "tenure": 24,
        "monthly_charges": 65.5,
        "total_charges": 1572.0,
        "contract_type": "Month-to-month"
    }
)

print(response.json())
# → {"churn_prediction": "Yes", "probability": 0.823}
```

**Option 3 — curl**
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"tenure": 24, "monthly_charges": 65.5, "total_charges": 1572.0, "contract_type": "Month-to-month"}'
```

---

## Adding Input Validation

Pydantic automatically validates — no extra code needed:

```python
class CustomerData(BaseModel):
    tenure: int                          # must be integer
    monthly_charges: float               # must be float
    contract_type: str                   # must be string

# If wrong type sent → FastAPI returns 422 automatically
# {"detail": [{"loc": ["body", "tenure"], "msg": "value is not a valid integer"}]}
```

---

## What I'll Build

This pattern — loading a trained Scikit-Learn model and wrapping it in a FastAPI endpoint — is exactly how to deploy my [Telecom Customer Churn](https://github.com/adheethii/Telecom-customer-churn) model as a real API.

---

## Key Takeaway

> A FastAPI ML endpoint is just 3 things: a Pydantic model for input, load your trained model, return a prediction. The `/docs` endpoint makes testing effortless. This is the standard pattern for deploying any ML model as an API.
