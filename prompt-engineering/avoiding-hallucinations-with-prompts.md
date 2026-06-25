# Avoiding Hallucinations with Prompts

**Date:** 2026-06-25

## What is Hallucination?

Hallucination is when an LLM **confidently states something false** — inventing facts, citations, names, or data that don't exist.

```
User: Who wrote the paper "Deep RAG: A Survey"?
LLM:  "It was written by Dr. James Chen at MIT in 2023."
Reality: This paper and author don't exist.
```

---

## Why LLMs Hallucinate

- Trained to sound confident and fluent
- Fill gaps in knowledge with plausible-sounding text
- No built-in fact-checking mechanism
- Pressure to give an answer rather than say "I don't know"

---

## Prompting Strategies to Reduce Hallucination

### 1. Explicit "I don't know" Permission

```
❌ Bad — forces an answer:
"Answer this question about the 2025 AI regulations."

✅ Good — allows uncertainty:
"Answer this question. If you don't know or are unsure,
say 'I don't have reliable information about this.'
Never guess or make up facts."
```

### 2. Source-Grounded Prompting

```
"Answer ONLY based on the provided context.
Do not use any outside knowledge.
If the answer isn't in the context, say:
'This information is not in the provided documents.'"
```

### 3. Confidence Rating

```
"Answer the question and rate your confidence:
- HIGH: You're certain this is accurate
- MEDIUM: You believe this is correct but aren't certain
- LOW: You're guessing — user should verify

Always explain LOW confidence ratings."
```

### 4. Step-by-Step Verification

```
"Before giving your final answer:
1. State what you know for certain
2. State what you're inferring
3. State what you don't know
Then give your answer."
```

### 5. Lowering Temperature

```python
# High temperature → more creative → more hallucination
llm = OllamaLLM(model="llama3", temperature=0.9)

# Low temperature → more focused → less hallucination
llm = OllamaLLM(model="llama3", temperature=0.1)
```

---

## Anti-Hallucination Prompt Template

```
You are a careful, accurate assistant.

Rules:
1. Only state facts you are certain about
2. Say "I'm not sure" rather than guessing
3. Never invent names, dates, statistics, or citations
4. If asked about recent events, note your knowledge cutoff
5. Prefer "I don't know" over a wrong answer

Question: {question}

Answer (be honest about uncertainty):
```

---

## RAG as Anti-Hallucination

RAG is the most effective technical solution:

```
Without RAG: LLM answers from training data → may hallucinate
With RAG:    LLM answers from retrieved facts → grounded in reality
```

Combined with grounding prompts:
```
"Answer ONLY from the context. Never use outside knowledge."
```

---

## Hallucination Detection

```python
# Simple check — does response cite sources?
def check_grounding(response, context):
    # Check if key phrases from response appear in context
    response_sentences = response.split(".")
    grounded = 0
    for sentence in response_sentences:
        if any(word in context for word in sentence.split()[:5]):
            grounded += 1
    return grounded / len(response_sentences)
```

---

## Key Takeaway

> Hallucination prevention starts with prompting: explicitly allow "I don't know", require source grounding, use low temperature, and add confidence ratings. RAG is the most powerful anti-hallucination technique — it gives the LLM real facts to work with instead of relying on training memory.
