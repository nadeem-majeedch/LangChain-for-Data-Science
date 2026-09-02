# Teaching Roadmap

Map all 17 notebooks into 9 teaching stages.

---

## Stage 1: Foundations (Weeks 1-2)

**Notebooks:** 01, 02, 03

**Teaching Objective:** Students understand LLM basics, LangChain architecture, prompts, and chains.

| Notebook | Topic | Key Concepts |
|----------|-------|-------------|
| 01 | Introduction | LLMs, LangChain, API vs Ollama |
| 02 | Models & Prompts | Chat models, messages, templates, structured output |
| 03 | Chains | LCEL, pipe operator, Runnables |

**Prerequisite Knowledge:** Basic Python, API concepts

**Recommended Teaching Time:** 6-9 hours

**Student Activities:**
- Run first LLM call
- Create prompt templates
- Build simple chains
- Experiment with temperature

**Assessment:** Quiz 1 (concepts + basic coding)

---

## Stage 2: Retrieval (Weeks 3-4)

**Notebooks:** 04, 05

**Teaching Objective:** Students understand embeddings, vector stores, and RAG.

| Notebook | Topic | Key Concepts |
|----------|-------|-------------|
| 04 | Embeddings | Vectors, cosine similarity, ChromaDB |
| 05 | RAG | Load, split, embed, store, retrieve, generate |

**Prerequisite Knowledge:** Stage 1

**Recommended Teaching Time:** 6 hours

**Student Activities:**
- Create embeddings
- Build vector store
- Implement RAG pipeline
- Test with different queries

**Assessment:** Quiz 2 + Lab 2

---

## Stage 3: Agents (Weeks 5-6)

**Notebooks:** 06, 07

**Teaching Objective:** Students understand tools, agents, and how to combine components.

| Notebook | Topic | Key Concepts |
|----------|-------|-------------|
| 06 | Tools & Agents | @tool, agent loop, tool calling |
| 07 | Capstone | Combining RAG + tools + prompts |

**Prerequisite Knowledge:** Stages 1-2

**Recommended Teaching Time:** 6-9 hours

**Student Activities:**
- Create Data Science tools
- Build tool-using agent
- Combine components in capstone

**Assessment:** Assignment 1 (RAG + Tools)

---

## Stage 4: Advanced RAG & Data (Weeks 7-8)

**Notebooks:** 08, 09, 10, 11

**Teaching Objective:** Students learn advanced RAG, document processing, SQL, and DS agents.

| Notebook | Topic | Key Concepts |
|----------|-------|-------------|
| 08 | Advanced RAG | Chunking, metadata, query transformation |
| 09 | Document Loading | PDF, CSV, JSON, multimodal |
| 10 | SQL | NL-to-SQL, safe queries |
| 11 | DS Agents | Autonomous analysis |

**Prerequisite Knowledge:** Stages 1-3

**Recommended Teaching Time:** 12 hours

**Student Activities:**
- Implement metadata filtering
- Load different document types
- Build SQL assistant
- Create DS analysis agent

**Assessment:** Assignment 2 + Midterm

---

## Stage 5: Orchestration (Week 9)

**Notebook:** 12

**Teaching Objective:** Students understand stateful workflows with LangGraph.

| Notebook | Topic | Key Concepts |
|----------|-------|-------------|
| 12 | LangGraph | State, nodes, edges, conditional routing |

**Prerequisite Knowledge:** Stages 1-4

**Recommended Teaching Time:** 3 hours

**Student Activities:**
- Build simple graph
- Implement conditional routing
- Add validation loops

**Assessment:** Lab 6

---

## Stage 6: Evaluation & Security (Week 10)

**Notebooks:** 13, 14

**Teaching Objective:** Students learn to evaluate and secure LLM applications.

| Notebook | Topic | Key Concepts |
|----------|-------|-------------|
| 13 | Evaluation | Metrics, LLM-as-judge, observability |
| 14 | Security | Prompt injection, tool security, defense |

**Prerequisite Knowledge:** Stages 1-5

**Recommended Teaching Time:** 6 hours

**Student Activities:**
- Build evaluation dataset
- Implement LLM-as-judge
- Test prompt injection defenses
- Design secure RAG

**Assessment:** Assignment 3

---

## Stage 7: Emerging Technologies (Week 11)

**Notebook:** 15

**Teaching Objective:** Students understand MCP and standardized tool integration.

| Notebook | Topic | Key Concepts |
|----------|-------|-------------|
| 15 | MCP | Protocol, servers, tools, resources |

**Prerequisite Knowledge:** Stages 1-6

**Recommended Teaching Time:** 3 hours

**Student Activities:**
- Create MCP server
- Connect to LangChain
- Test tool calling

**Assessment:** Lab 8

---

## Stage 8: Production (Week 11)

**Notebook:** 16

**Teaching Objective:** Students learn production deployment concepts.

| Notebook | Topic | Key Concepts |
|----------|-------|-------------|
| 16 | Production | Config, error handling, caching, deployment |

**Prerequisite Knowledge:** Stages 1-7

**Recommended Teaching Time:** 3 hours

**Student Activities:**
- Implement configuration management
- Add error handling and retries
- Build production-ready app

**Assessment:** Lab 8

---

## Stage 9: Capstone (Weeks 12-14)

**Notebook:** 17

**Teaching Objective:** Students build a complete Data Science AI Copilot.

| Notebook | Topic | Key Concepts |
|----------|-------|-------------|
| 17 | Final Capstone | Complete application combining all concepts |

**Prerequisite Knowledge:** All previous stages

**Recommended Teaching Time:** 6-9 hours

**Student Activities:**
- Design architecture
- Implement all components
- Evaluate and test
- Present to class

**Assessment:** Final Capstone (20% of grade)

---

**Back to:** [Instructor Guide](README.md) | [Course Plan](course_plan.md)
