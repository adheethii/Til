# GitHub Codespaces

**Date:** 2026-07-16

## What is GitHub Codespaces?

Codespaces is a cloud-based development environment — a full VS Code instance running in the browser, connected directly to your GitHub repo, with no local setup needed.

```
Traditional: Clone repo → install dependencies → configure environment → code
Codespaces:  Click "Create codespace" → coding in 30 seconds ✅
```

---

## Why Use Codespaces?

```
✅ No local setup — works on any device with a browser
✅ Consistent environment — same setup for every contributor
✅ Great for quick fixes — edit from a tablet/phone even
✅ Pre-configured — dependencies install automatically
✅ Free tier available (60 hours/month for personal accounts)
```

---

## Starting a Codespace

```
1. Go to your GitHub repo
2. Click green "Code" button
3. Click "Codespaces" tab
4. Click "Create codespace on main"
5. Wait ~30 seconds → full VS Code opens in browser
```

---

## devcontainer.json — Configuring the Environment

```json
{
  "name": "AI Interview Simulator Dev",
  "image": "mcr.microsoft.com/devcontainers/python:3.10",
  "postCreateCommand": "pip install -r requirements.txt",
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance"
      ]
    }
  },
  "forwardPorts": [8000, 8501]
}
```

Place this in `.devcontainer/devcontainer.json` — Codespaces reads it automatically to set up the exact environment your project needs.

---

## Port Forwarding

```
When you run: streamlit run app.py
Codespaces automatically detects port 8501 and gives you
a shareable URL to preview your app — even though it's
running in the cloud, not your local machine.
```

---

## Codespaces vs Local Development

| | Local Dev | Codespaces |
|--|-----------|-----------|
| Setup time | Minutes to hours | ~30 seconds |
| Consistency | Varies per machine | Identical every time |
| Cost | Free (your hardware) | Free tier, then paid |
| Offline work | ✅ Yes | ❌ Needs internet |
| Resource limits | Your machine's specs | Cloud tier limits |

---

## Managing Codespaces

```bash
# List your active codespaces (via GitHub CLI)
gh codespace list

# Stop a codespace (pauses billing)
gh codespace stop

# Delete a codespace
gh codespace delete
```

Always **stop** codespaces when done — they consume your free hours even when idle if left running.

---

## Key Takeaway

> Codespaces eliminates "works on my machine" problems entirely — everyone gets the exact same cloud environment. Use `.devcontainer/devcontainer.json` to define dependencies and settings once. Great for quick contributions, onboarding new team members instantly, or coding from any device.
