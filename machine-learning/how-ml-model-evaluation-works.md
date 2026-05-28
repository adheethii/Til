# How ML Model Evaluation Works

**Date:** 2026-05-28

## Why Evaluation Matters

Training a model is only half the job. Evaluation tells you **how well your model actually performs** on unseen data — and whether it's ready for real use.

---

## The Key Metrics

### For Classification Problems

| Metric | What it Measures | Best When |
|--------|-----------------|-----------|
| Accuracy | % of correct predictions | Classes are balanced |
| Precision | Of predicted positives, how many are actually positive | False positives are costly |
| Recall | Of actual positives, how many were caught | False negatives are costly |
| F1 Score | Balance between Precision and Recall | Imbalanced classes |
| ROC-AUC | Model's ability to distinguish classes | Overall performance comparison |

### For Regression Problems

| Metric | What it Measures |
|--------|-----------------|
| MAE | Average absolute error |
| MSE | Penalises large errors more |
| RMSE | Same as MSE but in original units |
| R² Score | How much variance the model explains |

---

## Confusion Matrix (Classification)

```
                 Predicted
                 Pos    Neg
Actual  Pos  [  TP  |  FN  ]
        Neg  [  FP  |  TN  ]

Accuracy  = (TP + TN) / Total
Precision = TP / (TP + FP)
Recall    = TP / (TP + FN)
F1        = 2 * (Precision * Recall) / (Precision + Recall)
```

---

## Train / Validation / Test Split

```python
from sklearn.model_selection import train_test_split

# Split into 70% train, 15% val, 15% test
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5)
```

Never evaluate on training data — it gives falsely high scores.

---

## Cross Validation

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5, scoring='f1')
print(f"F1: {scores.mean():.2f} ± {scores.std():.2f}")
```

Cross validation gives a more reliable estimate by testing across multiple data splits.

---

## Overfitting vs Underfitting

| Situation | Train Score | Test Score | Fix |
|-----------|-------------|------------|-----|
| Overfitting | High | Low | More data, regularization, simpler model |
| Underfitting | Low | Low | More features, complex model |
| Good fit | High | High | ✅ |

---

## What I Applied

Used these evaluation techniques in my [Telecom Customer Churn](https://github.com/adheethii/Telecom-customer-churn) project — evaluated with F1 score and ROC-AUC due to class imbalance in churn data, and used SMOTE to handle the imbalance before evaluation.

---

## Key Takeaway

> Always evaluate on unseen data. For imbalanced datasets, F1 and ROC-AUC are more meaningful than accuracy. Cross-validation gives a fairer picture than a single train-test split.
