# XGBoost Explained

**Date:** 2026-07-10

## What is XGBoost?

XGBoost (Extreme Gradient Boosting) is an optimized gradient boosting algorithm — one of the most powerful and widely used ML algorithms for structured/tabular data.

```
Random Forest → parallel trees (bagging)
XGBoost       → sequential trees (boosting) + regularization + speed
```

---

## How it Works

```
1. Start with a simple prediction (mean of target)
2. Calculate residuals (errors)
3. Train a tree to predict the residuals
4. Add tree to model (scaled by learning rate)
5. Recalculate residuals
6. Repeat until n_estimators trees built
7. Final prediction = sum of all trees
```

---

## Implementation

```python
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

model = XGBClassifier(
    n_estimators=100,       # number of trees
    max_depth=6,            # tree depth
    learning_rate=0.1,      # shrinkage — smaller = more conservative
    subsample=0.8,          # fraction of samples per tree
    colsample_bytree=0.8,   # fraction of features per tree
    use_label_encoder=False,
    eval_metric="logloss",
    random_state=42
)

model.fit(
    X_train, y_train,
    eval_set=[(X_test, y_test)],  # monitor test performance
    early_stopping_rounds=10,      # stop if no improvement
    verbose=False
)

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
```

---

## Key Hyperparameters

| Parameter | Effect |
|-----------|--------|
| `n_estimators` | More trees = better but slower |
| `max_depth` | 3-6 typical — deeper = more complex |
| `learning_rate` | 0.01-0.3 — smaller = more robust |
| `subsample` | Fraction of rows per tree — prevents overfitting |
| `colsample_bytree` | Fraction of columns per tree |
| `reg_alpha` | L1 regularization |
| `reg_lambda` | L2 regularization |

---

## XGBoost vs Random Forest

| | Random Forest | XGBoost |
|--|--------------|---------|
| Training | Parallel | Sequential |
| Method | Bagging | Boosting |
| Speed | Fast | Slower but faster than sklearn GBM |
| Accuracy | Good | Usually better |
| Overfitting | Less prone | More prone (tune carefully) |
| Handles missing | ❌ | ✅ Built-in |

---

## Feature Importance

```python
import matplotlib.pyplot as plt
from xgboost import plot_importance

plot_importance(model, max_num_features=10)
plt.show()

# Or as DataFrame
importance_df = pd.DataFrame({
    "feature": X.columns,
    "importance": model.feature_importances_
}).sort_values("importance", ascending=False)
```

---

## Key Takeaway

> XGBoost wins most Kaggle tabular competitions for a reason — it combines gradient boosting with regularization, handles missing values natively, and is highly optimized for speed. Always try XGBoost after Random Forest — it usually gives better accuracy with proper tuning.
