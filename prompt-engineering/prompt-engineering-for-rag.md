# Prompt Engineering for RAG Systems

**Date:** 2026-06-25

## What is RAG-Specific Prompt Engineering?

RAG (Retrieval Augmented Generation) systems have unique prompting challenges — you need prompts that work well with retrieved context, handle missing information gracefully, and prevent hallucination.

```
Retrieval → Context injection → Prompt → LLM → Answer
```

The prompt is the bridge between retrieved chunks and the final answer.

---

## Core RAG Prompt Template

```python
RAG_PROMPT = """You are a helpful AI assistant.
Answer the question ONLY based on the provided context.
If the answer is not in the context, say exactly:
"I don't have enough information in the provided documents to answer this."

Do NOT use outside knowledge. Do NOT make up answers.

Context:
{context}

Question: {question}

Answer:"""
```

---

## Handling Missing Information

```python
# ❌ Bad — allows hallucination
"Use the context to help answer the question."

# ✅ Good — strict grounding with fallback
"""Answer from the context only.
If not found, say: "This information is not in the provided documents."
Never guess or use outside knowledge."""
```

---

## Multi-Document RAG Prompt

```python
MULTI_DOC_PROMPT = """You have access to multiple documents.
Answer the question by synthesizing information across all documents.
Cite which document each piece of information comes from.

Documents:
{documents}

Question: {question}

Answer (with citations):"""
```

---

## Conversation History in RAG

```python
CHAT_RAG_PROMPT = """You are a helpful assistant with access to documents.
Use the conversation history and context to answer naturally.
Only use information from the context — not outside knowledge.

Conversation History:
{history}

Relevant Context:
{context}

Current Question: {question}

Answer:"""
```

---

## Chunk Quality Prompting

Sometimes retrieved chunks are incomplete. Handle this:

```python
"""The following context may be partial or incomplete.
Answer what you can from the available information.
Clearly state if the context seems incomplete for this question.

Context: {context}
Question: {question}"""
```

---

## What I Applied

Used these patterns in my [Agentic RAG Research Assistant](https://github.com/adheethii/agentic-rag-ai-research-assistant) — strict grounding prompts prevent the LLM from mixing retrieved document content with its own training knowledge.

---

## Key Takeaway

> RAG prompts need three things: strict grounding ("answer ONLY from context"), graceful fallback ("say you don't know if not found"), and clear context injection. The better your RAG prompt, the fewer hallucinations — regardless of retrieval quality.
