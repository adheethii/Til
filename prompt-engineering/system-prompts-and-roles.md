# System Prompts and Roles Explained

**Date:** 2026-06-05

## What is a System Prompt?

A system prompt is a hidden instruction given to the LLM **before** the conversation starts. It sets the behavior, tone, and personality of the model for the entire session.

```
[System Prompt] ← hidden, set by developer
[User Message]  ← what the user types
[AI Response]   ← shaped by both
```

---

## How it Works

```python
response = client.messages.create(
    model="claude-sonnet",
    system="You are a helpful data science tutor.
            Explain concepts simply. Use analogies.
            Always give a code example.",   # ← system prompt
    messages=[
        {"role": "user", "content": "What is overfitting?"}
    ]
)
```

Without the system prompt → generic answer.
With it → tutor-style answer with analogy and code.

---

## Role Prompting

Assigning a role makes the LLM respond from that perspective.

```
"You are an expert Python developer with 10 years
of experience. Review this code and suggest improvements."

vs

"You are a patient teacher explaining to a 10-year-old.
Explain what a for loop does."
```

Same question, completely different responses.

---

## Common System Prompt Patterns

```
# Persona
"You are MediBot, a hospital assistant that helps
patients find the right department."

# Format control
"Always respond in JSON format only.
No extra text or explanation."

# Constraint
"You only answer questions about data science.
Politely decline anything off-topic."

# Tone
"You are friendly, concise, and never use jargon."
```

---

## User vs System vs Assistant Roles

| Role | Who | Purpose |
|------|-----|---------|
| `system` | Developer | Sets overall behavior |
| `user` | End user | The actual question |
| `assistant` | LLM | The response |

---

## What I Apply

Used system prompts in my [Agentic RAG Research Assistant](https://github.com/adheethii/agentic-rag-ai-research-assistant) — the system prompt tells the LLM to only answer from retrieved documents and cite sources, preventing hallucination.

---

## Key Takeaway

> System prompts are the most powerful tool in prompt engineering. They shape the entire behavior of the model before the user even types anything. Role + constraints + format in the system prompt = consistent, reliable AI apps.
