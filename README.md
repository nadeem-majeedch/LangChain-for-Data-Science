# 🔗 LangChain for Data Science

### Tools and Techniques in Data Science

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-latest-orange?logo=chainlink&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter&logoColor=white)

---

## 📋 Course Title

**Tools and Techniques in Data Science — LangChain Module**

A hands-on, self-learning tutorial series that takes BS Data Science students from LangChain fundamentals to building advanced AI-powered applications for data science workflows.

---

## 🎯 Target Audience

- **Primary:** BS Data Science students enrolled in *Tools and Techniques in Data Science*
- **Secondary:** Graduate students, data analysts, and developers exploring LLM-based data science workflows
- **Level:** Beginner → Intermediate → Advanced (progressive notebooks)

---

## 🎓 Learning Objectives

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

## 📚 Prerequisites

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

## 🗺️ Learning Path

The notebooks are designed to be completed **in order**. Each notebook builds on concepts from the previous one.

```
┌─────────────────────────────────────────────────────────────┐
│                     LEARNING PATH                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  01 ──► 02 ──► 03 ──► 04 ──► 05 ──► 06 ──► 07              │
│  Intro   Msgs  LCEL   Embed   RAG   Agent  Project         │
│                                                             │
│  ◄── Foundations ──►◄── Core Skills ──►◄── Advanced ──►     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

| Phase | Notebooks | Focus |
|---|---|---|
| **Foundations** | 01 – 02 | What is LangChain, models, prompts, messages |
| **Core Skills** | 03 – 05 | Chains (LCEL), embeddings, vector stores, RAG |
| **Advanced** | 06 – 07 | Tools, agents, and a capstone project |

---

## 📓 Planned Notebook Roadmap

| # | Notebook | Topics | Est. Time |
|---|---|---|---|
| 01 | `01_LangChain_Introduction.ipynb` | What is LangChain? Ecosystem overview, installation, first model call, API vs Ollama setup | 60–90 min |
| 02 | `02_Models_Prompts_and_Messages.ipynb` | Chat models, prompt templates, few-shot prompting, message types (System/Human/AI), output parsers | 90–120 min |
| 03 | `03_LCEL_and_Chains.ipynb` | LangChain Expression Language (LCEL), pipe operator, RunnablePassthrough, RunnableLambda, sequential & parallel chains | 90–120 min |
| 04 | `04_Embeddings_and_Vector_Stores.ipynb` | Text embeddings, Chroma vector store, similarity search, metadata filtering, persistence | 90–120 min |
| 05 | `05_RAG_Applications.ipynb` | Retrieval-Augmented Generation, document loaders, text splitters, full RAG pipeline, evaluation | 120–150 min |
| 06 | `06_Tools_and_Agents.ipynb` | Custom tools, toolkits, ReAct agents, tool-calling, multi-step reasoning | 120–150 min |
| 07 | `07_Advanced_LangChain_Project.ipynb` | Capstone project: end-to-end data science Q&A system combining RAG + agents + tools | 150–180 min |

---

## ☁️ API vs 🦙 Local Ollama Approach

This repository supports **two parallel approaches** so you can choose what fits your situation:

| | **Cloud API (OpenAI)** | **Local (Ollama)** |
|---|---|---|
| **Location** | `examples/api/` | `examples/ollama/` |
| **Model provider** | OpenAI (GPT-4o, GPT-4o-mini) | Open-source models (Llama 3, Mistral, Phi-3, etc.) |
| **Cost** | Pay-per-token usage | Free (runs on your hardware) |
| **Internet** | Required | Not required after model download |
| **Speed** | Fast (cloud GPUs) | Depends on your hardware |
| **Setup** | API key only | Install Ollama + pull models |
| **Best for** | Quick prototyping, production | Learning, privacy, experimentation |
| **Data privacy** | Data sent to OpenAI servers | All data stays local |

### When to use which?

- **Classroom / Lab sessions with internet** → Use the OpenAI API approach
- **Self-study at home without credits** → Use the Ollama local approach
- **Both paths teach the same concepts** with identical LangChain code patterns

---

## ⚡ Installation

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
# Then pull a model:
ollama pull llama3.2
ollama pull mistral
```

---

## 🚀 Launching Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook

