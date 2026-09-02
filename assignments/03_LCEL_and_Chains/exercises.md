# Exercises: LCEL and Chains

📖 **Reading:** [LCEL and Chains](../../readings/03_LCEL_and_Chains.md)
💻 **Notebook:** [LCEL and Chains](../../notebooks/03_LCEL_and_Chains.ipynb)

---

## Level 1 — Basic

### Exercise 1: First Chain

**Objective:** Build a simple LCEL chain

**Task:** Create a chain that takes a topic and produces a one-paragraph explanation.

**Requirements:**
- Use the pipe operator
- Include prompt and parser
- Test with 3 topics

**Expected Learning Outcome:** Student can chain LLM components

---

## Level 2 — Intermediate

### Exercise 1: Parallel Analysis

**Objective:** Build a parallel chain

**Task:** Create a chain that takes a Data Science concept and generates both a definition AND a quiz question simultaneously.

**Requirements:**
- Use RunnableParallel
- Combine results
- Format output nicely

**Expected Learning Outcome:** Student understands parallel execution

---

## Level 3 — Advanced

### Exercise 1: Concept Explainer Pipeline

**Objective:** Build a multi-step concept explainer

**Task:** Build a pipeline that: 1) Classifies a topic, 2) Generates explanation appropriate for that level, 3) Creates a quiz, 4) Combines everything.

**Requirements:**
- Use multiple chain types
- Include conditional logic
- Handle errors gracefully

**Hints:**
- Use RunnableLambda for classification
- Chain parallel outputs

**Expected Learning Outcome:** Student can build complex LCEL pipelines

---


**Next:** [Take the Assessment](assessment.md) | [Attempt the Challenge](challenge.md)

**Back to:** [Assignment Index](../README.md)
