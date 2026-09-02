#!/usr/bin/env python3
"""Generate all assignment files for the LangChain-for-Data-Science repository."""
import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  Created: {path}")

# ============================================================
# ASSIGNMENTS INDEX
# ============================================================
write_file("assignments/README.md", """# Exercises & Assessments

This folder contains practice exercises, assessments, and challenges for each notebook.

## Learning Workflow

```
📖 Read the concept → 💻 Run the notebook → 🧪 Experiment → 📝 Practice exercises → 🎯 Take the assessment → 🚀 Attempt the challenge
```

| Layer | Purpose | Where |
|-------|---------|-------|
| **Readings** | Conceptual understanding | `readings/` |
| **Notebooks** | Hands-on coding | `notebooks/` |
| **Exercises** | Practice and reinforcement | `assignments/*/exercises.md` |
| **Assessments** | Test understanding | `assignments/*/assessment.md` |
| **Challenges** | Deep application | `assignments/*/challenge.md` |
| **Capstone** | Complete project | `assignments/final_capstone/` |

## All Assignments

| # | Topic | Exercises | Assessment | Challenge |
|---|-------|-----------|------------|-----------|
| 01 | [LangChain Introduction](01_LangChain_Introduction/) | [Exercises](01_LangChain_Introduction/exercises.md) | [Assessment](01_LangChain_Introduction/assessment.md) | [Challenge](01_LangChain_Introduction/challenge.md) |
| 02 | [Models, Prompts & Messages](02_Models_Prompts_and_Messages/) | [Exercises](02_Models_Prompts_and_Messages/exercises.md) | [Assessment](02_Models_Prompts_and_Messages/assessment.md) | [Challenge](02_Models_Prompts_and_Messages/challenge.md) |
| 03 | [LCEL and Chains](03_LCEL_and_Chains/) | [Exercises](03_LCEL_and_Chains/exercises.md) | [Assessment](03_LCEL_and_Chains/assessment.md) | [Challenge](03_LCEL_and_Chains/challenge.md) |
| 04 | [Embeddings & Vector Stores](04_Embeddings_and_Vector_Stores/) | [Exercises](04_Embeddings_and_Vector_Stores/exercises.md) | [Assessment](04_Embeddings_and_Vector_Stores/assessment.md) | [Challenge](04_Embeddings_and_Vector_Stores/challenge.md) |
| 05 | [RAG Applications](05_RAG_Applications/) | [Exercises](05_RAG_Applications/exercises.md) | [Assessment](05_RAG_Applications/assessment.md) | [Challenge](05_RAG_Applications/challenge.md) |
| 06 | [Tools and Agents](06_Tools_and_Agents/) | [Exercises](06_Tools_and_Agents/exercises.md) | [Assessment](06_Tools_and_Agents/assessment.md) | [Challenge](06_Tools_and_Agents/challenge.md) |
| 07 | [Advanced LangChain Project](07_Advanced_LangChain_Project/) | [Exercises](07_Advanced_LangChain_Project/exercises.md) | [Assessment](07_Advanced_LangChain_Project/assessment.md) | [Challenge](07_Advanced_LangChain_Project/challenge.md) |
| 08 | [Advanced RAG](08_Advanced_RAG/) | [Exercises](08_Advanced_RAG/exercises.md) | [Assessment](08_Advanced_RAG/assessment.md) | [Challenge](08_Advanced_RAG/challenge.md) |
| 09 | [Document Loading](09_Document_Loading_and_Multimodal_RAG/) | [Exercises](09_Document_Loading_and_Multimodal_RAG/exercises.md) | [Assessment](09_Document_Loading_and_Multimodal_RAG/assessment.md) | [Challenge](09_Document_Loading_and_Multimodal_RAG/challenge.md) |
| 10 | [SQL and Databases](10_SQL_and_Database_AI/) | [Exercises](10_SQL_and_Database_AI/exercises.md) | [Assessment](10_SQL_and_Database_AI/assessment.md) | [Challenge](10_SQL_and_Database_AI/challenge.md) |
| 11 | [Data Science Agents](11_Data_Science_Agents/) | [Exercises](11_Data_Science_Agents/exercises.md) | [Assessment](11_Data_Science_Agents/assessment.md) | [Challenge](11_Data_Science_Agents/challenge.md) |
| 12 | [LangGraph](12_LangGraph_for_Data_Science/) | [Exercises](12_LangGraph_for_Data_Science/exercises.md) | [Assessment](12_LangGraph_for_Data_Science/assessment.md) | [Challenge](12_LangGraph_for_Data_Science/challenge.md) |
| 13 | [Evaluation & Observability](13_LLM_Evaluation_and_Observability/) | [Exercises](13_LLM_Evaluation_and_Observability/exercises.md) | [Assessment](13_LLM_Evaluation_and_Observability/assessment.md) | [Challenge](13_LLM_Evaluation_and_Observability/challenge.md) |
| 14 | [Security](14_LLM_Security_and_Prompt_Injection/) | [Exercises](14_LLM_Security_and_Prompt_Injection/exercises.md) | [Assessment](14_LLM_Security_and_Prompt_Injection/assessment.md) | [Challenge](14_LLM_Security_and_Prompt_Injection/challenge.md) |
| 15 | [MCP](15_MCP_for_Data_Science/) | [Exercises](15_MCP_for_Data_Science/exercises.md) | [Assessment](15_MCP_for_Data_Science/assessment.md) | [Challenge](15_MCP_for_Data_Science/challenge.md) |
| 16 | [Production Applications](16_Production_LLM_Applications/) | [Exercises](16_Production_LLM_Applications/exercises.md) | [Assessment](16_Production_LLM_Applications/assessment.md) | [Challenge](16_Production_LLM_Applications/challenge.md) |
| 17 | [Final Capstone](17_Final_Data_Science_Copilot/) | [Exercises](17_Final_Data_Science_Copilot/exercises.md) | [Assessment](17_Final_Data_Science_Copilot/assessment.md) | [Challenge](17_Final_Data_Science_Copilot/challenge.md) |

## Final Projects

| Project | Description |
|---------|-------------|
| [Final Capstone](final_capstone/) | Build a complete Data Science AI Copilot |
| [Final Course Assessment](../final_course_assessment.md) | Comprehensive exam covering all topics |

## Grading Scale

| Grade | Percentage | Description |
|-------|-----------|-------------|
| A | 90-100% | Excellent understanding and application |
| B+ | 80-89% | Strong understanding with minor gaps |
| B | 70-79% | Good understanding, some areas need work |
| C+ | 60-69% | Satisfactory, major areas need improvement |
| C | 50-59% | Passing, significant gaps in understanding |
| F | <50% | Does not meet minimum requirements |

---

**Back to:** [Repository README](../README.md)
""")

# ============================================================
# EXERCISES TEMPLATE GENERATOR
# ============================================================
def gen_exercises(num, title, notebook_path, reading_path, exercises):
    """Generate exercises for a notebook."""
    content = f"""# Exercises: {title}

📖 **Reading:** [{title}]({reading_path})
💻 **Notebook:** [{title}]({notebook_path})

---

## Level 1 — Basic

"""
    for i, ex in enumerate(exercises.get('basic', []), 1):
        content += f"""### Exercise {i}: {ex['title']}

**Objective:** {ex['objective']}

**Task:** {ex['task']}

**Requirements:**
{chr(10).join('- ' + r for r in ex['requirements'])}

**Expected Learning Outcome:** {ex['outcome']}

---

"""
    content += """## Level 2 — Intermediate

"""
    for i, ex in enumerate(exercises.get('intermediate', []), 1):
        content += f"""### Exercise {i}: {ex['title']}

**Objective:** {ex['objective']}

**Task:** {ex['task']}

**Requirements:**
{chr(10).join('- ' + r for r in ex['requirements'])}

**Expected Learning Outcome:** {ex['outcome']}

---

"""
    content += """## Level 3 — Advanced

"""
    for i, ex in enumerate(exercises.get('advanced', []), 1):
        content += f"""### Exercise {i}: {ex['title']}

**Objective:** {ex['objective']}

**Task:** {ex['task']}

**Requirements:**
{chr(10).join('- ' + r for r in ex['requirements'])}

**Hints:**
{chr(10).join('- ' + h for h in ex.get('hints', []))}

**Expected Learning Outcome:** {ex['outcome']}

---

"""
    content += """
**Next:** [Take the Assessment](assessment.md) | [Attempt the Challenge](challenge.md)

**Back to:** [Assignment Index](../README.md)
"""
    return content

# ============================================================
# ASSESSMENT TEMPLATE GENERATOR
# ============================================================
def gen_assessment(num, title, notebook_path, reading_path, questions, total_marks=100):
    """Generate assessment for a notebook."""
    content = f"""# Assessment: {title}

📖 **Reading:** [{title}]({reading_path})
💻 **Notebook:** [{title}]({notebook_path})

**Total Marks:** {total_marks}
**Time:** 60 minutes

---

## Marking Rubric

| Performance Level | Description |
|------------------|-------------|
| **Excellent** | Complete, correct, well-documented, insightful |
| **Good** | Mostly correct with minor issues |
| **Satisfactory** | Partially correct, basic understanding shown |
| **Needs Improvement** | Significant errors or missing elements |

---

## Part A: Conceptual Questions ({questions['conceptual_marks']} marks)

"""
    for i, q in enumerate(questions.get('conceptual', []), 1):
        badge = q.get('badge', '')
        badge_str = f" {badge}" if badge else ""
        content += f"""### Q{i}:{badge_str} {q['question']}

*({q['marks']} marks)*

"""
    content += f"""
---

## Part B: Programming Questions ({questions['programming_marks']} marks)

"""
    for i, q in enumerate(questions.get('programming', []), 1):
        badge = q.get('badge', '')
        badge_str = f" {badge}" if badge else ""
        content += f"""### Q{i}:{badge_str} {q['question']}

*({q['marks']} marks)*

"""
    content += f"""
---

## Part C: Application & Analysis ({questions['application_marks']} marks)

"""
    for i, q in enumerate(questions.get('application', []), 1):
        badge = q.get('badge', '')
        badge_str = f" {badge}" if badge else ""
        content += f"""### Q{i}:{badge_str} {q['question']}

*({q['marks']} marks)*

"""
    content += """
---

**Next:** [Attempt the Challenge](challenge.md)

**Back to:** [Assignment Index](../README.md)
"""
    return content

