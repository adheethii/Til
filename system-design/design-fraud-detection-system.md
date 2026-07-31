# Worked Example — Design a Fraud Detection System

**Date:** 2026-07-30 

## The Question

"Design a system that detects fraudulent credit card transactions
in real time."

This closes the last unchecked item in my `interview-prep.md`
system design checklist — the ML system design framework and
worked examples for recommendation systems and RAG are already
covered; this is the third and final worked example.

---

## Step 1 — Clarify Requirements

```
Q: How fast must a decision be made?
A: Assume: transaction must be approved/declined in real time,
   under ~200ms — this rules out anything requiring a human
   in the loop for every transaction

Q: What's the cost of a false positive vs false negative?
A: False positive (blocking a real customer) → customer
   frustration, lost trust, but recoverable
   False negative (missing real fraud) → direct financial loss
   Neither cost is zero — this needs explicit discussion,
   not an assumption that one obviously outweighs the other

Q: Volume?
A: Assume: thousands of transactions per second at peak

Q: Is labeled fraud data available?
A: Assume yes, but SEVERELY imbalanced — fraud is a rare event,
   likely well under 1% of transactions
```

---

## Step 2 — Frame as an ML Problem

```
Core task: Binary classification (fraud / not fraud), but with
two properties that shape everything downstream:

1. Extreme class imbalance (rare positive class)
2. Real-time latency constraint (no room for slow models)
```

---

## Step 3 — Data

```
Transaction features: amount, merchant category, location,
                       time of day, device fingerprint

User history features: average transaction amount, typical
                        locations, typical merchant categories,
                        time since last transaction

Labels: confirmed fraud (from chargebacks, customer reports) —
        arrives LATE, often days or weeks after the transaction,
        which matters a lot for how retraining works
```

---

## Step 4 — Feature Engineering

```
Real-time features (must be computed in milliseconds):
- Is this amount unusually large for this user?
- Is this location unusual for this user?
- Time since user's last transaction (rapid-fire = suspicious)
- Is this merchant category new for this user?

Aggregated/historical features (precomputed, looked up fast):
- User's rolling 30-day average transaction amount
- User's typical transaction velocity (transactions per day)

This is a direct real-world case for a FEATURE STORE — the same
feature (e.g. "30-day average spend") must be computed identically
whether it's being calculated during training or looked up during
a live transaction, or the model sees different distributions in
production than what it learned on.
```

---

## Step 5 — Model Selection & Training

```
Given the extreme class imbalance, plain accuracy is meaningless
here — a model that predicts "not fraud" for everything is
99%+ "accurate" and completely useless.

Approach:
- Gradient boosted trees (XGBoost/LightGBM) — fast inference,
  handles tabular data well, gives feature importance
- Handle imbalance with class weighting or SMOTE-style resampling
  during TRAINING only (never on validation/test data)
- Consider an ensemble: a fast, simple model for the real-time
  path, plus a slower, more thorough model for a secondary
  async review of borderline cases

Why not deep learning by default:
Tabular fraud data with engineered features is usually where
gradient boosted trees outperform deep learning, and the
inference speed requirement makes a heavy model a real risk.
```

---

## Step 6 — Evaluation

```
Wrong metric: accuracy (misleading given the imbalance)

Right metrics:
- Precision-Recall AUC (more informative than ROC-AUC on
  heavily imbalanced problems)
- Precision at a fixed recall (e.g. "at 90% fraud caught,
  what's our false positive rate?") — directly maps to the
  real business trade-off from Step 1

Offline evaluation alone isn't enough here — fraud patterns
shift constantly as fraudsters adapt, so online A/B testing
and continuous monitoring matter more than in most ML systems.
```

---

## Step 7 — Deployment & Serving

```
Architecture:
Transaction request → Feature lookup (online feature store,
                       <10ms) → Fast model inference (<50ms)
                     → Decision: approve / decline / flag for review

"Flag for review" tier:
Borderline-confidence transactions can route to a slower,
more thorough model or a human review queue — NOT every
transaction needs the fastest possible path, only clear-cut
approvals do.
```

---

## Step 8 — Monitoring & Maintenance

```
- Fraud patterns drift FAST — fraudsters actively adapt to
  evade whatever the current model catches, so this is one
  of the strongest real-world cases for drift-triggered
  retraining, not just schedule-based retraining
- Delayed labels (chargebacks arrive weeks later) mean you're
  often training on data that's already somewhat stale relative
  to the CURRENT fraud patterns — worth being explicit about
  this limitation rather than assuming labels are always fresh
- Monitor: fraud caught rate, false positive rate, and model
  score distribution shift over time
```

---

## Step 9 — Scale & Trade-offs

```
At 10x transaction volume:
- Feature store lookups become the likely bottleneck before
  the model itself does — caching hot user profiles helps
- The precision/recall trade-off from Step 1 may need
  revisiting at scale — a false positive rate that was
  acceptable at current volume could mean a much larger
  absolute number of frustrated customers at 10x scale
```

---

## Key Takeaway

> Fraud detection is the clearest real-world case for taking class imbalance seriously from the start — accuracy is actively misleading here, not just suboptimal. The real-time latency constraint and the late-arriving labels problem (chargebacks take weeks) are the two things that most distinguish this from a typical classification system design question, and are worth naming explicitly rather than assuming labels arrive instantly like in most textbook examples.
