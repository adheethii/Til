# GitHub Workflow Best Practices

**Date:** 2026-07-04

## The Standard GitHub Flow

```
main (always deployable)
  ↓
Create feature branch
  ↓
Develop + commit
  ↓
Push branch
  ↓
Open Pull Request
  ↓
Code review
  ↓
Merge to main
  ↓
Delete branch
  ↓
Deploy
```

---

## Good Commit Messages

Follow the **Conventional Commits** standard:

```bash
# Format: type(scope): description

# Types:
feat:     # new feature
fix:      # bug fix
docs:     # documentation only
refactor: # code restructure (no feature/fix)
chore:    # maintenance (deps, config)
test:     # adding tests
ci:       # CI/CD changes

# Examples:
git commit -m "feat: add churn prediction endpoint"
git commit -m "fix: resolve face encoding crash on empty image"
git commit -m "docs: update README with architecture diagram"
git commit -m "refactor: extract retriever into separate module"
git commit -m "chore: update requirements.txt"
```

---

## .gitignore Best Practices

```gitignore
# Python
__pycache__/
*.pyc
*.pyo
.venv/
venv/
*.egg-info/

# Environment
.env
.env.local

# ML Models (large files)
*.pkl
*.h5
*.pt
models/

# Data files
data/raw/
*.csv
*.xlsx

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Docker
.docker/
```

---

## GitHub Issues

Use issues to track work — even on solo projects:

```
Bug report:
Title: "Face recognition fails on dark images"
Body: Steps to reproduce, expected vs actual, screenshots

Feature request:
Title: "Add Docker deployment support"
Body: Why needed, proposed solution, acceptance criteria
```

```bash
# Reference issues in commits
git commit -m "fix: handle dark image preprocessing (closes #5)"
# → automatically closes issue #5 when merged!
```

---

## README Best Practices

Every repo should have:

```markdown
# Project Name
Brief description (1-2 lines)

## 🎯 What it Does
Clear explanation of the problem solved

## 🛠️ Tech Stack
List of technologies + why

## 🚀 Getting Started
Step by step setup instructions

## 📸 Demo / Screenshots
Visual proof it works

## 🏗️ Architecture
How components connect

## 🔜 Future Improvements
Shows you think beyond the current state
```

---

## Protecting Main Branch

In team settings — protect main from direct pushes:

```
GitHub repo → Settings → Branches → Add rule
→ Branch name: main
→ ✅ Require pull request before merging
→ ✅ Require approvals: 1
→ ✅ Dismiss stale pull request approvals
```

---

## GitHub Actions (CI/CD Basics)

```yaml
# .github/workflows/test.yml
name: Run Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: "3.10"
      - run: pip install -r requirements.txt
      - run: pytest tests/
```

This runs your tests automatically on every push and PR!

---

## Key Takeaway

> Professional GitHub workflow = feature branches + conventional commits + PRs + issues. Even on solo projects, follow this workflow — it demonstrates professional habits to recruiters and makes your commit history readable and impressive.
