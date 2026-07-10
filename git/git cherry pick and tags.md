# Git Cherry-pick and Tags

**Date:** 2026-07-10

## Git Cherry-pick

Cherry-pick applies a specific commit from one branch to another — without merging the entire branch.

```
main:    A → B → C → D
                      ↑
feature: E → F → G   (cherry-pick G onto main)

After cherry-pick:
main:    A → B → C → D → G'
```

---

## When to Use Cherry-pick

```
✅ Apply a bug fix from feature branch to main immediately
✅ Pick one useful commit without merging everything
✅ Copy a commit to multiple branches
❌ Don't use when you need ALL changes from a branch (use merge)
```

---

## Cherry-pick Commands

```bash
# Get the commit hash you want
git log --oneline feature-branch
# → abc1234 fix: resolve encoding issue
# → def5678 feat: add new feature
# → ghi9012 docs: update README

# Cherry-pick a single commit
git checkout main
git cherry-pick abc1234

# Cherry-pick multiple commits
git cherry-pick abc1234 def5678

# Cherry-pick a range
git cherry-pick abc1234..ghi9012

# Cherry-pick without committing (stage only)
git cherry-pick -n abc1234
```

---

## Git Tags

Tags mark specific points in history — typically used for **releases and versions**.

```
main: A → B → C → D → E
              ↑         ↑
           v1.0.0    v1.1.0
```

---

## Creating Tags

```bash
# Lightweight tag (just a pointer)
git tag v1.0.0

# Annotated tag (recommended — includes message, author, date)
git tag -a v1.0.0 -m "First stable release"

# Tag a specific commit
git tag -a v1.0.0 abc1234 -m "Version 1.0.0"

# List all tags
git tag

# See tag details
git show v1.0.0
```

---

## Pushing Tags

```bash
# Push a specific tag
git push origin v1.0.0

# Push all tags
git push origin --tags

# Delete a tag locally
git tag -d v1.0.0

# Delete a tag on remote
git push origin --delete v1.0.0
```

---

## Semantic Versioning (SemVer)

```
v MAJOR . MINOR . PATCH
  v1     .  2   .  3

MAJOR → breaking changes (v2.0.0)
MINOR → new features, backward compatible (v1.3.0)
PATCH → bug fixes (v1.2.1)
```

---

## Key Takeaway

> Cherry-pick is surgical — apply one specific commit without merging a whole branch. Tags mark important milestones like releases. Use annotated tags with `-a` for releases — they store metadata. Follow semantic versioning (MAJOR.MINOR.PATCH) for professional project releases.
