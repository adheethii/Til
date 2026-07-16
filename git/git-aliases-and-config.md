# Git Aliases and Configuration

**Date:** 2026-07-16

## What are Git Aliases?

Aliases are shortcuts for long or frequently-used Git commands — save time by typing less.

```bash
# Instead of:
git log --oneline --graph --all

# Type:
git lg
```

---

## Creating Aliases

```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.cm "commit -m"
git config --global alias.lg "log --oneline --graph --all"
git config --global alias.unstage "reset HEAD --"
git config --global alias.last "log -1 HEAD"
```

Now you can use:
```bash
git st        # instead of git status
git co main   # instead of git checkout main
git cm "fix bug"  # instead of git commit -m "fix bug"
git lg        # instead of git log --oneline --graph --all
```

---

## Where Aliases Are Stored

```bash
# View your global git config
cat ~/.gitconfig
```

```ini
[alias]
    st = status
    co = checkout
    br = branch
    cm = commit -m
    lg = log --oneline --graph --all
    unstage = reset HEAD --
    last = log -1 HEAD
```

You can edit this file directly instead of running commands.

---

## Useful Advanced Aliases

```bash
# Undo last commit but keep changes
git config --global alias.undo "reset --soft HEAD~1"

# Show files changed in last commit
git config --global alias.dl "!git ls-tree -r --name-only HEAD"

# Delete merged branches automatically
git config --global alias.cleanup "!git branch --merged | grep -v '\\*\\|main\\|master' | xargs -n 1 git branch -d"

# Amend last commit without changing message
git config --global alias.amend "commit --amend --no-edit"
```

---

## Global Git Configuration

```bash
# Set your identity (required for commits)
git config --global user.name "Adheethi K Binu"
git config --global user.email "adheethii@gmail.com"

# Set default branch name
git config --global init.defaultBranch main

# Set default editor
git config --global core.editor "code --wait"

# Enable colored output
git config --global color.ui auto

# Set default merge tool
git config --global merge.tool vimdiff
```

---

## Viewing All Config

```bash
git config --list
git config --list --global
git config user.name    # check specific value
```

---

## Key Takeaway

> Aliases save significant typing over time — set up `st`, `co`, `cm`, `lg` at minimum. Global config in `~/.gitconfig` sets your identity and defaults once, applying to every repo on your machine. Small setup investment, big daily time savings.
