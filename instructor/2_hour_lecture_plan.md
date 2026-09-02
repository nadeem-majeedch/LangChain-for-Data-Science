# 2-Hour Lecture Plan

**Topic:** Introduction to LangChain for Data Science
**Duration:** 120 minutes
**Level:** Beginner

---

## Timeline

| Time | Section | Activity | Type |
|------|---------|----------|------|
| 0:00-0:10 | Introduction | Course overview, LLM applications | Lecture |
| 0:10-0:25 | LangChain | What is LangChain, architecture | Lecture + Demo |
| 0:25-0:45 | Models & Prompts | Chat models, messages, prompts | Lecture + Demo |
| 0:45-0:65 | Chains | LCEL, pipe operator, composition | Lecture + Demo |
| 0:65-0:80 | Embeddings | Vectors, similarity, vector stores | Lecture + Demo |
| 0:80-1:05 | RAG | Complete RAG pipeline | Lecture + Demo |
| 1:05-1:15 | Tools & Agents | Tool calling, agent loop | Lecture |
| 1:15-1:20 | Summary | Key takeaways, next steps | Lecture |

---

## Section 1: Introduction (0:00-0:10)

**Teaching Objective:** Understand what LLM applications are and why they matter for Data Science.

**Concepts:**
- LLMs generate text from patterns
- LLM applications wrap LLMs with additional logic
- Data Science use cases: tutors, RAG, SQL agents

**Discussion Question:**
> "How could an LLM help a Data Science student learn faster?"

**Expected Understanding:**
Students can explain what an LLM application is and name 3 Data Science use cases.

---

## Section 2: What is LangChain? (0:10-0:25)

**Teaching Objective:** Understand LangChain's role and architecture.

**Concepts:**
- Unified interface for multiple LLM providers
- Prompt management
- Chain composition
- Ecosystem of partner libraries

**Notebook Cells to Demonstrate:**
- Notebook 01, Cell 1-3 (imports and setup)

**Live Coding:**
Show the LangChain architecture diagram and explain each layer.

**Discussion Question:**
> "Why not just use the OpenAI API directly? What does LangChain add?"

**Expected Understanding:**
Students can explain why LangChain exists and its main components.

---

## Section 3: Models, Messages and Prompts (0:25-0:45)

**Teaching Objective:** Understand chat models, message types, and prompt templates.

**Concepts:**
- Chat Models vs raw LLMs
- System, Human, AI messages
- Prompt templates with variables
- Temperature parameter

**Notebook Cells to Demonstrate:**
- Notebook 02, Cells showing ChatPromptTemplate

**Live Coding:**
```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a Data Science tutor."),
    ("human", "Explain {topic} to a {level} student.")
])
model = ChatOpenAI(model="gpt-4o-mini")
chain = prompt | model

# Ask students: what happens with different levels?
```

**Student Experiment:**
> "Try changing 'beginner' to 'expert'. How does the response change?"

**Expected Understanding:**
Students can create prompt templates and explain message roles.

---

## Section 4: Chains and LCEL (0:45-0:65)

**Teaching Objective:** Understand the pipe operator and chain composition.

**Concepts:**
- LCEL pipe operator (|)
- Chaining components
- StrOutputParser
- Runnable concept

**Notebook Cells to Demonstrate:**
- Notebook 03, basic chain example

**Live Coding:**
```python
from langchain_core.output_parsers import StrOutputParser

chain = prompt | model | StrOutputParser()
result = chain.invoke({"topic": "PCA", "level": "beginner"})
print(result)
```

**Student Experiment:**
> "Add a second chain that takes the first chain's output and summarizes it."

**Expected Understanding:**
Students can build simple chains and explain the pipe operator.

---

## Section 5: Embeddings and Vector Search (0:65-0:80)

**Teaching Objective:** Understand embeddings and semantic search.

**Concepts:**
- Text to vectors
- Cosine similarity
- Vector stores
- Semantic vs keyword search

**Notebook Cells to Demonstrate:**
- Notebook 04, embedding creation and similarity

**Live Coding:**
```python
# Show how similar meanings get similar vectors
embeddings = OpenAIEmbeddings()
docs = ["Linear regression", "Logistic regression", "Stock market"]
vectors = embeddings.embed_documents(docs)
# Compute similarities
```

**Student Experiment:**
> "Which two concepts are most similar? Does the embedding agree with your intuition?"

**Expected Understanding:**
Students can explain embeddings and demonstrate semantic similarity.

---

## Section 6: RAG (0:80-1:05)

**Teaching Objective:** Understand the complete RAG pipeline.

**Concepts:**
- Why RAG? (LLM limitations)
- Load → Split → Embed → Store → Retrieve → Generate
- Chunking
- Context window

**Notebook Cells to Demonstrate:**
- Notebook 05, complete RAG pipeline

**Live Coding:**
Build a mini RAG system with 5 documents. Show:
1. Creating documents
2. Storing in vector DB
3. Retrieving relevant docs
4. Generating answer with context

**Student Experiment:**
> "What happens if we change top-k from 3 to 1? From 3 to 10?"

**Prediction Question:**
> "Before I run this: what do you think will happen if the question is about a topic NOT in our knowledge base?"

**Expected Understanding:**
Students can build a basic RAG system and explain each step.

---

## Section 7: Tools and Agents (1:05-1:15)

**Teaching Objective:** Understand tool calling and the agent loop.

**Concepts:**
- Tools extend LLM capabilities
- LLM decides which tool to use
- Agent loop: Think → Act → Observe
- Chain vs Agent

**Notebook Cells to Demonstrate:**
- Notebook 06, basic tool example

**Live Coding:**
```python
from langchain_core.tools import tool

@tool
def calculate_mean(numbers: str) -> str:
    """Calculate the mean of numbers."""
    nums = [float(x.strip()) for x in numbers.split(",")]
    return f"Mean: {sum(nums)/len(nums)}"
```

**Discussion Question:**
> "When would you use a chain instead of an agent? Give a specific example."

**Expected Understanding:**
Students can create tools and explain the agent loop.

---

## Section 8: Summary (1:15-1:20)

**Key Takeaways:**

| Concept | Key Point |
|---------|-----------|
| LangChain | Unified framework for LLM applications |
| Prompts | Templates make prompts reusable |
| Chains | Pipe operator connects components |
| Embeddings | Text → vectors for semantic search |
| RAG | Retrieve context before generating |
| Tools | Extend LLM beyond text generation |
| Agents | LLM decides which tools to use |

**Next Steps:**
- Complete the notebook exercises
- Try the lab activities
- Start thinking about your capstone project

---

## Live Demo Priorities

**Must demo live:**
1. First LLM call (Notebook 01)
2. Prompt template (Notebook 02)
3. Chain with pipe operator (Notebook 03)
4. Embedding similarity (Notebook 04)
5. RAG pipeline (Notebook 05)

**Can skip live (assign as self-study):**
- Detailed tool creation (Notebook 06)
- Agent loop (Notebook 06)

---

**Back to:** [Instructor Guide](README.md) | [Course Plan](course_plan.md)
