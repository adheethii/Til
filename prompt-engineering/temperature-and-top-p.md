# 🌡️ Temperature and Top-p Explained

## What are Temperature and Top-p?

Temperature and Top-p are parameters that control how a Large Language Model generates responses. They influence the balance between creativity and predictability.

---

## Temperature

Temperature controls randomness in the model's output.

- **Low Temperature (0–0.3):**
  - More deterministic
  - Focused and factual responses
  - Best for coding and summarization

- **Medium Temperature (0.5–0.7):**
  - Balanced creativity and accuracy
  - Suitable for general conversations

- **High Temperature (0.8–1.0+):**
  - More diverse and creative outputs
  - Useful for storytelling and brainstorming

### Example Prompt

**Prompt:**
> Suggest a title for a blog about AI.

**Low Temperature:**
> Understanding Artificial Intelligence

**High Temperature:**
> When Machines Dream: Exploring the Future of AI

---

## Top-p (Nucleus Sampling)

Top-p limits the model to choosing from the smallest set of words whose cumulative probability reaches a threshold.

- **Low Top-p (0.1–0.3):**
  - Safer and predictable responses

- **Medium Top-p (0.5–0.8):**
  - Balanced outputs

- **High Top-p (0.9–1.0):**
  - Greater diversity and creativity

---

## Temperature vs Top-p

| Temperature | Top-p |
|------------|--------|
| Controls randomness directly | Controls the pool of candidate tokens |
| Adjusts confidence | Adjusts diversity |
| Easier to understand | More selective generation |

---

## Recommended Settings

| Task | Temperature | Top-p |
|--------|------------|--------|
| Coding | 0.1–0.3 | 0.9 |
| Summarization | 0.2–0.4 | 0.9 |
| Question Answering | 0.2–0.5 | 0.9 |
| Brainstorming | 0.8–1.0 | 1.0 |
| Creative Writing | 0.9–1.0 | 1.0 |

---

## Key Takeaways

- Lower values produce reliable outputs.
- Higher values increase creativity.
- Start by adjusting Temperature before Top-p.
- Avoid changing both drastically at the same time.

---

## References

- OpenAI Documentation
- Anthropic Documentation
- Google Gemini Documentation
