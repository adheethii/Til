# Python OOP Basics

**Date:** 2026-07-08

## What is OOP?

Object-Oriented Programming organises code into **classes** — blueprints for objects that bundle data (attributes) and behaviour (methods) together.

```
Class  → Blueprint (like a template)
Object → Instance of a class (actual thing)
```

---

## Basic Class

```python
class MLModel:
    # Class attribute (shared by all instances)
    framework = "scikit-learn"

    # Constructor
    def __init__(self, name, version):
        # Instance attributes
        self.name = name
        self.version = version
        self.is_trained = False

    # Instance method
    def train(self, X, y):
        self.is_trained = True
        print(f"{self.name} v{self.version} trained!")

    def predict(self, X):
        if not self.is_trained:
            raise ValueError("Model not trained yet!")
        return f"Predictions from {self.name}"

    # String representation
    def __repr__(self):
        return f"MLModel(name={self.name}, version={self.version})"


# Create objects
model1 = MLModel("RandomForest", "1.0")
model2 = MLModel("LogisticRegression", "2.0")

model1.train(X_train, y_train)
print(model1.predict(X_test))
print(model1)   # → MLModel(name=RandomForest, version=1.0)
```

---

## Inheritance

```python
class BaseModel:
    def __init__(self, name):
        self.name = name
        self.is_trained = False

    def train(self, X, y):
        self.is_trained = True

    def evaluate(self, X, y):
        raise NotImplementedError("Subclass must implement evaluate()")


class ChurnModel(BaseModel):
    def __init__(self, threshold=0.5):
        super().__init__("ChurnPredictor")   # call parent __init__
        self.threshold = threshold

    def evaluate(self, X, y):
        # Custom evaluation for churn
        predictions = self.predict(X)
        return f1_score(y, predictions)

    def predict_churn_risk(self, X):
        proba = self.predict_proba(X)
        return ["High" if p > self.threshold else "Low" for p in proba]
```

---

## The 4 Pillars of OOP

| Pillar | Description | Example |
|--------|-------------|---------|
| **Encapsulation** | Bundle data + methods, hide internals | `self._private_attr` |
| **Inheritance** | Child class inherits from parent | `class ChurnModel(BaseModel)` |
| **Polymorphism** | Same interface, different behaviour | `model.predict()` works for any model |
| **Abstraction** | Hide complexity, show only what's needed | `model.train(X, y)` hides the math |

---

## Special Methods (Dunder Methods)

```python
class Dataset:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)          # len(dataset)

    def __getitem__(self, idx):
        return self.data[idx]          # dataset[0]

    def __repr__(self):
        return f"Dataset({len(self.data)} samples)"  # print(dataset)

    def __contains__(self, item):
        return item in self.data       # item in dataset
```

---

## Key Takeaway

> OOP organises code into reusable, logical units. Classes bundle related data and behaviour. Inheritance avoids code repetition. In ML, OOP is everywhere — sklearn models all follow the same fit/predict interface (polymorphism). Understanding OOP is essential for reading and contributing to any ML library.
