# Git Merging and Merge Conflicts

**Date:** 2026-07-02

## What is Merging?

Merging combines changes from one branch into another.

```
main:    A → B → C
                  ↘
feature:  D → E → MERGE → F (merged result)
```

---

## Types of Merges

### Fast-Forward Merge (no conflicts)
```bash
git checkout main
git merge feature-branch
# → "Fast-forward" — no conflict, linear history
```

### 3-Way Merge (branches diverged)
```bash
git checkout main
git merge feature-branch
# → Creates a merge commit combining both branches
```

---

## Merge Commands

```bash
# Switch to the branch you want to merge INTO
git checkout main

# Merge feature branch into main
git merge feature-add-prediction

# Delete branch after successful merge
git branch -d feature-add-prediction
```

---

## What is a Merge Conflict?

A conflict happens when **two branches changed the same line** of the same file — Git doesn't know which version to keep.

```
main branch:    result = model.predict(X)
feature branch: result = model.predict_proba(X)

→ CONFLICT — which line to keep?
```

---

## Resolving Merge Conflicts

```bash
# After running git merge and getting conflict:
git status
# → both modified: main.py

# Open the conflicted file — you'll see:
<<<<<<< HEAD (current branch — main)
result = model.predict(X)
=======
result = model.predict_proba(X)
>>>>>>> feature-add-prediction
```

**Manually edit the file** — keep what you want:
```python
# Keep both (or choose one):
prediction = model.predict(X)
probability = model.predict_proba(X)
```

Then:
```bash
# Mark as resolved
git add main.py

# Complete the merge
git commit -m "merge: resolve conflict in main.py"
```

---

## Avoiding Conflicts

```bash
# Before merging — update your branch with latest main
git checkout feature-branch
git pull origin main      # get latest changes from main

# Now merge is cleaner
git checkout main
git merge feature-branch
```

---

## Key Takeaway

> Merge conflicts happen when two branches edit the same line. Git marks conflicts with <<< === >>> markers — you manually choose what to keep, then git add and git commit to complete the merge. Pull from main regularly to minimise conflicts.
