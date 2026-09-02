# Answer Key: RAG Applications

---

### Q1

**Answer:** B

**Explanation:** RAG gives LLMs access to external knowledge bases they were not trained on.

**Concept:** RAG purpose

---

### Q2

**Answer:** B

**Explanation:** RAG follows: load documents, split into chunks, create embeddings, store, retrieve, generate answer.

**Concept:** RAG pipeline

---

### Q3

**Answer:** B

**Explanation:** Chunking splits documents into smaller pieces that fit within the LLM context window.

**Concept:** Chunking

---

### Q4

**Answer:** B

**Explanation:** Hallucination is when LLMs confidently generate incorrect or fabricated information.

**Concept:** Hallucination

---

### Q5

**Answer:** B

**Explanation:** LLMs have context limits. Large documents must be chunked to fit.

**Concept:** Context limits

---

### Q6

**Answer:** B

**Explanation:** The retriever searches the vector store and returns the most relevant documents.

**Concept:** Retriever

---

### Q7

**Answer:** B

**Explanation:** Context is the retrieved documents that provide background information for the answer.

**Concept:** RAG context

---

### Q8

**Answer:** B

**Explanation:** Grounding in context reduces hallucination by limiting answers to retrieved information.

**Concept:** Grounding

---

### Q9

**Answer:** B

**Explanation:** Without relevant context, the LLM may hallucinate or give unhelpful answers. Good prompts handle this.

**Concept:** Edge cases

---

### Q10

**Answer:** B

**Explanation:** Chunk size affects what information is available. Experiment to find the optimal size.

**Concept:** Chunking tradeoffs

---

### Q11

**Answer:** B

**Explanation:** RAG adds external knowledge retrieval. Fine-tuning modifies the model weights with training data.

**Concept:** RAG vs Fine-tuning

---

### Q12

**Answer:** B

**Explanation:** Source citation shows users which retrieved documents contributed to the answer.

**Concept:** Transparency

---

### Q13

**Answer:** B

**Explanation:** Evaluation measures whether the right documents are retrieved and whether answers are accurate.

**Concept:** Evaluation

---

### Q14

**Answer:** A

**Explanation:** Retrieving too many documents can include irrelevant content that confuses the LLM.

**Concept:** Context management

---

### Q15

**Answer:** B

**Explanation:** format_docs() joins multiple retrieved documents into a single context string for the prompt.

**Concept:** Context formatting

---


**Back to:** [Quiz Index](../README.md)
