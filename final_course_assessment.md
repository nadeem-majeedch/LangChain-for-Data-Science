# Final Course Assessment: LangChain for Data Science

**Total Marks:** 100
**Time:** 3 hours
**Materials:** Closed book (notes not permitted)

---

## Part A: Concepts (20 marks)

### Q1. (4 marks) 🟢 Understand

Explain the difference between a **chain** and an **agent** in LangChain. Provide a specific Data Science scenario where each would be appropriate.

### Q2. (4 marks) 🟢 Understand

What is **RAG** and why is it useful for Data Science applications? Explain the complete RAG pipeline from document loading to answer generation.

### Q3. (4 marks) 🟡 Apply

Your university wants to build a private Data Science assistant using confidential student data. Compare an **API-based solution** (OpenAI) with a **local Ollama solution**. Consider: privacy, cost, hardware, model quality, and deployment.

### Q4. (4 marks) 🟠 Analyze

A RAG system returns answers that sound correct but are factually wrong. Analyze **three possible causes** and propose a solution for each.

### Q5. (4 marks) 🔴 Evaluate

Compare **LangChain chains** with **LangGraph workflows**. When would you choose one over the other? Provide two specific scenarios for each.

---

## Part B: Code (25 marks)

### Q6. (10 marks) 🟡 Apply

Write a complete Python function that:

1. Creates a ChatPromptTemplate with system and human messages
2. Includes variables for topic and difficulty level
3. Calls the LLM and returns the response
4. Handles errors gracefully

Test your function with a Data Science topic at beginner and advanced levels.

### Q7. (8 marks) 🟡 Apply

Create a **LangChain tool** that calculates the F1 score from precision and recall. Include:

- Proper `@tool` decorator
- Type hints
- Input validation
- Error handling for invalid inputs

### Q8. (7 marks) 🟠 Analyze

The following code has a bug. Find it, explain why it fails, and fix it:

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a Data Science tutor."),
    ("human", "{question}")
])

model = ChatOpenAI(model="gpt-4o-mini")
chain = prompt | model  # Missing something!

response = chain.invoke({"question": "What is PCA?"})
print(response)  # What's wrong with this output?
```

---

## Part C: RAG & Agents (20 marks)

### Q9. (10 marks) 🟡 Apply

Design a RAG system for a Data Science course. Answer the following:

a) What documents would you include? (Name 5 specific document types)
b) How would you chunk them? What chunk size and why?
c) What metadata would you add to each document?
d) How would you handle questions outside the knowledge base?

### Q10. (10 marks) 🟠 Analyze

You are building a Data Science agent with these tools:

- `calculate_statistics(numbers)` — computes mean, median, std
- `query_database(sql)` — executes SQL queries
- `search_knowledge(query)` — searches course notes

Analyze:
a) How does the agent decide which tool to use?
b) What security risks exist with each tool?
c) How would you prevent the agent from executing dangerous SQL?
d) Design input validation for the statistics tool.

---

## Part D: Design (15 marks)

### Q11. (15 marks) 🔴 Create

Design a **Data Science Research Assistant** for a university. Address:

**Architecture (5 marks):**
- Draw the system architecture diagram
- List all components and their purposes
- Explain the data flow

**Features (5 marks):**
- What question types does it support?
- How does it handle different difficulty levels?
- What tools does it provide?

**Evaluation (5 marks):**
- How would you measure success?
- What metrics would you track?
- How would you collect user feedback?

---

## Part E: Security (10 marks)

### Q12. (5 marks) 🟡 Apply

Explain **three types of prompt injection** attacks and how to defend against each. Provide specific examples relevant to a Data Science application.

### Q13. (5 marks) 🟠 Analyze

Your RAG system ingests documents from untrusted sources. Analyze the security risks and propose a defense-in-depth strategy. Address:
- Document sanitization
- Prompt injection via documents
- Output validation
- Access control

---

## Part F: Case Study (10 marks)

### Q14. (10 marks) 🔴 Evaluate

**Case Study:** A university wants to deploy a Data Science AI assistant for 500 students. The assistant should:

- Answer questions about course materials
- Help with Python code for data analysis
- Generate practice quizzes
- Provide dataset analysis tools

Evaluate the following design decisions:

a) **Cloud API vs Local Ollama** — Which would you recommend and why?
b) **RAG vs Fine-tuning** — Which approach for course materials?
c) **Agent vs Chain** — When would you use each?
d) **Security measures** — What protections are needed for student data?
e) **Evaluation strategy** — How would you measure success after deployment?

Provide justified recommendations for each decision.

---

## Marking Guide

| Part | Topic | Marks |
|------|-------|-------|
| A | Concepts | 20 |
| B | Code | 25 |
| C | RAG & Agents | 20 |
| D | Design | 15 |
| E | Security | 10 |
| F | Case Study | 10 |
| **Total** | | **100** |

## Bloom's Taxonomy Labels

| Label | Level | Description |
|-------|-------|-------------|
| 🟢 | Understand | Explain, describe, summarize |
| 🟡 | Apply | Use, implement, demonstrate |
| 🟠 | Analyze | Compare, contrast, diagnose |
| 🔴 | Evaluate/Create | Design, evaluate, justify |

---

**Back to:** [Assignment Index](assignments/README.md) | [Repository README](README.md)
