# Discussion Questions

## Beginner Level

### Week 1-2

1. **Why not simply call an LLM API directly?** What does LangChain add?
2. **When is temperature 0 better than temperature 1?** Give a Data Science example.
3. **What's the difference between a system message and a human message?** Why do we need both?
4. **Why do we need prompt templates?** Can't we just write prompts as strings?

### Week 3-4

5. **When is semantic search better than keyword search?** When is keyword search better?
6. **Why do we need to chunk documents?** What happens if we don't?
7. **What is the difference between an embedding model and a chat model?**
8. **Why does RAG help reduce hallucination?** Does it eliminate it?

---

## Intermediate Level

### Week 5-6

9. **When should you use a chain instead of an agent?** Give specific scenarios.
10. **Why are tools important for LLM applications?** What can't LLMs do alone?
11. **How does the LLM decide which tool to use?** What are the limitations?
12. **What makes a good tool description?** Why does it matter?

### Week 7-8

13. **How does metadata filtering improve retrieval precision?** Give an example.
14. **When would you use RAG vs fine-tuning?** Compare the two approaches.
15. **Why is SQL generation dangerous?** What safeguards are needed?
16. **How do you handle documents from untrusted sources?**

---

## Advanced Level

### Week 9-10

17. **What problem does LangGraph solve that chains cannot?**
18. **When is an agent unnecessary overhead?** Give a specific example.
19. **How do you evaluate RAG quality?** What metrics matter most?
20. **Is prompt injection a real threat?** How would you defend against it?

### Week 11-12

21. **What problem does MCP solve?** Why do we need standardized tool protocols?
22. **Should confidential university data be sent to an external API?** Discuss privacy implications.
23. **Is a larger model always better?** When would you choose a smaller model?
24. **How do you balance model quality with cost and latency?**

---

## Prediction Questions

Use these before running experiments:

1. "What do you think will happen if we increase top-k from 3 to 20?"
2. "If we change the chunk size from 500 to 100, how will retrieval change?"
3. "What happens if we remove the system message entirely?"
4. "If we set temperature to 2.0, what kind of output will we get?"
5. "What happens if the retrieved documents are irrelevant to the question?"

---

## Think-Pair-Share Questions

1. "Think of a Data Science task. Would you use a chain or an agent? Why?"
2. "Discuss with your neighbor: What are the security risks of RAG?"
3. "Pair up: Design a prompt template for generating quiz questions."
4. "Share: What's the most surprising thing you learned about LLMs?"

---

## Quick Polls

1. "Raise your hand if you've used an API before."
2. "How many of you have worked with vector databases?"
3. "Do you think LLMs will replace Data Scientists? Why or why not?"
4. "Would you trust an LLM to write SQL for your company's database?"

---

## Debugging Activities

Give students broken code and ask them to fix it:

### Activity 1: Missing Parser
```python
chain = prompt | model  # Missing StrOutputParser
response = chain.invoke({"question": "What is PCA?"})
print(response)  # Students see raw model output
```
**Question:** "What's wrong? How do you fix it?"

### Activity 2: Empty Context
```python
# RAG with no documents
docs = retriever.invoke("What is machine learning?")
# docs is empty!
```
**Question:** "Why are we getting no results? What could be wrong?"

### Activity 3: Infinite Loop
```python
# LangGraph with no exit condition
while True:
    state = process(state)
```
**Question:** "What happens? How do you fix it?"

---

**Back to:** [Instructor Guide](README.md) | [Teaching Roadmap](teaching_roadmap.md)
