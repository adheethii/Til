# Pull Requests (PRs) Explained

**Date:** 2026-07-04

## What is a Pull Request?

A Pull Request (PR) is a way to propose changes — you ask the team to **review and merge** your branch into the main codebase.

```
Your branch → Open PR → Code review → Approved → Merged into main
```

PRs are the standard collaborative workflow in professional software development.

---

## Why PRs Matter

```
❌ Without PRs: Everyone pushes directly to main → broken code, no review
✅ With PRs:    Changes reviewed before merging → quality control, collaboration
```

---

## Creating a PR on GitHub

```bash
# 1. Create and switch to a new branch
git checkout -b feature-add-prediction-api

# 2. Make changes and commit
git add .
git commit -m "feat: add churn prediction FastAPI endpoint"

# 3. Push branch to GitHub
git push origin feature-add-prediction-api

# 4. Go to GitHub → you'll see "Compare & pull request" button
# 5. Click it → add title and description → Create pull request
```

---

## Good PR Description Template

```markdown
## What this PR does
Adds a FastAPI endpoint for churn prediction that accepts customer
data and returns churn probability.

## Changes made
- Added /predict POST endpoint in main.py
- Added CustomerData Pydantic model for input validation
- Added /health GET endpoint for monitoring

## How to test
1. Run: uvicorn main:app --reload
2. Go to http://localhost:8000/docs
3. Test /predict with sample customer data

## Related issue
Closes #12
```

---

## PR Review Process

```
1. Open PR → assign reviewers
2. Reviewers leave comments on specific lines
3. You respond to comments / make changes
4. Push new commits → PR updates automatically
5. Reviewer approves ✅
6. Merge into main
7. Delete branch
```

---

## PR on Your Own Repos (Solo Workflow)

Even working alone, PRs are good practice:

```bash
# Instead of pushing directly to main:
git checkout -b docs/update-readme
# make changes
git push origin docs/update-readme
# Open PR on GitHub → review your own changes → merge
```

Shows professional workflow to recruiters! 🟩

---

## Merging Options on GitHub

| Option | Description | When to Use |
|--------|-------------|-------------|
| Merge commit | Keeps all commits + adds merge commit | Default, shows full history |
| Squash and merge | Combines all commits into one | Clean history for feature branches |
| Rebase and merge | Replays commits on top of main | Linear history, no merge commits |

---

## Key Takeaway

> PRs are the standard professional workflow — never push directly to main in a team. Even on solo projects, using PRs shows good habits to recruiters. A good PR description explains WHAT changed, WHY, and HOW to test it.
