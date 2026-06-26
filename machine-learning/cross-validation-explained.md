# Cross-Validation Explained

**Date:** 2026-06-26

## What is Cross-Validation?

Cross-validation reliably evaluates model performance by testing on multiple splits — not just one.

```
Single split: Train 80%, test 20% → one score (unreliable)
Cross-validation: 5 different splits → 5 scores → average (reliable)
```

---

## K-Fold Cross-Validation

```
Fold 1: [TEST] [train] [train] [train] [train]
Fold 2: [train] [TEST] [train] [train] [train]
Fold 3: [train] [train] [TEST] [train] [train]
...
Final score = average of all fold scores
```

---

## Implementation

```python
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
import numpy as np

model = RandomForestClassifier(n_estimators=100)

# Stratified — keeps class distribution in each fold
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=skf, scoring="f1")

print(f"F1 scores: {scores}")
print(f"Mean F1: {scores.mean():.3f} ± {scores.std():.3f}")
```

---

## CV vs Single Split

| | Single Split | Cross-Validation |
|--|-------------|-----------------|
| Reliability | Low | High |
| Data usage | 80% train | ~100% used |
| Speed | Fast | Slower |

---

## Key Takeaway

> Cross-validation gives a reliable performance estimate. Use StratifiedKFold for imbalanced classification. Low standard deviation across folds means consistent model — high std means it's sensitive to data splits.
