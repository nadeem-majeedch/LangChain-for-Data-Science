# Exercises: RAG Applications

📖 **Reading:** [RAG Applications](../../readings/05_RAG_Applications.md)
💻 **Notebook:** [RAG Applications](../../notebooks/05_RAG_Applications.ipynb)

---

## Level 1 — Basic

### Exercise 1: First RAG Pipeline

**Objective:** Build a basic RAG system

**Task:** Build a RAG system that answers questions about 3 Data Science topics.

**Requirements:**
- Load documents
- Create vector store
- Implement retrieval + generation

**Expected Learning Outcome:** Student understands the RAG pipeline

---

## Level 2 — Intermediate

### Exercise 1: Chunking Experiment

**Objective:** Understand chunk size effects

**Task:** Compare RAG quality with chunk sizes of 200, 500, and 1000 tokens. Measure retrieval precision.

**Requirements:**
- Create evaluation dataset
- Test all chunk sizes
- Document results

**Expected Learning Outcome:** Student understands chunking tradeoffs

---

## Level 3 — Advanced

### Exercise 1: Course Q&A System

**Objective:** Build a complete course assistant

**Task:** Build a RAG system over course notes that answers questions, provides citations, and handles out-of-domain queries.

**Requirements:**
- 10+ documents
- Source inspection
- Graceful fallback
- Evaluation

**Hints:**
- Add metadata filtering
- Implement confidence scoring

**Expected Learning Outcome:** Student can build production RAG systems

---


**Next:** [Take the Assessment](assessment.md) | [Attempt the Challenge](challenge.md)

**Back to:** [Assignment Index](../README.md)
