# ReAct Prompting (Reason + Act)

**Date:** 2026-06-24

## What is ReAct?

**ReAct = Reasoning + Acting**

ReAct is a prompting technique where the LLM alternates between **thinking** (reasoning) and **doing** (acting with tools) — just like how humans solve problems.

```
Think → Act → Observe → Think → Act → Observe → Answer
```

---

## Why ReAct?

Standard prompting → LLM just generates text
Chain of Thought → LLM reasons but can't act
ReAct → LLM reasons AND uses tools → much more powerful

---

## The ReAct Loop

```
Question: What is the population of Kerala?

Thought 1: I need to find the current population of Kerala.
Action 1: Search["Kerala population 2024"]
Observation 1: Kerala has a population of approximately 35 million.

Thought 2: I now have the answer.
Action 2: Finish["Kerala's population is approximately 35 million."]
```

Each cycle:
- **Thought** — LLM reasons about what to do next
- **Action** — LLM calls a tool (search, calculator, database)
- **Observation** — Tool returns a result
- Repeat until answer is found

---

## ReAct vs Chain of Thought

| | Chain of Thought | ReAct |
|--|-----------------|-------|
| Reasoning | ✅ Yes | ✅ Yes |
| Tool use | ❌ No | ✅ Yes |
| Real-time data | ❌ No | ✅ Yes |
| Best for | Math, logic | Research, Q&A with tools |

---

## LangChain ReAct Agent

```python
from langchain.agents import create_react_agent, AgentExecutor
from langchain.tools import Tool
from langchain_ollama import OllamaLLM
from langchain import hub

llm = OllamaLLM(model="llama3")

# Define tools the agent can use
tools = [
    Tool(
        name="Search",
        func=lambda q: f"Search result for: {q}",
        description="Search the web for current information"
    ),
    Tool(
        name="Calculator",
        func=lambda x: str(eval(x)),
        description="Evaluate math expressions"
    )
]

# ReAct prompt template
prompt = hub.pull("hwchase17/react")

# Create ReAct agent
agent = create_react_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

result = executor.invoke({"input": "What is 25% of Kerala's population?"})
```

---

## ReAct in My Project

My [Agentic RAG Research Assistant](https://github.com/adheethii/agentic-rag-ai-research-assistant) uses ReAct — the agent reasons about whether to use the document retriever, summarizer, or web search tool based on the query.

---

## Key Takeaway

> ReAct combines reasoning and tool use in a loop — think, act, observe, repeat. It's the foundation of all modern AI agents. The key insight is that interleaving reasoning with real-world actions makes LLMs dramatically more capable than pure text generation.
