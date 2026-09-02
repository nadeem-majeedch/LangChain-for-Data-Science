# LangChain for Data Science

### Tools and Techniques in Data Science

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1.0-orange?logo=chainlink&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter&logoColor=white)

---

## Course Title

**Tools and Techniques in Data Science -- LangChain Module**

A hands-on, self-learning tutorial series that takes BS Data Science students from LangChain fundamentals to building advanced AI-powered applications for data science workflows.

---

## Target Audience

- **Primary:** BS Data Science students enrolled in *Tools and Techniques in Data Science*
- **Secondary:** Graduate students, data analysts, and developers exploring LLM-based data science workflows
- **Level:** Beginner to Expert (progressive notebooks)

---

## Learning Objectives

By completing this tutorial series, you will be able to:

1. **Understand** what LangChain is, its core architecture, and how it fits into the LLM application stack
2. **Configure** language models through both cloud APIs (OpenAI) and local runtimes (Ollama)
3. **Design and execute** prompt templates, message systems, and output parsers
4. **Build chains** using LangChain Expression Language (LCEL) for modular, composable pipelines
5. **Create embeddings** and manage vector stores for semantic search and retrieval
6. **Implement RAG** (Retrieval-Augmented Generation) applications that answer questions over custom datasets
7. **Develop tools and agents** that reason, plan, and take actions using LLMs
8. **Construct end-to-end projects** combining all techniques for real-world data science problems

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Python** | 3.10 or higher |
| **Jupyter Notebook / Lab** | For running `.ipynb` files |
| **Basic Python** | Functions, loops, list comprehensions, f-strings |
| **Data Science basics** | NumPy, Pandas, Matplotlib familiarity |
| **API Key** | OpenAI API key (for cloud-based notebooks) |
| **Ollama** (optional) | Installed locally for offline/free notebooks |
| **Terminal / CLI** | Comfortable running pip install commands |

---

## Learning Path

The notebooks are designed to be completed **in order**. Each notebook builds on concepts from the previous one.

```
LEARNING PATH

01 --> 02 --> 03 --> 04 --> 05 --> 06 --> 07 --> 08 --> 09 --> 10 --> 11 --> 12 --> 13 --> 14 --> 15 --> 16 --> 17
Intro   Msgs  LCEL   Embed   RAG   Agent  Capstone  Adv.RAG  Docs  SQL  DS   Graph  Eval  Sec  MCP  Prod  FINAL

<-- Foundations --><-- Core Skills --><-- Advanced --><-- Expert --><-- Mastery -->
```

| Phase | Notebooks | Focus |
|---|---|---|
| **Foundations** | 01 -- 02 | What is LangChain, models, prompts, messages |
| **Core Skills** | 03 -- 05 | Chains (LCEL), embeddings, vector stores, RAG |
| **Advanced** | 06 -- 11 | Tools, agents, capstone, advanced RAG, document processing, SQL, DS agents |
| **Expert** | 12 | LangGraph: stateful workflows, conditional routing, validation loops |
| **Mastery** | 13 -- 16 | Evaluation, observability, security, MCP, production deployment |
| **Capstone** | 17 | Final project: Complete Data Science AI Copilot |

---

## How to Use This Repository

The recommended learning workflow:

```
Read the concept → Understand the intuition → Open the notebook → Run the code → Experiment → Complete exercises → Build projects
```

| Step | Activity | Where |
|------|----------|-------|
| 1 | **Read** the conceptual notes | `readings/` folder |
| 2 | **Open** the corresponding notebook | `notebooks/` folder |
| 3 | **Run** the code examples | In Jupyter |
| 4 | **Experiment** by changing parameters | In Jupyter |
| 5 | **Complete** exercises and challenges | In the notebook |
| 6 | **Build** the capstone project | Notebook 17 |

---

## Learning Notes

**Conceptual learning notes** are available in the [`readings/`](readings/README.md) folder. These provide theory, intuition, and design principles for every concept in the notebooks.

