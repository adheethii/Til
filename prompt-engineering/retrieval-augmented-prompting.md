# Retrieval Augmented Prompting

**Date:** 2026-06-24

## What is Retrieval Augmented Prompting?

Retrieval Augmented Prompting is the prompt engineering side of RAG — specifically **how to write prompts that use retrieved context effectively**.

```
Retrieved chunks → Injected into prompt → LLM answers from context
```

The quality of your RAG system depends heavily on how well your prompt instructs the LLM to use the retrieved context.

---

## Basic RAG Prompt Structure

```
System: You are a helpful assistant. Answer questions ONLY based on 
        the provided context. If the answer is not in the context, 
        say "I don't know based on the provided documents."

Context:
{retrieved_chunks}

Question: {user_question}

Answer:
```

---

## Common RAG Prompt Mistakes

```
❌ Bad — no instruction on how to use context:
"Context: {chunks}\nQuestion: {question}"

❌ Bad — allows hallucination:
"Use the context if helpful, otherwise use your knowledge."

✅ Good — strict grounding:
"Answer ONLY from the provided context. 
 Do not use outside knowledge.
 If unsure, say 'The documents don't mention this.'"
```

---

## Advanced RAG Prompt Patterns

### Citation Pattern
```
Answer the question based on the context below.
After your answer, cite which part of the context 
you used in [brackets].

Context: {chunks}
Question: {question}
```

### Confidence Pattern
```
Answer the question from the context.
Rate your confidence: High / Medium / Low
Explain why if confidence is Low.

Context: {chunks}
Question: {question}
```

### Structured Output Pattern
```
Answer the question from the context.
Respond in this JSON format:
{
  "answer": "your answer",
  "source": "relevant quote from context",
  "confidence": "high/medium/low"
}

Context: {chunks}
Question: {question}
```

---

## LangChain RAG Prompt

```python
from langchain.prompts import PromptTemplate

rag_prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""You are an AI assistant. Answer the question 
based ONLY on the following context. If the answer is not 
in the context, say "I don't know based on the documents."

Context:
{context}

Question: {question}

Answer:"""
)
```

---

## Prompt Tips for Better RAG

| Tip | Example |
|-----|---------|
| Ground strictly | "Answer ONLY from context" |
| Handle gaps | "Say 'not mentioned' if unsure" |
| Request citations | "Quote the relevant sentence" |
| Set tone | "Be concise, 2-3 sentences max" |
| Structured output | "Respond in JSON" |

---

## What I Built

Used retrieval augmented prompting in my [Agentic RAG Research Assistant](https://github.com/adheethii/agentic-rag-ai-research-assistant) — the system prompt strictly instructs the LLM to answer only from retrieved document chunks, preventing hallucination.

---

## Key Takeaway

> RAG is only as good as its prompt. Always instruct the LLM to answer ONLY from context, handle gaps gracefully, and optionally request citations. The retrieval step finds relevant chunks — the prompt ensures the LLM actually uses them correctly.
