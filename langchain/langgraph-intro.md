# Introduction to LangGraph

**Date:** 2026-07-08

## What is LangGraph?

LangGraph is a framework built on top of LangChain for building **stateful, multi-agent workflows** — where multiple AI agents collaborate, loop, and make decisions.

```
LangChain → Single agent, linear flow
LangGraph  → Multiple agents, cyclic flow, state management
```

---

## Why LangGraph?

```
LangChain agents: Question → Think → Act → Answer (simple)
LangGraph:        Multiple agents with roles, loops, human approval
                  → much more powerful and controllable
```

---

## Core Concepts

### State
LangGraph passes a shared **state** between nodes — each node reads and updates it.

```python
from typing import TypedDict, List

class AgentState(TypedDict):
    messages: List[str]
    current_agent: str
    result: str
    iteration: int
```

### Nodes
Each node is a function that processes state:

```python
def researcher_node(state: AgentState):
    # Research the topic
    result = llm.invoke(f"Research: {state['messages'][-1]}")
    return {"messages": state["messages"] + [result]}

def writer_node(state: AgentState):
    # Write based on research
    result = llm.invoke(f"Write based on: {state['messages'][-1]}")
    return {"result": result}
```

### Edges
Edges connect nodes — can be conditional:

```python
from langgraph.graph import StateGraph, END

workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("researcher", researcher_node)
workflow.add_node("writer", writer_node)

# Add edges
workflow.set_entry_point("researcher")
workflow.add_edge("researcher", "writer")
workflow.add_edge("writer", END)

app = workflow.compile()
```

---

## Simple Multi-Agent Example

```python
from langgraph.graph import StateGraph, END
from langchain_ollama import OllamaLLM
from typing import TypedDict

llm = OllamaLLM(model="llama3")

class State(TypedDict):
    topic: str
    research: str
    final_answer: str

def research_agent(state: State):
    result = llm.invoke(f"Research this topic briefly: {state['topic']}")
    return {"research": result}

def answer_agent(state: State):
    result = llm.invoke(
        f"Based on this research: {state['research']}\n"
        f"Give a concise answer about: {state['topic']}"
    )
    return {"final_answer": result}

# Build graph
graph = StateGraph(State)
graph.add_node("researcher", research_agent)
graph.add_node("answerer", answer_agent)
graph.set_entry_point("researcher")
graph.add_edge("researcher", "answerer")
graph.add_edge("answerer", END)

app = graph.compile()

result = app.invoke({"topic": "What is RAG?"})
print(result["final_answer"])
```

---

## LangGraph vs LangChain Agents

| | LangChain Agent | LangGraph |
|--|----------------|-----------|
| Flow | Linear | Cyclic / Graph |
| State | Limited | Full state management |
| Multi-agent | Basic | First-class support |
| Human-in-loop | Hard | Built-in |
| Debugging | Difficult | Visual graph |

---

## Key Takeaway

> LangGraph is the next level after LangChain agents — it enables true multi-agent workflows with shared state, cycles, and conditional routing. Think of it as building a flowchart where each node is an AI agent and edges define the flow of information.
