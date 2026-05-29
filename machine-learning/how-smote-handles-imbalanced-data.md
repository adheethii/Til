# How SMOTE Handles Imbalanced Data

**Date:** 2026-05-29

## What is Class Imbalance?

In many real-world datasets, one class has far fewer samples than the other.

Example — Telecom Churn:
- 85% customers → Not churned
- 15% customers → Churned ← minority class

A model trained on this will just predict "Not churned" for everything and still get 85% accuracy — but it's useless.

---

## What is SMOTE?

**SMOTE = Synthetic Minority Oversampling Technique**

Instead of just duplicating minority class samples, SMOTE **creates brand new synthetic samples** by interpolating between existing minority samples.

---

## How It Works

```
1. Pick a minority class sample (point A)
2. Find its k nearest neighbours (also minority class)
3. Pick one neighbour randomly (point B)
4. Create a new synthetic point somewhere between A and B

New point = A + random(0,1) × (B - A)
```

```
Before SMOTE:          After SMOTE:
● ● ● ● ● ●           ● ● ● ● ● ●   (majority)
○                      ○ ○ ○ ○ ○ ○   (minority + synthetic)
```

---

## Code Example

```python
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Apply SMOTE only on training data — never on test data!
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

print(f"Before: {y_train.value_counts().to_dict()}")
print(f"After:  {y_resampled.value_counts().to_dict()}")
```

---

## Important Rules

| Rule | Why |
|------|-----|
| Apply SMOTE only on training data | Applying on test data causes data leakage |
| Use F1/ROC-AUC for evaluation | Accuracy is misleading on imbalanced data |
| Try different k values | Default k=5, but tune for your dataset |

---

## SMOTE vs Other Techniques

| Technique | How | Downside |
|-----------|-----|----------|
| Random Oversampling | Duplicate minority samples | Overfitting |
| **SMOTE** | Synthesize new minority samples | Can create noisy samples |
| Random Undersampling | Remove majority samples | Loses data |
| Class Weights | Penalise misclassification | No new data created |

---

## What I Applied

Used SMOTE in my [Telecom Customer Churn](https://github.com/adheethii/Telecom-customer-churn) project — churn data was heavily imbalanced, so SMOTE was applied on training data before fitting the model, which significantly improved recall for the minority (churned) class.

---

## Key Takeaway

> SMOTE doesn't duplicate — it interpolates. Always apply it after the train-test split, never before. Pair it with F1 or ROC-AUC for honest evaluation.
