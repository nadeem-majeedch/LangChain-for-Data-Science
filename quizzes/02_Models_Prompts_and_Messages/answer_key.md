# Answer Key: Models, Prompts & Messages

---

### Q1

**Answer:** B

**Explanation:** Chat Models work with structured messages (system, human, AI roles). Raw LLMs take plain text.

**Concept:** Chat Models

---

### Q2

**Answer:** B

**Explanation:** System messages define the AI personality, behavior, and constraints before the conversation starts.

**Concept:** Message types

---

### Q3

**Answer:** B

**Explanation:** Prompt templates have variables that get filled in at runtime, making prompts reusable.

**Concept:** Prompt templates

---

### Q4

**Answer:** B

**Explanation:** Temperature 0 makes the model deterministic — same input always produces same output.

**Concept:** Model parameters

---

### Q5

**Answer:** B

**Explanation:** Structured output forces the LLM to return data in a defined format (like JSON with specific fields).

**Concept:** Structured output

---

### Q6

**Answer:** C

**Explanation:** System messages set the context and behavior before any human input.

**Concept:** Message ordering

---

### Q7

**Answer:** B

**Explanation:** Missing required variables cause a KeyError. Always provide all template variables.

**Concept:** Template variables

---

### Q8

**Answer:** B

**Explanation:** Few-shot prompting provides examples so the model learns the pattern before generating.

**Concept:** Few-shot prompting

---

### Q9

**Answer:** B

**Explanation:** Temperature 0 = consistent/factual. Temperature 0.7 = creative/varied. Match to your use case.

**Concept:** Temperature

---

### Q10

**Answer:** C

**Explanation:** Literal type constrains values to specific options, ensuring valid difficulty levels.

**Concept:** Structured output

---

### Q11

**Answer:** B

**Explanation:** Without a system message, the LLM has no behavior constraints and may give inconsistent responses.

**Concept:** System messages

---

### Q12

**Answer:** B

**Explanation:** ChatPromptTemplate.from_messages() takes a list of (role, content) tuples.

**Concept:** Prompt creation

---

### Q13

**Answer:** B

**Explanation:** with_structured_output() constrains the LLM to return data matching your Pydantic model.

**Concept:** Structured output

---

### Q14

**Answer:** B

**Explanation:** Including AI messages maintains conversation context so the model knows what was said before.

**Concept:** Conversation context

---

### Q15

**Answer:** B

**Explanation:** Structured output with Pydantic ensures consistent, validated output with all required fields.

**Concept:** Structured output

---


**Back to:** [Quiz Index](../README.md)
