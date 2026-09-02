# Exercises: LangChain Introduction

📖 **Reading:** [LangChain Introduction](../../readings/01_LangChain_Introduction.md)
💻 **Notebook:** [LangChain Introduction](../../notebooks/01_LangChain_Introduction.ipynb)

---

## Level 1 — Basic

### Exercise 1: Hello LangChain

**Objective:** Set up and run a basic LangChain call

**Task:** Write a LangChain program that sends a question about Data Science to the LLM and prints the response.

**Requirements:**
- Use ChatOpenAI or ChatOllama
- Include a system message
- Handle missing API key gracefully

**Expected Learning Outcome:** Student can create a basic LLM interaction

---

## Level 2 — Intermediate

### Exercise 1: Model Comparison

**Objective:** Compare different model configurations

**Task:** Send the same Data Science question to two different model configurations (e.g., temperature 0 vs 0.7) and compare the responses.

**Requirements:**
- Create two LLM instances with different parameters
- Send identical prompts
- Compare response quality and consistency

**Expected Learning Outcome:** Student understands model parameter effects

---

## Level 3 — Advanced

### Exercise 1: Multi-Provider Setup

**Objective:** Build a provider-agnostic LLM interface

**Task:** Create a function that can switch between OpenAI API and Ollama with a single configuration change.

**Requirements:**
- Use environment variables for provider selection
- Handle both providers gracefully
- Include error handling for unavailable providers

**Hints:**
- Use os.getenv to select provider
- Create factory functions

**Expected Learning Outcome:** Student understands provider abstraction

---


**Next:** [Take the Assessment](assessment.md) | [Attempt the Challenge](challenge.md)

**Back to:** [Assignment Index](../README.md)
