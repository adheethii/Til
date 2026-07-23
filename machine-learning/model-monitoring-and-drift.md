# Model Monitoring and Drift Detection

**Date:** 2026-07-23

## Why Models Need Monitoring After Deployment

A model that performs well at launch can silently degrade over time —
without monitoring, you often only find out when the business metric
(revenue, conversion) has already dropped.

```
Model trained on Jan 2026 data → deployed → world changes →
model still runs, still returns predictions, but they're
increasingly WRONG → nobody notices until it's a real problem
```

---

## Two Types of Drift

### Data Drift (a.k.a. Feature Drift / Covariate Shift)

```
The INPUT distribution changes — the features look different
than what the model was trained on.

Example: A churn model trained pre-pandemic sees very different
customer behavior patterns post-pandemic — same features,
different distribution.
```

### Concept Drift

```
The RELATIONSHIP between features and target changes — even if
inputs look the same, what they PREDICT has changed.

Example: "High monthly charges" used to predict churn strongly.
After a pricing restructure, high charges might correlate with
premium loyal customers instead — same feature, opposite meaning.
```

---

## Detecting Data Drift

```python
from scipy.stats import ks_2samp

# Compare distribution of a feature: training data vs recent production data
def detect_drift(training_feature, production_feature, threshold=0.05):
    statistic, p_value = ks_2samp(training_feature, production_feature)
    drift_detected = p_value < threshold
    return drift_detected, p_value

# Example: check if tenure distribution has shifted
drift_found, p_val = detect_drift(
    train_df["tenure"],
    recent_prod_df["tenure"]
)
if drift_found:
    print(f"⚠️ Drift detected in 'tenure' feature (p={p_val:.4f})")
```

**Population Stability Index (PSI)** — another common metric:
```
PSI < 0.1  → no significant drift
PSI 0.1-0.25 → moderate drift, monitor closely
PSI > 0.25 → significant drift, investigate/retrain
```

---

## Detecting Concept Drift

```
Harder to detect directly (requires ground truth labels, which
often arrive late — e.g., "did they actually churn" takes weeks
to confirm).

Common approach: monitor the model's PREDICTION distribution
over time, even without labels yet:

- Is the % predicted "High risk" suddenly very different
  from historical baseline?
- Are prediction confidence scores shifting?
```

---

## What to Monitor in Production

```
Input monitoring:
- Feature distributions (mean, std, missing value rate)
- Schema violations (unexpected categories, out-of-range values)

Output monitoring:
- Prediction distribution (% positive class over time)
- Confidence/probability score distribution
- Latency (p50, p95, p99 response times)

Business monitoring (the metrics that actually matter):
- Actual outcome vs predicted (once labels arrive)
- Business KPI the model is supposed to improve
```

---

## Setting Up Alerts

```python
def check_prediction_distribution(predictions, baseline_positive_rate=0.15, tolerance=0.05):
    current_rate = sum(predictions) / len(predictions)

    if abs(current_rate - baseline_positive_rate) > tolerance:
        send_alert(
            f"Prediction rate shifted: {current_rate:.2%} "
            f"vs baseline {baseline_positive_rate:.2%}"
        )
```

---

## Retraining Triggers

```
Schedule-based: retrain weekly/monthly regardless (simple, safe default)

Performance-based: retrain when a monitored metric crosses
                    a threshold (more efficient, needs good monitoring)

Drift-based: retrain when PSI or KS-test flags significant
             distribution shift (proactive, catches issues early)
```

---

## Key Takeaway

> Monitoring is what separates a deployed model from a production-ready ML system. Data drift = inputs changed; concept drift = the relationship changed (harder to catch, needs delayed ground truth). Track feature distributions and prediction distributions continuously, and always have a defined retraining trigger — schedule-based at minimum, drift-based ideally.
