# LLM Application Flow with LangChain

```mermaid
flowchart TD
    A["👤 User"] -->|"Natural language query"| B["📝 Prompt Template"]
    B -->|"Formatted messages"| C["🤖 Chat Model"]
    C -->|"Raw AI response"| D["📋 Output Parser"]
    D -->|"Structured result"| E["💻 Application"]
    E -->|"Formatted answer"| A

    B -.->|"Parameters"| B1["{topic}<br/>{context}<br/>{format}"]
    C -.->|"Providers"| C1["OpenAI<br/>Ollama<br/>Anthropic"]
    D -.->|"Formats"| D1["String<br/>JSON<br/>Pydantic"]

    style A fill:#e1f5fe,stroke:#0288d1
    style B fill:#fff9c4,stroke:#f9a825
    style C fill:#e8f5e9,stroke:#388e3c
    style D fill:#f3e5f5,stroke:#7b1fa2
    style E fill:#fff3e0,stroke:#f57c00
```

## Description

This diagram shows a structured LLM application built with LangChain:

1. **User** submits a natural language query
2. **Prompt Template** formats the query with variables and system instructions
3. **Chat Model** processes the formatted prompt (supports multiple providers)
4. **Output Parser** converts the raw AI response into structured data
5. **Application** presents the formatted answer to the user

Each component is modular and can be swapped independently — change the model provider, adjust the prompt template, or switch output formats without rewriting the entire pipeline.
