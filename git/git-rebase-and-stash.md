# Git Rebase and Stash

**Date:** 2026-07-08

## Git Rebase

Rebase moves your branch commits on top of another branch — creating a cleaner, linear history.

```
Before rebase:
main:    A → B → C
                  ↘
feature:           D → E

After rebase:
main:    A → B → C
                   ↘
feature:            D' → E'  (replayed on top of C)
```

### When to Use Rebase

```bash
# Update feature branch with latest main (cleaner than merge)
git checkout feature-branch
git rebase main

# Interactive rebase — clean up commits before PR
git rebase -i HEAD~3    # edit last 3 commits
```

### Interactive Rebase Options

```
pick   → keep commit as is
squash → combine with previous commit
reword → change commit message
drop   → delete commit entirely
```

### Squash Example

```bash
git rebase -i HEAD~3

# In editor:
pick   abc123 feat: add prediction endpoint
squash def456 fix: typo in endpoint
squash ghi789 fix: another typo

# Result: one clean commit instead of 3 messy ones
```

---

## Git Stash

Stash temporarily saves uncommitted changes so you can switch branches.

```bash
# Save current changes to stash
git stash

# See all stashes
git stash list
# → stash@{0}: WIP on feature: abc123 add endpoint
# → stash@{1}: WIP on main: def456 update README

# Apply most recent stash (keeps it in list)
git stash apply

# Apply AND remove from list
git stash pop

# Apply specific stash
git stash apply stash@{1}

# Delete a stash
git stash drop stash@{0}

# Clear all stashes
git stash clear
```

### Practical Stash Workflow

```bash
# Working on feature, urgent bug fix needed on main
git stash                   # save current work
git checkout main
git checkout -b hotfix      # fix the bug
git commit -m "fix: urgent bug"
git checkout feature-branch
git stash pop               # restore your work ✅
```

---

## Rebase vs Merge

| | Merge | Rebase |
|--|-------|--------|
| History | Shows branch history | Linear, clean |
| Conflicts | Resolved once | May resolve multiple times |
| Safety | Safe (non-destructive) | Never rebase shared branches |
| Best for | Team branches | Local cleanup before PR |

---

## Key Takeaway

> Rebase creates clean linear history — great for local cleanup before opening a PR. Stash is a temporary clipboard for uncommitted work. Golden rule: never rebase branches that others are working on — only rebase your local feature branches.
