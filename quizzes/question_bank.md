# Question Bank

Reusable questions organized by topic for quiz generation.

---

## LLM Fundamentals

1. What does LLM stand for? (A: Large Language Model)
2. Why are LLMs probabilistic? (A: They generate text based on patterns, not rules)
3. What is hallucination? (A: Generating plausible but false information)
4. What does temperature control? (A: Randomness of output)
5. Why do LLMs have context limits? (A: Fixed attention window in transformer architecture)

## LangChain Architecture

6. What are the three layers of LangChain? (A: Core, Partner packages, Application)
7. What is langchain-core? (A: Base abstractions, LCEL, prompts)
8. What is a partner package? (A: Integration with specific providers like OpenAI, Ollama)
9. Why use LangChain instead of direct API calls? (A: Unified interface, multiple providers, ecosystem)
10. What is LCEL? (A: LangChain Expression Language for composing chains)

## Models and Messages

11. What is the difference between LLM and Chat Model? (A: Chat Model works with structured messages)
12. What is a system message? (A: Sets AI behavior and constraints)
13. What is temperature 0? (A: Deterministic output, same input always same output)
14. What is structured output? (A: LLM output constrained to a specific schema)
15. What Pydantic feature ensures valid field values? (A: Literal type)

## Prompt Engineering

16. What is a prompt template? (A: Reusable text pattern with variables)
17. What is few-shot prompting? (A: Providing examples before asking the question)
18. Why include previous messages in conversation? (A: Maintain context across turns)
19. What happens if a template variable is missing? (A: KeyError is raised)
20. How do you create a chat prompt? (A: ChatPromptTemplate.from_messages([...])

## Chains and LCEL

21. What does the pipe operator (|) do? (A: Passes output to next component)
22. What is a Runnable? (A: Component implementing .invoke())
23. What is StrOutputParser? (A: Extracts text from model response)
24. What is RunnableParallel? (A: Runs multiple chains simultaneously)
25. What is RunnablePassthrough? (A: Forwards input unchanged)

## Embeddings and Vector Stores

26. What is an embedding? (A: Numerical vector representing text meaning)
27. What is cosine similarity? (A: Measures angle between vectors)
28. What is a vector store? (A: Database for storing and searching embeddings)
29. What is ChromaDB? (A: Local vector database)
30. What is top-k retrieval? (A: Returning k most similar documents)

## RAG

31. What does RAG stand for? (A: Retrieval-Augmented Generation)
32. What is the RAG pipeline? (A: Load, Split, Embed, Store, Retrieve, Generate)
33. What is chunking? (A: Splitting documents into smaller pieces)
34. What is context in RAG? (A: Retrieved documents formatted as text)
35. How does RAG reduce hallucination? (A: Grounds answers in retrieved documents)

## Tools and Agents

36. What is a LangChain tool? (A: External function the LLM can call)
37. What decorator creates a tool? (A: @tool)
38. What is an agent? (A: LLM that decides which tools to use)
39. What is the agent loop? (A: Think, Act, Observe, Think again)
40. When use chain vs agent? (A: Chain for fixed workflow, agent for dynamic)

## LangGraph

41. What is LangGraph? (A: Framework for stateful graph workflows)
42. What are nodes? (A: Functions that process state)
43. What are edges? (A: Connections between nodes)
44. What are conditional edges? (A: Connections that depend on state)
45. What is START/END? (A: Graph entry and exit points)

## Evaluation

46. Why is LLM evaluation hard? (A: Subjective, multiple valid answers)
47. What is LLM-as-judge? (A: Using one LLM to evaluate another)
48. What metrics measure RAG quality? (A: Retrieval precision, answer relevance, faithfulness)
49. What is grounding? (A: Answer supported by retrieved context)
50. What is observability? (A: Understanding what happened inside the application)

## Security

51. What is prompt injection? (A: User overriding system instructions)
52. What is indirect prompt injection? (A: Malicious text in retrieved documents)
53. Why validate tool inputs? (A: Prevent dangerous operations)
54. Why use read-only database access? (A: Prevent LLM from modifying data)
55. What is defense in depth? (A: Multiple security layers)

## MCP

56. What is MCP? (A: Model Context Protocol for standardized tool integration)
57. What are MCP tools? (A: Functions exposed by MCP servers)
58. What are MCP resources? (A: Readable data exposed by MCP servers)
59. What is FastMCP? (A: Python library for creating MCP servers)
60. What is the benefit of MCP? (A: Interoperability across AI applications)

## Production

61. What is configuration management? (A: Using env vars instead of hardcoded values)
62. What is exponential backoff? (A: Increasing delay between retries)
63. Why cache LLM responses? (A: Reduce cost and latency)
64. What is rate limiting? (A: Restricting number of requests per time)
65. What is the production lifecycle? (A: Develop, Test, Evaluate, Deploy, Monitor, Improve)

---

**Back to:** [Quiz Index](README.md)