# ============================================================
# CHALLENGE TEMPLATE GENERATOR
# ============================================================
def gen_challenge(num, title, notebook_path, reading_path, challenge):
    """Generate challenge for a notebook."""
    content = f"""# Challenge: {title}

📖 **Reading:** [{title}]({reading_path})
💻 **Notebook:** [{title}]({notebook_path})

**Difficulty:** {challenge['difficulty']}
**Estimated Time:** {challenge['time']}

---

## {challenge['title']}

{challenge['description']}

### Requirements

{chr(10).join(str(i+1) + '. ' + r for i, r in enumerate(challenge['requirements']))}

### Deliverables

{chr(10).join('- ' + d for d in challenge['deliverables'])}

### Evaluation Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
{chr(10).join('| ' + c['name'] + ' | ' + c['weight'] + ' | ' + c['desc'] + ' |' for c in challenge['criteria'])}

### Getting Started

{challenge.get('getting_started', 'Start by reviewing the notebook and identifying the key concepts you need to combine.')}

---

**Next:** [Back to Assignments](../README.md)

**Back to:** [Assignment Index](../README.md)
"""
    return content

# ============================================================
# SOLUTION STUB GENERATOR
# ============================================================
def gen_solution_stub(num, title):
    return f"""# Solution: {title}

> This file is for **instructors only**. Do not share with students.

## Overview

This solution provides the expected approach and key concepts for the exercises in Notebook {num:02d}.

## Key Concepts Tested

- Concept 1
- Concept 2
- Concept 3

## Exercise Solutions

### Level 1

**Approach:** [Describe the expected approach]

**Key points:**
- Point 1
- Point 2

### Level 2

**Approach:** [Describe the expected approach]

**Key points:**
- Point 1
- Point 2

### Level 3

**Approach:** [Describe the expected approach]

**Key points:**
- Point 1
- Point 2

## Assessment Solutions

### Part A: Conceptual

1. [Expected answer]
2. [Expected answer]

### Part B: Programming

1. [Expected approach and key code]

### Part C: Application

1. [Expected analysis]

## Common Student Mistakes

- Mistake 1
- Mistake 2

## Grading Notes

- Adjust marks based on code quality, not just correctness
- Partial credit for correct approach with implementation errors
- Bonus for innovative solutions
"""

# ============================================================
# GENERATE ALL FILES
# ============================================================

