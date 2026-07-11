# LangGraph State Management

**Date:** 2026-07-11

## What is State in LangGraph?

State is the shared data structure that flows through your graph — every node reads from it and can update it.

```
State enters Node A → Node A updates state → State enters Node B → ...
```

---

## Defining State with TypedDict

```python
from typing import TypedDict, List, Annotated
import operator

class AgentState(TypedDict):
    question: str
    documents: List[str]
    answer: str
    iteration_count: int
```

---

## Updating vs Replacing State

By default, returning from a node **replaces** that key:

```python
def node_a(state: AgentState):
    return {"answer": "new answer"}   # replaces state["answer"]
```

To **append** instead of replace, use `Annotated` with an operator:

```python
from typing import Annotated
import operator

class AgentState(TypedDict):
    messages: Annotated[List[str], operator.add]   # appends!

def node_a(state: AgentState):
    return {"messages": ["Hello"]}   # ADDS to existing list, not replace
```

---

## Full Example with Message History

```python
from typing import TypedDict, Annotated, List
import operator
from langgraph.graph import StateGraph, END

class ChatState(TypedDict):
    messages: Annotated[List[str], operator.add]
    turn_count: int

def user_node(state: ChatState):
    return {
        "messages": [f"User: {state['messages'][-1] if state['messages'] else 'Hi'}"],
        "turn_count": state.get("turn_count", 0) + 1
    }

def ai_node(state: ChatState):
    return {
        "messages": [f"AI: Response to turn {state['turn_count']}"]
    }

graph = StateGraph(ChatState)
graph.add_node("user", user_node)
graph.add_node("ai", ai_node)
graph.set_entry_point("user")
graph.add_edge("user", "ai")
graph.add_edge("ai", END)

app = graph.compile()
result = app.invoke({"messages": [], "turn_count": 0})
print(result["messages"])
# → ['User: Hi', 'AI: Response to turn 1']
```

---

## Persisting State (Checkpointing)

```python
from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()
app = graph.compile(checkpointer=memory)

# Now state persists across invocations with same thread_id
config = {"configurable": {"thread_id": "user-123"}}
result1 = app.invoke({"messages": ["Hello"]}, config)
result2 = app.invoke({"messages": ["What did I say?"]}, config)
# result2 has access to result1's state! ✅
```

---

## Key Takeaway

> State is the backbone of LangGraph — it's what makes multi-step agent workflows possible. Use TypedDict to define structure. By default, node returns REPLACE state keys — use `Annotated[List, operator.add]` to APPEND instead. Checkpointing enables conversation memory across multiple invocations.
