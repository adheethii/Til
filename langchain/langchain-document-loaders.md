# LangChain Document Loaders

**Date:** 2026-06-26

## What are Document Loaders?

Document loaders load data from various sources into LangChain's Document format — ready for chunking and embedding in RAG pipelines.

```
PDF / URL / CSV → Document Loader → [Documents] → Splitter → Embeddings
```

---

## Common Loaders

```python
# PDF
from langchain.document_loaders import PyPDFLoader
loader = PyPDFLoader("paper.pdf")
documents = loader.load()

# Web URL
from langchain.document_loaders import WebBaseLoader
loader = WebBaseLoader("https://example.com")
documents = loader.load()

# CSV
from langchain.document_loaders.csv_loader import CSVLoader
loader = CSVLoader("data.csv")
documents = loader.load()

# Multiple files
from langchain.document_loaders import DirectoryLoader
loader = DirectoryLoader("./docs/", glob="**/*.pdf")
documents = loader.load()
```

---

## Document Object Structure

```python
from langchain.schema import Document

doc = Document(
    page_content="This is the text content",
    metadata={"source": "file.pdf", "page": 1}
)
```

---

## After Loading — Split

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)
```

---

## Key Takeaway

> Document loaders are the entry point of any RAG pipeline. Always check page_content and metadata after loading. Chunk size and overlap significantly affect RAG quality — 500 chunk size with 50 overlap is a good starting point.
