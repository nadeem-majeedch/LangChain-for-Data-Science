# 03 — LCEL and Chains

> 📓 **Hands-on Notebook:** [03 — LCEL and Chains](../notebooks/03_LCEL_and_Chains.ipynb)

**Level:** Intermediate | **Reading time:** 25-35 minutes

## Learning Objectives

- Understand what a chain is and why it matters
- Learn the LCEL pipe operator (`|`)
- Know the difference between sequential and parallel chains
- Understand RunnablePassthrough, RunnableLambda, RunnableParallel
- Know when to use chains vs agents

---

## 1. What is a Chain?

A **chain** connects multiple operations into a pipeline. Data flows through each step, being transformed at each stage.

```
Input → Prompt → Model → Parser → Output
```

**Why chains matter:**
- Separate concerns (prompt design, model call, output parsing)
- Reuse components across different workflows
- Test each component independently
- Compose complex workflows from simple parts

## 2. LCEL — LangChain Expression Language

LCEL is LangChain's way of composing components using the **pipe operator** (`|`).

**Before LCEL (verbose):**
```python
chain = prompt | model | StrOutputParser()
```

**The pipe operator** connects components left to right. The output of one becomes the input of the next.

**Key principle:** Each component must be a **Runnable** — something that implements `.invoke()`.

## 3. Core Runnables

| Runnable | Purpose | Example |
|----------|---------|---------|
| `ChatPromptTemplate` | Formats messages | `prompt \| model` |
| `ChatOpenAI` | Calls the LLM | `model \| parser` |
| `StrOutputParser` | Extracts text | `chain \| parser` |
| `RunnablePassthrough` | Passes input unchanged | `{"context": retriever, "question": passthrough}` |
| `RunnableLambda` | Wraps a Python function | `RunnableLambda(my_func)` |
| `RunnableParallel` | Runs multiple chains simultaneously | `{"a": chain1, "b": chain2}` |

## 4. Sequential Chains

Data flows through one step at a time:

```
Input → Step 1 → Step 2 → Step 3 → Output
```

**Example:** Translate → Summarize → Format

## 5. Parallel Chains

Multiple steps run simultaneously on the same input:

```
Input → Step A ─┐
        Step B ─┤→ Combine → Output
        Step C ─┘
```

**Example:** Analyze sentiment + Extract keywords + Count tokens — all from the same input.

## 6. The Dict Pattern

A powerful pattern for forwarding input to multiple chains:

```python
{
    "context": retriever,
    "question": RunnablePassthrough()
}
```

This sends the same input to both the retriever (for context) and passes it through as the question.

## 7. Chains vs Agents

| Aspect | Chain | Agent |
|--------|-------|-------|
| **Flow** | Fixed, deterministic | Dynamic, LLM-decided |
| **Transparency** | High (you see the flow) | Low (LLM decides) |
| **Speed** | Fast (no LLM routing call) | Slower (routing overhead) |
| **Reliability** | Very reliable | Can make wrong decisions |
| **Best for** | Known workflows | Open-ended tasks |

**Use a chain when:** You know the exact steps and order.
**Use an agent when:** The LLM needs to decide what to do.

## 8. Data Science Applications

| Application | Chain Pattern |
|------------|--------------|
| Concept explainer | Prompt → LLM → Parser (sequential) |
| Multi-perspective analysis | Input → [Pro, Con, Neutral] → Combine (parallel) |
| ML pipeline recommender | Dataset → [Preprocessing, Models, Metrics] → Format (parallel) |
| Chained refinement | Generate → Evaluate → Improve → Final |

## 9. Common Mistakes

- **Not using StrOutputParser:** Raw model output includes metadata you don't need
- **Over-complicating chains:** Start simple, add complexity only when needed
- **Forgetting RunnablePassthrough:** Without it, data doesn't flow correctly in dict patterns
- **Using agents for simple tasks:** Chains are faster and more reliable for fixed workflows

## 10. Key Takeaways

- LCEL uses the `|` pipe operator to connect components
- Every component in a chain must be a Runnable
- Sequential chains process data step-by-step
- Parallel chains run multiple steps simultaneously
- Use chains for fixed workflows, agents for dynamic ones

## 11. Before You Run the Notebook

1. Complete Readings 01 and 02 first
2. The notebook builds progressively — each cell depends on previous ones
3. All imports are at the top

## 12. Further Reading

**Official Documentation:**
- [LCEL (LangChain)](https://python.langchain.com/docs/concepts/lcel/)
- [How to chain Runnables](https://python.langchain.com/docs/how_to/lcel_cheatsheet/)

---

**Previous:** [02 — Models, Prompts and Messages](02_Models_Prompts_and_Messages.md)
**Next:** [04 — Embeddings and Vector Stores](04_Embeddings_and_Vector_Stores.md)

**Back to:** [Reading Index](README.md)
