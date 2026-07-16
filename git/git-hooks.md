# Git Hooks

**Date:** 2026-07-15

## What are Git Hooks?

Git hooks are scripts that run automatically at specific points in the Git workflow — like "before commit" or "before push" — used to enforce quality checks.

```
git commit → [pre-commit hook runs] → commit created
git push   → [pre-push hook runs]   → push happens
```

---

## Where Hooks Live

```
.git/hooks/
├── pre-commit.sample
├── pre-push.sample
├── commit-msg.sample
└── ...

# Rename by removing .sample to activate
```

---

## Common Hook Types

| Hook | Runs When | Common Use |
|------|-----------|------------|
| `pre-commit` | Before commit is created | Run linter, formatter, tests |
| `commit-msg` | After message is written | Enforce commit message format |
| `pre-push` | Before push to remote | Run full test suite |
| `post-merge` | After a merge completes | Reinstall dependencies |

---

## Simple Pre-commit Hook Example

```bash
#!/bin/sh
# .git/hooks/pre-commit

echo "Running tests before commit..."
python -m pytest tests/

if [ $? -ne 0 ]; then
    echo "❌ Tests failed. Commit aborted."
    exit 1
fi

echo "✅ Tests passed!"
exit 0
```

Make it executable:
```bash
chmod +x .git/hooks/pre-commit
```

---

## Enforcing Commit Message Format

```bash
#!/bin/sh
# .git/hooks/commit-msg

commit_msg=$(cat "$1")
pattern="^(feat|fix|docs|refactor|test|chore):"

if ! echo "$commit_msg" | grep -qE "$pattern"; then
    echo "❌ Commit message must start with feat/fix/docs/refactor/test/chore:"
    exit 1
fi
```

---

## The Problem — Hooks Aren't Shared via Git

Since `.git/hooks/` isn't tracked by Git itself, hooks don't automatically apply to teammates who clone your repo.

**Solution: Use a tool like `pre-commit` (Python package)**

```bash
pip install pre-commit
```

```yaml
# .pre-commit-config.yaml (this file IS tracked in git)
repos:
  - repo: https://github.com/psf/black
    rev: 23.1.0
    hooks:
      - id: black
  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
```

```bash
pre-commit install   # sets up the actual git hook
# Now every commit automatically runs black + flake8
```

---

## Key Takeaway

> Git hooks automate quality checks at key workflow points. Raw hooks in `.git/hooks/` aren't shared with teammates — use the `pre-commit` framework with a tracked `.pre-commit-config.yaml` for team-wide enforcement. Essential for maintaining code quality automatically, without relying on developers remembering to run checks manually.
