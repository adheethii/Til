# Random Forest Explained

**Date:** 2026-06-26

## What is Random Forest?

Random Forest is an ensemble method that builds **many decision trees** and combines their predictions — reducing overfitting and improving accuracy.

```
Single Decision Tree → overfits, unstable
Random Forest (100 trees) → stable, accurate, robust
```

---

## How it Works

```
1. Create N decision trees (e.g. 100 trees)
2. Each tree trained on a random subset of data (bootstrap sampling)
3. Each split uses a random subset of features
4. For classification → majority vote across all trees
5. For regression → average of all tree predictions
```

---

## Implementation

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier(
    n_estimators=100,      # number of trees
    max_depth=None,        # let trees grow fully
    min_samples_split=2,
    random_state=42
)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))
```

---

## Feature Importance

```python
import pandas as pd

# Which features matter most?
importance = pd.DataFrame({
    "feature": X.columns,
    "importance": model.feature_importances_
}).sort_values("importance", ascending=False)

print(importance.head(10))
```

---

## Key Hyperparameters

| Parameter | Effect |
|-----------|--------|
| `n_estimators` | More trees = better but slower |
| `max_depth` | Deeper = more complex = risk of overfitting |
| `max_features` | Features per split — `sqrt` for classification |
| `min_samples_leaf` | Minimum samples in leaf — controls overfitting |

---

## What I Applied

Used Random Forest in my [Telecom Customer Churn](https://github.com/adheethii/Telecom-customer-churn) project — it outperformed logistic regression due to its ability to capture non-linear relationships between features like tenure, contract type, and monthly charges.

---

## Key Takeaway

> Random Forest reduces overfitting by averaging many trees trained on random data subsets. Always check feature_importances_ — it tells you which features actually drive predictions. Start with n_estimators=100 and tune from there.
