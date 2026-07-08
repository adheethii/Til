# Logistic Regression Explained

**Date:** 2026-07-08

## What is Logistic Regression?

Despite the name, logistic regression is a **classification** algorithm — not regression. It predicts the probability that an input belongs to a class.

```
Linear Regression  → predicts continuous values (price, temperature)
Logistic Regression → predicts probability (0 to 1) → classification
```

---

## How it Works

```
Input features → Linear combination → Sigmoid function → Probability → Class
```

### Sigmoid Function

```
σ(z) = 1 / (1 + e^(-z))

Output always between 0 and 1:
z → -∞ : σ(z) → 0
z = 0  : σ(z) = 0.5
z → +∞ : σ(z) → 1
```

### Decision Boundary

```
P(y=1) >= 0.5 → predict class 1
P(y=1) <  0.5 → predict class 0
```

---

## Implementation

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.preprocessing import StandardScaler

# Preprocessing — logistic regression needs scaled features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train
model = LogisticRegression(
    C=1.0,              # regularization strength (smaller = more regularization)
    max_iter=1000,      # increase if model doesn't converge
    random_state=42
)
model.fit(X_train_scaled, y_train)

# Predict
y_pred = model.predict(X_test_scaled)
y_prob = model.predict_proba(X_test_scaled)[:, 1]   # probability of class 1

print(classification_report(y_test, y_pred))
print(f"ROC-AUC: {roc_auc_score(y_test, y_prob):.3f}")
```

---

## Key Hyperparameters

| Parameter | Effect |
|-----------|--------|
| `C` | Inverse of regularization — smaller = more regularized |
| `penalty` | l1 (Lasso) or l2 (Ridge) regularization |
| `max_iter` | Increase if ConvergenceWarning appears |
| `solver` | Algorithm — `lbfgs` default, `saga` for large datasets |

---

## Logistic Regression vs Random Forest

| | Logistic Regression | Random Forest |
|--|---------------------|---------------|
| Interpretability | ✅ High | ❌ Low (black box) |
| Non-linear patterns | ❌ No | ✅ Yes |
| Speed | ✅ Fast | Slower |
| Feature scaling | Required | Not required |
| Best for | Linearly separable data | Complex patterns |

---

## What I Applied

Used logistic regression as a baseline in my [Telecom Customer Churn](https://github.com/adheethii/Telecom-customer-churn) project before switching to Random Forest — it's always good practice to start with a simple interpretable model.

---

## Key Takeaway

> Logistic regression is the go-to baseline for binary classification. Always scale features first. Use C to control regularization. Despite being "simple", it's highly interpretable and often competitive with complex models on linearly separable data.