# Define exercises for each notebook
all_exercises = {
    1: {
        'basic': [
            {'title': 'Hello LangChain', 'objective': 'Set up and run a basic LangChain call', 'task': 'Write a LangChain program that sends a question about Data Science to the LLM and prints the response.', 'requirements': ['Use ChatOpenAI or ChatOllama', 'Include a system message', 'Handle missing API key gracefully'], 'outcome': 'Student can create a basic LLM interaction'}
        ],
        'intermediate': [
            {'title': 'Model Comparison', 'objective': 'Compare different model configurations', 'task': 'Send the same Data Science question to two different model configurations (e.g., temperature 0 vs 0.7) and compare the responses.', 'requirements': ['Create two LLM instances with different parameters', 'Send identical prompts', 'Compare response quality and consistency'], 'outcome': 'Student understands model parameter effects'}
        ],
        'advanced': [
            {'title': 'Multi-Provider Setup', 'objective': 'Build a provider-agnostic LLM interface', 'task': 'Create a function that can switch between OpenAI API and Ollama with a single configuration change.', 'requirements': ['Use environment variables for provider selection', 'Handle both providers gracefully', 'Include error handling for unavailable providers'], 'hints': ['Use os.getenv to select provider', 'Create factory functions'], 'outcome': 'Student understands provider abstraction'}
        ]
    },
    2: {
        'basic': [
            {'title': 'Prompt Template Creation', 'objective': 'Create reusable prompt templates', 'task': 'Create a prompt template that explains a Data Science concept at different difficulty levels (beginner, intermediate, advanced).', 'requirements': ['Use ChatPromptTemplate', 'Include variables for concept and level', 'Test with at least 3 concepts'], 'outcome': 'Student can create parameterized prompts'}
        ],
        'intermediate': [
            {'title': 'Few-Shot Classification', 'objective': 'Build a few-shot prompt for classification', 'task': 'Create a few-shot prompt that classifies Data Science questions into categories (theory, code, math, data).', 'requirements': ['Include at least 4 examples', 'Test with 5 unseen questions', 'Measure accuracy'], 'outcome': 'Student understands few-shot prompting'}
        ],
        'advanced': [
            {'title': 'Structured Output Pipeline', 'objective': 'Build a structured output pipeline', 'task': 'Create a system that takes an algorithm name and returns a structured explanation with name, definition, intuition, use_case, and difficulty.', 'requirements': ['Use Pydantic model', 'Use with_structured_output()', 'Validate output programmatically'], 'hints': ['Define a clear Pydantic schema', 'Test with 5 different algorithms'], 'outcome': 'Student can build type-safe LLM outputs'}
        ]
    },
    3: {
        'basic': [
            {'title': 'First Chain', 'objective': 'Build a simple LCEL chain', 'task': 'Create a chain that takes a topic and produces a one-paragraph explanation.', 'requirements': ['Use the pipe operator', 'Include prompt and parser', 'Test with 3 topics'], 'outcome': 'Student can chain LLM components'}
        ],
        'intermediate': [
            {'title': 'Parallel Analysis', 'objective': 'Build a parallel chain', 'task': 'Create a chain that takes a Data Science concept and generates both a definition AND a quiz question simultaneously.', 'requirements': ['Use RunnableParallel', 'Combine results', 'Format output nicely'], 'outcome': 'Student understands parallel execution'}
        ],
        'advanced': [
            {'title': 'Concept Explainer Pipeline', 'objective': 'Build a multi-step concept explainer', 'task': 'Build a pipeline that: 1) Classifies a topic, 2) Generates explanation appropriate for that level, 3) Creates a quiz, 4) Combines everything.', 'requirements': ['Use multiple chain types', 'Include conditional logic', 'Handle errors gracefully'], 'hints': ['Use RunnableLambda for classification', 'Chain parallel outputs'], 'outcome': 'Student can build complex LCEL pipelines'}
        ]
    },
    4: {
        'basic': [
            {'title': 'Embedding Comparison', 'objective': 'Understand embedding similarity', 'task': 'Create embeddings for 5 Data Science terms and compute pairwise cosine similarities.', 'requirements': ['Use OpenAIEmbeddings or OllamaEmbeddings', 'Compute cosine similarity', 'Display results in a table'], 'outcome': 'Student understands embedding similarity'}
        ],
        'intermediate': [
            {'title': 'Knowledge Base Builder', 'objective': 'Build a searchable knowledge base', 'task': 'Create a vector store with 10+ Data Science documents and test similarity search with 5 queries.', 'requirements': ['Use ChromaDB', 'Include metadata', 'Test different k values'], 'outcome': 'Student can build vector search systems'}
        ],
        'advanced': [
            {'title': 'Semantic Search Engine', 'objective': 'Build a complete semantic search system', 'task': 'Build a search system that supports: keyword filtering, metadata filtering, similarity scores, and result ranking.', 'requirements': ['Implement all search modes', 'Compare results across modes', 'Include evaluation metrics'], 'hints': ['Use similarity_search_with_score', 'Add metadata filtering'], 'outcome': 'Student can build production search systems'}
        ]
    },
    5: {
        'basic': [
            {'title': 'First RAG Pipeline', 'objective': 'Build a basic RAG system', 'task': 'Build a RAG system that answers questions about 3 Data Science topics.', 'requirements': ['Load documents', 'Create vector store', 'Implement retrieval + generation'], 'outcome': 'Student understands the RAG pipeline'}
        ],
        'intermediate': [
            {'title': 'Chunking Experiment', 'objective': 'Understand chunk size effects', 'task': 'Compare RAG quality with chunk sizes of 200, 500, and 1000 tokens. Measure retrieval precision.', 'requirements': ['Create evaluation dataset', 'Test all chunk sizes', 'Document results'], 'outcome': 'Student understands chunking tradeoffs'}
        ],
        'advanced': [
            {'title': 'Course Q&A System', 'objective': 'Build a complete course assistant', 'task': 'Build a RAG system over course notes that answers questions, provides citations, and handles out-of-domain queries.', 'requirements': ['10+ documents', 'Source inspection', 'Graceful fallback', 'Evaluation'], 'hints': ['Add metadata filtering', 'Implement confidence scoring'], 'outcome': 'Student can build production RAG systems'}
        ]
    },
    6: {
        'basic': [
            {'title': 'First Tool', 'objective': 'Create and use a LangChain tool', 'task': 'Create a tool that calculates the F1 score from precision and recall values.', 'requirements': ['Use @tool decorator', 'Include type hints', 'Test the tool'], 'outcome': 'Student can create LangChain tools'}
        ],
        'intermediate': [
            {'title': 'Multi-Tool Agent', 'objective': 'Build an agent with multiple tools', 'task': 'Build an agent with 4 tools: calculate_mean, calculate_std, calculate_f1, and dataset_summary.', 'requirements': ['Implement all 4 tools', 'Test agent with various queries', 'Verify correct tool selection'], 'outcome': 'Student understands tool routing'}
        ],
        'advanced': [
            {'title': 'Safe DS Agent', 'objective': 'Build a safe Data Science agent', 'task': 'Build an agent that validates all tool inputs, logs all calls, and handles errors gracefully.', 'requirements': ['Input validation', 'Error handling', 'Logging', 'Rate limiting'], 'hints': ['Wrap tools with validation', 'Add try/except blocks'], 'outcome': 'Student can build secure agents'}
        ]
    },
    7: {
        'basic': [
            {'title': 'Component Review', 'objective': 'Review capstone architecture', 'task': 'Document the architecture of the capstone project, listing each component and its purpose.', 'requirements': ['Identify all components', 'Draw architecture diagram', 'Explain data flow'], 'outcome': 'Student understands application architecture'}
        ],
        'intermediate': [
            {'title': 'Feature Extension', 'objective': 'Extend the capstone application', 'task': 'Add a new feature to the Data Science AI Tutor (e.g., quiz generation, code review).', 'requirements': ['Follow existing patterns', 'Include tests', 'Document the feature'], 'outcome': 'Student can extend LLM applications'}
        ],
        'advanced': [
            {'title': 'Architecture Redesign', 'objective': 'Redesign for production', 'task': 'Propose production-ready changes to the capstone: error handling, logging, caching, rate limiting.', 'requirements': ['Identify production gaps', 'Propose solutions', 'Implement at least 2 improvements'], 'hints': ['Review notebook 16 for production patterns'], 'outcome': 'Student understands production readiness'}
        ]
    },
    8: {
        'basic': [
            {'title': 'Chunking Comparison', 'objective': 'Compare chunking strategies', 'task': 'Compare fixed-size vs recursive chunking on the same document set.', 'requirements': ['Implement both strategies', 'Compare retrieval quality', 'Document findings'], 'outcome': 'Student understands chunking impacts'}
        ],
        'intermediate': [
            {'title': 'Metadata-Enhanced RAG', 'objective': 'Add metadata filtering to RAG', 'task': 'Add difficulty-level metadata to documents and filter retrieval by student level.', 'requirements': ['Add metadata to documents', 'Implement filtering', 'Test with different levels'], 'outcome': 'Student can use metadata for precision'}
        ],
        'advanced': [
            {'title': 'Query Transformation', 'objective': 'Implement query rewriting', 'task': 'Implement query rewriting that expands abbreviations and adds synonyms before retrieval.', 'requirements': ['Implement rewriting function', 'Compare results with/without', 'Measure improvement'], 'hints': ['Use LLM to rewrite queries', 'Test with ambiguous queries'], 'outcome': 'Student can improve retrieval quality'}
        ]
    },
    9: {
        'basic': [
            {'title': 'Document Loading', 'objective': 'Load different file formats', 'task': 'Create a Markdown file, a CSV file, and load both using appropriate LangChain loaders.', 'requirements': ['Create sample files', 'Use correct loaders', 'Verify document content'], 'outcome': 'Student can load multiple formats'}
        ],
        'intermediate': [
            {'title': 'Multi-Format RAG', 'objective': 'Build RAG over mixed formats', 'task': 'Build a RAG system that searches across Markdown notes AND a CSV dataset.', 'requirements': ['Load both formats', 'Create unified vector store', 'Test cross-format search'], 'outcome': 'Student can handle heterogeneous data'}
        ],
        'advanced': [
            {'title': 'PDF Processing Pipeline', 'objective': 'Process PDF documents', 'task': 'Create a small PDF with Data Science content and build a RAG pipeline for it.', 'requirements': ['Generate or find a PDF', 'Extract text correctly', 'Handle tables and figures'], 'hints': ['Use fpdf2 or reportlab to create PDF', 'Test extraction quality'], 'outcome': 'Student can process PDF documents'}
        ]
    },
    10: {
        'basic': [
            {'title': 'SQL Basics', 'objective': 'Write safe SQL queries', 'task': 'Write 5 SELECT queries for the student database created in the notebook.', 'requirements': ['Use SELECT only', 'Include WHERE clauses', 'Use aggregation'], 'outcome': 'Student can query databases safely'}
        ],
        'intermediate': [
            {'title': 'NL-to-SQL Translation', 'objective': 'Translate natural language to SQL', 'task': 'Test the NL-to-SQL system with 10 different natural language questions.', 'requirements': ['Test simple queries', 'Test complex queries', 'Test edge cases'], 'outcome': 'Student understands NL-to-SQL challenges'}
        ],
        'advanced': [
            {'title': 'Safe SQL Agent', 'objective': 'Build a secure SQL assistant', 'task': 'Build a SQL assistant that validates all queries, blocks dangerous operations, and provides natural language explanations.', 'requirements': ['Input validation', 'Query validation', 'Result explanation', 'Error handling'], 'hints': ['Create a whitelist of allowed operations', 'Add query complexity limits'], 'outcome': 'Student can build secure database tools'}
        ]
    },
    11: {
        'basic': [
            {'title': 'DS Tool Suite', 'objective': 'Create Data Science tools', 'task': 'Create 3 tools: calculate_correlation, detect_outliers, and feature_importance.', 'requirements': ['Use @tool decorator', 'Include proper type hints', 'Test each tool'], 'outcome': 'Student can create DS-specific tools'}
        ],
        'intermediate': [
            {'title': 'Analysis Pipeline', 'objective': 'Build an analysis agent', 'task': 'Build an agent that can analyze a CSV dataset through multiple steps.', 'requirements': ['Load data', 'Profile dataset', 'Calculate statistics', 'Generate report'], 'outcome': 'Student can build analysis agents'}
        ],
        'advanced': [
            {'title': 'Autonomous DS Analyst', 'objective': 'Build a fully autonomous analyst', 'task': 'Build an agent that takes a dataset and automatically: profiles, analyzes, identifies patterns, and suggests models.', 'requirements': ['Full automation', 'Multiple tools', 'Error recovery', 'Comprehensive output'], 'hints': ['Use tool selection wisely', 'Add fallback strategies'], 'outcome': 'Student can build autonomous DS systems'}
        ]
    },
    12: {
        'basic': [
            {'title': 'First Graph', 'objective': 'Build a simple LangGraph workflow', 'task': 'Build a graph with 3 nodes: classify, process, and respond.', 'requirements': ['Use StateGraph', 'Add nodes and edges', 'Test with different inputs'], 'outcome': 'Student can create basic graphs'}
        ],
        'intermediate': [
            {'title': 'Conditional Routing', 'objective': 'Implement conditional routing', 'task': 'Build a graph that routes to different handlers based on question type.', 'requirements': ['Implement routing function', 'Add conditional edges', 'Test all routes'], 'outcome': 'Student understands conditional routing'}
        ],
        'advanced': [
            {'title': 'DS Research Graph', 'objective': 'Build a research assistant graph', 'task': 'Build a graph that: classifies questions, routes to RAG/tools/LLM, validates answers, and loops if needed.', 'requirements': ['All route types', 'Validation node', 'Retry loop', 'State management'], 'hints': ['Use TypedDict for state', 'Add max iteration limit'], 'outcome': 'Student can build complex LangGraph workflows'}
        ]
    },
    13: {
        'basic': [
            {'title': 'Build Eval Dataset', 'objective': 'Create an evaluation dataset', 'task': 'Create an evaluation dataset with 10 questions covering different difficulty levels.', 'requirements': ['Include expected answers', 'Cover multiple topics', 'Include edge cases'], 'outcome': 'Student can create evaluation datasets'}
        ],
        'intermediate': [
            {'title': 'LLM-as-Judge', 'objective': 'Implement LLM evaluation', 'task': 'Implement an LLM-as-judge that evaluates RAG answers on relevance and groundedness.', 'requirements': ['Design judge prompt', 'Score on multiple criteria', 'Compare with manual evaluation'], 'outcome': 'Student can automate evaluation'}
        ],
        'advanced': [
            {'title': 'Evaluation Framework', 'objective': 'Build a complete evaluation system', 'task': 'Build a system that evaluates: retrieval quality, answer quality, latency, and cost.', 'requirements': ['Multiple metrics', 'Automated pipeline', 'Report generation', 'Comparison across models'], 'hints': ['Track timing separately', 'Use structured output for scores'], 'outcome': 'Student can build evaluation frameworks'}
        ]
    },
    14: {
        'basic': [
            {'title': 'Input Filter', 'objective': 'Implement basic input validation', 'task': 'Create a function that detects and blocks common prompt injection attempts.', 'requirements': ['Check for injection patterns', 'Block suspicious input', 'Log blocked attempts'], 'outcome': 'Student understands basic input validation'}
        ],
        'intermediate': [
            {'title': 'Secure RAG Pipeline', 'objective': 'Add security to RAG', 'task': 'Add input validation, output sanitization, and document sanitization to a RAG pipeline.', 'requirements': ['Validate user input', 'Sanitize retrieved documents', 'Check output for leakage'], 'outcome': 'Student can secure RAG systems'}
        ],
        'advanced': [
            {'title': 'Security Audit', 'objective': 'Perform a security audit', 'task': 'Audit a provided LLM application for security vulnerabilities and implement fixes.', 'requirements': ['Identify vulnerabilities', 'Prioritize by severity', 'Implement fixes', 'Document findings'], 'hints': ['Check for prompt injection, data leakage, tool abuse'], 'outcome': 'Student can perform security audits'}
        ]
    },
    15: {
        'basic': [
            {'title': 'MCP Server Basics', 'objective': 'Create a simple MCP server', 'task': 'Create an MCP server with 2 tools using FastMCP.', 'requirements': ['Use @mcp.tool()', 'Include proper documentation', 'Test the server'], 'outcome': 'Student can create MCP servers'}
        ],
        'intermediate': [
            {'title': 'MCP + LangChain', 'objective': 'Connect MCP to LangChain', 'task': 'Connect an MCP server to a LangChain agent and test tool calling.', 'requirements': ['Use MultiServerMCPClient', 'Test with multiple queries', 'Handle errors'], 'outcome': 'Student can integrate MCP with LangChain'}
        ],
        'advanced': [
            {'title': 'Multi-Server System', 'objective': 'Build a multi-server MCP system', 'task': 'Create 2 MCP servers (stats and data) and connect both to a single agent.', 'requirements': ['Two independent servers', 'Single agent using both', 'Demonstrate tool routing'], 'hints': ['Use MultiServerMCPClient with multiple entries'], 'outcome': 'Student can build multi-server architectures'}
        ]
    },
    16: {
        'basic': [
            {'title': 'Configuration Manager', 'objective': 'Implement proper configuration', 'task': 'Create a configuration class that loads settings from environment variables.', 'requirements': ['Use dataclass', 'Include defaults', 'Support .env file'], 'outcome': 'Student understands configuration management'}
        ],
        'intermediate': [
            {'title': 'Error Recovery', 'objective': 'Implement retry logic', 'task': 'Add exponential backoff retry logic to an LLM application.', 'requirements': ['Implement retry function', 'Handle rate limits', 'Add logging'], 'outcome': 'Student can handle production errors'}
        ],
        'advanced': [
            {'title': 'Production App', 'objective': 'Build a production-ready app', 'task': 'Add caching, rate limiting, cost tracking, and input validation to an LLM application.', 'requirements': ['All four features', 'Unit tests', 'Documentation'], 'hints': ['Review the notebook for implementation patterns'], 'outcome': 'Student can build production applications'}
        ]
    },
    17: {
        'basic': [
            {'title': 'Architecture Review', 'objective': 'Review the complete copilot', 'task': 'Document the architecture of the Data Science AI Copilot, explaining each component.', 'requirements': ['Architecture diagram', 'Component descriptions', 'Data flow explanation'], 'outcome': 'Student understands complete application architecture'}
        ],
        'intermediate': [
            {'title': 'Feature Addition', 'objective': 'Extend the copilot', 'task': 'Add a new capability to the copilot (e.g., code review, data visualization).', 'requirements': ['New tool or route', 'Integration with router', 'Testing'], 'outcome': 'Student can extend complex applications'}
        ],
        'advanced': [
            {'title': 'Evaluation Framework', 'objective': 'Build comprehensive evaluation', 'task': 'Build a test suite with 15+ test cases covering all copilot capabilities.', 'requirements': ['All route types', 'Edge cases', 'Security tests', 'Performance tests'], 'hints': ['Use the evaluation pattern from notebook 13'], 'outcome': 'Student can build comprehensive test suites'}
        ]
    }
}

