# Temperature and Top-p Explained

**Date:** 2026-06-15

## What are These Parameters?

When an LLM generates text, it doesn't just pick the most likely next word — it samples from a probability distribution. **Temperature** and **top-p** control how that sampling works.

---

## Temperature

Temperature controls how **creative vs predictable** the output is.

```
Low temperature  → conservative, focused, deterministic
High temperature → creative, diverse, sometimes random
```

### Scale

| Temperature | Behavior | Use Case |
|-------------|----------|----------|
| 0.0 | Always picks the most likely token | Factual Q&A, code generation |
| 0.3 | Mostly predictable, slight variation | Summarization, classification |
| 0.7 | Balanced — default for most LLMs | General chat, writing |
| 1.0 | More creative, less predictable | Brainstorming, creative writing |
| 1.5+ | Very random, may be incoherent | Experimental only |

### Example

```python
# Low temperature — precise and factual
response = llm.invoke("What is RAG?", temperature=0.1)
# → Gives a consistent, accurate definition every time

# High temperature — creative
response = llm.invoke("Write a tagline for my AI app", temperature=0.9)
# → Gives different, creative answers each time
```

---

## Top-p (Nucleus Sampling)

Top-p controls which **pool of tokens** the LLM can sample from.

```
top-p = 0.9 → only consider tokens whose cumulative
               probability adds up to 90%
```

It cuts off the long tail of unlikely tokens dynamically.

| Top-p | Behavior |
|-------|----------|
| 0.1 | Very restricted — only top tokens |
| 0.5 | Moderate variety |
| 0.9 | Default — good balance |
| 1.0 | All tokens considered |

---

## Temperature vs Top-p

| | Temperature | Top-p |
|--|-------------|-------|
| Controls | Sharpness of distribution | Size of token pool |
| Effect | How random the output is | Which tokens are available |
| Typical default | 0.7 | 0.9 |

**Best practice** — tune one at a time. Don't change both simultaneously.

---

## Practical Settings

```python
# For RAG / factual answers
temperature = 0.1, top_p = 0.9

# For general chat
temperature = 0.7, top_p = 0.9

# For creative writing
temperature = 0.9, top_p = 0.95

# For code generation
temperature = 0.2, top_p = 0.9
```

---

## What I Apply

In my [Agentic RAG Research Assistant](https://github.com/adheethii/agentic-rag-ai-research-assistant) — low temperature (0.1–0.2) is used for document Q&A to keep answers grounded and consistent, while slightly higher temperature is used for summarization to allow more natural phrasing.

---

## Key Takeaway

> Temperature controls creativity — lower is more focused, higher is more random. Top-p controls which tokens are even considered. For factual AI apps like RAG, keep temperature low. For creative tasks, raise it.
