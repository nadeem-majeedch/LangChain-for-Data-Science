# Final Quiz: LangChain for Data Science

**Total Marks:** 100
**Time:** 60 minutes
**Questions:** 40

---

## Section A: LLM Fundamentals (15 marks)

### Q1. (2 marks) 🟢

What does LLM stand for?

- A) Large Language Model
- B) Linear Language Machine
- C) Learning Language Method
- D) Logical Language Module

### Q2. (2 marks) 🟢

What is hallucination in LLMs?

- A) The model crashes
- B) The model generates plausible but false information
- C) The model refuses to answer
- D) The model is too slow

### Q3. (2 marks) 🟢

What does temperature=0 produce?

- A) Random output
- B) Deterministic output
- C) Longer output
- D) Shorter output

### Q4. (3 marks) 🟡

Explain the difference between a raw LLM and a Chat Model in LangChain.

### Q5. (3 marks) 🟡

Why is LangChain useful compared to calling the OpenAI API directly?

### Q6. (3 marks) 🟡

A university wants to use an LLM to answer questions about confidential student records. What approach would you recommend and why?

---

## Section B: Prompts and Chains (15 marks)

### Q7. (2 marks) 🟢

What is the purpose of a system message?

- A) It is the user input
- B) It sets the AI behavior and constraints
- C) It is the AI response
- D) It logs the conversation

### Q8. (2 marks) 🟢

What does StrOutputParser do?

- A) Parses database queries
- B) Extracts clean text from model response
- C) Formats output as JSON
- D) Stores output in a file

### Q9. (3 marks) 🟡

Given this chain:

```python
chain = prompt | model | StrOutputParser()
result = chain.invoke({"topic": "PCA"})
```

What does `result` contain? Explain.

### Q10. (4 marks) 🟡

Create a prompt template that explains a Data Science concept at different difficulty levels (beginner, intermediate, advanced). Include the system message.

### Q11. (4 marks) 🔴

Compare chains and agents. When would you use each for a Data Science application? Give specific examples.

---

## Section C: Embeddings and RAG (20 marks)

### Q12. (2 marks) 🟢

What is an embedding?

- A) A type of LLM
- B) A numerical vector representing text meaning
- C) A database index
- D) A prompt template

### Q13. (2 marks) 🟢

What does cosine similarity measure?

- A) Vector length
- B) Angle between vectors
- C) Number of dimensions
- D) Computation speed

### Q14. (3 marks) 🟡

What is the correct order of the RAG pipeline?

### Q15. (3 marks) 🟡

Explain why chunking is necessary in RAG. What happens if documents are not chunked?

### Q16. (4 marks) 🟡

A RAG system retrieves 10 documents but the answer is poor. List 3 possible causes and solutions.

### Q17. (3 marks) 🔴

Compare RAG and fine-tuning. When would you use each? Give Data Science examples.

### Q18. (3 marks) 🔴

A company wants to build a RAG system over 1000 research papers. What advanced techniques would you recommend to improve retrieval quality?

---

## Section D: Tools and Agents (15 marks)

### Q19. (2 marks) 🟢

What decorator creates a LangChain tool?

- A) @chain
- B) @tool
- C) @agent
- D) @runnable

### Q20. (2 marks) 🟢

What is the agent loop?

- A) A fixed sequence
- B) Think, Act, Observe, Think again
- C) A single LLM call
- D) A database query

### Q21. (3 marks) 🟡

Create a tool that calculates the F1 score from precision and recall. Include the @tool decorator and type hints.

### Q22. (4 marks) 🟡

Why is tool input validation important? Give 3 specific examples of dangerous inputs that should be blocked.

### Q23. (4 marks) 🔴

Design a Data Science agent for a research lab. What tools would it need? How would you ensure safety?

---

## Section E: LangGraph (10 marks)

### Q24. (2 marks) 🟢

What is LangGraph used for?

- A) Training models
- B) Building stateful graph workflows
- C) Storing data
- D) Generating images

### Q25. (3 marks) 🟡

Explain the roles of State, Node, and Edge in LangGraph.

### Q26. (5 marks) 🔴

Design a LangGraph workflow for a Data Science assistant that routes questions to different handlers. Include at least 3 routes and explain your design.

---

## Section F: SQL and Data Science AI (10 marks)

### Q27. (2 marks) 🟢

Why is SQL generation with LLMs dangerous?

- A) It is too slow
- B) LLMs can generate destructive queries like DROP TABLE
- C) LLMs cannot write SQL
- D) SQL is outdated

### Q28. (3 marks) 🟡

How would you safely implement natural language to SQL translation? List 4 safety measures.

### Q29. (5 marks) 🔴

A company wants natural-language access to their sales database. Design the architecture including: NL-to-SQL, query validation, result explanation, and security measures.

---

## Section G: Evaluation and Observability (5 marks)

### Q30. (2 marks) 🟢

What is LLM-as-judge?

- A) A human evaluator
- B) Using one LLM to evaluate another LLM's output
- C) A testing framework
- D) A type of LLM

### Q31. (3 marks) 🟡

List 4 metrics you would use to evaluate a RAG system and explain what each measures.

---

## Section H: Security (5 marks)

### Q32. (2 marks) 🟢

What is prompt injection?

- A) Adding prompts to a database
- B) User overriding system instructions via crafted input
- C) Creating prompt templates
- D) Loading prompts from files

### Q33. (3 marks) 🟡

Explain 3 security measures you would implement in a RAG system that processes documents from untrusted sources.

---

## Section I: MCP and Production (5 marks)

### Q34. (2 marks) 🟢

What problem does MCP solve?

- A) Model training
- B) Standardized tool integration across AI applications
- C) Data storage
- D) Image generation

### Q35. (3 marks) 🟡

List 4 production requirements for deploying an LLM application.

---

## Section J: Architecture and Design (5 marks)

### Q36. (5 marks) 🔴

Design a complete Data Science AI assistant for a university. Address:

1. What question types does it support?
2. What components would you use (RAG, tools, SQL)?
3. How would you ensure security?
4. How would you evaluate success?
5. Draw the architecture diagram.

---

**Total: 100 marks**

---

**Back to:** [Quiz Index](README.md) | [Answer Key](answer_key.md)
