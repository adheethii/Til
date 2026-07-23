# LangChain Output Parsers

**Date:** 2026-07-23

## What are Output Parsers?

Output parsers convert an LLM's raw text response into structured
Python objects — dicts, Pydantic models, lists — instead of manually
parsing strings yourself.

```
Raw LLM output: "The sentiment is positive with 0.87 confidence"
                        ↓ (parser)
Structured:     {"sentiment": "positive", "confidence": 0.87}
```

---

## StrOutputParser (Simplest)

```python
from langchain_ollama import OllamaLLM
from langchain.schema.output_parser import StrOutputParser

llm = OllamaLLM(model="llama3")
parser = StrOutputParser()

chain = llm | parser
result = chain.invoke("What is RAG?")
# result is a plain string, extracted from the LLM's message object
```

---

## PydanticOutputParser (Structured, Type-safe)

```python
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from pydantic import BaseModel, Field

class SentimentResult(BaseModel):
    sentiment: str = Field(description="positive, negative, or neutral")
    confidence: float = Field(description="confidence score 0 to 1")
    reasoning: str = Field(description="brief explanation")

parser = PydanticOutputParser(pydantic_object=SentimentResult)

prompt = PromptTemplate(
    template="Analyze sentiment of this text.\n{format_instructions}\n\nText: {text}",
    input_variables=["text"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = prompt | llm | parser

result = chain.invoke({"text": "I love this product!"})
print(result.sentiment)    # "positive" — a real Python attribute, type-checked
print(result.confidence)   # 0.92
```

`parser.get_format_instructions()` automatically generates the JSON
schema instructions injected into the prompt — you don't write them
by hand.

---

## JsonOutputParser (Simpler than Pydantic, still structured)

```python
from langchain_core.output_parsers import JsonOutputParser

parser = JsonOutputParser()

prompt = PromptTemplate(
    template="Return a JSON object with 'answer' and 'confidence' keys.\n{format_instructions}\n\nQuestion: {question}",
    input_variables=["question"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = prompt | llm | parser
result = chain.invoke({"question": "What is FAISS?"})
# result is a plain dict: {"answer": "...", "confidence": 0.9}
```

---

## Handling Parser Failures — OutputFixingParser

LLMs sometimes produce malformed output (invalid JSON, missing fields).
Rather than crashing, use a self-correcting parser:

```python
from langchain.output_parsers import OutputFixingParser

base_parser = PydanticOutputParser(pydantic_object=SentimentResult)

fixing_parser = OutputFixingParser.from_llm(
    parser=base_parser,
    llm=llm   # uses the LLM to FIX its own malformed output
)

# If the first attempt produces invalid output, fixing_parser
# automatically asks the LLM to correct it before failing
result = fixing_parser.parse(raw_llm_output)
```

---

## Why This Matters for Production

```
Without output parsers:
response = llm.invoke(prompt)
data = json.loads(response)   # crashes if LLM adds extra text/backticks

With output parsers:
- Automatic format instructions injected into the prompt
- Type validation (Pydantic catches wrong types immediately)
- Self-correction available for malformed output
- Consistent, predictable structure for downstream code
```

---

## What I Apply

Used a similar JSON-parsing pattern (manual, with regex fallback) in my
[Agentic RAG Research Assistant](https://github.com/adheethii/agentic-rag-ai-research-assistant)
and [AI Interview Simulator](https://github.com/adheethii/ai-interview-simulator) —
`PydanticOutputParser` would be a cleaner replacement for the manual
`json.loads()` + regex approach currently used there.

---

## Key Takeaway

> Output parsers turn unreliable raw LLM text into structured, type-safe Python objects. PydanticOutputParser is the strongest choice when downstream code needs guaranteed structure — it validates types AND auto-generates the format instructions for your prompt. OutputFixingParser adds resilience by using the LLM to self-correct malformed output instead of crashing.
