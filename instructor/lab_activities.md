# Lab Activities

## Lab 1: First LangChain Application

**Objective:** Set up and run a basic LangChain application.

**Duration:** 90 minutes

**Prerequisites:** Python, Jupyter installed

**Tasks:**
1. Install dependencies (`pip install -r requirements.txt`)
2. Set up API key in `.env` file
3. Run first LLM call in Notebook 01
4. Experiment with different prompts
5. Try changing the model temperature

**Expected Output:**
- Working LangChain setup
- Understanding of basic LLM interaction
- Ability to modify prompts and see different outputs

**Extension Challenge:**
Try sending the same question to both OpenAI and Ollama. Compare the responses.

---

## Lab 2: Prompt Engineering

**Objective:** Master prompt templates and structured output.

**Duration:** 90 minutes

**Prerequisites:** Lab 1

**Tasks:**
1. Create a prompt template with variables (Notebook 02)
2. Build a few-shot prompt for classification
3. Create a Pydantic model for structured output
4. Test with 5 different Data Science topics

**Expected Output:**
- Reusable prompt templates
- Working few-shot classifier
- Structured output with validation

**Extension Challenge:**
Create a quiz generator that produces questions at 3 difficulty levels.

---

## Lab 3: Building Chains

**Objective:** Learn LCEL and chain composition.

**Duration:** 90 minutes

**Prerequisites:** Lab 2

**Tasks:**
1. Build a simple chain (prompt → model → parser)
2. Create a parallel chain that runs two analyses simultaneously
3. Build a sequential chain that chains multiple operations
4. Test with different Data Science topics

**Expected Output:**
- Simple chain working
- Parallel chain executing
- Sequential chain chaining operations

**Extension Challenge:**
Build a "Data Science Concept Pipeline" that takes a topic and produces: definition, quiz question, and Python example.

---

## Lab 4: Semantic Search

**Objective:** Build a semantic search system.

**Duration:** 90 minutes

**Prerequisites:** Lab 3

**Tasks:**
1. Create embeddings for 10 Data Science documents (Notebook 04)
2. Store in ChromaDB vector store
3. Test similarity search with 5 queries
4. Compare results with keyword search
5. Experiment with different k values

**Expected Output:**
- Vector store with 10+ documents
- Working similarity search
- Comparison of search quality

**Extension Challenge:**
Add metadata filtering to search only "beginner" level documents.

---

## Lab 5: Building RAG

**Objective:** Build a complete RAG application.

**Duration:** 120 minutes

**Prerequisites:** Lab 4

**Tasks:**
1. Load documents from files (Notebook 05)
2. Split into chunks
3. Create embeddings and store
4. Build retriever
5. Create RAG chain
6. Test with 10 questions
7. Implement source citations

**Expected Output:**
- Complete RAG pipeline
- Working retrieval and generation
- Source citations in answers

**Extension Challenge:**
Compare RAG quality with chunk sizes of 200, 500, and 1000 tokens.

---

## Lab 6: Creating Tools

**Objective:** Build Data Science tools.

**Duration:** 90 minutes

**Prerequisites:** Lab 5

**Tasks:**
1. Create 3 Data Science tools (Notebook 06)
   - `calculate_statistics`
   - `dataset_summary`
   - `generate_quiz`
2. Test each tool individually
3. Add input validation
4. Test error handling

**Expected Output:**
- 3 working tools
- Input validation
- Error handling

**Extension Challenge:**
Add a `detect_outliers` tool that identifies outliers in a dataset.

---

## Lab 7: Building an Agent

**Objective:** Build a tool-using agent.

**Duration:** 90 minutes

**Prerequisites:** Lab 6

**Tasks:**
1. Create an agent with 4 tools
2. Test with various questions
3. Verify correct tool selection
4. Add logging for all tool calls
5. Test edge cases

**Expected Output:**
- Working agent
- Correct tool selection
- Audit logging

**Extension Challenge:**
Add rate limiting to prevent excessive tool calls.

---

## Lab 8: LangGraph Workflow

**Objective:** Build a stateful workflow with LangGraph.

**Duration:** 90 minutes

**Prerequisites:** Lab 7

**Tasks:**
1. Build a simple graph with 3 nodes (Notebook 12)
2. Add conditional routing
3. Implement a validation node
4. Test with different question types
5. Add retry logic

**Expected Output:**
- Working graph with routing
- Validation and retry logic
- State management

**Extension Challenge:**
Add a human-in-the-loop step that requires approval before executing tools.

---

## Lab 9: Evaluating RAG

**Objective:** Learn to evaluate LLM applications.

**Duration:** 90 minutes

**Prerequisites:** Lab 5

**Tasks:**
1. Create an evaluation dataset with 10 questions (Notebook 13)
2. Implement retrieval precision measurement
3. Build an LLM-as-judge
4. Compare automated vs manual evaluation
5. Generate evaluation report

**Expected Output:**
- Evaluation dataset
- Automated metrics
- Comparison report

**Extension Challenge:**
Build a benchmark comparing RAG quality across different models.

---

## Lab 10: Securing RAG

**Objective:** Add security to a RAG system.

**Duration:** 90 minutes

**Prerequisites:** Lab 5

**Tasks:**
1. Implement input validation (Notebook 14)
2. Add document sanitization
3. Implement output validation
4. Test with prompt injection attempts
5. Document security measures

**Expected Output:**
- Secure RAG system
- Defense against prompt injection
- Security documentation

**Extension Challenge:**
Test your system with 5 different attack scenarios.

---

## Lab 11: Natural-Language SQL

**Objective:** Build a natural language database assistant.

**Duration:** 90 minutes

**Prerequisites:** Lab 6

**Tasks:**
1. Create a SQLite database (Notebook 10)
2. Test NL-to-SQL translation
3. Implement query validation
4. Add natural language explanations
5. Test with 10 questions

**Expected Output:**
- Working NL-to-SQL system
- Query validation
- Natural language explanations

**Extension Challenge:**
Add support for multi-table joins.

---

## Lab 12: Building a Data Science Copilot

**Objective:** Build a complete Data Science AI Copilot.

**Duration:** 180 minutes

**Prerequisites:** All previous labs

**Tasks:**
1. Design architecture (Notebook 17)
2. Implement router
3. Add RAG pipeline
4. Add tools
5. Add SQL capability
6. Implement evaluation
7. Add security measures
8. Test thoroughly
9. Present to class

**Expected Output:**
- Complete copilot application
- All routes working
- Evaluation results
- Security documentation

**Extension Challenge:**
Deploy the copilot as a web service.

---

**Back to:** [Instructor Guide](README.md) | [Teaching Roadmap](teaching_roadmap.md)
