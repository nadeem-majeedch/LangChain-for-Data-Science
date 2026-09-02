# Course Plan: LangChain for Data Science

## Course Information

| Field | Details |
|-------|---------|
| **Course** | Tools and Techniques in Data Science |
| **Module** | LangChain for Data Science |
| **Level** | BS Data Science (3rd/4th year) |
| **Duration** | 8-12 weeks (adjustable) |
| **Hours per week** | 3 hours lecture + 2 hours lab |
| **Total hours** | 40-60 hours |

## Prerequisites

| Skill | Level | How Verified |
|-------|-------|-------------|
| Python | Intermediate | Programming courses |
| Pandas | Basic | Data Science courses |
| NumPy | Basic | Data Science courses |
| ML Concepts | Basic | Machine Learning course |
| SQL | Basic | Database courses |
| Command line | Basic | Prerequisite |

## Learning Outcomes

By the end of this course, students will be able to:

1. **Explain** LLM application architecture and components
2. **Use** LangChain to interact with LLMs
3. **Design** effective prompts for Data Science tasks
4. **Build** chains using LCEL
5. **Generate** and use embeddings for semantic search
6. **Build** vector-search systems with ChromaDB
7. **Implement** RAG applications for knowledge retrieval
8. **Create** tools that extend LLM capabilities
9. **Build** agents that select and use tools dynamically
10. **Design** stateful workflows with LangGraph
11. **Evaluate** LLM applications systematically
12. **Identify** and mitigate LLM security risks
13. **Build** natural-language SQL applications safely
14. **Understand** MCP for standardized tool integration
15. **Design** production-oriented LLM systems
16. **Build** a complete Data Science AI Copilot

## Teaching Methodology

| Method | Percentage | Description |
|--------|-----------|-------------|
| **Lectures** | 30% | Conceptual explanations, live demos |
| **Labs** | 25% | Hands-on coding, experiments |
| **Exercises** | 15% | Practice problems, homework |
| **Assessments** | 15% | Quizzes, module tests |
| **Projects** | 15% | Mini-projects, capstone |

## Notebook Mapping

| Week | Notebook | Topic | Hours |
|------|----------|-------|-------|
| 1 | 01 | LangChain Introduction | 3 |
| 1 | 02 | Models, Prompts, Messages | 3 |
| 2 | 03 | LCEL and Chains | 3 |
| 2 | 04 | Embeddings & Vector Stores | 3 |
| 3 | 05 | RAG Applications | 3 |
| 3 | 06 | Tools and Agents | 3 |
| 4 | 07 | Capstone Project | 3 |
| 4 | 08 | Advanced RAG | 3 |
| 5 | 09 | Document Loading | 3 |
| 5 | 10 | SQL & Databases | 3 |
| 6 | 11 | Data Science Agents | 3 |
| 6 | 12 | LangGraph | 3 |
| 7 | 13 | Evaluation & Observability | 3 |
| 7 | 14 | Security | 3 |
| 8 | 15 | MCP | 3 |
| 8 | 16 | Production Applications | 3 |
| 9 | 17 | Final Capstone | 6 |

## Reading Mapping

Each notebook has a corresponding reading in `readings/`:

| Notebook | Reading | Pre-reading? |
|----------|---------|-------------|
| 01 | 01_LangChain_Introduction.md | Yes |
| 02 | 02_Models_Prompts_and_Messages.md | Yes |
| 03 | 03_LCEL_and_Chains.md | Yes |
| 04 | 04_Embeddings_and_Vector_Stores.md | Yes |
| 05 | 05_RAG_Applications.md | Yes |
| 06 | 06_Tools_and_Agents.md | Yes |
| 07 | 07_Advanced_LangChain_Project.md | Optional |
| 08 | 08_Advanced_RAG.md | Yes |
| 09 | 09_Document_Loading_and_Multimodal_RAG.md | Yes |
| 10 | 10_SQL_and_Database_AI.md | Yes |
| 11 | 11_Data_Science_Agents.md | Yes |
| 12 | 12_LangGraph_for_Data_Science.md | Yes |
| 13 | 13_LLM_Evaluation_and_Observability.md | Yes |
| 14 | 14_LLM_Security_and_Prompt_Injection.md | Yes |
| 15 | 15_MCP_for_Data_Science.md | Yes |
| 16 | 16_Production_LLM_Applications.md | Yes |
| 17 | 17_Final_Data_Science_Copilot.md | Optional |

## Assessment Mapping

| Assessment | Notebooks Covered | Weight |
|-----------|-------------------|--------|
| Quiz 1 | 01-02 | 5% |
| Quiz 2 | 03-04 | 5% |
| Lab 1 | 01-03 | 5% |
| Lab 2 | 04-05 | 5% |
| Assignment 1 | 05-06 | 10% |
| Midterm | 01-08 | 15% |
| Assignment 2 | 08-12 | 10% |
| Assignment 3 | 12-16 | 10% |
| Capstone | 17 | 20% |
| Final Exam | 01-17 | 15% |

## API vs Ollama Teaching Strategy

| Phase | Approach | Rationale |
|-------|----------|-----------|
| **Weeks 1-4** | API only | Simple setup, consistent results |
| **Weeks 5-8** | Introduce Ollama | Privacy, cost, local inference |
| **Weeks 9+** | Both | Students choose based on use case |

**Recommendation:** Start with API for simplicity, then demonstrate Ollama to teach privacy and local deployment concepts.

## Resources Needed

| Resource | Quantity | Notes |
|----------|----------|-------|
| **Computers** | 1 per student | Jupyter Notebook access |
| **Internet** | Required | For API calls (or Ollama for offline) |
| **API Key** | 1 per student or shared | OpenAI API key |
| **Ollama** | Optional | For local model experiments |
| **Projector** | 1 | For live demos |

## Course Schedule (12-Week Version)

| Week | Topic | Notebook | Lab | Assessment |
|------|-------|----------|-----|------------|
| 1 | Introduction & Models | 01, 02 | Lab 1 | Quiz 1 |
| 2 | Chains & Embeddings | 03, 04 | Lab 2 | Quiz 2 |
| 3 | RAG & Tools | 05, 06 | Lab 3 | Assignment 1 |
| 4 | Capstone & Advanced RAG | 07, 08 | Lab 4 | - |
| 5 | Documents & SQL | 09, 10 | Lab 5 | - |
| 6 | Agents & LangGraph | 11, 12 | Lab 6 | Assignment 2 |
| 7 | Evaluation & Security | 13, 14 | Lab 7 | Midterm |
| 8 | MCP & Production | 15, 16 | Lab 8 | Assignment 3 |
| 9-11 | Capstone Project | 17 | Lab 9-11 | - |
| 12 | Final Presentations | - | - | Final Exam |

---

**Back to:** [Instructor Guide](README.md) | [Repository README](../README.md)
