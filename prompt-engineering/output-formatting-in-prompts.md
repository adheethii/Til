# Output Formatting in Prompts

**Date:** 2026-06-24

## What is Output Formatting?

Output formatting means **telling the LLM exactly how to structure its response** — as JSON, markdown, a list, a table, or any other format you need.

Without formatting instructions → LLM returns unstructured text
With formatting instructions → LLM returns exactly what your app needs

---

## Why it Matters

```
❌ Without format instruction:
"What are the top 3 Python libraries for ML?"

Response: "There are many great Python libraries for machine 
learning. Some of the most popular ones include Scikit-learn, 
which is great for classical ML algorithms, TensorFlow which 
is used for deep learning, and Pandas which helps with data..."

✅ With format instruction:
"List the top 3 Python libraries for ML.
Respond as a JSON array with name and use_case fields."

Response:
[
  {"name": "Scikit-learn", "use_case": "Classical ML algorithms"},
  {"name": "TensorFlow", "use_case": "Deep learning"},
  {"name": "Pandas", "use_case": "Data manipulation"}
]
```

---

## Common Output Formats

### JSON
```
"Respond ONLY in valid JSON. No extra text, no markdown backticks.
Format: {"answer": "...", "confidence": "high/medium/low"}"
```

### Markdown
```
"Format your response in markdown with:
- A ## heading
- 3 bullet points
- A code example in a code block"
```

### Table
```
"Present the comparison as a markdown table with columns:
Feature | Option A | Option B"
```

### Numbered List
```
"Give me 5 steps. Use this format:
1. [Step name]: [Brief description]"
```

### Structured Sections
```
"Respond with exactly these sections:
**Summary:** (1 sentence)
**Key Points:** (3 bullets)
**Recommendation:** (1 sentence)"
```

---

## JSON Output in FastAPI + LangChain

```python
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
import json

llm = OllamaLLM(model="llama3", temperature=0.1)

prompt = PromptTemplate(
    input_variables=["text"],
    template="""Analyze the sentiment of this text.
Respond ONLY in valid JSON with no extra text:
{{"sentiment": "positive/negative/neutral", "score": 0.0-1.0, "reason": "brief explanation"}}

Text: {text}"""
)

chain = prompt | llm

result = chain.invoke({"text": "I love this product!"})
data = json.loads(result)
print(data["sentiment"])   # → "positive"
```

---

## Tips for Reliable JSON Output

```
✅ "Respond ONLY in valid JSON. No markdown, no backticks."
✅ "Do not include any text before or after the JSON."
✅ Use low temperature (0.0-0.2) for structured output
✅ Show an example of the exact format you want
✅ Validate with json.loads() and handle errors
```

---

## Format by Use Case

| Use Case | Best Format |
|----------|-------------|
| API response | JSON |
| Documentation | Markdown |
| Data extraction | JSON |
| Step-by-step guide | Numbered list |
| Comparison | Table |
| Summary | Structured sections |
| Chat response | Plain text |

---

## Key Takeaway

> Always tell the LLM exactly what format you want — don't leave it to chance. For programmatic use (APIs, apps), always use JSON with `temperature=0.1` and validate the output. The more specific your format instruction, the more reliable the output.
