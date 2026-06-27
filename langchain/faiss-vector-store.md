# FAISS Vector Store in LangChain

**Date:** 2026-06-27

## What is FAISS?

FAISS (Facebook AI Similarity Search) is a library for **fast similarity search** across millions of vectors — the core of any RAG system's retrieval step.

```
Query → Embed → Search FAISS → Top-K similar chunks → LLM
```

---

## How it Works

```
1. Documents are split into chunks
2. Each chunk is converted to a vector (embedding)
3. Vectors are stored in FAISS index
4. At query time: query is embedded → nearest vectors found
5. Corresponding text chunks are retrieved → passed to LLM
```

---

## Creating a FAISS Vector Store

```python
from langchain.vectorstores import FAISS
from langchain.embeddings import OllamaEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load and split documents
loader = PyPDFLoader("document.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# Create embeddings
embeddings = OllamaEmbeddings(model="llama3")

# Build FAISS index
vectorstore = FAISS.from_documents(chunks, embeddings)
```

---

## Save and Load

```python
# Save to disk
vectorstore.save_local("faiss_index")

# Load from disk (no need to rebuild every time!)
vectorstore = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)
```

---

## Similarity Search

```python
# Search for similar chunks
query = "What is retrieval augmented generation?"
results = vectorstore.similarity_search(query, k=3)

for doc in results:
    print(doc.page_content)
    print(doc.metadata)
    print("---")
```

---

## Use as Retriever in RAG Chain

```python
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# Use in RAG chain
from langchain.chains import RetrievalQA

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)

result = qa_chain.invoke({"query": "What is RAG?"})
```

---

## What I Built

Used FAISS in my [Agentic RAG Research Assistant](https://github.com/adheethii/agentic-rag-ai-research-assistant) — documents are chunked, embedded with Ollama, and stored in a local FAISS index that persists across sessions.

---

## Key Takeaway

> FAISS converts text search into vector similarity search — much more powerful than keyword matching. Always save your FAISS index to disk so you don't rebuild it every run. The quality of embeddings directly determines retrieval quality.
