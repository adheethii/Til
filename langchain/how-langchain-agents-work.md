# How LangChain Agents Work

**Date:** 2026-05-28

## What is a LangChain Agent?

A LangChain agent is an LLM that can **decide what actions to take** and **use tools** to complete a task — instead of just generating a static response.

Normal LLM: Question → Answer  
Agent: Question → Think → Use Tool → Observe Result → Think Again → Answer

---

## How It Works (ReAct Loop)

```
User Input
    ↓
1. THINK — LLM reasons about what to do next
    ↓
2. ACT — LLM chooses a tool and inputs to use
    ↓
3. OBSERVE — Tool runs and returns result
    ↓
4. THINK AGAIN — LLM processes the result
    ↓
Repeat until task is complete
    ↓
Final Answer
```

This loop is called **ReAct (Reasoning + Acting)**.

---

## Key Components

| Component | Role |
|-----------|------|
| LLM | The brain — decides what to do |
| Tools | Functions the agent can call (search, calculator, retriever) |
| Agent Executor | Runs the think-act-observe loop |
| Memory | Optionally stores conversation history |

---

## Simple Code Example

```python
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.llms import Ollama

llm = Ollama(model="llama3")

tools = [
    Tool(
        name="Search",
        func=lambda q: "Result for: " + q,
        description="Use this to search for information"
    )
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

agent.run("What is the capital of France?")
```

---

## Types of Agents in LangChain

| Agent Type | When to Use |
|------------|-------------|
| `ZERO_SHOT_REACT_DESCRIPTION` | General purpose, no memory |
| `CONVERSATIONAL_REACT_DESCRIPTION` | Multi-turn conversations |
| `OPENAI_FUNCTIONS` | When using OpenAI function calling |
| Custom Agent | Full control over reasoning logic |

---

## Agents vs Chains

| | Chain | Agent |
|--|-------|-------|
| Flow | Fixed, predefined steps | Dynamic, decided by LLM |
| Tools | No | Yes |
| Flexibility | Low | High |
| Best for | Predictable tasks | Open-ended tasks |

---

## What I Built

Used agents in my [Agentic RAG Research Assistant](https://github.com/adheethii/agentic-rag-ai-research-assistant) — the agent decides whether to search the vector store, summarize a document, or perform a web search based on the user's query.

---

## Key Takeaway

> A LangChain agent is an LLM with superpowers — it can reason, pick tools, observe results, and loop until the task is done. The magic is in the ReAct loop.