| Step | Layer | Purpose |
|------|-------|--------|
| 1 | **Readings** | Concepts, terminology, architecture, comparisons |
| 2 | **Notebooks** | Hands-on code, experiments, exercises |

> Read the concept first, then run the code.

---

## Notebook Roadmap

| # | Notebook | Topics | Difficulty | Est. Time |
|---|---|---|---|---|
| 01 | `01_LangChain_Introduction.ipynb` | [LLMs](readings/01_LangChain_Introduction.md#what-is-an-llm) · [LangChain](readings/01_LangChain_Introduction.md#why-langchain) · [Architecture](readings/01_LangChain_Introduction.md#langchain-architecture) | Beginner | 60--90 min |
| 02 | `02_Models_Prompts_and_Messages.ipynb` | [Chat Models](readings/02_Models_Prompts_and_Messages.md#chat-models) · [Messages](readings/02_Models_Prompts_and_Messages.md#messages) · [Prompts](readings/02_Models_Prompts_and_Messages.md#prompt-templates) · [Structured Output](readings/02_Models_Prompts_and_Messages.md#structured-output) | Beginner | 90--120 min |
| 03 | `03_LCEL_and_Chains.ipynb` | [Chains](readings/03_LCEL_and_Chains.md#what-is-a-chain) · [LCEL](readings/03_LCEL_and_Chains.md#lcel--langchain-expression-language) · [Runnables](readings/03_LCEL_and_Chains.md#core-runnables) | Intermediate | 90--120 min |
| 04 | `04_Embeddings_and_Vector_Stores.ipynb` | [Embeddings](readings/04_Embeddings_and_Vector_Stores.md#what-are-embeddings) · [Vector Stores](readings/04_Embeddings_and_Vector_Stores.md#vector-stores) · [Similarity Search](readings/04_Embeddings_and_Vector_Stores.md#similarity-search) | Intermediate | 90--120 min |
| 05 | `05_RAG_Applications.ipynb` | [RAG](readings/05_RAG_Applications.md#what-is-rag) · [Chunking](readings/05_RAG_Applications.md#chunking) · [Retrieval](readings/05_RAG_Applications.md#retrieval-quality) · [Hallucination](readings/05_RAG_Applications.md#hallucination) | Advanced | 120--150 min |
| 06 | `06_Tools_and_Agents.ipynb` | [Tools](readings/06_Tools_and_Agents.md#what-is-a-tool) · [Agent Loop](readings/06_Tools_and_Agents.md#the-agent-loop) · [Chain vs Agent](readings/06_Tools_and_Agents.md#chain-vs-agent) | Advanced | 120--150 min |
| 07 | `07_Advanced_LangChain_Project.ipynb` | [Architecture](readings/07_Advanced_LangChain_Project.md#architecture-principles) · [Integration](readings/07_Advanced_LangChain_Project.md#integration-patterns) | Expert | 150--180 min |
| 08 | `08_Advanced_RAG.ipynb` | [Advanced Chunking](readings/08_Advanced_RAG.md#advanced-chunking) · [Query Transformation](readings/08_Advanced_RAG.md#query-transformation) · [Reranking](readings/08_Advanced_RAG.md#reranking) | Expert | 180--240 min |
| 09 | `09_Document_Loading_and_Multimodal_RAG.ipynb` | [Document Loading](readings/09_Document_Loading_and_Multimodal_RAG.md#real-world-knowledge-bases) · [Multimodal](readings/09_Document_Loading_and_Multimodal_RAG.md#multimodal-rag) | Expert | 150--180 min |
| 10 | `10_SQL_and_Database_AI.ipynb` | [NL-to-SQL](readings/10_SQL_and_Database_AI.md#natural-language-to-sql) · [SQL Safety](readings/10_SQL_and_Database_AI.md#sql-safety) | Expert | 120--150 min |
| 11 | `11_Data_Science_Agents.ipynb` | [DS Agents](readings/11_Data_Science_Agents.md#traditional-vs-agent-based-workflows) · [Agent Design](readings/11_Data_Science_Agents.md#agent-design-principles) | Expert | 120--150 min |
| 12 | `12_LangGraph_for_Data_Science.ipynb` | [LangGraph](readings/12_LangGraph_for_Data_Science.md#why-langgraph) · [State](readings/12_LangGraph_for_Data_Science.md#core-concepts) · [Conditional Routing](readings/12_LangGraph_for_Data_Science.md#conditional-routing) | Expert | 180--240 min |
| 13 | `13_LLM_Evaluation_and_Observability.ipynb` | [Evaluation](readings/13_LLM_Evaluation_and_Observability.md#why-llm-evaluation-is-hard) · [LLM-as-Judge](readings/13_LLM_Evaluation_and_Observability.md#llm-as-a-judge) · [Observability](readings/13_LLM_Evaluation_and_Observability.md#observability) | Expert | 180--240 min |
| 14 | `14_LLM_Security_and_Prompt_Injection.ipynb` | [Threat Model](readings/14_LLM_Security_and_Prompt_Injection.md#threat-model) · [Prompt Injection](readings/14_LLM_Security_and_Prompt_Injection.md#prompt-injection) · [Tool Security](readings/14_LLM_Security_and_Prompt_Injection.md#tool-security) | Expert | 180--240 min |
| 15 | `15_MCP_for_Data_Science.ipynb` | [MCP](readings/15_MCP_for_Data_Science.md#what-is-mcp) · [MCP Concepts](readings/15_MCP_for_Data_Science.md#mcp-concepts) · [LangChain vs MCP](readings/15_MCP_for_Data_Science.md#langchain-tools-vs-mcp-tools) | Expert | 180--240 min |
| 16 | `16_Production_LLM_Applications.ipynb` | [Production Lifecycle](readings/16_Production_LLM_Applications.md#production-lifecycle) · [Error Handling](readings/16_Production_LLM_Applications.md#error-handling) · [Cost Control](readings/16_Production_LLM_Applications.md#cost-control) | Expert | 180--240 min |
| 17 | `17_Final_Data_Science_Copilot.ipynb` | [Architecture](readings/17_Final_Data_Science_Copilot.md#architecture-components) · [Design Principles](readings/17_Final_Data_Science_Copilot.md#design-principles) · [Evaluation](readings/17_Final_Data_Science_Copilot.md#evaluation-framework) | Expert | 240--360 min |

---

## API vs Local Ollama Approach

This repository supports **two parallel approaches** so you can choose what fits your situation:

| | **Cloud API (OpenAI)** | **Local (Ollama)** |
|---|---|---|
| **Model provider** | OpenAI (GPT-4o, GPT-4o-mini) | Open-source models (Llama 3.2, Mistral, Qwen, etc.) |
| **Cost** | Pay-per-token usage | Free (runs on your hardware) |
| **Internet** | Required | Not required after model download |
| **Speed** | Fast (cloud GPUs) | Depends on your hardware |
| **Setup** | API key only | Install Ollama + pull models |
| **Best for** | Quick prototyping, production | Learning, privacy, experimentation |
| **Data privacy** | Data sent to OpenAI servers | All data stays local |

### When to use which?

- **Classroom / Lab sessions with internet** -- Use the OpenAI API approach
- **Self-study at home without credits** -- Use the Ollama local approach
- **Both paths teach the same concepts** with identical LangChain code patterns

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/LangChain-for-Data-Science.git
cd LangChain-for-Data-Science
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your environment

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your API key (see Security Notes below)
```

### 5. (Optional) Set up Ollama for local models

```bash
# Install Ollama: https://ollama.com/download
ollama --version          # Verify installation
ollama pull llama3.2      # Pull the default model
ollama pull nomic-embed-text  # Pull embedding model
ollama list               # Verify models are available
```

---

## Launching Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook

# Or start JupyterLab (recommended)
jupyter lab
```

Then navigate to the `notebooks/` directory and open the first notebook.

---

## Security Notes -- API Keys

> **NEVER commit API keys to version control.**

This repository uses `python-dotenv` and a `.env` file to manage secrets safely.

| Do | Do Not |
|---|---|
| Store keys in `.env` (git-ignored) | Hardcode keys in notebooks or `.py` files |
| Use `.env.example` as a template | Commit `.env` to Git |
| Share `.env.example` with teammates | Share actual API keys |
| Use environment variables | Paste keys in screenshots or chat |

Your `.env` file is listed in `.gitignore` and **will not** be tracked by Git.

```python
# Correct way to use API keys:
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
```

---

## Suggested 2-Hour Classroom Lecture Structure

### Hour 1: Foundations (60 minutes)

| Time | Segment | Activities |
|---|---|---|
| 0:00 -- 0:10 | **Introduction & Motivation** | What is LangChain? Why should data scientists care? Live demo of a simple chat model call |
| 0:10 -- 0:25 | **Models, Prompts & Messages** | Walk through Notebook 02: prompt templates, few-shot examples, message types. Students follow along |
| 0:25 -- 0:40 | **LCEL & Chains** | Demonstrate the pipe `\|` operator, chaining prompts to models to output parsers. Students build their first chain |
| 0:40 -- 0:50 | **Hands-on Exercise** | Students build a simple chain that transforms data (e.g., summarize, translate, format) |
| 0:50 -- 1:00 | **Q&A & Recap** | Review key concepts, address questions |

### Hour 2: Applied Skills (60 minutes)

| Time | Segment | Activities |
|---|---|---|
| 1:00 -- 1:15 | **Embeddings & Vector Stores** | Explain embeddings conceptually, demo Chroma setup, similarity search on sample data |
| 1:15 -- 1:35 | **RAG Pipeline** | Walk through a complete RAG application: load documents, split, embed, store, retrieve, generate |
| 1:35 -- 1:50 | **Agents & Tools (Preview)** | Brief demo of an agent that uses tools. Explain what is coming in Notebook 06 |
| 1:50 -- 2:00 | **Wrap-up & Next Steps** | Point students to remaining notebooks (07-17): advanced topics plus the final capstone project building a complete Data Science AI Copilot |

---

## Capstone Project

Notebook 07 is a **complete capstone project** that combines everything from Notebooks 01--06 into a single **Data Science AI Tutor** application. The capstone includes:

- RAG pipeline with a knowledge base of Data Science notes
- Structured output using Pydantic models (concept explanations, quiz questions)
- Numerical calculation tools (mean, standard deviation, correlation, dataset summary)
- Both API and local Ollama implementations
- A final assignment to build your own domain-specific AI tutor

See the **Capstone Assignment** section in Notebook 07 for detailed requirements and domain ideas.

---

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| `ModuleNotFoundError: No module named 'langchain'` | Packages not installed | Run `pip install -r requirements.txt` |
| `AuthenticationError: Incorrect API key` | Wrong or missing API key | Check your `.env` file has the correct `OPENAI_API_KEY` |
| `ConnectionError` when using Ollama | Ollama not running | Start Ollama: `ollama serve` (or launch the Ollama app) |
| `Model not found` in Ollama | Model not pulled yet | Run `ollama pull llama3.2` and `ollama pull nomic-embed-text` |
| Notebook won't run top-to-top | Variables from previous cells needed | Restart kernel and run all cells from the beginning |
| ChromaDB errors | Corrupted vector store | Delete the `data/chroma_db/` directory and re-run |
| `RateLimitError` from OpenAI | Too many requests or quota exceeded | Wait and retry, or switch to Ollama for local execution |
| Emoji rendering issues in terminal | Windows terminal encoding | Use Windows Terminal or VS Code terminal instead of cmd.exe |

---

## Repository Structure

```
LangChain-for-Data-Science/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── .env.example              # API key template (safe to commit)
├── .gitignore                # Protects secrets and temp files
├── readings/                 # Conceptual learning notes (17 readings)
│   └── README.md             # Reading index and learning path
├── notebooks/                # Jupyter notebooks (01--17)
│   ├── 01_LangChain_Introduction.ipynb
│   ├── 02_Models_Prompts_and_Messages.ipynb
│   ├── 03_LCEL_and_Chains.ipynb
│   ├── 04_Embeddings_and_Vector_Stores.ipynb
│   ├── 05_RAG_Applications.ipynb
│   ├── 06_Tools_and_Agents.ipynb
│   ├── 07_Advanced_LangChain_Project.ipynb
│   ├── 08_Advanced_RAG.ipynb
│   ├── 09_Document_Loading_and_Multimodal_RAG.ipynb
│   ├── 10_SQL_and_Database_AI.ipynb
│   ├── 11_Data_Science_Agents.ipynb
│   ├── 12_LangGraph_for_Data_Science.ipynb
│   ├── 13_LLM_Evaluation_and_Observability.ipynb
│   ├── 14_LLM_Security_and_Prompt_Injection.ipynb
│   ├── 15_MCP_for_Data_Science.ipynb
│   ├── 16_Production_LLM_Applications.ipynb
│   └── 17_Final_Data_Science_Copilot.ipynb
├── data/
│   ├── README.md             # Data directory guide
│   └── ds_notes/             # Knowledge base for RAG notebooks
├── docs/                     # Additional documentation
├── images/
│   └── diagrams/            # Architecture and concept diagrams
└── examples/
    ├── api/                  # OpenAI API example scripts
    ├── mcp/                  # MCP server examples
    └── ollama/               # Local Ollama example scripts
```

---

## Key Dependencies

| Package | Purpose |
|---|---|
| `langchain` | Core LangChain framework (v1.0+) |
| `langchain-core` | Core abstractions (LCEL, prompts, output parsers) |
| `langchain-openai` | OpenAI chat models and embeddings |
| `langchain-ollama` | Ollama chat models and embeddings |
| `langchain-text-splitters` | Document chunking for RAG |
| `langchain-chroma` | Chroma vector store integration |
| `chromadb` | Vector database engine |
| `openai` | OpenAI Python SDK |
| `pydantic` | Data validation and structured outputs |
| `python-dotenv` | Secure environment variable management |
| `numpy` | Numerical computing |
| `pandas` | Data manipulation |
| `scikit-learn` | ML utilities and evaluation metrics |
| `matplotlib` | Data visualization |

---

## LangChain 1.0 APIs Used

This repository uses current LangChain 1.0 (October 2025) APIs:

| API | Package | Purpose |
|-----|---------|---------|
| `ChatOpenAI` | `langchain-openai` | Cloud-based chat model |
| `ChatOllama` | `langchain-ollama` | Local chat model |
| `OpenAIEmbeddings` | `langchain-openai` | Cloud embeddings |
| `OllamaEmbeddings` | `langchain-ollama` | Local embeddings |
| `ChatPromptTemplate` | `langchain-core` | Prompt construction |
| `StrOutputParser` | `langchain-core` | Text output parsing |
| `RunnablePassthrough` | `langchain-core` | LCEL pipeline composition |
| `@tool` | `langchain-core` | Tool creation |
| `bind_tools()` | `langchain-core` | Attach tools to models |
| `create_tool_calling_agent` | `langchain.agents` | Classic agent builder |
| `create_agent` | `langchain.agents` | LangChain 1.0 agent builder |
| `with_structured_output()` | `langchain-core` | Structured/typed output |
| `Chroma` | `langchain-chroma` | Vector store |
| `RecursiveCharacterTextSplitter` | `langchain-text-splitters` | Document chunking |

**Note:** `langchain-community` is **archived** (June 2026) and is deliberately not used.

---

## Contributing

Contributions welcome! This is an educational repository -- feel free to:

- Fix typos or improve explanations
- Add example datasets to `data/`
- Create architecture diagrams for `images/diagrams/`
- Suggest new notebook topics via Issues

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Acknowledgements

- [LangChain Documentation](https://docs.langchain.com/) -- Official LangChain docs
- [OpenAI API Documentation](https://platform.openai.com/docs/) -- OpenAI platform
- [Ollama](https://ollama.com/) -- Local LLM runtime
- [Chroma](https://www.trychroma.com/) -- Open-source vector database

---

<p align="center">
  <i>Built for BS Data Science students -- Learn by doing.</i>
</p>
