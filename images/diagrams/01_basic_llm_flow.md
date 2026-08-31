# Basic LLM Interaction Flow

```mermaid
flowchart TD
    A["👤 User"] -->|"Types a question"| B["💻 Application"]
    B -->|"Sends API request"| C["🤖 LLM"]
    C -->|"Generates response"| B
    B -->|"Displays result"| A

    style A fill:#e1f5fe,stroke:#0288d1
    style B fill:#fff3e0,stroke:#f57c00
    style C fill:#e8f5e9,stroke:#388e3c
```

## Description

This diagram shows the simplest form of LLM interaction:

1. **User** types a natural language question
2. **Application** sends the question to the LLM via API
3. **LLM** processes the input and generates a response
4. **Application** displays the response to the user

Without a framework like LangChain, the application must handle all the details: formatting the request, managing the API connection, parsing the response, and handling errors.
