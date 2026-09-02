# Post-Quiz: Embeddings & Vector Stores

**Purpose:** Test your understanding AFTER studying this topic.
**Time:** 10-15 minutes
**Questions:** 10

---

## Learning Objectives Tested

- Understand embeddings and cosine similarity
- Build vector search systems
- Use metadata for filtering

---

### Q1: What is the typical output of an embedding model for a short sentence?

- A) A single number
- B) A list of hundreds of numbers (vector)
- C) A text string
- D) A True/False value

### Q2: If two vectors have cosine similarity of 0.95, what does this mean?

- A) They are completely different
- B) They are very similar in meaning
- C) They are identical
- D) They are unrelated

### Q3: Why add metadata to documents before storing them?

- A) To make them load faster
- B) To enable filtering search results by attributes
- C) To compress the data
- D) To encrypt the content

### Q4: What happens if you set k=1 in similarity_search?

- A) The search fails
- B) Only the most similar document is returned
- C) All documents are returned
- D) The search is faster but less accurate

### Q5: 🟡 Apply A student searches for "classification" but gets "clustering" results. What could improve this?

- A) Increase k
- B) Add metadata filtering by topic
- C) Use a slower model
- D) Remove all documents

### Q6: Which is TRUE about ChromaDB?

- A) It requires a server
- B) It stores data on disk and runs locally
- C) It only works with OpenAI embeddings
- D) It is a cloud service

### Q7: What is the difference between API embeddings and local Ollama embeddings?

- A) API is always better
- B) API requires internet, local runs on your machine
- C) Local is always faster
- D) There is no difference

### Q8: 🔴 Evaluate Why might a chunk size of 50 tokens be too small for RAG?

- A) It uses too many tokens
- B) It loses context by splitting information across chunks
- C) It is too fast
- D) It creates too many documents

### Q9: How does similarity_search_with_score differ from similarity_search?

- A) It is slower
- B) It returns similarity scores alongside documents
- C) It returns different documents
- D) It requires different parameters

### Q10: 🔴 Evaluate A Data Science course has 50 lecture notes. What is the best approach for searchable access?

- A) Put all text in one file
- B) Load as documents, chunk, embed, store in vector DB
- C) Use keyword search only
- D) Read them manually


---

**Check your answers:** [Answer Key](answer_key.md)

**Back to:** [Quiz Index](../README.md)
