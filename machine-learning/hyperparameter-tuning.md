# Hyperparameter Tuning

**Date:** 2026-06-27

## What are Hyperparameters?

Hyperparameters are settings you choose **before** training — they control how the model learns.

```
Parameters    → learned during training (weights)
Hyperparameters → set before training (learning rate, n_estimators)
```

---

## Why Tune?

Default hyperparameters rarely give the best results. Tuning finds the combination that maximises your metric (F1, accuracy, AUC).

---

## Grid Search

Tries every combination — exhaustive but slow:

```python
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 10, 20],
    "min_samples_split": [2, 5, 10]
}

model = RandomForestClassifier(random_state=42)

grid_search = GridSearchCV(
    model,
    param_grid,
    cv=5,
    scoring="f1",
    n_jobs=-1,      # use all CPU cores
    verbose=1
)

grid_search.fit(X_train, y_train)

print(f"Best params: {grid_search.best_params_}")
print(f"Best F1: {grid_search.best_score_:.3f}")
```

---

## Random Search

Tries random combinations — faster, often just as good:

```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint

param_dist = {
    "n_estimators": randint(50, 300),
    "max_depth": [None, 10, 20, 30],
    "min_samples_split": randint(2, 20)
}

random_search = RandomizedSearchCV(
    model,
    param_distributions=param_dist,
    n_iter=20,          # try 20 random combinations
    cv=5,
    scoring="f1",
    random_state=42
)

random_search.fit(X_train, y_train)
print(f"Best params: {random_search.best_params_}")
```

---

## Grid Search vs Random Search

| | Grid Search | Random Search |
|--|-------------|--------------|
| Tries | All combinations | Random subset |
| Speed | Slow | Fast |
| Best for | Small param space | Large param space |

---

## What I Applied

Used GridSearchCV on my [Telecom Customer Churn](https://github.com/adheethii/Telecom-customer-churn) Random Forest model — tuning n_estimators and max_depth improved F1 score from 0.78 to 0.84.

---

## Key Takeaway

> Always tune hyperparameters — defaults are rarely optimal. Use GridSearch for small spaces, RandomSearch for large ones. Always tune using cross-validation (cv=5) to avoid overfitting to the validation set.
