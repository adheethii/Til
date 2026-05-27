# How RAG (Retrieval Augmented Generation) Works

**Date:** 2026-05-27

## What is RAG?

RAG is a technique that improves LLM responses by giving the model access to external knowledge at query time — instead of relying only on what it learned during training.

## The Problem RAG Solves

LLMs have a knowledge cutoff and can hallucinate facts. RAG fixes this by retrieving relevant, up-to-date context before generating a response.

## How It Works (Step by Step)

```
User Query
    ↓
1. EMBED the query → convert to a vector
    ↓
2. SEARCH the vector store (FAISS) → find top-k similar chunks
    ↓
3. RETRIEVE the matching document chunks
    ↓
4. AUGMENT the prompt → inject retrieved chunks as context
    ↓
5. GENERATE → LLM produces answer grounded in retrieved context
    ↓
Final Response
```

## Key Components

| Component | Role | Tool Used |
|-----------|------|-----------|
| Document Loader | Load PDFs, text, web pages | LangChain loaders |
| Text Splitter | Chunk documents into smaller pieces | RecursiveCharacterTextSplitter |
| Embedding Model | Convert text to vectors | Ollama / HuggingFace |
| Vector Store | Store and search embeddings | FAISS |
| LLM | Generate the final answer | Ollama (local) |
| Chain | Connect all components | LangChain |

## Chunking Strategy Matters

- Too large → irrelevant context gets passed to the LLM
- Too small → loses context, answers feel disconnected
- Sweet spot → `chunk_size=500`, `chunk_overlap=50` for most use cases

## What I Built

Used this in my [Agentic RAG Research Assistant](https://github.com/adheethii/agentic-rag-ai-research-assistant) — a locally running AI that answers questions from uploaded documents using LangChain + FAISS + Ollama.

## Key Takeaway

> RAG = Retrieval + Augmentation + Generation. The retrieval step is what makes LLMs actually reliable for domain-specific or up-to-date knowledge.
