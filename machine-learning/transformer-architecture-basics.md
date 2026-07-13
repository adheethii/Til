# Transformer Architecture Basics

**Date:** 2026-07-13

## What is a Transformer?

The Transformer is the architecture behind all modern LLMs (GPT, Claude, Llama). It processes entire sequences at once using **attention** — instead of one word at a time like older RNNs.

```
RNN:         word1 → word2 → word3 → ... (sequential, slow)
Transformer: [word1, word2, word3] → all at once (parallel, fast)
```

---

## Core Innovation — Self-Attention

Self-attention lets each word "look at" every other word to understand context.

```
Sentence: "The cat sat on the mat because it was tired"

When processing "it", attention helps the model figure out
"it" refers to "cat" — by looking at relationships between
all words simultaneously.
```

---

## The Attention Mechanism (Simplified)

```
For each word, calculate:
Query (Q)  → "What am I looking for?"
Key (K)    → "What do I contain?"
Value (V)  → "What information do I provide?"

Attention Score = Query · Key (how relevant is this word?)
Output = weighted sum of Values (based on attention scores)
```

```python
import torch
import torch.nn.functional as F

def simple_attention(query, key, value):
    # Calculate attention scores
    scores = torch.matmul(query, key.transpose(-2, -1))
    scores = scores / (key.size(-1) ** 0.5)   # scale

    # Convert to probabilities
    attention_weights = F.softmax(scores, dim=-1)

    # Weighted sum of values
    output = torch.matmul(attention_weights, value)
    return output
```

---

## Transformer Building Blocks

```
Input Embeddings
    ↓
Positional Encoding (tells model word ORDER)
    ↓
Multi-Head Self-Attention
    ↓
Feed Forward Network
    ↓
(repeat N times — "layers")
    ↓
Output
```

---

## Why Positional Encoding?

Attention has no built-in sense of word order — "cat sat mat" and "mat sat cat" would look identical without it.

```python
# Positional encoding adds position info to embeddings
position_encoding = sin(position / 10000^(2i/d_model))
embedding_with_position = word_embedding + position_encoding
```

---

## Multi-Head Attention

Instead of one attention calculation, use multiple "heads" — each learns different relationships:

```
Head 1: focuses on grammar relationships
Head 2: focuses on semantic meaning
Head 3: focuses on long-range dependencies
...
All heads combined → richer understanding
```

---

## Encoder vs Decoder

| | Encoder | Decoder |
|--|---------|---------|
| Purpose | Understand input | Generate output |
| Attention | Sees all words | Only sees previous words |
| Used in | BERT | GPT, Claude (decoder-only) |
| Example task | Classification | Text generation |

---

## Why This Matters for RAG

```
Understanding transformers helps explain WHY:
- Embeddings capture semantic meaning (via attention)
- Longer context = more computation (attention is O(n²))
- Chunking is needed — transformers have context limits
```

---

## Key Takeaway

> Transformers use self-attention to let every word see every other word simultaneously — enabling parallel processing and capturing long-range relationships. This is THE architecture behind every modern LLM. Understanding attention explains why context windows matter and why chunking is necessary in RAG systems.
