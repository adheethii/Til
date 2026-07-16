# Git Submodules

**Date:** 2026-07-15

## What is a Submodule?

A submodule is a Git repository embedded inside another Git repository — used when your project depends on another separate repo (e.g. a shared library).

```
my-project/
├── src/
├── shared-utils/    ← this is actually a SEPARATE git repo
└── README.md
```

---

## Adding a Submodule

```bash
git submodule add https://github.com/user/shared-utils.git shared-utils

# This creates:
# - A folder with the submodule's content
# - A .gitmodules file tracking the submodule's URL
```

---

## .gitmodules File

```ini
[submodule "shared-utils"]
    path = shared-utils
    url = https://github.com/user/shared-utils.git
```

---

## Cloning a Repo WITH Submodules

```bash
# Method 1 — clone then initialize submodules
git clone https://github.com/user/my-project.git
cd my-project
git submodule init
git submodule update

# Method 2 — clone everything in one command
git clone --recurse-submodules https://github.com/user/my-project.git
```

---

## Updating Submodules

```bash
# Pull latest changes for a specific submodule
cd shared-utils
git pull origin main
cd ..
git add shared-utils
git commit -m "chore: update shared-utils submodule"

# Update ALL submodules to their latest commits
git submodule update --remote --merge
```

---

## Removing a Submodule

```bash
git submodule deinit -f shared-utils
git rm -f shared-utils
rm -rf .git/modules/shared-utils
```

---

## Submodules vs Alternatives

| Approach | When to Use |
|----------|-------------|
| Submodules | Need exact version control of dependency |
| Git subtree | Simpler alternative, merges history in |
| Package manager (pip, npm) | Standard published libraries |
| Monorepo | Everything in one repo, no submodules needed |

---

## Key Takeaway

> Submodules link to a specific commit of another repo — not the latest automatically. Always `git submodule update --remote` to pull latest changes. Most modern projects prefer package managers or monorepos over submodules due to their complexity — but they're essential to recognize when working with legacy codebases.
