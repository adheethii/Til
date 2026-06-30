# Python Virtual Environments

**Date:** 2026-06-30

## What is a Virtual Environment?

A virtual environment is an isolated Python environment — each project gets its own packages without conflicts.

```
Without venv: All projects share same packages → version conflicts 💥
With venv:    Each project has own packages → clean isolation ✅
```

---

## Why You Need It

```bash
# Project A needs scikit-learn 1.0
# Project B needs scikit-learn 1.4
# Without venv → one overwrites the other 💥
# With venv → both coexist perfectly ✅
```

---

## Creating and Using venv

```bash
# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (Mac/Linux)
source .venv/bin/activate

# You'll see (.venv) in terminal prompt ✅

# Install packages inside venv
pip install fastapi scikit-learn pandas

# Deactivate when done
deactivate
```

---

## requirements.txt

```bash
# Save current environment packages
pip freeze > requirements.txt

# Install from requirements.txt (on new machine or venv)
pip install -r requirements.txt
```

---

## .gitignore — Never Push venv

```
# .gitignore
.venv/
venv/
__pycache__/
*.pyc
.env
```

The venv folder is huge (hundreds of MBs) — never commit it. Share requirements.txt instead.

---

## Project Setup Workflow

```bash
# 1. Create project folder
mkdir my_project && cd my_project

# 2. Create venv
python -m venv .venv

# 3. Activate
source .venv/bin/activate   # or .venv\Scripts\activate on Windows

# 4. Install packages
pip install fastapi uvicorn scikit-learn pandas

# 5. Save dependencies
pip freeze > requirements.txt

# 6. Start coding!
```

---

## venv vs conda

| | venv | conda |
|--|------|-------|
| Built-in | ✅ Python standard | ❌ Separate install |
| Package manager | pip | conda + pip |
| Non-Python deps | ❌ | ✅ (e.g. CUDA) |
| Best for | Web/ML projects | Data science/GPU |

---

## Key Takeaway

> Always create a virtual environment for every project. Never install packages globally. Never commit the venv folder — share requirements.txt instead. This is professional Python development practice and prevents 90% of "it works on my machine" issues.
