# Final Capstone: Build a Data Science AI Copilot

## Overview

This is the **final capstone project** of the LangChain-for-Data-Science course. You will build a complete Data Science AI Copilot that combines concepts from all 17 notebooks.

**Estimated Time:** 15-20 hours
**Difficulty:** Expert

## Project Description

Build an AI assistant that helps Data Science students learn, practice, and apply their knowledge. The system should support multiple interaction types and provide helpful, accurate responses.

## Minimum Requirements (70 points)

| # | Requirement | Points |
|---|-------------|--------|
| 1 | **LLM Integration** — Use ChatOpenAI or ChatOllama | 5 |
| 2 | **Prompt Engineering** — Use ChatPromptTemplate with system messages | 5 |
| 3 | **Structured Output** — Use Pydantic models for consistent responses | 5 |
| 4 | **RAG Pipeline** — Search a knowledge base of 10+ documents | 10 |
| 5 | **Embeddings** — Use OpenAI or Ollama embeddings | 5 |
| 6 | **Vector Store** — Use ChromaDB with persistence | 5 |
| 7 | **2+ Tools** — Create at least 2 Data Science tools | 10 |
| 8 | **Data Science Dataset** — Use a real CSV dataset | 5 |
| 9 | **Evaluation** — Test with 10+ questions, measure quality | 10 |
| 10 | **Security** — Input validation, output validation | 10 |

## Advanced Requirements (30 bonus points)

| # | Requirement | Bonus |
|---|-------------|-------|
| 11 | **Agent** — LLM selects tools automatically | +5 |
| 12 | **LangGraph** — Stateful workflow with routing | +5 |
| 13 | **SQL** — Natural language database queries | +5 |
| 14 | **Metadata Filtering** — Filter by topic/difficulty | +3 |
| 15 | **Advanced RAG** — Query rewriting or reranking | +3 |
| 16 | **Observability** — Logging, metrics, tracing | +3 |
| 17 | **MCP** — MCP server integration | +3 |
| 18 | **Production Features** — Caching, rate limiting | +3 |

## Deliverables

1. **Source Code** — Complete, well-documented Python code
2. **README** — Setup instructions and architecture description
3. **Architecture Diagram** — Mermaid or hand-drawn diagram
4. **Evaluation Report** — Test results with 10+ questions
5. **Security Documentation** — Security measures implemented
6. **Demo** — Working demonstration of all features

## Domain Selection

Choose ONE domain for your copilot:

| Domain | Example Use Cases |
|--------|------------------|
| **Healthcare Education** | Medical terminology, drug interactions, clinical guidelines |
| **Finance Education** | Financial metrics, investment concepts, risk analysis |
| **Agriculture** | Crop science, soil analysis, climate data |
| **Cybersecurity Education** | Threat types, security protocols, vulnerability analysis |
| **Software Engineering** | Design patterns, algorithms, code review |
| **Business Analytics** | KPIs, market analysis, customer segmentation |

## Architecture Requirements

Your copilot must include:

```
User Question
    |
    v
Input Validation
    |
    v
Router (classify question type)
    |
    +---> RAG Pipeline (conceptual questions)
    +---> Tools (numerical questions)
    +---> SQL (database questions)
    +---> LLM (general questions)
    |
    v
Output Validation
    |
    v
Response to User
```

## Evaluation

See [rubric.md](rubric.md) for the detailed grading rubric.

## Getting Started

1. Review all 17 notebooks and readings
2. Choose your domain
3. Create your knowledge base (10+ documents)
4. Design your tools and prompts
5. Implement step by step
6. Test thoroughly
7. Document everything

---

**Back to:** [Assignment Index](../README.md)
