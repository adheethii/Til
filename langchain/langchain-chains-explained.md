# LangChain Chains Explained

**Date:** 2026-06-26

## What are Chains in LangChain?

Chains connect multiple components — prompt + LLM + output parser — into a reusable pipeline.

```
Prompt → LLM → Output Parser → Result
```

---

## The Modern LCEL Syntax

LangChain Expression Language (LCEL) uses | to chain components:

```python
from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from langchain.schema.output_parser import StrOutputParser

llm = OllamaLLM(model="llama3")
parser = StrOutputParser()

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in one sentence."
)

chain = prompt | llm | parser
result = chain.invoke({"topic": "RAG"})
```

---

## Sequential Chain

```python
outline_chain = outline_prompt | llm | parser
write_chain = write_prompt | llm | parser

full_chain = {"outline": outline_chain} | write_chain
result = full_chain.invoke({"topic": "Machine Learning"})
```

---

## Common Chain Types

| Chain | Purpose |
|-------|---------|
| LLMChain | Basic prompt + LLM |
| SequentialChain | Output feeds next chain |
| RetrievalQA | RAG — retrieve + answer |
| ConversationChain | Chat with memory |

---

## Key Takeaway

> LangChain chains are pipelines: prompt → LLM → parser. LCEL's | operator makes them clean and readable. Use sequential chains when one step's output feeds the next — it's the foundation of all LangChain applications.
