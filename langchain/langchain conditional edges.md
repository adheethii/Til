# LangGraph Conditional Edges

**Date:** 2026-07-10

## What are Conditional Edges?

Conditional edges in LangGraph allow the workflow to **branch based on the current state** — like if/else logic in a graph.

```
Node A → [condition] → Node B (if condition met)
                    → Node C (if condition not met)
                    → END    (if task complete)
```

---

## Why Conditional Edges?

Without conditional edges, your graph is linear — every step follows the same path. With them, the agent can **decide its own path** based on what happened.

---

## Basic Conditional Edge

```python
from langgraph.graph import StateGraph, END
from typing import TypedDict

class State(TypedDict):
    question: str
    answer: str
    needs_search: bool
    search_result: str

def router(state: State) -> str:
    """Decide which node to go to next"""
    if state["needs_search"]:
        return "search_node"
    else:
        return "answer_node"

def analyze_node(state: State):
    # Decide if web search is needed
    needs_search = "current" in state["question"].lower()
    return {"needs_search": needs_search}

def search_node(state: State):
    # Simulate web search
    return {"search_result": f"Search results for: {state['question']}"}

def answer_node(state: State):
    context = state.get("search_result", "")
    answer = f"Answer based on {'search' if context else 'knowledge'}"
    return {"answer": answer}

# Build graph
graph = StateGraph(State)
graph.add_node("analyze", analyze_node)
graph.add_node("search_node", search_node)
graph.add_node("answer_node", answer_node)

graph.set_entry_point("analyze")

# Add conditional edge from analyze
graph.add_conditional_edges(
    "analyze",          # from this node
    router,             # call this function to decide
    {
        "search_node": "search_node",   # if returns "search_node"
        "answer_node": "answer_node"    # if returns "answer_node"
    }
)

graph.add_edge("search_node", "answer_node")
graph.add_edge("answer_node", END)

app = graph.compile()
result = app.invoke({"question": "What is the current Bitcoin price?"})
```

---

## Multi-path Routing

```python
def tool_router(state: State) -> str:
    """Route to different tools based on query type"""
    query = state["question"].lower()

    if "calculate" in query or "math" in query:
        return "calculator"
    elif "search" in query or "find" in query:
        return "web_search"
    elif "document" in query or "pdf" in query:
        return "retriever"
    else:
        return "direct_answer"

graph.add_conditional_edges(
    "router_node",
    tool_router,
    {
        "calculator": "calculator_node",
        "web_search": "search_node",
        "retriever": "retriever_node",
        "direct_answer": "answer_node"
    }
)
```

---

## Loop Until Complete

```python
def should_continue(state: State) -> str:
    """Keep researching until confident"""
    if state.get("confidence", 0) >= 0.8:
        return "finish"
    elif state.get("iterations", 0) >= 5:
        return "finish"   # safety limit
    else:
        return "research_more"

graph.add_conditional_edges(
    "research_node",
    should_continue,
    {
        "research_more": "research_node",  # loop back!
        "finish": END
    }
)
```

---

## Key Takeaway

> Conditional edges are what make LangGraph truly agentic — the graph decides its own path based on state. Router functions return strings that map to node names. You can create loops, branches, and multi-path workflows — making agents that adapt to what they discover along the way.
