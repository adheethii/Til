# Deploying a FastAPI App

**Date:** 2026-06-23

## Deployment Options

| Platform | Cost | Best For |
|----------|------|----------|
| Uvicorn (local) | Free | Development |
| Railway | Free tier | Quick deployment |
| Render | Free tier | Portfolio projects |
| Hugging Face Spaces | Free | ML model APIs |
| Docker + VPS | Paid | Production |

---

## Step 1 — Prepare Your App

```
my_api/
├── main.py           ← FastAPI app
├── model.pkl         ← trained ML model
├── requirements.txt  ← dependencies
└── .env              ← secrets (never push this!)
```

**requirements.txt:**
```
fastapi
uvicorn
scikit-learn
pandas
numpy
pydantic
python-dotenv
```

---

## Step 2 — Run Locally

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

- `--reload` → auto-restart on code changes (dev only)
- `--host 0.0.0.0` → accessible from other devices on network
- `--port 8000` → port number

---

## Step 3 — Deploy to Render (Free)

1. Push your project to GitHub
2. Go to [render.com](https://render.com) → New → Web Service
3. Connect your GitHub repo
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Click Deploy

Your API will be live at `https://your-app.onrender.com` 🎉

---

## Step 4 — Deploy to Hugging Face Spaces (Best for ML)

1. Go to [huggingface.co/spaces](https://huggingface.co/spaces)
2. Create new Space → SDK: **Docker**
3. Add a `Dockerfile`:

```dockerfile
FROM python:3.10

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
```

4. Push your code — HF builds and deploys automatically

---

## Environment Variables

Never hardcode secrets — use environment variables:

```python
# main.py
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
```

On Render/Railway → add environment variables in the dashboard.
On local → use `.env` file (add to `.gitignore`!)

---

## Testing Your Deployed API

```python
import requests

# Replace with your deployed URL
BASE_URL = "https://your-app.onrender.com"

response = requests.post(f"{BASE_URL}/predict",
    json={"tenure": 24, "monthly_charges": 65.5})

print(response.json())
```

---

## What I'll Build Next

Deploying my [Telecom Customer Churn](https://github.com/adheethii/Telecom-customer-churn) model as a FastAPI app on Render — making it accessible via a real public URL, not just a local Jupyter notebook.

---

## Key Takeaway

> Deployment = making your API accessible to the world. Render and Hugging Face Spaces are the easiest free options for ML APIs. Always use environment variables for secrets, never hardcode them. Your `requirements.txt` is critical — missing packages will break the deployment.
