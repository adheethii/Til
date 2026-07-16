# Git Log and History Exploration

**Date:** 2026-07-15

## Basic Log

```bash
git log
# Full commit history with hash, author, date, message

git log --oneline
# Compact — one line per commit
# abc1234 feat: add prediction endpoint
# def5678 fix: encoding bug
```

---

## Useful Log Formats

```bash
# Graph view — see branches and merges visually
git log --oneline --graph --all

# Last N commits
git log -5

# Commits by a specific author
git log --author="Adheethi"

# Commits touching a specific file
git log -- main.py

# Commits between two dates
git log --since="2026-07-01" --until="2026-07-15"

# Search commit messages
git log --grep="fix"

# Show actual code changes per commit
git log -p
```

---

## Seeing What Changed

```bash
# Diff between working directory and last commit
git diff

# Diff between two commits
git diff abc1234 def5678

# Diff for a specific file
git diff main.py

# See what's staged vs not staged
git diff --staged
```

---

## Blame — Who Changed This Line?

```bash
git blame main.py
# Shows commit hash + author for every line

git blame -L 10,20 main.py
# Only lines 10-20
```

---

## Finding a Specific Commit

```bash
# Find commit that introduced a bug (binary search through history)
git bisect start
git bisect bad                  # current commit is broken
git bisect good abc1234         # this old commit was working
# Git checks out commits for you to test — mark each good/bad
git bisect reset                # when done
```

---

## Show Details of a Commit

```bash
git show abc1234
# Full diff + metadata for that specific commit
```

---

## Key Takeaway

> `git log --oneline --graph --all` is the most useful command for understanding project history at a glance. `git blame` finds who wrote a line and when. `git bisect` is a powerful tool for finding exactly which commit introduced a bug.
