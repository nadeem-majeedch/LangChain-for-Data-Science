# Exercises: LangGraph for Data Science

📖 **Reading:** [LangGraph for Data Science](../../readings/12_LangGraph_for_Data_Science.md)
💻 **Notebook:** [LangGraph for Data Science](../../notebooks/12_LangGraph_for_Data_Science.ipynb)

---

## Level 1 — Basic

### Exercise 1: First Graph

**Objective:** Build a simple LangGraph workflow

**Task:** Build a graph with 3 nodes: classify, process, and respond.

**Requirements:**
- Use StateGraph
- Add nodes and edges
- Test with different inputs

**Expected Learning Outcome:** Student can create basic graphs

---

## Level 2 — Intermediate

### Exercise 1: Conditional Routing

**Objective:** Implement conditional routing

**Task:** Build a graph that routes to different handlers based on question type.

**Requirements:**
- Implement routing function
- Add conditional edges
- Test all routes

**Expected Learning Outcome:** Student understands conditional routing

---

## Level 3 — Advanced

### Exercise 1: DS Research Graph

**Objective:** Build a research assistant graph

**Task:** Build a graph that: classifies questions, routes to RAG/tools/LLM, validates answers, and loops if needed.

**Requirements:**
- All route types
- Validation node
- Retry loop
- State management

**Hints:**
- Use TypedDict for state
- Add max iteration limit

**Expected Learning Outcome:** Student can build complex LangGraph workflows

---


**Next:** [Take the Assessment](assessment.md) | [Attempt the Challenge](challenge.md)

**Back to:** [Assignment Index](../README.md)