# Define assessments for each notebook
all_assessments = {
    1: {'conceptual_marks': 20, 'programming_marks': 30, 'application_marks': 50,
        'conceptual': [
            {'question': 'Explain the difference between an LLM and a Chat Model in your own words.', 'marks': 5},
            {'question': 'Why would you use LangChain instead of calling the OpenAI API directly?', 'marks': 5},
            {'question': 'Describe the LangChain architecture layers and their purposes.', 'marks': 5, 'badge': '🟢 Understand'},
            {'question': 'What are the tradeoffs between using a cloud API vs a local Ollama model?', 'marks': 5, 'badge': '🟡 Apply'}
        ],
        'programming': [
            {'question': 'Write a LangChain program that asks the LLM to explain a Data Science concept and prints the response. Include proper error handling for missing API keys.', 'marks': 10, 'badge': '🟡 Apply'},
            {'question': 'Create a function that selects between OpenAI and Ollama based on an environment variable.', 'marks': 10, 'badge': '🟡 Apply'},
            {'question': 'Debug this code: [provide broken code with missing import]. Explain the error and fix it.', 'marks': 10, 'badge': '🟠 Analyze'}
        ],
        'application': [
            {'question': 'Your university wants to build a private Data Science assistant using confidential student data. Compare an API-based solution with a local Ollama solution, considering privacy, cost, hardware, and model quality.', 'marks': 25, 'badge': '🔴 Evaluate'},
            {'question': 'Design the architecture for a Data Science tutoring system. What components would you need? Draw a diagram and explain your choices.', 'marks': 25, 'badge': '🔴 Create'}
        ]},
    2: {'conceptual_marks': 20, 'programming_marks': 35, 'application_marks': 45,
        'conceptual': [
            {'question': 'What is the purpose of a system message in a chat model interaction?', 'marks': 5},
            {'question': 'Explain the difference between few-shot and zero-shot prompting.', 'marks': 5, 'badge': '🟢 Understand'},
            {'question': 'Why is structured output important for LLM applications?', 'marks': 5},
            {'question': 'How does temperature affect LLM output quality?', 'marks': 5, 'badge': '🟡 Apply'}
        ],
        'programming': [
            {'question': 'Create a ChatPromptTemplate that takes an algorithm name and student level, and produces an appropriate explanation. Test with 3 algorithms at 3 levels.', 'marks': 15, 'badge': '🟡 Apply'},
            {'question': 'Build a few-shot prompt that classifies Data Science questions into categories. Include at least 4 examples.', 'marks': 10, 'badge': '🟡 Apply'},
            {'question': 'Fix this broken prompt template: [provide template with syntax error]. Explain what was wrong.', 'marks': 10, 'badge': '🟠 Analyze'}
        ],
        'application': [
            {'question': 'Design a prompt system for a Data Science quiz generator that creates questions at different difficulty levels. Show your prompt templates and explain your design choices.', 'marks': 25, 'badge': '🔴 Create'},
            {'question': 'You are building a Data Science tutor. How would you use structured output to return consistent quiz questions? Design the Pydantic model and explain why each field is necessary.', 'marks': 20, 'badge': '🔴 Create'}
        ]},
    3: {'conceptual_marks': 20, 'programming_marks': 35, 'application_marks': 45,
        'conceptual': [
            {'question': 'What is the pipe operator (|) in LCEL and how does it connect components?', 'marks': 5, 'badge': '🟢 Understand'},
            {'question': 'Explain the difference between RunnablePassthrough and RunnableLambda.', 'marks': 5},
            {'question': 'When would you use a parallel chain vs a sequential chain?', 'marks': 5, 'badge': '🟠 Analyze'},
            {'question': 'What are the advantages of LCEL over traditional chain construction?', 'marks': 5}
        ],
        'programming': [
            {'question': 'Build a chain that takes a Data Science topic and produces: 1) a definition, 2) a quiz question, 3) a Python example. Use parallel execution.', 'marks': 15, 'badge': '🟡 Apply'},
            {'question': 'Create a chain that formats retrieved documents and passes them to the LLM. Use RunnablePassthrough correctly.', 'marks': 10, 'badge': '🟡 Apply'},
            {'question': 'Debug this chain: prompt | model (missing StrOutputParser). Explain why the output is not what you expect.', 'marks': 10, 'badge': '🟠 Analyze'}
        ],
        'application': [
            {'question': 'Design a multi-step Data Science concept explainer pipeline. It should: classify the topic difficulty, generate appropriate explanation, create a quiz, and format the output. Draw the pipeline diagram.', 'marks': 25, 'badge': '🔴 Create'},
            {'question': 'Compare when you would use a chain vs an agent for a Data Science application. Provide 3 specific scenarios for each.', 'marks': 20, 'badge': '🔴 Evaluate'}
        ]},
    4: {'conceptual_marks': 25, 'programming_marks': 35, 'application_marks': 40,
        'conceptual': [
            {'question': 'Explain what an embedding is and why it captures meaning, not just words.', 'marks': 5, 'badge': '🟢 Understand'},
            {'question': 'How does cosine similarity work? What does a score of 0.8 mean?', 'marks': 5},
            {'question': 'Why is keyword search sometimes insufficient for Data Science queries?', 'marks': 5},
            {'question': 'Explain the difference between an embedding model and a chat model.', 'marks': 5},
            {'question': 'What role does metadata play in vector search?', 'marks': 5, 'badge': '🟡 Apply'}
        ],
        'programming': [
            {'question': 'Create a vector store with 5 Data Science documents including metadata (topic, difficulty). Test similarity search with 3 queries.', 'marks': 15, 'badge': '🟡 Apply'},
            {'question': 'Implement a function that computes cosine similarity manually using NumPy. Compare results with the library implementation.', 'marks': 10, 'badge': '🟡 Apply'},
            {'question': 'Your search returns irrelevant results. Diagnose the problem by testing: 1) different k values, 2) metadata filtering, 3) different queries.', 'marks': 10, 'badge': '🟠 Analyze'}
        ],
        'application': [
            {'question': 'Design a semantic search system for a Data Science course. What documents would you include? How would you structure metadata? How would you handle different query types?', 'marks': 20, 'badge': '🔴 Create'},
            {'question': 'Compare API embeddings vs local Ollama embeddings for a university setting. Consider cost, privacy, quality, and latency.', 'marks': 20, 'badge': '🔴 Evaluate'}
        ]},
    5: {'conceptual_marks': 20, 'programming_marks': 35, 'application_marks': 45,
        'conceptual': [
            {'question': 'What problem does RAG solve that a standalone LLM cannot?', 'marks': 5, 'badge': '🟢 Understand'},
            {'question': 'Explain the RAG pipeline from document loading to answer generation.', 'marks': 5},
            {'question': 'What is hallucination and how does RAG help reduce it?', 'marks': 5, 'badge': '🟡 Apply'},
            {'question': 'When would you use RAG vs fine-tuning?', 'marks': 5, 'badge': '🟠 Analyze'}
        ],
        'programming': [
            {'question': 'Build a complete RAG system over 5 Data Science documents. Include: loading, chunking, embedding, storage, retrieval, and generation.', 'marks': 15, 'badge': '🟡 Apply'},
            {'question': 'Experiment with chunk sizes (200, 500, 1000). Create an evaluation dataset and measure retrieval precision for each size.', 'marks': 10, 'badge': '🟠 Analyze'},
            {'question': 'Your RAG system returns irrelevant documents. Write a debugging plan listing 5 things to investigate.', 'marks': 10, 'badge': '🟠 Analyze'}
        ],
        'application': [
            {'question': 'Design a RAG system for a university Data Science course. What documents would you include? How would you chunk them? How would you handle different question types?', 'marks': 25, 'badge': '🔴 Create'},
            {'question': 'Your RAG system sometimes gives wrong answers even with correct retrieved documents. Analyze possible causes and propose solutions.', 'marks': 20, 'badge': '🔴 Evaluate'}
        ]},
    6: {'conceptual_marks': 20, 'programming_marks': 35, 'application_marks': 45,
        'conceptual': [
            {'question': 'What is the agent loop and how does it differ from a chain?', 'marks': 5, 'badge': '🟢 Understand'},
            {'question': 'Explain how the LLM decides which tool to use.', 'marks': 5},
            {'question': 'Why is tool validation important for agent safety?', 'marks': 5, 'badge': '🟡 Apply'},
            {'question': 'When would you use an agent instead of a fixed chain?', 'marks': 5, 'badge': '🟠 Analyze'}
        ],
        'programming': [
            {'question': 'Create 3 Data Science tools: calculate_f1, detect_outliers, and suggest_model. Test each tool individually.', 'marks': 15, 'badge': '🟡 Apply'},
            {'question': 'Build an agent that uses all 3 tools and answer questions about a sample dataset.', 'marks': 10, 'badge': '🟡 Apply'},
            {'question': 'Add input validation to one of your tools. Test with valid and invalid inputs. Document what you blocked and why.', 'marks': 10, 'badge': '🟠 Analyze'}
        ],
        'application': [
            {'question': 'Design a Data Science agent for a research lab. What tools would it need? How would you ensure safety? How would you handle tool failures?', 'marks': 25, 'badge': '🔴 Create'},
            {'question': 'Compare the agent approach with a fixed pipeline for analyzing a dataset. What are the tradeoffs? When is each appropriate?', 'marks': 20, 'badge': '🔴 Evaluate'}
        ]},
    7: {'conceptual_marks': 25, 'programming_marks': 30, 'application_marks': 45,
        'conceptual': [
            {'question': 'What are the key components of the Data Science AI Tutor?', 'marks': 5},
            {'question': 'How does the application switch between API and Ollama modes?', 'marks': 5, 'badge': '🟢 Understand'},
            {'question': 'Explain the factory pattern used in the capstone project.', 'marks': 5, 'badge': '🟡 Apply'},
            {'question': 'Why is the Config class important for the application?', 'marks': 5},
            {'question': 'How does error handling differ in a notebook vs a production application?', 'marks': 5, 'badge': '🟠 Analyze'}
        ],
        'programming': [
            {'question': 'Add a new tool to the capstone application (e.g., generate_code). Follow the existing patterns.', 'marks': 15, 'badge': '🟡 Apply'},
            {'question': 'Write 3 test cases for the capstone application covering: normal use, edge case, and error case.', 'marks': 15, 'badge': '🟡 Apply'}
        ],
        'application': [
            {'question': 'Redesign the capstone for production deployment. What changes would you make? Consider: error handling, logging, caching, rate limiting, security.', 'marks': 25, 'badge': '🔴 Create'},
            {'question': 'Evaluate the capstone application. What are its strengths? What are its limitations? How would you improve it?', 'marks': 20, 'badge': '🔴 Evaluate'}
        ]},
    8: {'conceptual_marks': 20, 'programming_marks': 35, 'application_marks': 45,
        'conceptual': [
            {'question': 'What are the limitations of naive RAG that advanced techniques address?', 'marks': 5, 'badge': '🟢 Understand'},
            {'question': 'Explain query rewriting and when it helps.', 'marks': 5},
            {'question': 'What is reranking and why is vector similarity not enough?', 'marks': 5, 'badge': '🟡 Apply'},
            {'question': 'How does metadata filtering improve retrieval precision?', 'marks': 5}
        ],
        'programming': [
            {'question': 'Implement query rewriting using the LLM. Compare retrieval results with and without rewriting.', 'marks': 15, 'badge': '🟡 Apply'},
            {'question': 'Build a metadata-filtered search that returns only beginner-level documents.', 'marks': 10, 'badge': '🟡 Apply'},
            {'question': 'Implement a simple reranker that scores retrieved documents by relevance to the query.', 'marks': 10, 'badge': '🟠 Analyze'}
        ],
        'application': [
            {'question': 'Design an advanced RAG system for a Data Science course. Address: chunking strategy, metadata, query handling, and evaluation.', 'marks': 25, 'badge': '🔴 Create'},
            {'question': 'Your advanced RAG system is slow. Analyze the performance bottlenecks and propose optimizations.', 'marks': 20, 'badge': '🔴 Evaluate'}
        ]},
    9: {'conceptual_marks': 20, 'programming_marks': 35, 'application_marks': 45,
        'conceptual': [
            {'question': 'Why do different document formats need different loaders?', 'marks': 5, 'badge': '🟢 Understand'},
            {'question': 'What is the difference between document retrieval and structured data analysis?', 'marks': 5},
            {'question': 'Explain the concept of multimodal RAG.', 'marks': 5, 'badge': '🟡 Apply'},
            {'question': 'What security risks exist when processing external documents?', 'marks': 5}
        ],
        'programming': [
            {'question': 'Create a Markdown file and a CSV file with Data Science content. Load both using appropriate LangChain loaders.', 'marks': 15, 'badge': '🟡 Apply'},
            {'question': 'Build a RAG system that searches across both Markdown and CSV content.', 'marks': 10, 'badge': '🟡 Apply'},
            {'question': 'Test your document loader with edge cases: empty files, very long files, files with special characters.', 'marks': 10, 'badge': '🟠 Analyze'}
        ],
        'application': [
            {'question': 'Design a multi-format knowledge assistant that handles: lecture notes (Markdown), datasets (CSV), research papers (PDF), and FAQs (JSON).', 'marks': 25, 'badge': '🔴 Create'},
            {'question': 'Evaluate the security of a system that processes documents from untrusted sources. What protections would you implement?', 'marks': 20, 'badge': '🔴 Evaluate'}
        ]},
    10: {'conceptual_marks': 20, 'programming_marks': 35, 'application_marks': 45,
        'conceptual': [
            {'question': 'Why is SQL injection a concern with LLM-generated queries?', 'marks': 5, 'badge': '🟢 Understand'},
            {'question': 'Explain the difference between read-only and read-write database access.', 'marks': 5},
            {'question': 'How does natural language to SQL translation work?', 'marks': 5, 'badge': '🟡 Apply'},
            {'question': 'What are the limitations of NL-to-SQL systems?', 'marks': 5, 'badge': '🟠 Analyze'}
        ],
        'programming': [
            {'question': 'Write 5 SELECT queries for the student database. Include: filtering, aggregation, joins, sorting.', 'marks': 15, 'badge': '🟡 Apply'},
            {'question': 'Test the NL-to-SQL system with 5 natural language questions. Document which ones work and which fail.', 'marks': 10, 'badge': '🟠 Analyze'},
            {'question': 'Implement a SQL validator that blocks: DROP, DELETE, UPDATE, INSERT. Test with safe and unsafe queries.', 'marks': 10, 'badge': '🟡 Apply'}
        ],
        'application': [
            {'question': 'Design a natural language database assistant for a university registrar. What tables would it query? What security measures are needed?', 'marks': 25, 'badge': '🔴 Create'},
            {'question': 'Compare using LLM for SQL generation vs using traditional BI tools. When is each appropriate?', 'marks': 20, 'badge': '🔴 Evaluate'}
        ]},
    11: {'conceptual_marks': 20, 'programming_marks': 35, 'application_marks': 45,
        'conceptual': [
            {'question': 'How does a Data Science agent differ from a traditional data analysis pipeline?', 'marks': 5, 'badge': '🟢 Understand'},
            {'question': 'Explain the concept of tool selection in agent-based systems.', 'marks': 5},
            {'question': 'Why is agent safety particularly important for Data Science tools?', 'marks': 5, 'badge': '🟡 Apply'},
            {'question': 'When would you use an agent vs a fixed pipeline for data analysis?', 'marks': 5, 'badge': '🟠 Analyze'}
        ],
        'programming': [
            {'question': 'Create 4 Data Science tools and build an agent that can select the appropriate tool for each question.', 'marks': 15, 'badge': '🟡 Apply'},
            {'question': 'Test your agent with 5 different questions. Document which tools it selects and whether the answers are correct.', 'marks': 10, 'badge': '🟠 Analyze'},
            {'question': 'Add error handling to your agent. Test with edge cases: empty dataset, invalid input, tool failure.', 'marks': 10, 'badge': '🟡 Apply'}
        ],
        'application': [
            {'question': 'Design a Data Science agent for a healthcare analytics team. What tools would it need? What security measures are required?', 'marks': 25, 'badge': '🔴 Create'},
            {'question': 'Evaluate the reliability of your Data Science agent. What failure modes exist? How would you mitigate them?', 'marks': 20, 'badge': '🔴 Evaluate'}
        ]},
    12: {'conceptual_marks': 20, 'programming_marks': 35, 'application_marks': 45,
        'conceptual': [
            {'question': 'What is LangGraph and why was it created?', 'marks': 5, 'badge': '🟢 Understand'},
            {'question': 'Explain the roles of State, Node, and Edge in LangGraph.', 'marks': 5},
            {'question': 'How does conditional routing work in a LangGraph workflow?', 'marks': 5, 'badge': '🟡 Apply'},
            {'question': 'Compare LangChain chains with LangGraph workflows.', 'marks': 5, 'badge': '🟠 Analyze'}
        ],
        'programming': [
            {'question': 'Build a LangGraph workflow with 3 routes: conceptual (RAG), numerical (tools), and general (LLM).', 'marks': 15, 'badge': '🟡 Apply'},
            {'question': 'Add a validation node that checks answer quality and loops back if needed.', 'marks': 10, 'badge': '🟡 Apply'},
            {'question': 'Test your graph with 5 questions. Document which route each takes and whether the answer is correct.', 'marks': 10, 'badge': '🟠 Analyze'}
        ],
        'application': [
            {'question': 'Design a LangGraph workflow for a complete Data Science research assistant. Include routing, tools, validation, and error handling.', 'marks': 25, 'badge': '🔴 Create'},
            {'question': 'Your LangGraph application has an infinite loop. Analyze possible causes and implement safeguards.', 'marks': 20, 'badge': '🔴 Evaluate'}
        ]},
    13: {'conceptual_marks': 20, 'programming_marks': 35, 'application_marks': 45,
        'conceptual': [
            {'question': 'Why is LLM evaluation different from traditional ML evaluation?', 'marks': 5, 'badge': '🟢 Understand'},
            {'question': 'Explain the concept of LLM-as-a-judge and its limitations.', 'marks': 5},
            {'question': 'What metrics would you use to evaluate a RAG system?', 'marks': 5, 'badge': '🟡 Apply'},
            {'question': 'How does observability differ from logging?', 'marks': 5}
        ],
        'programming': [
            {'question': 'Build an evaluation dataset with 10 questions covering different difficulty levels and topics.', 'marks': 15, 'badge': '🟡 Apply'},
            {'question': 'Implement an LLM-as-judge that scores answers on relevance and groundedness.', 'marks': 10, 'badge': '🟡 Apply'},
            {'question': 'Compare LLM-as-judge scores with manual evaluation for 5 questions. Analyze discrepancies.', 'marks': 10, 'badge': '🟠 Analyze'}
        ],
        'application': [
            {'question': 'Design an evaluation framework for a Data Science tutoring system. What metrics would you track? How would you automate evaluation?', 'marks': 25, 'badge': '🔴 Create'},
            {'question': 'Your evaluation shows high relevance but low groundedness. Analyze what this means and how to fix it.', 'marks': 20, 'badge': '🔴 Evaluate'}
        ]},
    14: {'conceptual_marks': 25, 'programming_marks': 30, 'application_marks': 45,
        'conceptual': [
            {'question': 'Explain the difference between direct and indirect prompt injection.', 'marks': 5, 'badge': '🟢 Understand'},
            {'question': 'Why should retrieved documents be treated as untrusted data?', 'marks': 5},
            {'question': 'What is defense in depth in the context of LLM security?', 'marks': 5, 'badge': '🟡 Apply'},
            {'question': 'How does tool validation protect against agent abuse?', 'marks': 5},
            {'question': 'When should you use local models instead of cloud APIs for security reasons?', 'marks': 5, 'badge': '🟠 Analyze'}
        ],
        'programming': [
            {'question': 'Implement an input validator that blocks prompt injection attempts. Test with 5 attack patterns.', 'marks': 15, 'badge': '🟡 Apply'},
            {'question': 'Add output validation to prevent data leakage. Test with sample outputs containing API keys.', 'marks': 15, 'badge': '🟡 Apply'}
        ],
        'application': [
            {'question': 'Design a secure RAG system for a healthcare application. What security layers would you implement? Draw the architecture.', 'marks': 25, 'badge': '🔴 Create'},
            {'question': 'Your LLM application was attacked via indirect prompt injection through a retrieved document. Analyze what happened and how to prevent it.', 'marks': 20, 'badge': '🔴 Evaluate'}
        ]},
    15: {'conceptual_marks': 25, 'programming_marks': 30, 'application_marks': 45,
        'conceptual': [
            {'question': 'What is MCP and what problem does it solve?', 'marks': 5, 'badge': '🟢 Understand'},
            {'question': 'Explain the difference between MCP tools, resources, and prompts.', 'marks': 5},
            {'question': 'Compare LangChain tools with MCP tools. When would you use each?', 'marks': 5, 'badge': '🟡 Apply'},
            {'question': 'What is the benefit of MCP for interoperability?', 'marks': 5},
            {'question': 'What security considerations exist when using MCP servers?', 'marks': 5, 'badge': '🟠 Analyze'}
        ],
        'programming': [
            {'question': 'Create an MCP server with 3 Data Science tools using FastMCP.', 'marks': 15, 'badge': '🟡 Apply'},
            {'question': 'Connect your MCP server to a LangChain agent and test tool calling.', 'marks': 15, 'badge': '🟡 Apply'}
        ],
        'application': [
            {'question': 'Design an MCP-based Data Science toolkit that provides tools for multiple AI applications. What tools would you include? How would you secure the server?', 'marks': 25, 'badge': '🔴 Create'},
            {'question': 'Compare building tools as MCP servers vs directly in the application. What are the tradeoffs for a university setting?', 'marks': 20, 'badge': '🔴 Evaluate'}
        ]},
    16: {'conceptual_marks': 20, 'programming_marks': 35, 'application_marks': 45,
        'conceptual': [
            {'question': 'What are the key differences between a notebook prototype and a production application?', 'marks': 5, 'badge': '🟢 Understand'},
            {'question': 'Why is configuration management important for LLM applications?', 'marks': 5},
            {'question': 'Explain exponential backoff and when to use it.', 'marks': 5, 'badge': '🟡 Apply'},
            {'question': 'How does caching reduce cost in LLM applications?', 'marks': 5}
        ],
        'programming': [
            {'question': 'Create a configuration class that loads settings from environment variables. Include at least 5 configurable parameters.', 'marks': 15, 'badge': '🟡 Apply'},
            {'question': 'Implement a rate limiter that allows at most 10 requests per minute. Test it with 15 rapid requests.', 'marks': 10, 'badge': '🟡 Apply'},
            {'question': 'Add caching to an LLM application. Measure the cost savings for repeated queries.', 'marks': 10, 'badge': '🟠 Analyze'}
        ],
        'application': [
            {'question': 'Design a production deployment plan for a Data Science AI assistant. Consider: infrastructure, monitoring, scaling, security, and cost.', 'marks': 25, 'badge': '🔴 Create'},
            {'question': 'Your LLM application is experiencing high latency. Analyze possible causes and propose solutions.', 'marks': 20, 'badge': '🔴 Evaluate'}
        ]},
    17: {'conceptual_marks': 15, 'programming_marks': 35, 'application_marks': 50,
        'conceptual': [
            {'question': 'How does the smart router in the Data Science AI Copilot decide which handler to use?', 'marks': 5, 'badge': '🟢 Understand'},
            {'question': 'Explain the architecture of the complete copilot system.', 'marks': 5, 'badge': '🟡 Apply'},
            {'question': 'What security measures are implemented in the copilot?', 'marks': 5}
        ],
        'programming': [
            {'question': 'Add a new route and handler to the copilot (e.g., code_review). Follow the existing patterns.', 'marks': 15, 'badge': '🟡 Apply'},
            {'question': 'Build a test suite with 5 test cases covering all route types.', 'marks': 10, 'badge': '🟡 Apply'},
            {'question': 'Implement caching for the copilot. Test with repeated queries.', 'marks': 10, 'badge': '🟠 Analyze'}
        ],
        'application': [
            {'question': 'Evaluate the complete Data Science AI Copilot. What are its strengths and limitations? How would you improve it for a real university deployment?', 'marks': 25, 'badge': '🔴 Evaluate'},
            {'question': 'Design the next version of the copilot. What new features would you add? How would you scale it? What security improvements are needed?', 'marks': 25, 'badge': '🔴 Create'}
        ]}
}

