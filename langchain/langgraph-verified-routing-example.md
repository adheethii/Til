# LangGraph — A Real Conditional Routing Example (Ticket Classifier)

**Date:** 2026-07-29

## Why This Note Is Different

Earlier LangGraph notes (`langgraph-conditional-edges.md`,
`langgraph-multi-agent-example.md`) covered the concepts well but
leaned on illustrative code that wasn't run against a real graph
compile. This one is a complete, self-contained example that was
actually executed and verified — every assertion below genuinely
passed, not just described.

---

## The Task

A support ticket classifier: read incoming ticket text, route it
to billing / technical / general support, and confirm the routing
worked correctly — a realistic, small version of a pattern used
constantly in production (customer support triage, content
moderation routing, request classification).

---

## Full Working Code

```python
from langgraph.graph import StateGraph, END
from typing import TypedDict

class TicketState(TypedDict):
    ticket_text: str
    category: str
    response: str

def classify_ticket(state: TicketState) -> dict:
    """In production, this would call an LLM. Kept as simple
    keyword matching here so the example runs without needing
    a live model — the GRAPH STRUCTURE is what's being
    demonstrated, not the classification quality itself."""
    text = state["ticket_text"].lower()
    if "refund" in text or "charge" in text or "billing" in text:
        category = "billing"
    elif "broken" in text or "error" in text or "bug" in text:
        category = "technical"
    else:
        category = "general"
    return {"category": category}

def route_by_category(state: TicketState) -> str:
    """The router function LangGraph calls to decide the next node.
    Must return a string matching one of the keys in the mapping
    passed to add_conditional_edges below."""
    return state["category"]

def handle_billing(state: TicketState) -> dict:
    return {"response": "Routed to billing specialist."}

def handle_technical(state: TicketState) -> dict:
    return {"response": "Routed to technical support."}

def handle_general(state: TicketState) -> dict:
    return {"response": "Routed to general support."}

# ── Build the graph ──
graph = StateGraph(TicketState)
graph.add_node("classify", classify_ticket)
graph.add_node("billing", handle_billing)
graph.add_node("technical", handle_technical)
graph.add_node("general", handle_general)

graph.set_entry_point("classify")

graph.add_conditional_edges(
    "classify",
    route_by_category,
    {
        "billing": "billing",
        "technical": "technical",
        "general": "general",
    }
)

graph.add_edge("billing", END)
graph.add_edge("technical", END)
graph.add_edge("general", END)

app = graph.compile()
```

---

## Running It — Actual Verified Output

```python
result = app.invoke({
    "ticket_text": "I was charged twice for my subscription",
    "category": "",
    "response": ""
})
print(result)
```

```
{
  'ticket_text': 'I was charged twice for my subscription',
  'category': 'billing',
  'response': 'Routed to billing specialist.'
}
```

Tested against three different inputs — a billing complaint, a
technical bug report, and a general question — and all three
routed to the correct branch, confirmed with real assertions:

```python
assert result["category"] == "billing"
assert result["response"] == "Routed to billing specialist."
```

All passed.

---

## The Part Worth Understanding Deeply — `add_conditional_edges`

```python
graph.add_conditional_edges(
    "classify",           # FROM this node
    route_by_category,    # CALL this function to decide where next
    {                      # MAP its return value to a destination node
        "billing": "billing",
        "technical": "technical",
        "general": "general",
    }
)
```

The router function's return value is just a string — LangGraph
looks that string up in the mapping dict to decide which node
runs next. If the router returns something not in the mapping,
it raises an error at runtime, not at graph-build time — worth
testing all expected branches explicitly, as done above, rather
than assuming the mapping is exhaustive.

---

## Swapping in a Real LLM

Replacing the keyword-matching `classify_ticket` with an actual
LLM call is a small, contained change — only that one function's
body changes, the graph structure stays identical:

```python
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3", temperature=0.1)

def classify_ticket(state: TicketState) -> dict:
    prompt = f"""Classify this support ticket as exactly one word:
billing, technical, or general.

Ticket: {state['ticket_text']}

Category:"""
    category = llm.invoke(prompt).strip().lower()
    if category not in ["billing", "technical", "general"]:
        category = "general"   # fallback if the LLM returns something unexpected
    return {"category": category}
```

The fallback line matters — LLM output isn't guaranteed to match
one of the three expected strings exactly, and an unhandled
mismatch here would crash the conditional edge lookup.

---

## Key Takeaway

> The graph-building mechanics (nodes, conditional edges, the router-function-returns-a-string-that-maps-to-a-node pattern) are the reusable skill — the classification logic inside any individual node is swappable, whether it's keyword matching, an LLM call, or something else entirely. Always account for the LLM potentially returning something outside your expected category set when swapping in a real model, since the conditional-edge mapping has no built-in fallback of its own.
