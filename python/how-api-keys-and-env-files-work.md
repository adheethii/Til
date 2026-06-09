# How API Keys and .env Files Work

**Date:** 2026-06-04

## What is an API Key?

An API key is a secret token that identifies you when calling an external service (OpenAI, HuggingFace, Google Maps, etc). Think of it as a password for your app.

```
Without API key → 401 Unauthorized
With API key    → ✅ Access granted
```

---

## The Problem

You need the key in your code — but you can't hardcode it:

```python
# ❌ NEVER do this — exposes your key on GitHub
client = OpenAI(api_key="sk-abc123secretkey")
```

If you push this to GitHub, bots scan for it within seconds and abuse it.

---

## The Solution — .env File

Store secrets in a `.env` file that never gets pushed to GitHub.

```bash
# .env file
OPENAI_API_KEY=sk-abc123secretkey
HUGGINGFACE_TOKEN=hf_xyz789
```

Then load it in Python:

```python
from dotenv import load_dotenv
import os

load_dotenv()  # reads the .env file

api_key = os.getenv("OPENAI_API_KEY")
```

---

## Critical — Add .env to .gitignore

```bash
# .gitignore
.env
```

This tells Git to never track the `.env` file — your secrets stay local.

---

## Full Setup

```bash
# 1. Install python-dotenv
pip install python-dotenv

# 2. Create .env file
echo "OPENAI_API_KEY=your_key_here" > .env

# 3. Add to .gitignore
echo ".env" >> .gitignore
```

---

## What I Applied

Used this in my [Agentic RAG Research Assistant](https://github.com/adheethii/agentic-rag-ai-research-assistant) — API keys and model configs stored in `.env`, never exposed on GitHub.

---

## Key Takeaway

> Never hardcode API keys. Always use `.env` + `python-dotenv` + `.gitignore`. One accidental push can get your key stolen in seconds.
