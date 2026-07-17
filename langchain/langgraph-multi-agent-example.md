# LangGraph Multi-Agent Example

**Date:** 2026-07-17

## Building a Real Multi-Agent System

A common pattern: **Planner → Researcher → Writer → Critic** — each agent has a specific role, and they pass work between each other.

```
User Task
    ↓
Planner  (breaks task into steps)
    ↓
Researcher (gathers information)
    ↓
Writer   (drafts the answer)
    ↓
Critic   (reviews, sends back if needs improvement)
    ↓
Final Output
```

---

## Full Implementation

```python
from langgraph.graph import StateGraph, END
from langchain_ollama import OllamaLLM
from typing import TypedDict

llm = OllamaLLM(model="llama3")

class ResearchState(TypedDict):
    task: str
    plan: str
    research: str
    draft: str
    critique: str
    approved: bool
    revision_count: int

# ── Planner Agent ──
def planner_agent(state: ResearchState):
    prompt = f"Break this task into a research plan: {state['task']}"
    plan = llm.invoke(prompt)
    return {"plan": plan}

# ── Researcher Agent ──
def researcher_agent(state: ResearchState):
    prompt = f"Research this plan and gather key facts: {state['plan']}"
    research = llm.invoke(prompt)
    return {"research": research}

# ── Writer Agent ──
def writer_agent(state: ResearchState):
    prompt = f"""Write a clear answer based on this research: {state['research']}
    Previous critique (if any): {state.get('critique', 'None')}"""
    draft = llm.invoke(prompt)
    return {"draft": draft}

# ── Critic Agent ──
def critic_agent(state: ResearchState):
    prompt = f"""Review this draft critically: {state['draft']}
    Is it accurate, clear, and complete? Respond with 'APPROVED' or
    give specific feedback for improvement."""
    critique = llm.invoke(prompt)
    approved = "APPROVED" in critique.upper()
    return {
        "critique": critique,
        "approved": approved,
        "revision_count": state.get("revision_count", 0) + 1
    }

# ── Router: decide if we need another revision ──
def should_revise(state: ResearchState) -> str:
    if state["approved"] or state["revision_count"] >= 3:
        return "finish"
    return "revise"

# ── Build the Graph ──
graph = StateGraph(ResearchState)

graph.add_node("planner", planner_agent)
graph.add_node("researcher", researcher_agent)
graph.add_node("writer", writer_agent)
graph.add_node("critic", critic_agent)

graph.set_entry_point("planner")
graph.add_edge("planner", "researcher")
graph.add_edge("researcher", "writer")
graph.add_edge("writer", "critic")

graph.add_conditional_edges(
    "critic",
    should_revise,
    {
        "revise": "writer",    # loop back to writer!
        "finish": END
    }
)

app = graph.compile()

result = app.invoke({
    "task": "Explain the benefits of RAG for enterprise search",
    "revision_count": 0
})

print(result["draft"])
```

---

## What Makes This "Truly Agentic"

```
✅ Multiple specialized agents (not one agent doing everything)
✅ Agents pass structured work to each other
✅ Conditional looping (critic can send writer back for revisions)
✅ Self-correction (up to 3 revision attempts)
✅ Shared state (every agent sees the full context)
```

---

## Real-World Applications

| Pattern | Use Case |
|---------|----------|
| Planner → Researcher → Writer | Content generation, reports |
| Coder → Tester → Debugger | Automated code generation |
| Router → Specialist Agents | Customer support triage |
| Generator → Critic (loop) | Self-improving outputs |

---

## Key Takeaway

> Multi-agent LangGraph systems shine when different steps genuinely need different "expertise" — planning vs researching vs writing vs critiquing are different skills. The critic-writer loop with a revision limit is a powerful self-correction pattern that single-agent systems can't easily replicate.
