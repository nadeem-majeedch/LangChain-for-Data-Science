# Answer Key: Final Quiz

---

## Section A: LLM Fundamentals

**Q1:** A — LLM stands for Large Language Model.

**Q2:** B — Hallucination is generating plausible but false information.

**Q3:** B — Temperature 0 produces deterministic output.

**Q4:** Chat Models work with structured messages (system, human, AI roles). Raw LLMs take plain text. Chat Models are the standard in LangChain.

**Q5:** LangChain provides: unified interface for multiple providers, prompt management, chain composition, ecosystem of partner libraries.

**Q6:** Use local Ollama models to keep data on-premises. Never send confidential data to external APIs.

---

## Section B: Prompts and Chains

**Q7:** B — System messages set AI behavior and constraints.

**Q8:** B — StrOutputParser extracts clean text from model response.

**Q9:** `result` contains a plain text string with the explanation of PCA. StrOutputParser extracts the text content from the AIMessage.

**Q10:** Example:
```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "Explain {topic} at {level} level. Be clear and use examples."),
    ("human", "Explain {topic}")
])
```

**Q11:** Chains: fixed workflow, fast, reliable (e.g., RAG pipeline). Agents: dynamic decisions, multiple tools (e.g., DS analysis selecting tools). Use chains for known steps, agents for dynamic tasks.

---

## Section C: Embeddings and RAG

**Q12:** B — Embedding is a numerical vector representing text meaning.

**Q13:** B — Cosine similarity measures angle between vectors.

**Q14:** Load → Split → Embed → Store → Retrieve → Generate.

**Q15:** LLMs have limited context windows. Chunking splits documents to fit within limits. Without chunking, documents may exceed context window or lose important information.

**Q16:** Causes: (1) Irrelevant documents retrieved — solution: add metadata filtering. (2) Wrong chunk size — solution: experiment with sizes. (3) Poor embeddings — solution: try different embedding models.

**Q17:** RAG: retrieves external knowledge, good for knowledge retrieval, easy to update. Fine-tuning: modifies model behavior, good for style/tasks, expensive. Use RAG for knowledge, fine-tuning for behavior.

**Q18:** Metadata filtering by topic/year, query rewriting, reranking, hybrid search, parent-child chunking.

---

## Section D: Tools and Agents

**Q19:** B — @tool decorator creates LangChain tools.

**Q20:** B — Think, Act, Observe, Think again.

**Q21:**
```python
from langchain_core.tools import tool

@tool
def calculate_f1(precision: float, recall: float) -> float:
    """Calculate F1 score from precision and recall."""
    if precision + recall == 0:
        return 0.0
    return 2 * (precision * recall) / (precision + recall)
```

**Q22:** Validation prevents: (1) SQL injection — block DROP/DELETE. (2) Code injection — validate input format. (3) Resource exhaustion — limit input size.

**Q23:** Tools: dataset_summary, calculate_statistics, correlation_analysis, suggest_model. Safety: input validation, rate limiting, logging, read-only data access.

---

## Section E: LangGraph

**Q24:** B — LangGraph builds stateful graph workflows.

**Q25:** State: dictionary carrying information through graph. Node: function that reads/writes state. Edge: connection between nodes.

**Q26:** Design: START → classify → {conceptual: RAG, numerical: tools, general: LLM} → validate → END. State carries question, route, context, answer.

---

## Section F: SQL and Data Science AI

**Q27:** B — LLMs can generate destructive queries.

**Q28:** (1) SELECT-only validation. (2) No DROP/DELETE/UPDATE. (3) Show SQL before execution. (4) Read-only database connection.

**Q29:** Architecture: User → NL input → LLM generates SQL → Validate SQL → Execute on read-only DB → Format results → LLM explains in natural language. Security: input validation, query validation, rate limiting, logging.

---

## Section G: Evaluation

**Q30:** B — Using one LLM to evaluate another's output.

**Q31:** (1) Retrieval precision: are retrieved docs relevant? (2) Answer relevance: does answer address question? (3) Faithfulness: is answer supported by context? (4) Latency: how fast is response?

---

## Section H: Security

**Q32:** B — User overriding system instructions via crafted input.

**Q33:** (1) Input validation — block injection attempts. (2) Document sanitization — remove malicious content. (3) Output validation — prevent data leakage.

---

## Section I: MCP and Production

**Q34:** B — MCP standardizes tool integration across AI applications.

**Q35:** (1) Configuration management. (2) Error handling and retries. (3) Caching and rate limiting. (4) Logging and monitoring.

---

## Section J: Architecture

**Q36:** Complete answer should include:
- Router classifying questions
- RAG for conceptual questions
- Tools for numerical analysis
- SQL for database queries
- Input/output validation
- Evaluation metrics
- Security measures
- Architecture diagram

---

**Back to:** [Final Quiz](final_quiz.md) | [Quiz Index](README.md)
