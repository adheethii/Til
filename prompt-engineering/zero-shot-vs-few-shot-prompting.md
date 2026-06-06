# Zero-shot vs Few-shot Prompting

**Date:** 2026-06-05

## Zero-shot Prompting

Giving the LLM a task with **no examples** — just instructions.

```
Prompt:
"Classify this review as Positive or Negative.
Review: The product broke after one day."

Response:
Negative
```

The model uses its training knowledge to figure it out. No examples needed.

---

## Few-shot Prompting

Giving the LLM **a few examples** before the actual task — teaching it the pattern you want.

```
Prompt:
"Classify reviews as Positive or Negative.

Review: Great quality, love it! → Positive
Review: Stopped working after a week. → Negative
Review: Decent but overpriced. → Negative

Review: Best purchase I've made this year."

Response:
Positive
```

The model learns the pattern from your examples and applies it.

---

## When to Use Which

| Situation | Use |
|-----------|-----|
| Simple, clear task | Zero-shot |
| Task needs a specific format | Few-shot |
| Model keeps getting it wrong | Few-shot |
| Custom classification categories | Few-shot |
| Quick and general response | Zero-shot |

---

## One-shot Prompting

Between zero and few — giving just **one example**.

```
Prompt:
"Translate English to French.
English: Good morning → French: Bonjour

English: How are you?"

Response:
Comment allez-vous?
```

---

## Key Takeaway

> Zero-shot = trust the model. Few-shot = show the model. When zero-shot gives wrong or inconsistent results, add 2-3 examples and the output quality improves dramatically.
