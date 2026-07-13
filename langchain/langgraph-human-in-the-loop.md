# LangGraph Human-in-the-Loop

**Date:** 2026-07-13

## What is Human-in-the-Loop?

Human-in-the-loop (HITL) pauses the agent workflow to get human approval or input before continuing — critical for high-stakes actions.

```
Agent decides action → PAUSE → Human approves/edits → Agent continues
```

---

## Why HITL Matters

```
❌ Without HITL: Agent sends email, deletes file, makes payment
                 → all automatically, no oversight

✅ With HITL: Agent proposes action → human reviews → then executes
              → safety for irreversible or sensitive actions
```

---

## Implementing Interrupts in LangGraph

```python
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from typing import TypedDict

class State(TypedDict):
    task: str
    proposed_action: str
    approved: bool
    result: str

def propose_action(state: State):
    return {"proposed_action": f"Send email about: {state['task']}"}

def execute_action(state: State):
    return {"result": f"Executed: {state['proposed_action']}"}

graph = StateGraph(State)
graph.add_node("propose", propose_action)
graph.add_node("execute", execute_action)
graph.set_entry_point("propose")
graph.add_edge("propose", "execute")
graph.add_edge("execute", END)

memory = MemorySaver()

# Interrupt BEFORE the execute node — pause for human approval
app = graph.compile(
    checkpointer=memory,
    interrupt_before=["execute"]   # ← pauses here!
)
```

---

## Running with Interrupts

```python
config = {"configurable": {"thread_id": "task-1"}}

# First call — stops before "execute" node
result = app.invoke({"task": "notify team about deadline"}, config)
print(result["proposed_action"])
# → "Send email about: notify team about deadline"

# Human reviews... then approve to continue
final_result = app.invoke(None, config)   # None = continue from pause
print(final_result["result"])
# → "Executed: Send email about: notify team about deadline"
```

---

## Allowing Human Edits Before Continuing

```python
# Get current state at the pause point
current_state = app.get_state(config)
print(current_state.values["proposed_action"])

# Human edits the proposed action
app.update_state(config, {"proposed_action": "Send SLACK message instead"})

# Continue with the edited state
final_result = app.invoke(None, config)
```

---

## Use Cases for HITL

| Scenario | Why HITL Needed |
|----------|-----------------|
| Sending emails | Prevent unwanted communications |
| Financial transactions | Prevent costly mistakes |
| Deleting data | Prevent accidental data loss |
| Code deployment | Review before production changes |
| Customer-facing responses | Ensure quality/tone before sending |

---

## Key Takeaway

> Human-in-the-loop is essential for production agentic systems — never let AI agents execute high-stakes actions without oversight. LangGraph's `interrupt_before` pauses the graph at critical nodes. Combined with checkpointing, humans can review, edit, or approve before the agent continues.
