# Answer Key: LCEL and Chains

---

### Q1

**Answer:** A

**Explanation:** LCEL stands for LangChain Expression Language — the syntax for composing chains.

**Concept:** LCEL

---

### Q2

**Answer:** B

**Explanation:** Unix pipes pass output to the next command. LCEL uses the same concept for chaining components.

**Concept:** Pipe operator

---

### Q3

**Answer:** B

**Explanation:** Runnables are components that implement .invoke() and can be chained together with |.

**Concept:** Runnables

---

### Q4

**Answer:** B

**Explanation:** Without StrOutputParser, you get raw model metadata. The parser extracts just the text.

**Concept:** Output parsing

---

### Q5

**Answer:** B

**Explanation:** Chains follow predetermined steps. Agents use the LLM to decide which steps to take.

**Concept:** Chain vs Agent

---

### Q6

**Answer:** B

**Explanation:** StrOutputParser extracts the text content from the model response, returning a clean string.

**Concept:** Chain output

---

### Q7

**Answer:** B

**Explanation:** RunnableParallel runs multiple chains at the same time, useful for generating multiple outputs.

**Concept:** Parallel execution

---

### Q8

**Answer:** A

**Explanation:** RunnablePassthrough forwards the input without modification, useful in dict patterns.

**Concept:** Passthrough

---

### Q9

**Answer:** B

**Explanation:** The retriever processes input to get docs. RunnablePassthrough forwards the original input unchanged.

**Concept:** Dict pattern

---

### Q10

**Answer:** B

**Explanation:** Chains are faster and more reliable for fixed workflows. Use agents when the LLM needs to decide.

**Concept:** Chain vs Agent

---

### Q11

**Answer:** B

**Explanation:** Without the parser, you get AIMessage objects with metadata. StrOutputParser extracts just the text.

**Concept:** Output parsing

---

### Q12

**Answer:** B

**Explanation:** RunnableLambda wraps regular Python functions so they can be used in LCEL chains.

**Concept:** RunnableLambda

---

### Q13

**Answer:** C

**Explanation:** Most chains need StrOutputParser to extract clean text from the model response.

**Concept:** Chain debugging

---

### Q14

**Answer:** B

**Explanation:** LCEL uses | operator for clean, readable chain composition that is easy to understand and modify.

**Concept:** LCEL benefits

---

### Q15

**Answer:** B

**Explanation:** Sequential chaining passes output from one step to the next, creating a pipeline.

**Concept:** Sequential chains

---


**Back to:** [Quiz Index](../README.md)
