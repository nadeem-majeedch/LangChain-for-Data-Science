# Exercises: Tools and Agents

📖 **Reading:** [Tools and Agents](../../readings/06_Tools_and_Agents.md)
💻 **Notebook:** [Tools and Agents](../../notebooks/06_Tools_and_Agents.ipynb)

---

## Level 1 — Basic

### Exercise 1: First Tool

**Objective:** Create and use a LangChain tool

**Task:** Create a tool that calculates the F1 score from precision and recall values.

**Requirements:**
- Use @tool decorator
- Include type hints
- Test the tool

**Expected Learning Outcome:** Student can create LangChain tools

---

## Level 2 — Intermediate

### Exercise 1: Multi-Tool Agent

**Objective:** Build an agent with multiple tools

**Task:** Build an agent with 4 tools: calculate_mean, calculate_std, calculate_f1, and dataset_summary.

**Requirements:**
- Implement all 4 tools
- Test agent with various queries
- Verify correct tool selection

**Expected Learning Outcome:** Student understands tool routing

---

## Level 3 — Advanced

### Exercise 1: Safe DS Agent

**Objective:** Build a safe Data Science agent

**Task:** Build an agent that validates all tool inputs, logs all calls, and handles errors gracefully.

**Requirements:**
- Input validation
- Error handling
- Logging
- Rate limiting

**Hints:**
- Wrap tools with validation
- Add try/except blocks

**Expected Learning Outcome:** Student can build secure agents

---


**Next:** [Take the Assessment](assessment.md) | [Attempt the Challenge](challenge.md)

**Back to:** [Assignment Index](../README.md)
