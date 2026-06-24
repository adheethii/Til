# Self-Consistency Prompting

**Date:** 2026-06-24

## What is Self-Consistency?

Self-consistency is a technique where you **run the same prompt multiple times** and take the most common answer — like majority voting.

```
Same prompt → Run 5 times → Get 5 answers → Pick most common answer
```

The idea: if multiple independent reasoning paths reach the same answer, that answer is more likely to be correct.

---

## Why it Works

LLMs are probabilistic — different runs can give different reasoning paths. Some paths lead to wrong answers. But if most paths agree → higher confidence the answer is correct.

```
Run 1: Reasoning path A → Answer: 42 ✅
Run 2: Reasoning path B → Answer: 42 ✅
Run 3: Reasoning path C → Answer: 38 ❌
Run 4: Reasoning path D → Answer: 42 ✅
Run 5: Reasoning path E → Answer: 42 ✅

Majority vote: 42 (4/5 agree) → Final answer: 42
```

---

## Self-Consistency vs Standard CoT

| | Standard CoT | Self-Consistency |
|--|-------------|-----------------|
| Runs | 1 | Multiple (3-10) |
| Answer selection | First result | Majority vote |
| Accuracy | Good | Better |
| Cost | Low | Higher |

---

## Implementation in Python

```python
from langchain_ollama import OllamaLLM
from collections import Counter

llm = OllamaLLM(model="llama3", temperature=0.7)

def self_consistency(prompt, runs=5):
    answers = []

    for i in range(runs):
        response = llm.invoke(prompt + "\nLet's think step by step.")
        # Extract final answer (simplified)
        answers.append(response.strip())

    # Return most common answer
    most_common = Counter(answers).most_common(1)[0][0]
    return most_common

result = self_consistency("If I have 3 apples and give away 1, then buy 4 more, how many do I have?")
```

---

## When to Use

✅ Math and reasoning problems where accuracy matters
✅ Classification tasks
✅ When you need high confidence answers
✅ Medical, legal, or financial AI applications

❌ Creative writing (you want variety)
❌ Simple factual lookups
❌ When cost/speed is a priority

---

## Key Takeaway

> Self-consistency improves accuracy by running the same prompt multiple times and voting on the most common answer. It's especially powerful for math and reasoning tasks. Trade-off: more API calls = higher cost. Use it when accuracy matters more than speed.
