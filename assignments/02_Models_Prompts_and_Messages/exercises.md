# Exercises: Models, Prompts & Messages

📖 **Reading:** [Models, Prompts & Messages](../../readings/02_Models_Prompts_and_Messages.md)
💻 **Notebook:** [Models, Prompts & Messages](../../notebooks/02_Models_Prompts_and_Messages.ipynb)

---

## Level 1 — Basic

### Exercise 1: Prompt Template Creation

**Objective:** Create reusable prompt templates

**Task:** Create a prompt template that explains a Data Science concept at different difficulty levels (beginner, intermediate, advanced).

**Requirements:**
- Use ChatPromptTemplate
- Include variables for concept and level
- Test with at least 3 concepts

**Expected Learning Outcome:** Student can create parameterized prompts

---

## Level 2 — Intermediate

### Exercise 1: Few-Shot Classification

**Objective:** Build a few-shot prompt for classification

**Task:** Create a few-shot prompt that classifies Data Science questions into categories (theory, code, math, data).

**Requirements:**
- Include at least 4 examples
- Test with 5 unseen questions
- Measure accuracy

**Expected Learning Outcome:** Student understands few-shot prompting

---

## Level 3 — Advanced

### Exercise 1: Structured Output Pipeline

**Objective:** Build a structured output pipeline

**Task:** Create a system that takes an algorithm name and returns a structured explanation with name, definition, intuition, use_case, and difficulty.

**Requirements:**
- Use Pydantic model
- Use with_structured_output()
- Validate output programmatically

**Hints:**
- Define a clear Pydantic schema
- Test with 5 different algorithms

**Expected Learning Outcome:** Student can build type-safe LLM outputs

---


**Next:** [Take the Assessment](assessment.md) | [Attempt the Challenge](challenge.md)

**Back to:** [Assignment Index](../README.md)
