# Prompt Engineering for Agents

**Date:** 2026-06-25

## What are AI Agents?

AI agents are LLMs that can **decide what actions to take**, use tools, and complete multi-step tasks autonomously. Prompting agents is different from prompting regular LLMs — you're not just getting text, you're directing behavior.

```
Regular LLM: Question → Answer
Agent:       Goal → Think → Act → Observe → Think → Act → Final Answer
```

---

## The Agent System Prompt

The system prompt is the most critical part of agent prompting — it defines the agent's identity, tools, and behavior.

```python
AGENT_SYSTEM_PROMPT = """You are a research assistant with access to tools.

Your goal: Answer the user's question as accurately as possible.

Available tools:
- search: Search the web for current information
- retriever: Search uploaded documents
- calculator: Perform mathematical calculations

Rules:
1. ALWAYS think before acting — explain your reasoning
2. Use tools when you need real information — don't guess
3. If one tool fails, try another approach
4. Give a clear, concise final answer after gathering information
5. If you cannot find the answer, say so honestly
"""
```

---

## ReAct Prompt Pattern for Agents

```
Thought: I need to find the current price of Bitcoin.
Action: search
Action Input: "Bitcoin price today 2026"
Observation: Bitcoin is currently trading at $67,432.

Thought: I have the information needed.
Final Answer: Bitcoin is currently trading at approximately $67,432.
```

---

## Tool Description Prompting

How you describe tools matters enormously:

```python
# ❌ Vague tool description
Tool(name="search", description="searches things")

# ✅ Clear tool description
Tool(
    name="web_search",
    description="""Search the web for current information.
    Use this when you need: recent news, current prices,
    today's date, or any information that might have changed recently.
    Input: a specific search query string."""
)
```

---

## Controlling Agent Behavior

```python
# Limit reasoning steps to prevent infinite loops
executor = AgentExecutor(
    agent=agent,
    tools=tools,
    max_iterations=5,          # max tool calls
    max_execution_time=30,     # timeout in seconds
    early_stopping_method="generate",
    verbose=True
)
```

---

## Prompt Tips for Reliable Agents

| Tip | Why |
|-----|-----|
| Define tools clearly | Agent picks right tool |
| Set explicit stopping conditions | Prevents infinite loops |
| Add "think before acting" instruction | Reduces wrong tool use |
| Define failure behavior | Agent handles errors gracefully |
| Keep system prompt focused | Too many instructions = confusion |

---

## What I Applied

Used agent prompting in my [Agentic RAG Research Assistant](https://github.com/adheethii/agentic-rag-ai-research-assistant) — the system prompt defines 3 tools (retriever, summarizer, web search) with clear descriptions so the agent selects the right one based on query intent.

---

## Key Takeaway

> Agent prompts must do three things: define the agent's role clearly, describe each tool precisely (the agent picks tools based on descriptions), and set behavioral guardrails like max iterations. Vague tool descriptions are the #1 cause of agent failures.
