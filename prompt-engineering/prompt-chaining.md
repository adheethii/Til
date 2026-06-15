# Prompt Chaining

**Date:** 2026-06-15

## What is Prompt Chaining?

Prompt chaining is the technique of **breaking a complex task into smaller steps** — where the output of one prompt becomes the input of the next.

```
Prompt 1 → Output 1 → Prompt 2 → Output 2 → Prompt 3 → Final Result
```

Instead of asking the LLM to do everything in one shot, you guide it through a pipeline of focused steps.

---

## Why Use It?

A single complex prompt often gives mediocre results because the LLM tries to do too much at once. Chaining keeps each step focused and manageable.

```
❌ One prompt trying to do everything:
"Read this research paper, extract the key findings,
compare them with existing literature, identify gaps,
and write a structured report with citations."

✅ Chained prompts:
Step 1: "Extract the key findings from this paper."
Step 2: "Given these findings: {output1}, identify
         how they differ from traditional approaches."
Step 3: "Based on this analysis: {output2}, write
         a structured summary with recommendations."
```

---

## Simple Code Example

```python
from langchain.llms import Ollama

llm = Ollama(model="llama3")

# Step 1 — Extract key points
step1_prompt = f"Extract 5 key points from this text:\n\n{document}"
key_points = llm.invoke(step1_prompt)

# Step 2 — Summarize key points
step2_prompt = f"Summarize these points in 2 sentences:\n\n{key_points}"
summary = llm.invoke(step2_prompt)

# Step 3 — Generate action items
step3_prompt = f"Based on this summary, list 3 action items:\n\n{summary}"
actions = llm.invoke(step3_prompt)
```

---

## Types of Chains

| Type | Description | Example |
|------|-------------|---------|
| Sequential | Output feeds directly into next prompt | Summarize → Translate → Format |
| Branching | Different paths based on output | Classify → Route to specialist prompt |
| Parallel | Multiple prompts run simultaneously | Extract facts + Extract tone → Combine |
| Recursive | Same prompt applied repeatedly | Refine draft until quality threshold met |

---

## LangChain Implementation

```python
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain.prompts import PromptTemplate

# Chain 1 — Extract
extract_prompt = PromptTemplate(
    input_variables=["document"],
    template="Extract key findings from:\n{document}"
)

# Chain 2 — Summarize
summary_prompt = PromptTemplate(
    input_variables=["findings"],
    template="Summarize these findings:\n{findings}"
)

chain = SimpleSequentialChain(chains=[
    LLMChain(llm=llm, prompt=extract_prompt),
    LLMChain(llm=llm, prompt=summary_prompt)
])

result = chain.run(document)
```

---

## What I Apply

Used prompt chaining in my [Agentic RAG Research Assistant](https://github.com/adheethii/agentic-rag-ai-research-assistant) — the pipeline first retrieves relevant chunks, then passes them to a prompt that synthesizes the answer, then optionally passes the answer to a summarization prompt.

---

## Key Takeaway

> Prompt chaining turns one hard problem into many easy ones. Each step is focused, verifiable, and improvable independently. It's the foundation of all LLM pipelines and agentic systems.
