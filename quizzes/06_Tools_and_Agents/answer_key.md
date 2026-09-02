# Answer Key: Tools and Agents

---

### Q1

**Answer:** B

**Explanation:** Tools extend LLM capabilities by letting them call external functions.

**Concept:** Tools

---

### Q2

**Answer:** B

**Explanation:** LLMs predict text patterns. They cannot reliably perform arithmetic.

**Concept:** LLM limitations

---

### Q3

**Answer:** B

**Explanation:** An agent uses the LLM to dynamically decide which tools to call based on the question.

**Concept:** Agents

---

### Q4

**Answer:** B

**Explanation:** The agent loop is: LLM thinks, calls a tool, observes the result, then decides next step.

**Concept:** Agent loop

---

### Q5

**Answer:** B

**Explanation:** Chains are faster and more reliable for fixed workflows. Use agents for dynamic decisions.

**Concept:** Chain vs Agent

---

### Q6

**Answer:** B

**Explanation:** @tool from langchain_core.tools decorates functions to make them available to agents.

**Concept:** Tool creation

---

### Q7

**Answer:** B

**Explanation:** The schema tells the LLM what the tool does and what inputs it expects.

**Concept:** Tool schema

---

### Q8

**Answer:** B

**Explanation:** The LLM reads tool descriptions and decides which tool best answers the question.

**Concept:** Tool selection

---

### Q9

**Answer:** B

**Explanation:** The tool result goes back to the LLM, which uses it to generate a natural language answer.

**Concept:** Agent flow

---

### Q10

**Answer:** B

**Explanation:** Validation prevents malicious or incorrect inputs from causing harmful tool executions.

**Concept:** Tool security

---

### Q11

**Answer:** B

**Explanation:** Agents can choose the right tool (statistics, visualization, SQL) based on the question.

**Concept:** DS agents

---

### Q12

**Answer:** A

**Explanation:** For simple, fixed tasks, a chain is faster and more reliable than an agent.

**Concept:** Agent overhead

---

### Q13

**Answer:** B

**Explanation:** An allow list restricts which tools are available, implementing least-privilege security.

**Concept:** Tool security

---

### Q14

**Answer:** B

**Explanation:** Structured logging records every tool call for debugging and audit purposes.

**Concept:** Observability

---

### Q15

**Answer:** B

**Explanation:** A good description helps the LLM understand when and how to use the tool.

**Concept:** Tool design

---


**Back to:** [Quiz Index](../README.md)