# Define challenges for each notebook
all_challenges = {
    1: {'title': 'Multi-Provider LLM Interface', 'difficulty': 'Intermediate', 'time': '2-3 hours',
        'description': 'Build a Python module that provides a unified interface to multiple LLM providers (OpenAI, Ollama) with automatic fallback.',
        'requirements': ['Support at least 2 providers', 'Automatic fallback on failure', 'Configuration via environment variables', 'Proper error handling and logging'],
        'deliverables': ['Python module with unified interface', 'Configuration documentation', 'Test script with 5 queries'],
        'criteria': [
            {'name': 'Functionality', 'weight': '40%', 'desc': 'Works with all providers'},
            {'name': 'Error handling', 'weight': '25%', 'desc': 'Graceful fallback and logging'},
            {'name': 'Code quality', 'weight': '20%', 'desc': 'Clean, documented, testable'},
            {'name': 'Documentation', 'weight': '15%', 'desc': 'Clear usage instructions'}
        ]},
    2: {'title': 'Data Science Quiz Generator', 'difficulty': 'Intermediate', 'time': '3-4 hours',
        'description': 'Build a quiz generator that creates Data Science questions at different difficulty levels using structured output.',
        'requirements': ['Pydantic model for quiz questions', 'Support for beginner/intermediate/advanced', 'Multiple question types (MCQ, short answer, code)', 'Quiz scoring and feedback'],
        'deliverables': ['Quiz generator module', 'Sample quizzes at each level', 'Scoring system'],
        'criteria': [
            {'name': 'Quiz quality', 'weight': '35%', 'desc': 'Questions are accurate and educational'},
            {'name': 'Structured output', 'weight': '25%', 'desc': 'Proper Pydantic usage'},
            {'name': 'Difficulty levels', 'weight': '25%', 'desc': 'Appropriate complexity per level'},
            {'name': 'User experience', 'weight': '15%', 'desc': 'Clear presentation and feedback'}
        ]},
    3: {'title': 'Data Science Concept Pipeline', 'difficulty': 'Advanced', 'time': '4-5 hours',
        'description': 'Build a multi-step pipeline that takes a Data Science topic and produces a comprehensive learning module.',
        'requirements': ['Topic classification', 'Multi-perspective explanation', 'Quiz generation', 'Code example generation', 'All connected via LCEL chains'],
        'deliverables': ['Complete pipeline code', 'Example output for 3 topics', 'Architecture diagram'],
        'criteria': [
            {'name': 'Pipeline design', 'weight': '30%', 'desc': 'Clean LCEL composition'},
            {'name': 'Output quality', 'weight': '30%', 'desc': 'Comprehensive and accurate'},
            {'name': 'Chain types', 'weight': '25%', 'desc': 'Uses sequential, parallel, and conditional'},
            {'name': 'Documentation', 'weight': '15%', 'desc': 'Clear explanation of design choices'}
        ]},
    4: {'title': 'Semantic Search Engine for ML Concepts', 'difficulty': 'Advanced', 'time': '4-5 hours',
        'description': 'Build a semantic search engine specifically for Machine Learning concepts with advanced filtering.',
        'requirements': ['20+ documents with metadata', 'Semantic search', 'Metadata filtering', 'Similarity scores', 'Search result ranking'],
        'deliverables': ['Search engine module', '20+ ML concept documents', 'Evaluation results', 'Comparison with keyword search'],
        'criteria': [
            {'name': 'Search quality', 'weight': '35%', 'desc': 'Relevant results'},
            {'name': 'Metadata usage', 'weight': '25%', 'desc': 'Effective filtering'},
            {'name': 'Evaluation', 'weight': '25%', 'desc': 'Measurable improvement over baseline'},
            {'name': 'Documentation', 'weight': '15%', 'desc': 'Clear usage and results'}
        ]},
    5: {'title': 'Course RAG Assistant', 'difficulty': 'Advanced', 'time': '5-6 hours',
        'description': 'Build a complete RAG assistant for a Data Science course with source citations and quality scoring.',
        'requirements': ['15+ course documents', 'Source citations in answers', 'Confidence scoring', 'Out-of-domain detection', 'Evaluation framework'],
        'deliverables': ['RAG assistant', 'Course document collection', 'Evaluation results', 'Test script with 10 queries'],
        'criteria': [
            {'name': 'Retrieval quality', 'weight': '30%', 'desc': 'Relevant document retrieval'},
            {'name': 'Answer quality', 'weight': '25%', 'desc': 'Grounded, accurate answers'},
            {'name': 'Source citation', 'weight': '20%', 'desc': 'Proper attribution'},
            {'name': 'Evaluation', 'weight': '15%', 'desc': 'Comprehensive testing'},
            {'name': 'Error handling', 'weight': '10%', 'desc': 'Graceful failure modes'}
        ]},
    6: {'title': 'Safe Data Science Tool Agent', 'difficulty': 'Advanced', 'time': '5-6 hours',
        'description': 'Build a Data Science agent with comprehensive safety measures including input validation, rate limiting, and audit logging.',
        'requirements': ['5+ Data Science tools', 'Input validation for all tools', 'Rate limiting', 'Audit logging', 'Error recovery', 'Security documentation'],
        'deliverables': ['Safe agent implementation', 'Security documentation', 'Test results with attacks', 'Audit log examples'],
        'criteria': [
            {'name': 'Tool functionality', 'weight': '25%', 'desc': 'All tools work correctly'},
            {'name': 'Security', 'weight': '30%', 'desc': 'Comprehensive protections'},
            {'name': 'Logging', 'weight': '20%', 'desc': 'Complete audit trail'},
            {'name': 'Testing', 'weight': '15%', 'desc': 'Security testing results'},
            {'name': 'Documentation', 'weight': '10%', 'desc': 'Security analysis'}
        ]},
    7: {'title': 'Capstone Feature Extension', 'difficulty': 'Advanced', 'time': '4-5 hours',
        'description': 'Extend the Data Science AI Tutor with a new major feature while maintaining code quality.',
        'requirements': ['New feature (student chooses)', 'Follows existing patterns', 'Includes tests', 'Documentation', 'Security considerations'],
        'deliverables': ['Extended application', 'Feature documentation', 'Test results', 'Security review'],
        'criteria': [
            {'name': 'Feature quality', 'weight': '30%', 'desc': 'Feature works well'},
            {'name': 'Integration', 'weight': '25%', 'desc': 'Fits existing architecture'},
            {'name': 'Testing', 'weight': '20%', 'desc': 'Comprehensive tests'},
            {'name': 'Documentation', 'weight': '15%', 'desc': 'Clear documentation'},
            {'name': 'Security', 'weight': '10%', 'desc': 'Security reviewed'}
        ]},
    8: {'title': 'Advanced RAG Optimization', 'difficulty': 'Expert', 'time': '6-8 hours',
        'description': 'Optimize a RAG system by implementing advanced techniques: query transformation, metadata filtering, and reranking.',
        'requirements': ['Query rewriting implementation', 'Metadata-based filtering', 'Result reranking', 'A/B comparison', 'Evaluation metrics'],
        'deliverables': ['Optimized RAG system', 'Comparison results', 'Evaluation report', 'Performance analysis'],
        'criteria': [
            {'name': 'Improvement', 'weight': '35%', 'desc': 'Measurable quality improvement'},
            {'name': 'Techniques', 'weight': '25%', 'desc': 'Correct implementation'},
            {'name': 'Evaluation', 'weight': '25%', 'desc': 'Rigorous comparison'},
            {'name': 'Documentation', 'weight': '15%', 'desc': 'Clear methodology'}
        ]},
    9: {'title': 'Multi-Format Knowledge Assistant', 'difficulty': 'Advanced', 'time': '5-6 hours',
        'description': 'Build a knowledge assistant that handles multiple document formats: Markdown, CSV, and JSON.',
        'requirements': ['3+ document formats', 'Unified search across formats', 'Format-appropriate processing', 'Metadata preservation', 'Security for untrusted documents'],
        'deliverables': ['Multi-format assistant', 'Sample documents in each format', 'Search results comparison', 'Security analysis'],
        'criteria': [
            {'name': 'Format handling', 'weight': '30%', 'desc': 'Correct processing per format'},
            {'name': 'Search quality', 'weight': '25%', 'desc': 'Relevant cross-format results'},
            {'name': 'Security', 'weight': '20%', 'desc': 'Document sanitization'},
            {'name': 'Documentation', 'weight': '15%', 'desc': 'Format-specific notes'},
            {'name': 'Testing', 'weight': '10%', 'desc': 'Edge case handling'}
        ]},
    10: {'title': 'Natural Language Database Analyst', 'difficulty': 'Advanced', 'time': '5-6 hours',
        'description': 'Build a natural language database analyst that translates questions to SQL and provides natural language explanations.',
        'requirements': ['Multi-table database', 'NL-to-SQL translation', 'Result explanation', 'Query validation', 'Error handling'],
        'deliverables': ['Database analyst module', 'Sample database', 'Test results with 10 questions', 'Security analysis'],
        'criteria': [
            {'name': 'SQL accuracy', 'weight': '30%', 'desc': 'Correct query generation'},
            {'name': 'Explanation quality', 'weight': '25%', 'desc': 'Clear natural language'},
            {'name': 'Security', 'weight': '25%', 'desc': 'Query validation'},
            {'name': 'Testing', 'weight': '20%', 'desc': 'Comprehensive test cases'}
        ]},
    11: {'title': 'Autonomous Data Science Analyst', 'difficulty': 'Expert', 'time': '6-8 hours',
        'description': 'Build an autonomous agent that takes a dataset and performs complete analysis: profiling, statistics, pattern detection, and model suggestion.',
        'requirements': ['Full automation', 'Multiple analysis tools', 'Comprehensive output', 'Error recovery', 'Security measures'],
        'deliverables': ['Autonomous analyst', 'Analysis report for sample dataset', 'Tool documentation', 'Security review'],
        'criteria': [
            {'name': 'Automation', 'weight': '30%', 'desc': 'Fully autonomous'},
            {'name': 'Analysis quality', 'weight': '25%', 'desc': 'Insightful results'},
            {'name': 'Tool design', 'weight': '20%', 'desc': 'Well-designed tools'},
            {'name': 'Security', 'weight': '15%', 'desc': 'Comprehensive protections'},
            {'name': 'Documentation', 'weight': '10%', 'desc': 'Clear explanation'}
        ]},
    12: {'title': 'LangGraph Research Assistant', 'difficulty': 'Expert', 'time': '6-8 hours',
        'description': 'Build a LangGraph-based research assistant with conditional routing, validation loops, and state management.',
        'requirements': ['3+ routing paths', 'Validation node', 'Retry logic', 'State management', 'Human-in-the-loop concept'],
        'deliverables': ['LangGraph application', 'Architecture diagram', 'Test results', 'Performance analysis'],
        'criteria': [
            {'name': 'Graph design', 'weight': '30%', 'desc': 'Clean, efficient graph'},
            {'name': 'Routing', 'weight': '25%', 'desc': 'Correct conditional routing'},
            {'name': 'State management', 'weight': '20%', 'desc': 'Proper state handling'},
            {'name': 'Testing', 'weight': '15%', 'desc': 'Comprehensive test cases'},
            {'name': 'Documentation', 'weight': '10%', 'desc': 'Architecture explanation'}
        ]},
    13: {'title': 'LLM Evaluation Framework', 'difficulty': 'Expert', 'time': '6-8 hours',
        'description': 'Build a complete evaluation framework for LLM applications with automated metrics and reporting.',
        'requirements': ['Multiple evaluation metrics', 'Automated pipeline', 'LLM-as-judge integration', 'Report generation', 'Comparison capabilities'],
        'deliverables': ['Evaluation framework', 'Sample evaluation report', 'Comparison results', 'Documentation'],
        'criteria': [
            {'name': 'Framework design', 'weight': '30%', 'desc': 'Reusable, extensible'},
            {'name': 'Metrics', 'weight': '25%', 'desc': 'Comprehensive metrics'},
            {'name': 'Automation', 'weight': '20%', 'desc': 'Fully automated pipeline'},
            {'name': 'Reporting', 'weight': '15%', 'desc': 'Clear, informative reports'},
            {'name': 'Documentation', 'weight': '10%', 'desc': 'Usage instructions'}
        ]},
    14: {'title': 'Secure RAG System', 'difficulty': 'Expert', 'time': '6-8 hours',
        'description': 'Design and implement a secure RAG system with comprehensive security measures.',
        'requirements': ['Input validation', 'Document sanitization', 'Output validation', 'Security logging', 'Penetration testing', 'Security documentation'],
        'deliverables': ['Secure RAG system', 'Security documentation', 'Penetration test results', 'Security architecture diagram'],
        'criteria': [
            {'name': 'Security measures', 'weight': '35%', 'desc': 'Comprehensive protections'},
            {'name': 'Testing', 'weight': '25%', 'desc': 'Thorough security testing'},
            {'name': 'Documentation', 'weight': '20%', 'desc': 'Security analysis'},
            {'name': 'Implementation', 'weight': '20%', 'desc': 'Clean, maintainable code'}
        ]},
    15: {'title': 'MCP Data Science Toolkit', 'difficulty': 'Expert', 'time': '5-6 hours',
        'description': 'Build a complete MCP-based Data Science toolkit with multiple servers and a LangGraph client.',
        'requirements': ['2+ MCP servers', '10+ tools total', 'LangGraph client', 'Security measures', 'Documentation'],
        'deliverables': ['MCP servers', 'LangGraph client', 'Tool documentation', 'Integration test results'],
        'criteria': [
            {'name': 'Tool design', 'weight': '30%', 'desc': 'Well-designed, useful tools'},
            {'name': 'MCP compliance', 'weight': '25%', 'desc': 'Correct MCP implementation'},
            {'name': 'Integration', 'weight': '20%', 'desc': 'Smooth LangGraph integration'},
            {'name': 'Security', 'weight': '15%', 'desc': 'Security measures'},
            {'name': 'Documentation', 'weight': '10%', 'desc': 'Clear usage instructions'}
        ]},
    16: {'title': 'Production LLM Application', 'difficulty': 'Expert', 'time': '6-8 hours',
        'description': 'Take a notebook prototype and deploy it as a production-ready application with all operational requirements.',
        'requirements': ['Configuration management', 'Error handling', 'Caching', 'Rate limiting', 'Logging', 'Monitoring', 'Tests'],
        'deliverables': ['Production application', 'Deployment documentation', 'Test suite', 'Monitoring dashboard concept'],
        'criteria': [
            {'name': 'Production readiness', 'weight': '30%', 'desc': 'All operational features'},
            {'name': 'Reliability', 'weight': '25%', 'desc': 'Graceful error handling'},
            {'name': 'Monitoring', 'weight': '20%', 'desc': 'Comprehensive logging'},
            {'name': 'Testing', 'weight': '15%', 'desc': 'Thorough test suite'},
            {'name': 'Documentation', 'weight': '10%', 'desc': 'Deployment guide'}
        ]},
    17: {'title': 'Complete Data Science AI Copilot', 'difficulty': 'Expert', 'time': '8-10 hours',
        'description': 'Build the most complete Data Science AI Copilot possible, combining all concepts from the course.',
        'requirements': ['All route types', 'RAG pipeline', 'Tools', 'SQL', 'Evaluation', 'Security', 'Caching', 'Production features'],
        'deliverables': ['Complete copilot application', 'Evaluation results', 'Security documentation', 'Architecture diagram', 'Demo presentation'],
        'criteria': [
            {'name': 'Completeness', 'weight': '25%', 'desc': 'All features implemented'},
            {'name': 'Architecture', 'weight': '20%', 'desc': 'Clean, scalable design'},
            {'name': 'Quality', 'weight': '20%', 'desc': 'High-quality outputs'},
            {'name': 'Security', 'weight': '15%', 'desc': 'Comprehensive protections'},
            {'name': 'Evaluation', 'weight': '10%', 'desc': 'Thorough testing'},
            {'name': 'Presentation', 'weight': '10%', 'desc': 'Clear demonstration'}
        ]}
}