# Or start JupyterLab (recommended)
jupyter lab
```

Then navigate to the `notebooks/` directory and open the first notebook:

```
notebooks/
├── 01_LangChain_Introduction.ipynb
├── 02_Models_Prompts_and_Messages.ipynb
├── 03_LCEL_and_Chains.ipynb
├── 04_Embeddings_and_Vector_Stores.ipynb
├── 05_RAG_Applications.ipynb
├── 06_Tools_and_Agents.ipynb
└── 07_Advanced_LangChain_Project.ipynb
```

---

## 🔐 Security Notes — API Keys

> **⚠️ NEVER commit API keys to version control.**

This repository uses `python-dotenv` and a `.env` file to manage secrets safely.

| Do ✅ | Don't ❌ |
|---|---|
| Store keys in `.env` (git-ignored) | Hardcode keys in notebooks or `.py` files |
| Use `.env.example` as a template | Commit `.env` to Git |
| Share `.env.example` with teammates | Share actual API keys |
| Use environment variables | Paste keys in screenshots or chat |

Your `.env` file is listed in `.gitignore` and **will not** be tracked by Git. Always load keys with:

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
```

---

## 🕐 Suggested 2-Hour Classroom Lecture Structure

### Hour 1: Foundations (60 minutes)

| Time | Segment | Activities |
|---|---|---|
| 0:00 – 0:10 | **Introduction & Motivation** | What is LangChain? Why should data scientists care? Live demo of a simple chat model call |
| 0:10 – 0:25 | **Models, Prompts & Messages** | Walk through Notebook 02: prompt templates, few-shot examples, message types. Students follow along |
| 0:25 – 0:40 | **LCEL & Chains** | Demonstrate the pipe `|` operator, chaining prompts → models → output parsers. Students build their first chain |
| 0:40 – 0:50 | **Hands-on Exercise** | Students build a simple chain that transforms data (e.g., summarize → translate → format) |
| 0:50 – 1:00 | **Q&A & Recap** | Review key concepts, address questions |

### Hour 2: Applied Skills (60 minutes)

| Time | Segment | Activities |
|---|---|---|
| 1:00 – 1:15 | **Embeddings & Vector Stores** | Explain embeddings conceptually, demo Chroma setup, similarity search on sample data |
| 1:15 – 1:35 | **RAG Pipeline** | Walk through a complete RAG application: load documents → split → embed → store → retrieve → generate |
| 1:35 – 1:50 | **Agents & Tools (Preview)** | Brief demo of an agent that uses tools. Explain what's coming in Notebook 06 |
| 1:50 – 2:00 | **Wrap-up & Next Steps** | Point students to remaining notebooks, project expectations, and office hours |

---

## 📁 Repository Structure

```
LangChain-for-Data-Science/
├── README.md                 ← You are here
├── requirements.txt          ← Python dependencies
├── .env.example              ← API key template (safe to commit)
├── .gitignore                ← Protects secrets & temp files
├── notebooks/                ← Jupyter notebooks (01–07)
├── data/                     ← Sample datasets for exercises
│   └── README.md
├── docs/                     ← Additional documentation & notes
├── images/
│   └── diagrams/            ← Architecture & concept diagrams
└── examples/
    ├── api/                  ← OpenAI API example scripts
    └── ollama/               ← Local Ollama example scripts
```

---

## 📦 Key Dependencies

| Package | Purpose |
|---|---|
| `langchain` | Core LangChain framework |
| `langchain-openai` | OpenAI chat models & embeddings |
| `langchain-ollama` | Ollama (local) chat models & embeddings |
| `langchain-text-splitters` | Document chunking for RAG |
| `langchain-chroma` | Chroma vector store integration |
| `openai` | OpenAI Python SDK |
| `chromadb` | Vector database |
| `pydantic` | Data validation & structured outputs |
| `python-dotenv` | Secure environment variable management |
| `numpy` | Numerical computing |
| `pandas` | Data manipulation |
| `scikit-learn` | ML utilities & evaluation metrics |
| `matplotlib` | Data visualization |

---

## 🤝 Contributing

Contributions welcome! This is an educational repository — feel free to:

- Fix typos or improve explanations
- Add example datasets to `data/`
- Create architecture diagrams for `images/diagrams/`
- Suggest new notebook topics via Issues

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgements

- [LangChain Documentation](https://docs.langchain.com/) — Official LangChain docs
- [OpenAI API Documentation](https://platform.openai.com/docs/) — OpenAI platform
- [Ollama](https://ollama.com/) — Local LLM runtime
- [Chroma](https://www.trychroma.com/) — Open-source vector database

---

<p align="center">
  <i>Built for BS Data Science students — Learn by doing.</i>
</p>
