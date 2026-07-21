# Feature Stores Explained

**Date:** 2026-07-19

## What is a Feature Store?

A feature store is a centralized system that stores, manages, and serves
ML features — solving the problem of features being computed differently
(and inconsistently) in training versus production.

```
Without feature store: training code computes features one way,
                        serving code computes them ANOTHER way
                        → training-serving skew → model performs worse
                          in production than in testing

With feature store:    ONE definition of each feature, used
                        identically everywhere
```

---

## The Problem It Solves — Training-Serving Skew

```python
# Training pipeline (batch, computed in a notebook)
df["avg_purchase_30d"] = df.groupby("user_id")["amount"].transform(
    lambda x: x.rolling(30).mean()
)

# Serving pipeline (real-time, computed in the API — written separately!)
avg_purchase = get_last_30_purchases(user_id) / 30   # subtly different logic!
```

Even a tiny difference in how a feature is calculated between these two
places causes the model to see different input distributions than it
was trained on — a common, hard-to-debug source of production issues.

---

## Two Types of Features

```
Batch features (computed periodically, don't change fast):
- User's total lifetime purchases
- Account age
- Historical average order value
  → computed nightly/hourly, stored, served from a fast lookup

Real-time / streaming features (change constantly):
- Current session length
- Items currently in cart
- Time since last click
  → computed on-the-fly at request time
```

---

## Feature Store Architecture

```
                  ┌─────────────────┐
Data Sources  →   │  Feature         │  →  Offline Store (for training)
(logs, DB,        │  Transformation  │     e.g. data warehouse, Parquet files
 events)          │  Pipeline        │
                  └────────┬─────────┘
                           │
                           ↓
                  Online Store (for serving)
                  e.g. Redis, DynamoDB — low latency lookups

Training job  ←── reads from Offline Store
Prediction API ←── reads from Online Store (same feature DEFINITIONS)
```

---

## Popular Feature Store Tools

| Tool | Type |
|------|------|
| Feast | Open-source, most widely adopted |
| Tecton | Managed/commercial |
| SageMaker Feature Store | AWS-native |
| Vertex AI Feature Store | GCP-native |
| Databricks Feature Store | Integrated with Databricks |

---

## Simple Feast Example

```python
from feast import FeatureStore

store = FeatureStore(repo_path=".")

# Training: get historical features for a training dataset
training_df = store.get_historical_features(
    entity_df=entity_df,
    features=["user_stats:avg_purchase_30d", "user_stats:account_age"]
).to_df()

# Serving: get real-time features for a single prediction
online_features = store.get_online_features(
    features=["user_stats:avg_purchase_30d", "user_stats:account_age"],
    entity_rows=[{"user_id": 12345}]
).to_dict()
```

Same feature definitions, same code path — no more skew.

---

## When You Actually Need One

```
✅ Multiple models sharing the same features (avoid recomputing)
✅ Team has separate training and serving codebases (the skew risk)
✅ Real-time serving requirements with complex features
✅ Need feature versioning/lineage for compliance or debugging

❌ Small team, single model, simple features — often overkill
   (a simple shared function/module may be enough)
```

---

## Key Takeaway

> Feature stores exist to eliminate training-serving skew — the #1 silent killer of production ML model performance. The core idea is simple: define each feature ONCE, serve it from both an offline store (training) and online store (real-time prediction) using identical logic. Not every project needs one, but every ML engineer should recognize the problem it solves.