# Generate all files
print("Generating assignment files...")

for num in range(1, 18):
    title_map = {
        1: 'LangChain Introduction', 2: 'Models, Prompts & Messages',
        3: 'LCEL and Chains', 4: 'Embeddings & Vector Stores',
        5: 'RAG Applications', 6: 'Tools and Agents',
        7: 'Advanced LangChain Project', 8: 'Advanced RAG',
        9: 'Document Loading & Multimodal RAG', 10: 'SQL & Database AI',
        11: 'Data Science Agents', 12: 'LangGraph for Data Science',
        13: 'LLM Evaluation & Observability', 14: 'LLM Security & Prompt Injection',
        15: 'MCP for Data Science', 16: 'Production LLM Applications',
        17: 'Final Data Science Copilot'
    }
    
    dir_map = {
        1: '01_LangChain_Introduction', 2: '02_Models_Prompts_and_Messages',
        3: '03_LCEL_and_Chains', 4: '04_Embeddings_and_Vector_Stores',
        5: '05_RAG_Applications', 6: '06_Tools_and_Agents',
        7: '07_Advanced_LangChain_Project', 8: '08_Advanced_RAG',
        9: '09_Document_Loading_and_Multimodal_RAG', 10: '10_SQL_and_Database_AI',
        11: '11_Data_Science_Agents', 12: '12_LangGraph_for_Data_Science',
        13: '13_LLM_Evaluation_and_Observability', 14: '14_LLM_Security_and_Prompt_Injection',
        15: '15_MCP_for_Data_Science', 16: '16_Production_LLM_Applications',
        17: '17_Final_Data_Science_Copilot'
    }
    
    nb_map = {
        1: '01_LangChain_Introduction', 2: '02_Models_Prompts_and_Messages',
        3: '03_LCEL_and_Chains', 4: '04_Embeddings_and_Vector_Stores',
        5: '05_RAG_Applications', 6: '06_Tools_and_Agents',
        7: '07_Advanced_LangChain_Project', 8: '08_Advanced_RAG',
        9: '09_Document_Loading_and_Multimodal_RAG', 10: '10_SQL_and_Database_AI',
        11: '11_Data_Science_Agents', 12: '12_LangGraph_for_Data_Science',
        13: '13_LLM_Evaluation_and_Observability', 14: '14_LLM_Security_and_Prompt_Injection',
        15: '15_MCP_for_Data_Science', 16: '16_Production_LLM_Applications',
        17: '17_Final_Data_Science_Copilot'
    }
    
    title = title_map[num]
    dir_name = dir_map[num]
    nb_name = nb_map[num]
    
    notebook_path = f'../../notebooks/{nb_name}.ipynb'
    reading_path = f'../../readings/{nb_name}.md'
    
    # Exercises
    exercises = all_exercises.get(num, all_exercises[1])
    content = gen_exercises(num, title, notebook_path, reading_path, exercises)
    write_file(f'assignments/{dir_name}/exercises.md', content)
    
    # Assessment
    assessment = all_assessments.get(num, all_assessments[1])
    content = gen_assessment(num, title, notebook_path, reading_path, assessment)
    write_file(f'assignments/{dir_name}/assessment.md', content)
    
    # Challenge
    challenge = all_challenges.get(num, all_challenges[1])
    content = gen_challenge(num, title, notebook_path, reading_path, challenge)
    write_file(f'assignments/{dir_name}/challenge.md', content)
    
    # Solution stub
    content = gen_solution_stub(num, title)
    write_file(f'solutions/{dir_name}/README.md', content)

print("\nAll assignment files generated!")
