# Worked Example — Design an Enterprise RAG System

**Date:** 2026-07-18

## The Question

"Design a RAG system that lets employees ask questions about internal
company documents (policies, wikis, past reports)."

This connects directly to my [Agentic RAG Research Assistant](https://github.com/adheethii/agentic-rag-ai-research-assistant)
project — a great one to reference in the actual interview.

---

## Step 1 — Clarify Requirements

```
Q: How many documents, how often do they change?
A: Assume 100K documents, updated a few hundred times per day

Q: How many concurrent users?
A: Assume 5,000 employees, maybe 500 concurrent at peak

Q: Latency requirement?
A: Chat-like experience — under 3 seconds end-to-end

Q: Data sensitivity — can we use external APIs (OpenAI) or must
   everything stay on-premise?
A: Assume: sensitive data, prefer self-hosted/local models
   (directly informed my choice of Ollama in my own project)
```

---

## Step 2 — Frame as an ML Problem

```
Core task: Given a query, retrieve relevant document chunks,
then generate a grounded answer using those chunks as context.

Two sub-problems:
1. Retrieval — semantic search over document embeddings
2. Generation — LLM synthesizes an answer from retrieved context
```

---

## Step 3 — Data

```
Document sources: Confluence, SharePoint, PDFs, Google Docs
Update frequency: needs a pipeline to detect and re-index changes
Access control: CRITICAL — a document a user can't normally see
                shouldn't be retrievable through the RAG system either
```

---

## Step 4 — Feature Engineering (for RAG, this means chunking + embedding)

```
Chunking strategy:
- 500 tokens per chunk, 50 token overlap (my project's approach)
- Preserve document structure — don't split mid-table or mid-list

Embedding model:
- Self-hosted sentence-transformer model (for data sensitivity)
- Re-embed only CHANGED documents, not the whole corpus, on updates
```

---

## Step 5 — Model Selection & Training

```
Retrieval: Hybrid search
  - Dense: FAISS with sentence-transformer embeddings
  - Sparse: BM25 for exact keyword/term matches
  - Fusion: Reciprocal Rank Fusion combines both result sets
  - Reranking: cross-encoder reranks top candidates for precision

Generation: Self-hosted LLM (Llama 3 via Ollama) for data sensitivity,
            OR a hosted API if data allows and higher quality is needed

Why hybrid retrieval specifically:
Dense embeddings miss exact terms (policy numbers, specific names).
BM25 catches those. Combining both consistently outperforms either alone —
this is exactly what I measured in my own project's evaluation.
```

---

## Step 6 — Evaluation

```
Retrieval quality:
- Recall@K — is the right chunk in the top K retrieved?
- Manual evaluation set: 20-50 real employee questions with
  known correct source documents (exactly what I did for my project)

Generation quality:
- Faithfulness — does the answer only use retrieved context? (no hallucination)
- Relevance — does it actually answer the question?
- Human evaluation or LLM-as-judge for these subjective metrics
```

---

## Step 7 — Deployment & Serving

```
Architecture:
Employee query → API Gateway (auth check)
              → Access-control filter (only search docs user can see)
              → Hybrid Retriever (FAISS + BM25)
              → Reranker
              → LLM generates answer from top chunks
              → Response with source citations

Indexing pipeline (separate, async):
New/changed document → Chunking → Embedding → Update FAISS index
                                              → Update BM25 index
```

---

## Step 8 — Monitoring & Maintenance

```
- Log queries with no good retrieval match (retrieval gaps → add docs)
- Track "I don't know" response rate — should be low but non-zero
  (a 0% "I don't know" rate suggests hallucination, not honesty)
- User feedback (thumbs up/down) on answer quality
- Re-index trigger on document changes (webhook from Confluence/SharePoint)
```

---

## Step 9 — Scale & Trade-offs

```
At 10x scale (1M documents):
- FAISS flat index becomes too slow → switch to IVF or HNSW index
  (approximate nearest neighbor, trades small accuracy loss for
  massive speed gain)
- Consider caching frequent queries
- Self-hosted LLM becomes the bottleneck → may need GPU cluster
  or batch multiple requests together
```

---

## Access Control — The Part Most Candidates Forget

```
This is THE differentiator question in enterprise RAG design:
"How do you prevent someone from seeing a document they don't have
 permission to access, through the RAG system?"

Answer: Metadata filtering at retrieval time.
Every chunk stores which users/groups can access its source document.
Retrieval query includes: "only search chunks where user_id in
allowed_users" — filtering happens BEFORE the LLM ever sees the chunk,
not after.
```

---

## Key Takeaway

> Enterprise RAG design questions reward the same fundamentals from my own project (hybrid retrieval, chunking strategy, local LLMs for data sensitivity) plus one enterprise-specific concern almost everyone forgets: access control must filter at the retrieval stage, not the generation stage. Mentioning this specifically signals production-readiness thinking.
