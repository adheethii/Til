# Git Reset vs Revert

**Date:** 2026-07-16

## The Core Difference

```
git reset  → moves history backward (rewrites it — dangerous on shared branches)
git revert → adds a NEW commit that undoes changes (safe on shared branches)
```

---

## Git Reset

Reset moves your branch pointer to a previous commit — three modes control what happens to your working directory and staging area.

```bash
# Soft — undo commit, keep changes staged
git reset --soft HEAD~1

# Mixed (default) — undo commit, keep changes unstaged
git reset HEAD~1

# Hard — undo commit, DISCARD all changes (destructive!)
git reset --hard HEAD~1
```

```
Before: A → B → C (HEAD)
git reset --hard B
After:  A → B (HEAD)   ← commit C is gone entirely
```

### Reset Modes Compared

| Mode | Commit | Staged files | Working directory |
|------|--------|---------------|-------------------|
| `--soft` | Undone | Kept | Kept |
| `--mixed` (default) | Undone | Unstaged | Kept |
| `--hard` | Undone | Cleared | **Discarded** |

---

## Git Revert

Revert creates a **new commit** that undoes a previous commit — history is preserved, nothing is deleted.

```bash
git revert abc1234
```

```
Before: A → B → C (HEAD)
git revert B
After:  A → B → C → D (HEAD)   ← D undoes B's changes, B still exists
```

---

## When to Use Which

```
✅ Use RESET when:
- Undoing LOCAL commits not yet pushed
- Cleaning up your own branch before opening a PR

✅ Use REVERT when:
- Undoing commits already pushed/shared with others
- You need a clear audit trail of what was undone and why
- Working on main/production branches
```

---

## Golden Rule

```
NEVER use git reset --hard on commits already pushed and shared.
It rewrites history — anyone else who pulled will have conflicts.

Always use git revert for shared/public branches instead.
```

---

## Key Takeaway

> Reset rewrites history (safe only locally), revert adds new history (safe everywhere). If you've already pushed a commit others might have pulled, always revert — never reset --hard.
