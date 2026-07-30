# Precision-Recall Trade-off and PR-AUC

**Date:** 2026-07-29

## Why This Note Now

Today's fraud detection system design note leaned on "Precision-Recall
AUC is more informative than ROC-AUC on imbalanced problems" without
fully unpacking why — worth actually working through that claim
properly rather than leaving it as an assertion.

---

## Precision vs Recall — The Core Trade-off

```
Precision = TP / (TP + FP)
"Of everything I FLAGGED as positive, how much was actually positive?"

Recall = TP / (TP + FN)
"Of everything that WAS actually positive, how much did I catch?"

These two pull against each other:
- Flag EVERYTHING as fraud → Recall = 100% (caught it all),
  Precision = terrible (mostly false alarms)
- Flag NOTHING as fraud → Precision = undefined/meaningless,
  Recall = 0% (caught nothing)
```

---

## Why This Matters More Under Class Imbalance

```
Imagine 10,000 transactions, only 20 are actually fraud (0.2%).

A model predicting "not fraud" for ALL 10,000 transactions:
- Accuracy = 9,980 / 10,000 = 99.8% — looks GREAT
- Recall = 0 / 20 = 0% — caught ZERO fraud, completely useless
- Precision = undefined (never predicted positive at all)

This is exactly why accuracy is the wrong metric on imbalanced
problems — a trivially useless model scores almost perfectly on it.
```

---

## Why PR-AUC Beats ROC-AUC Specifically Here

```
ROC curve plots: True Positive Rate vs False Positive Rate
PR curve plots:  Precision vs Recall

The key difference: False Positive Rate = FP / (FP + TN)

With 9,980 negative examples and only 20 positive, TN is HUGE.
Even a fairly large number of false positives barely moves FPR,
because it's divided by a massive TN. This makes ROC-AUC look
artificially good even when precision is genuinely poor.

PR-AUC doesn't have this problem — Precision is FP / (TP + FP),
with no TN term to dilute the effect of false positives. This
is why PR-AUC gives a more honest picture specifically when the
negative class vastly outnumbers the positive class.
```

---

## Working This Through With Numbers

```
Same 10,000 transactions, 20 actual fraud cases.
Model flags 100 transactions as fraud, correctly catching 15 of
the 20 real fraud cases (15 TP, 85 FP, 5 FN, 9,895 TN).

Precision = 15 / (15 + 85) = 15%   ← quite poor, most flags are wrong
Recall    = 15 / (15 + 5)  = 75%   ← caught most of the real fraud

FPR = 85 / (85 + 9,895) = 0.85%   ← looks tiny, barely registers on ROC

The same 85 false positives look "barely worth mentioning" on
an ROC curve (0.85% FPR) but are clearly a real problem on a
PR curve (only 15% precision) — this is the concrete version of
the abstract claim above.
```

---

## Choosing an Operating Point — Precision at Fixed Recall

```
Rather than picking a single threshold, plot Precision vs Recall
across ALL possible thresholds, then pick based on the real
business trade-off named in the fraud detection design (Step 1):

"At 90% recall (catching 90% of real fraud), what precision do
we get?" — directly answerable from the PR curve, and directly
maps back to a business conversation about acceptable false-alarm
rates, rather than an abstract "AUC = 0.94" number.
```

```python
from sklearn.metrics import precision_recall_curve, average_precision_score

precisions, recalls, thresholds = precision_recall_curve(y_true, y_scores)
pr_auc = average_precision_score(y_true, y_scores)

# Find precision at a specific recall target, e.g. recall >= 0.90
import numpy as np
target_recall = 0.90
idx = np.argmin(np.abs(recalls - target_recall))
print(f"At recall={recalls[idx]:.2f}, precision={precisions[idx]:.2f}")
```

---

## F1 Score — A Single-Number Compromise

```
F1 = 2 * (Precision * Recall) / (Precision + Recall)

Useful as a single summary number, but it implicitly assumes
precision and recall matter EQUALLY — which often isn't true
(fraud detection usually cares more about recall; a spam filter
usually cares more about precision). F-beta generalizes this
with a weight, but the PR curve itself is more informative than
collapsing to any single number when the trade-off genuinely
depends on business context.
```

---

## Key Takeaway

> On imbalanced problems, ROC-AUC can look deceptively good because False Positive Rate is diluted by a huge true-negative count — PR-AUC avoids this because Precision has no TN term to dilute it. The concrete number-walkthrough above (85 false positives reading as "0.85% FPR" but "only 15% precision") is worth being able to reproduce from memory in an interview, not just cite as a rule.
