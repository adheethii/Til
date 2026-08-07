# LangChain Retriever Search Types — Beyond Basic Similarity

**Date:** 2026-08-07

## Why This Gap Existed

Every RAG note so far (FAISS Vector Store, Document Loaders,
Prompt Engineering for RAG) has used the default `similarity_search`
without ever looking at what other retrieval modes exist on the
same retriever object — worth closing that gap directly, and
worth confirming against the actual current source rather than
writing from memory, since library internals shift between
versions.

---

## Confirmed From Actual Source (not assumed)

Checked directly against the installed `langchain-core` package's
`VectorStoreRetriever` class — there are exactly three allowed
`search_type` values, enforced by a real validator that raises a
`ValueError` on anything else:

```python
allowed_search_types = ("similarity", "similarity_score_threshold", "mmr")
```

Worth flagging: `langchain-community` (where `FAISS` currently
lives) carries an active deprecation warning as of this check,
pointing toward standalone integration packages instead — worth
checking current docs before relying on this exact import path
in new code going forward.

---

## similarity (the default, already used throughout)

```python
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)
```

Returns the top-k nearest neighbors by embedding distance — no
filtering, no diversity consideration, just the k closest matches.

---

## similarity_score_threshold — Confirmed Validation Requirement

```python
retriever = vectorstore.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"score_threshold": 0.75, "k": 5}
)
```

Only returns documents scoring above the threshold — genuinely
useful for avoiding low-confidence matches being fed to the LLM
as if they were relevant context. Confirmed directly from source:
this mode has an ENFORCED requirement — `score_threshold` must be
present in `search_kwargs` AND must be a `float`, or the retriever
raises a `ValueError` immediately when constructed, not silently
at query time. Passing an int (e.g. `0` instead of `0.0`) would
fail this check.

---

## mmr (Maximal Marginal Relevance) — Diversity, Not Just Relevance

```python
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 5, "fetch_k": 20, "lambda_mult": 0.5}
)
```

Plain similarity search can return 5 chunks that are all nearly
identical paraphrases of the same point — MMR instead fetches a
larger candidate pool (`fetch_k`), then selects a final set that
balances relevance against DIVERSITY from each other, avoiding
redundant near-duplicate chunks in the final context.

`lambda_mult` controls the balance: closer to 1.0 favors pure
relevance (behaves more like plain similarity search), closer to
0.0 favors diversity more heavily.

---

## Why This Matters for RAG Quality Specifically

```
A document that discusses the same policy point in three
different sections (common in real company wikis, handbooks)
can cause plain similarity search to retrieve three near-
duplicate chunks — wasting context window space on repetition
instead of covering different relevant angles of the question.

MMR is the direct mitigation for this specific failure mode.
```

---

## What This Suggests for My Own RAG Project

The Agentic RAG Research Assistant currently uses default
similarity search — worth testing whether switching to MMR
changes retrieval quality on documents with repetitive sections,
as a genuine follow-up rather than just theoretical.

---

## Key Takeaway

> Three retriever modes exist on the same vectorstore object, confirmed directly from source rather than assumed: `similarity` (default, closest-k), `similarity_score_threshold` (with an enforced float requirement on the threshold value), and `mmr` (trades some pure relevance for diversity across the returned chunks, useful specifically when source documents repeat the same point in multiple places). Checking library internals directly, rather than trusting memory of how an API "usually" works, caught a real detail here — the score_threshold type enforcement — that would have been easy to get wrong otherwise.
