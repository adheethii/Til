# Worked Example — Design a Recommendation System

**Date:** 2026-07-18

## The Question

"Design a system that recommends products to users on an e-commerce platform."

This is one of the most commonly asked ML system design questions — walking
through it fully once makes the pattern reusable for similar questions
(video recommendations, content feeds, job matching).

---

## Step 1 — Clarify Requirements

```
Q: How many users and products? 
A: 10M users, 1M products (assume, if not given)

Q: Real-time or can recommendations be precomputed?
A: Homepage can be precomputed nightly; "similar items" needs real-time

Q: What's success? Clicks, purchases, time-on-site?
A: Assume: increase click-through rate (CTR) and purchase conversion

Q: Cold start — new users/products with no history?
A: Yes, must be handled
```

---

## Step 2 — Frame as an ML Problem

```
Core task: Ranking — given a user, rank all products by predicted
relevance/likelihood of interaction.

Not: multi-class classification (too many products to be a fixed class set)
Not: simple similarity (need personalization, not just "similar items")
```

---

## Step 3 — Data

```
Implicit feedback (most e-commerce data):
- Clicks, views, add-to-cart, purchases, time spent

Explicit feedback (rarer, valuable when available):
- Ratings, reviews

Data sources:
- User behavior logs (clickstream)
- Product catalog (category, price, description)
- User profile (demographics, if available)
```

---

## Step 4 — Feature Engineering

```
User features:
- Purchase history embedding
- Category preferences (% purchases per category)
- Recency/frequency/monetary value (RFM)

Product features:
- Category, price, popularity, embedding from description

Interaction features:
- User-product affinity score (collaborative filtering signal)
- Time since last interaction with similar products
```

---

## Step 5 — Model Selection & Training

### Two-Stage Architecture (Industry Standard)

```
Stage 1: CANDIDATE GENERATION (retrieval)
  Goal: narrow 1M products down to ~500 candidates, FAST
  Method: Collaborative filtering (matrix factorization) or
          two-tower neural network (user embedding · item embedding)

Stage 2: RANKING
  Goal: precisely rank the ~500 candidates
  Method: Gradient boosted trees (XGBoost) or deep ranking model
          using rich features (can afford to be slower/heavier here)
```

```
Why two stages?
Running a heavy, accurate model on ALL 1M products per user is too slow.
Candidate generation is fast+approximate, ranking is slow+precise —
combining them gives both speed and accuracy.
```

### Handling Cold Start

```
New user: recommend popular items / trending items until enough
          interaction data accumulates
New product: use content-based features (category, description
             embedding) until enough interaction data exists
```

---

## Step 6 — Evaluation

```
Offline metrics:
- Precision@K, Recall@K (did we recommend relevant items in top K?)
- NDCG (Normalized Discounted Cumulative Gain — rewards correct ORDER)

Online metrics (the ones that actually matter):
- Click-through rate (CTR)
- Conversion rate
- A/B test: new model vs current production model
```

---

## Step 7 — Deployment & Serving

```
Candidate generation: precomputed nightly (batch), stored in a
                       fast key-value store (Redis) per user

Ranking: real-time — happens when user loads the page,
         using cached candidates + live re-ranking

Architecture:
User request → Load precomputed candidates (Redis, <5ms)
             → Real-time ranking model (<50ms)
             → Return top 10 to frontend
```

---

## Step 8 — Monitoring & Maintenance

```
- Track CTR/conversion daily — alert if it drops
- Monitor for feedback loops (recommending only popular items
  makes them MORE popular, starving good but less-known products)
- Retrain candidate generation weekly, ranking model daily
  (ranking model needs to react faster to trending behavior)
```

---

## Step 9 — Scale & Trade-offs

```
At 10x scale (100M users):
- Candidate generation becomes the bottleneck → need approximate
  nearest neighbor search (FAISS!) instead of exact matrix factorization
- Consider sharding by user region for lower latency
```

---

## Key Takeaway

> Recommendation systems almost always use a two-stage architecture: fast approximate candidate generation, then precise ranking. This pattern directly reuses skills from RAG systems — candidate generation is conceptually the same problem as retrieval (find relevant items fast), and FAISS applies to both.
