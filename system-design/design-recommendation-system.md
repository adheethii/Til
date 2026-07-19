# ML System Design — Interview Framework

**Date:** 2026-07-18

## Why ML System Design is Different

Regular system design asks "how do you scale a web app?"
ML system design asks "how do you scale a **prediction**?" — which adds
data pipelines, training, model serving, and monitoring on top of
standard infrastructure concerns.

```
Standard System Design: Client → API → Database → Response
ML System Design:        Client → API → Feature Pipeline → Model → Response
                                              ↑                ↓
                                        Training Pipeline ← Feedback Loop
```

---

## The Universal Framework (Use This Every Time)

```
1. Clarify Requirements       (5 min)
2. Frame as an ML Problem     (5 min)
3. Data                       (10 min)
4. Feature Engineering        (5 min)
5. Model Selection & Training (10 min)
6. Evaluation                 (5 min)
7. Deployment & Serving       (10 min)
8. Monitoring & Maintenance   (5 min)
9. Scale & Trade-offs         (5 min)
```

Never skip step 1 — jumping straight to "I'd use XGBoost" without
clarifying the problem is the #1 mistake candidates make.

---

## Step 1 — Clarify Requirements

Always ask these before proposing anything:

```
- What's the business goal? (reduce churn, increase engagement, detect fraud)
- What's the scale? (100 users vs 100 million users)
- Real-time or batch predictions?
- What's an acceptable latency? (10ms vs 1 hour)
- What's the cost of a false positive vs false negative?
- Is there existing data, or starting from scratch?
```

**Example — "Design a system to detect fraudulent transactions"**
```
Clarifying questions:
- Real-time (block transaction) or batch (flag for review)?
- What's the acceptable false positive rate? (blocking real customers is costly)
- Volume: transactions per second?
- Is labeled fraud data available?
```

---

## Step 2 — Frame as an ML Problem

Convert the business problem into a concrete ML task:

| Business Problem | ML Framing |
|---|---|
| Detect fraud | Binary classification (fraud/not fraud) |
| Recommend products | Ranking / recommendation |
| Predict churn | Binary classification with probability |
| Detect spam | Binary classification (often needs low latency) |
| Forecast demand | Time series regression |

---

## Step 3 — Data

```
- Where does data come from? (logs, user actions, external APIs)
- Labeled or unlabeled? (supervised vs unsupervised approach)
- How much data? (affects model complexity choice)
- Data freshness — how quickly does data go stale?
- Class imbalance? (fraud, churn — rare event problems)
```

---

## Step 4 — Feature Engineering

```
- What signals predict the outcome?
- Real-time features (session length, current cart) vs
  batch features (historical purchase pattern, account age)
- Feature store needed? (for consistency between training and serving)
```

---

## Step 5 — Model Selection & Training

```
Start simple, justify complexity:
Baseline (Logistic Regression) → Tree-based (XGBoost/RF) → Deep Learning

Always explain WHY:
"I'd start with XGBoost because it handles tabular data well,
 gives feature importance, and trains fast for iteration.
 Only move to deep learning if XGBoost plateaus and we have
 enough data to justify it."
```

---

## Step 6 — Evaluation

```
- What metric matches the business goal?
  (F1 for imbalanced fraud detection, not accuracy)
- Offline evaluation (test set metrics)
- Online evaluation (A/B testing in production)
- How do you know the model is actually helping the business?
```

---

## Step 7 — Deployment & Serving

```
- Batch prediction (nightly job) vs Real-time API (< 100ms)
- Model versioning — how do you roll back a bad model?
- Shadow deployment — test new model alongside old one silently
```

---

## Step 8 — Monitoring & Maintenance

```
- Model drift — does performance degrade over time?
- Data drift — has the input distribution changed?
- Retraining schedule — daily, weekly, triggered by drift?
- Alerting — who gets notified if predictions look wrong?
```

---

## Step 9 — Scale & Trade-offs

```
- What breaks first at 10x scale?
- Latency vs accuracy trade-off
- Cost of retraining vs cost of stale model
```

---

## Key Takeaway

> ML system design interviews reward structured thinking over technical depth in any single area. Always clarify requirements first, frame the problem clearly, and walk through data → features → model → serving → monitoring in order. Interviewers care more about your reasoning process than your final answer.
