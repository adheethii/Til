# Git Worktrees

**Date:** 2026-07-21

## The Problem Worktrees Solve

```
Normal Git: your repo folder can only have ONE branch checked
            out at a time. Switching branches means stashing
            or committing whatever you're mid-way through.

Common annoying scenario:
"I'm halfway through a feature, but I need to quickly check
 out main to fix an urgent bug — now I have to stash my
 half-done work, switch, fix, switch back, unstash..."
```

Worktrees let you have **multiple branches checked out
simultaneously**, each in its own separate folder, all sharing
the same underlying `.git` history.

---

## Basic Usage

```bash
# You're on 'feature-branch' inside my-project/
cd my-project

# Create a NEW worktree for 'main', in a sibling folder
git worktree add ../my-project-main main

# Now you have TWO folders:
# my-project/       → still on feature-branch, untouched
# my-project-main/  → checked out on main, completely separate

# Go fix the bug without disturbing your feature work at all
cd ../my-project-main
# ... fix bug, commit, push ...

# Come back to your original work exactly as you left it
cd ../my-project
```

---

## Creating a Worktree for a New Branch

```bash
# Create a new branch AND a new worktree for it in one step
git worktree add ../my-project-hotfix -b hotfix/urgent-bug

cd ../my-project-hotfix
# fresh checkout, new branch, separate folder — ready to work
```

---

## Listing and Managing Worktrees

```bash
# See all active worktrees
git worktree list

# Output:
# /home/user/my-project         abc1234 [feature-branch]
# /home/user/my-project-main    def5678 [main]
# /home/user/my-project-hotfix  ghi9012 [hotfix/urgent-bug]
```

```bash
# Remove a worktree when done with it
git worktree remove ../my-project-main

# If a worktree folder was deleted manually (not via the command
# above), clean up Git's internal references to it
git worktree prune
```

---

## Practical Use Cases

```
✅ Reviewing a teammate's PR without disturbing your own branch
   git worktree add ../review-pr-42 origin/pr-42-branch

✅ Running tests on main while developing a feature simultaneously
   git worktree add ../my-project-tests main

✅ Comparing behavior between two branches side by side
   (two folders open in two editor windows at once)

✅ Working on an urgent hotfix mid-feature, without stash juggling
```

---

## Worktrees vs Stashing vs Cloning

| Approach | Downside |
|----------|----------|
| `git stash` | Easy to forget a stash exists; only one at a time comfortably |
| Separate `git clone` | Duplicates the ENTIRE repo history on disk, wasteful |
| **Worktree** | Shares one `.git` history, minimal extra disk space, no stash juggling |

---

## Key Takeaway

> Worktrees let you check out multiple branches at once, each in its own folder, without duplicating repo history like a fresh clone would. `git worktree add <path> <branch>` is the core command. This directly replaces the "stash, switch, fix, switch back, unstash" dance for urgent interruptions — genuinely useful once you form the habit of reaching for it instead of stashing.
