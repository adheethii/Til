# Git Branching Basics

**Date:** 2026-07-02

## What is a Branch?

A branch is an independent line of development — you can work on a new feature or fix without affecting the main code.

```
main branch:    A → B → C → D
                         ↓
feature branch:          E → F → G
```

---

## Why Use Branches?

```
❌ Without branches: Everyone commits to main → conflicts, broken code
✅ With branches:    Each feature in its own branch → clean, safe workflow
```

---

## Basic Branch Commands

```bash
# See all branches
git branch

# Create new branch
git branch feature-login

# Switch to branch
git checkout feature-login

# Create AND switch in one command (modern way)
git checkout -b feature-login

# Even newer syntax
git switch -c feature-login
```

---

## Branch Workflow

```bash
# 1. Create branch for your feature
git checkout -b feature-add-prediction

# 2. Make changes and commit
git add .
git commit -m "feat: add churn prediction endpoint"

# 3. Push branch to GitHub
git push origin feature-add-prediction

# 4. Open Pull Request on GitHub
# 5. Review → Merge into main
# 6. Delete branch after merge
git branch -d feature-add-prediction
```

---

## Switching Between Branches

```bash
# Switch to main
git checkout main

# Switch to existing branch
git checkout feature-login

# See which branch you're on
git status
# → On branch feature-login
```

---

## Common Branch Naming Conventions

```
feature/add-user-auth     ← new features
fix/login-bug             ← bug fixes
docs/update-readme        ← documentation
refactor/clean-api        ← code cleanup
chore/update-deps         ← maintenance
```

---

## Key Takeaway

> Branches keep your main code safe while you experiment. Always create a new branch for each feature or fix — never commit experimental code directly to main. The workflow is: branch → develop → PR → merge → delete branch.
