# Role Prompting Techniques

**Date:** 2026-06-09

## What is Role Prompting?

Role prompting is assigning a specific persona or identity to the LLM before asking your question. It shifts the model's perspective, tone, vocabulary, and depth of response.

```
Without role: "Explain neural networks"
With role:    "You are a university professor teaching
               deep learning. Explain neural networks
               to a first-year student."
```

---

## Why it Works

LLMs are trained on vast amounts of text from different domains. Assigning a role **activates** the relevant subset of that knowledge and communication style.

---

## Common Role Patterns

### Expert Role
```
"You are a senior machine learning engineer
with 10 years of experience at top AI companies.
Review this code and suggest improvements."
```

### Teacher Role
```
"You are a patient tutor explaining concepts
to a complete beginner. Use simple language,
analogies, and avoid technical jargon."
```

### Critic Role
```
"You are a harsh but fair code reviewer.
Point out every flaw, inefficiency, and
bad practice in this code."
```

### Domain Specialist
```
"You are a medical data analyst specializing
in hospital management systems. Analyze this
patient visit data and identify patterns."
```

---

## Stacking Roles with Constraints

The most powerful pattern — role + task + constraint:

```
"You are an expert prompt engineer.
Your task is to improve the following prompt
to get better results from an LLM.
Keep your response under 100 words and
explain WHY each change improves the prompt."
```

---

## Role Prompting for Different Outputs

| Goal | Role to Assign |
|------|---------------|
| Simple explanation | Patient teacher / tutor |
| Code review | Senior developer / architect |
| Creative writing | Experienced author |
| Data analysis | Data scientist / analyst |
| Career advice | HR professional / recruiter |
| Debugging | Expert in that language |

---

## What to Avoid

```
❌ Too vague:
"You are an expert. Help me."

✅ Specific and useful:
"You are an expert in LangChain and RAG systems.
Help me debug why my retriever returns irrelevant chunks."
```

---

## Key Takeaway

> Role prompting works because it narrows the model's focus to a specific domain, style, and depth. The more specific the role, the more tailored the response. Combine role + task + constraint for the best results.
