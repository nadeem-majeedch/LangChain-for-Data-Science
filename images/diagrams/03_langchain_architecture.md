# LangChain Architecture Overview

```mermaid
flowchart TB
    subgraph "Your Application"
        A["User Interface"]
        B["Business Logic"]
    end

    subgraph "LangChain Framework"
        C["Prompt Templates"]
        D["Chat Models"]
        E["Output Parsers"]
        F["Chains (LCEL)"]
    end

    subgraph "Model Providers"
        G["OpenAI API"]
        H["Ollama (Local)"]
        I["Other Providers"]
    end

    A --> B
    B --> C
    B --> F
    C --> F
    F --> D
    D --> E
    D --> G
    D --> H
    D --> I

    style A fill:#e1f5fe,stroke:#0288d1
    style B fill:#e1f5fe,stroke:#0288d1
    style C fill:#fff9c4,stroke:#f9a825
    style D fill:#e8f5e9,stroke:#388e3c
    style E fill:#f3e5f5,stroke:#7b1fa2
    style F fill:#fce4ec,stroke:#c62828
    style G fill:#e0e0e0,stroke:#616161
    style H fill:#e0e0e0,stroke:#616161
    style I fill:#e0e0e0,stroke:#616161
```

## Description

LangChain sits between your application and model providers:

### Layer 1: Your Application
- **User Interface** — How users interact with your app
- **Business Logic** — Your data science workflows and decision-making

### Layer 2: LangChain Framework
- **Prompt Templates** — Reusable, parameterized instructions for LLMs
- **Chat Models** — Unified interface to different LLM providers
- **Output Parsers** — Convert LLM text output to structured data
- **Chains (LCEL)** — Connect components into pipelines using the `|` operator

### Layer 3: Model Providers
- **OpenAI API** — Cloud-based models (GPT-4o, GPT-4o-mini)
- **Ollama (Local)** — Run models on your own hardware
- **Other Providers** — Anthropic, Google, open-source models

### Key Insight
LangChain lets you swap any layer independently. Switch from OpenAI to Ollama by changing one line. Modify your prompt template without touching model code. Add output parsing without rewriting your prompts.
