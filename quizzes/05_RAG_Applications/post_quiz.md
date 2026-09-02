# Post-Quiz: RAG Applications

**Purpose:** Test your understanding AFTER studying this topic.
**Time:** 10-15 minutes
**Questions:** 10

---

## Learning Objectives Tested

- Build complete RAG pipelines
- Understand chunking strategies
- Evaluate retrieval quality

---

### Q1: In a RAG pipeline, what does the retriever do?

- A) Generates the final answer
- B) Finds documents similar to the query
- C) Creates embeddings
- D) Stores documents

### Q2: What is the "context" in a RAG prompt?

- A) The user question
- B) The retrieved documents formatted as text
- C) The system message
- D) The model parameters

### Q3: 🟡 Apply Why should RAG prompts instruct the LLM to use ONLY the provided context?

- A) To make responses shorter
- B) To prevent hallucination by grounding answers in retrieved docs
- C) To reduce token usage
- D) To enable tool calling

### Q4: What happens when the user asks a question outside the knowledge base?

- A) The LLM always says "I don't know"
- B) The LLM may hallucinate or give a generic answer
- C) The system crashes
- D) The retriever returns all documents

### Q5: 🟡 Apply What is the relationship between chunk size and retrieval quality?

- A) Larger is always better
- B) There is a tradeoff — too small loses context, too large adds noise
- C) Smaller is always better
- D) Chunk size does not matter

### Q6: 🔴 Evaluate How does RAG differ from fine-tuning?

- A) They are the same thing
- B) RAG retrieves external knowledge, fine-tuning modifies the model
- C) Fine-tuning is faster
- D) RAG requires more compute

### Q7: What is source citation in RAG?

- A) Citing the LLM provider
- B) Showing which documents the answer was based on
- C) Citing the programming language
- D) Citing the API documentation

### Q8: Why is evaluating RAG quality important?

- A) LLMs always give correct answers
- B) To measure retrieval accuracy and answer quality
- C) To reduce costs
- D) To make the system faster

### Q9: 🔴 Evaluate A RAG system retrieves 20 documents but the answer is poor. What could be wrong?

- A) Too many irrelevant documents diluting the context
- B) The LLM is too small
- C) The documents are too short
- D) The query is too simple

### Q10: What is the purpose of the format_docs() function in RAG?

- A) To format the user question
- B) To convert retrieved documents into a text string for the context
- C) To format the final answer
- D) To format error messages


---

**Check your answers:** [Answer Key](answer_key.md)

**Back to:** [Quiz Index](../README.md)
