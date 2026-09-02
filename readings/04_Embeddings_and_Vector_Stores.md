# 04 — Embeddings, Semantic Search and Vector Stores

> 📓 **Hands-on Notebook:** [04 — Embeddings and Vector Stores](../notebooks/04_Embeddings_and_Vector_Stores.ipynb)

**Level:** Intermediate | **Reading time:** 30-40 minutes

## Learning Objectives

- Understand why keyword search is sometimes insufficient
- Learn what embeddings are and how they work
- Understand cosine similarity
- Know the difference between embedding models and chat models
- Learn how vector stores enable semantic search

---

## 1. Why Keyword Search Is Insufficient

**Keyword search** matches exact words. It fails when:
- A user asks about "ML model evaluation" but documents say "assessing model performance"
- Synonyms are used (fast/quick, big/large)
- The concept is described differently than it's asked about

**Semantic search** understands meaning, not just words.

| Query | Keyword Match | Semantic Match |
|-------|--------------|----------------|
| "How to assess model quality?" | Low (no exact match) | High (matches evaluation content) |
| "ML model performance assessment" | Medium | High |
| "Evaluating predictive models" | Low | High |

## 2. What Are Embeddings?

An **embedding** is a list of numbers (vector) that represents the meaning of a text. Similar texts get similar vectors.

```
"The cat sat on the mat" → [0.2, 0.8, 0.1, ...]
"A feline rested on the rug" → [0.2, 0.7, 0.1, ...]  (similar!)
"The stock market crashed" → [0.9, 0.1, 0.6, ...]     (different!)
```

**Key insight:** Embeddings capture *meaning*, not *words*.

## 3. Cosine Similarity

**Cosine similarity** measures the angle between two vectors. Closer angle = more similar meaning.

```
Similarity = cos(angle between vectors)

1.0 = identical meaning
0.7 = very similar
0.3 = somewhat related
0.0 = unrelated
-1.0 = opposite meaning
```

## 4. Chat Models vs Embedding Models

| Aspect | Chat Model | Embedding Model |
|--------|-----------|----------------|
| **Purpose** | Generate text | Convert text to vectors |
| **Input** | Messages | Text strings |
| **Output** | Text response | List of numbers |
| **Use case** | Conversation, generation | Search, similarity |
| **Example** | gpt-4o-mini | text-embedding-3-small |

## 5. Documents

A **Document** in LangChain has two parts:
- `page_content`: The actual text
- `metadata`: Additional information (source, topic, date, etc.)

Metadata is crucial for filtering search results.

## 6. Vector Stores

A **vector store** (or vector database) stores embeddings and enables fast similarity search.

**What it does:**
1. Stores text + embeddings
2. When you search, finds the most similar vectors
3. Returns the original text

**ChromaDB** is used in this repository because:
- Runs locally (no server needed)
- Lightweight and fast
- Stores data on disk (persists between sessions)
- Simple API

## 7. Similarity Search

When you search a vector store:
1. Your query is converted to an embedding
2. The store finds the most similar stored embeddings
3. Returns the corresponding documents

**Top-k:** You can control how many results to return (e.g., top 3 most similar).

## 8. API vs Local Embeddings

| Aspect | API (OpenAI) | Local (Ollama) |
|--------|-------------|----------------|
| Quality | Generally higher | Model-dependent |
| Cost | Per-token | Free |
| Privacy | Data leaves machine | Data stays local |
| Speed | Network + compute | Hardware-dependent |

## 9. Common Mistakes

- **Using chat models for embeddings:** They are different tools
- **Ignoring metadata:** Metadata filtering dramatically improves search quality
- **Too small k:** You might miss relevant documents
- **Too large k:** Irrelevant documents dilute the context

## 10. Key Takeaways

- Embeddings convert text to numerical vectors capturing meaning
- Cosine similarity measures how close two vectors are
- Vector stores enable fast semantic search over large document collections
- Metadata improves search precision
- API and local embeddings are both viable options

## 11. Further Reading

**Official Documentation:**
- [Embeddings (LangChain)](https://python.langchain.com/docs/concepts/embedding_models/)
- [Vector Stores (LangChain)](https://python.langchain.com/docs/concepts/vectorstores/)
- [ChromaDB](https://docs.trychroma.com/)

**Research:**
- [BERT: Pre-training of Deep Bidirectional Transformers](https://arxiv.org/abs/1810.04805) — foundational embedding research

---

**Previous:** [03 — LCEL and Chains](03_LCEL_and_Chains.md)
**Next:** [05 — RAG Applications](05_RAG_Applications.md)

**Back to:** [Reading Index](README.md)
