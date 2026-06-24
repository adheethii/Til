# Tree of Thought Prompting

**Date:** 2026-06-24

## What is Tree of Thought?

Tree of Thought (ToT) is an advanced prompting technique where the LLM **explores multiple reasoning paths simultaneously** — like a tree — and selects the best one.

```
                    Question
                       │
          ┌────────────┼────────────┐
        Path A       Path B       Path C
          │            │            │
       Explore       Explore     Explore
          │            │            │
       ❌ Dead      ✅ Good      ❌ Dead
       end           path         end
                       │
                   Best Answer
```

---

## ToT vs Chain of Thought

| | Chain of Thought | Tree of Thought |
|--|-----------------|----------------|
| Paths explored | 1 (linear) | Multiple (tree) |
| Backtracking | ❌ No | ✅ Yes |
| Best for | Straightforward problems | Complex, multi-step problems |
| Cost | Low | Higher (more tokens) |

---

## How it Works

**Step 1 — Generate multiple thoughts**
```
Problem: Plan a 3-day ML study schedule

Thought A: Start with theory → practice → projects
Thought B: Start with projects → learn theory as needed
Thought C: Alternate theory and practice each day
```

**Step 2 — Evaluate each path**
```
Evaluate A: Good for beginners, structured ✅
Evaluate B: Risk of confusion without foundation ⚠️
Evaluate C: Balanced but may feel scattered ⚠️
```

**Step 3 — Select best path and continue**
```
Best: Path A → continue expanding...
```

---

## Simple ToT Prompt

```
Problem: [your problem here]

Generate 3 different approaches to solve this.
For each approach:
1. Describe the approach
2. List its pros and cons
3. Rate it 1-10

Then select the best approach and solve the problem using it.
```

---

## When to Use ToT

✅ Complex planning problems
✅ Creative tasks with multiple valid solutions
✅ Strategic decision making
✅ Problems where the first approach might be wrong

❌ Simple factual questions (overkill)
❌ When speed matters more than quality

---

## Key Takeaway

> Tree of Thought lets the LLM explore multiple solution paths and backtrack from dead ends — mimicking how humans brainstorm. It's more powerful than CoT for complex problems but uses more tokens. Use it when the problem has multiple valid approaches and you want the best one.
