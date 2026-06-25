# LangChain Memory Types

**Date:** 2026-06-25

## What is Memory in LangChain?

LLMs have no memory between calls — each call is stateless. LangChain memory adds conversation history so the LLM can refer to previous messages.

```
Without memory: Each message is independent — LLM forgets everything
With memory:    LLM remembers the conversation context
```

---

## Types of Memory

### 1. ConversationBufferMemory
Stores the full conversation history.

```python
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
memory.chat_memory.add_user_message("My name is Adheethi")
memory.chat_memory.add_ai_message("Nice to meet you, Adheethi!")

print(memory.load_memory_variables({}))
# → {"history": "Human: My name is Adheethi\nAI: Nice to meet you, Adheethi!"}
```

**Best for:** Short conversations. Simple to use.
**Downside:** Gets expensive with long conversations.

---

### 2. ConversationBufferWindowMemory
Only keeps the last K messages.

```python
from langchain.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(k=3)  # keep last 3 exchanges
```

**Best for:** Long conversations where only recent context matters.

---

### 3. ConversationSummaryMemory
Summarizes old messages to save tokens.

```python
from langchain.memory import ConversationSummaryMemory
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")
memory = ConversationSummaryMemory(llm=llm)
```

**Best for:** Very long conversations. Saves tokens.
**Downside:** Loses specific details in summaries.

---

## Memory in a Chain

```python
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")
memory = ConversationBufferMemory()

conversation = ConversationChain(llm=llm, memory=memory, verbose=True)

conversation.predict(input="My name is Adheethi")
conversation.predict(input="What is my name?")
# → "Your name is Adheethi"  ✅ remembers!
```

---

## Memory Comparison

| Memory Type | Stores | Token Cost | Best For |
|-------------|--------|------------|----------|
| Buffer | Full history | High | Short chats |
| Window | Last K messages | Medium | Medium chats |
| Summary | Compressed history | Low | Long chats |

---

## Key Takeaway

> LangChain memory gives stateless LLMs the ability to remember conversations. Use Buffer for short chats, Window for medium chats, and Summary for long chats. Memory is essential for any chatbot or conversational AI application.
