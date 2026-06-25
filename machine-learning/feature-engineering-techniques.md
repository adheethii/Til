# Feature Engineering Techniques

**Date:** 2026-06-25

## What is Feature Engineering?

Feature engineering is the process of **transforming raw data into features that better represent the problem** to the ML model — often more impactful than choosing the algorithm.

```
Raw data → Feature Engineering → Better features → Better model
```

---

## Common Techniques

### 1. Handling Missing Values

```python
import pandas as pd
from sklearn.impute import SimpleImputer

df = pd.DataFrame({"age": [25, None, 30], "salary": [50000, 60000, None]})

# Fill with mean
imputer = SimpleImputer(strategy="mean")
df_imputed = imputer.fit_transform(df)

# Or fill manually
df["age"].fillna(df["age"].median(), inplace=True)
```

### 2. Encoding Categorical Variables

```python
# Label Encoding (for ordinal data)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df["contract"] = le.fit_transform(df["contract"])
# Month-to-month=0, One year=1, Two year=2

# One-Hot Encoding (for nominal data)
df = pd.get_dummies(df, columns=["gender", "payment_method"])
```

### 3. Feature Scaling

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# StandardScaler — mean=0, std=1 (best for most ML models)
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[["tenure", "monthly_charges"]])

# MinMaxScaler — scales to 0-1 range
minmax = MinMaxScaler()
df_minmax = minmax.fit_transform(df[["tenure", "monthly_charges"]])
```

### 4. Creating New Features

```python
# Combine existing features
df["charge_per_month"] = df["total_charges"] / df["tenure"]

# Binning continuous variables
df["tenure_group"] = pd.cut(df["tenure"],
    bins=[0, 12, 24, 48, 72],
    labels=["0-1yr", "1-2yr", "2-4yr", "4+yr"])

# Extracting from datetime
df["month"] = pd.to_datetime(df["date"]).dt.month
df["day_of_week"] = pd.to_datetime(df["date"]).dt.dayofweek
```

---

## What I Applied

Used these techniques in my [Telecom Customer Churn](https://github.com/adheethii/Telecom-customer-churn) project — encoding contract types, scaling tenure and charges, and creating ratio features that improved model performance.

---

## Key Takeaway

> Feature engineering often matters more than algorithm choice. Always handle missing values, encode categoricals, scale numerics, and consider creating new features from existing ones. Fit transformers on training data only — never on test data.
