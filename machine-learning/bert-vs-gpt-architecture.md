# BERT vs GPT Architecture

**Date:** 2026-07-17

## The Core Difference

Both are built on the Transformer architecture, but they use different halves of it.

```
BERT → Encoder-only  → understands text (bidirectional)
GPT  → Decoder-only  → generates text (unidirectional/causal)
```

---

## BERT (Bidirectional Encoder Representations from Transformers)

```
Sentence: "The [MASK] sat on the mat"

BERT looks at BOTH directions simultaneously:
← "The" ... "sat on the mat" →
     ↓
Predicts: [MASK] = "cat"
```

BERT sees the **entire sentence at once** — words before AND after the current position.

### Training Objective — Masked Language Modeling

```python
# BERT is trained by randomly masking ~15% of words and predicting them
input:  "The [MASK] sat on the [MASK]"
target: "The cat sat on the mat"
```

---

## GPT (Generative Pre-trained Transformer)

```
Sentence: "The cat sat on the"

GPT only looks LEFT (causal/autoregressive):
"The cat sat on the" → predicts next word
     ↓
Predicts: "mat"
```

GPT can only see **previous words** — it generates one word at a time, left to right.

### Training Objective — Next Token Prediction

```python
# GPT is trained to predict the NEXT word given all previous words
input:  "The cat sat on the"
target: "mat"   (next word)
```

---

## Side-by-Side Comparison

| | BERT | GPT |
|--|------|-----|
| Architecture | Encoder-only | Decoder-only |
| Attention | Bidirectional | Causal (left-to-right only) |
| Training task | Masked word prediction | Next word prediction |
| Best at | Understanding (classification, Q&A) | Generation (chat, writing) |
| Example use | Sentiment analysis, search | ChatGPT, Claude, text completion |

---

## Why This Matters for RAG

```
Embeddings for retrieval → often use BERT-style encoders
  (they're great at understanding meaning for similarity search)

Generation of answers → uses GPT-style decoders
  (they're great at producing fluent, coherent text)

Most RAG systems: BERT-style embedder + GPT-style LLM
```

---

## Modern LLMs (Claude, GPT-4, Llama)

```
Almost all modern chat-focused LLMs are DECODER-ONLY (GPT-style)
because:
- Generation is the primary use case (chat, code, writing)
- Decoder-only scales better with more parameters
- Simpler architecture for the "predict next token" paradigm
```

---

## Key Takeaway

> BERT sees the whole sentence at once (bidirectional) — great for understanding. GPT only sees what came before (causal) — great for generating. This explains why embedding models (for RAG retrieval) are often BERT-style, while chat models (for generation) are almost universally GPT-style decoder-only architectures.
