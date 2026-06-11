# Chain of Thought (CoT) Prompting

**Date:** 2026-06-11

## What is Chain of Thought Prompting?

Chain of Thought (CoT) prompting is a technique that encourages the LLM to **think step by step** before giving a final answer — instead of jumping straight to a conclusion.

```
Without CoT → LLM guesses the answer directly
With CoT    → LLM reasons through the problem step by step → better answer
```

---

## Why it Works

LLMs generate text token by token. When forced to write out reasoning steps, each step becomes context for the next — leading to more accurate, logical answers. It's like showing your work in a maths exam.

---

## Zero-shot CoT

Just add **"Let's think step by step"** to your prompt — no examples needed.

```
❌ Without CoT:
"If a train travels 60km/h for 2.5 hours, how far does it go?"
→ LLM: "150km" (sometimes wrong on complex problems)

✅ With CoT:
"If a train travels 60km/h for 2.5 hours, how far does it go?
Let's think step by step."

→ LLM:
Step 1: Speed = 60 km/h
Step 2: Time = 2.5 hours
Step 3: Distance = Speed × Time = 60 × 2.5 = 150km
Answer: 150km
```

---

## Few-shot CoT

Provide examples that show the reasoning process:

```
Q: Roger has 5 tennis balls. He buys 2 more cans of 3 balls each.
   How many does he have?
A: Roger starts with 5. He buys 2 × 3 = 6 more.
   Total = 5 + 6 = 11. The answer is 11.

Q: The cafeteria had 23 apples. They used 20 for lunch and
   bought 6 more. How many do they have?
A: [LLM follows the same reasoning pattern]
```

---

## When to Use CoT

| Task | Use CoT? |
|------|----------|
| Multi-step math problems | ✅ Yes |
| Logical reasoning | ✅ Yes |
| Code debugging | ✅ Yes |
| Complex decision making | ✅ Yes |
| Simple factual questions | ❌ Not needed |
| Creative writing | ❌ Not needed |

---

## CoT vs Standard Prompting

| | Standard | Chain of Thought |
|--|----------|-----------------|
| Output | Direct answer | Reasoning + answer |
| Accuracy | Lower on complex tasks | Higher |
| Token usage | Less | More |
| Best for | Simple tasks | Multi-step reasoning |

---

## Practical Tips

```
# Trigger phrases that activate CoT:
"Let's think step by step."
"Walk me through your reasoning."
"Think carefully before answering."
"Explain your thought process."
"Break this down step by step."
```

---

## What I Apply

Using CoT in my [Agentic RAG Research Assistant](https://github.com/adheethii/agentic-rag-ai-research-assistant) — the system prompt instructs the agent to reason through which tool to use before acting, improving retrieval accuracy.

---

## Key Takeaway

> Chain of Thought works because reasoning is itself context. When an LLM writes out its thinking, each step guides the next — turning a guess into a reasoned answer. Add "Let's think step by step" to any complex prompt and watch accuracy improve.
