# Post-Quiz: LCEL and Chains

**Purpose:** Test your understanding AFTER studying this topic.
**Time:** 10-15 minutes
**Questions:** 10

---

## Learning Objectives Tested

- Understand the pipe operator
- Build sequential and parallel chains
- Use RunnablePassthrough and RunnableLambda

---

### Q1: 🟢 Understand What does this chain produce?

```python
chain = prompt | model | StrOutputParser()
result = chain.invoke({"topic": "PCA"})
```

- A) A raw model response object
- B) Clean text string
- C) A list of tokens
- D) A dictionary

### Q2: What is RunnableParallel used for?

- A) Running chains sequentially
- B) Running multiple chains simultaneously on the same input
- C) Making chains run faster
- D) Parallelizing database queries

### Q3: What does RunnablePassthrough do?

- A) Passes input unchanged to the next component
- B) Generates random output
- C) Skips the current component
- D) Logs the input

### Q4: 🟡 Apply In the dict pattern `{"context": retriever, "question": RunnablePassthrough()}`, what does each key receive?

- A) Both get the same input
- B) "context" gets retrieved docs, "question" gets the original input
- C) "context" gets the question, "question" gets the docs
- D) Both get None

### Q5: 🟡 Apply When would you use a chain instead of an agent?

- A) When you need dynamic decision-making
- B) When you know the exact sequence of steps
- C) When you have many tools
- D) When the task is ambiguous

### Q6: What happens if you remove StrOutputParser from `prompt | model`?

- A) The chain crashes
- B) You get raw AIMessage objects instead of strings
- C) Nothing changes
- D) The output is truncated

### Q7: Which component wraps a regular Python function for use in a chain?

- A) RunnablePassthrough
- B) RunnableLambda
- C) StrOutputParser
- D) ChatPromptTemplate

### Q8: A student builds `prompt | model` and gets an error. What is most likely missing?

- A) The prompt template
- B) The model instance
- C) StrOutputParser
- D) The environment variables

### Q9: What is the key advantage of LCEL over traditional chain construction?

- A) It is faster
- B) Declarative syntax makes chains readable and composable
- C) It supports more models
- D) It requires less code

### Q10: 🔴 Evaluate How would you chain three operations: classify → explain → format?

- A) Run them in separate scripts
- B) Use sequential chaining: classify | explain | format
- C) Use parallel chaining for all three
- D) Use an agent to choose between them


---

**Check your answers:** [Answer Key](answer_key.md)

**Back to:** [Quiz Index](../README.md)
