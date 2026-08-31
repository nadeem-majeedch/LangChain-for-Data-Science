# Direct API Calls vs LangChain

## Without LangChain (Direct API Calls)

```mermaid
flowchart LR
    subgraph "Without LangChain"
        A1["👤 User"] --> B1["Your Code"]
        B1 -->|"Manual HTTP request"| C1["OpenAI API"]
        B1 -->|"Different HTTP format"| D1["Ollama API"]
        B1 -->|"Yet another format"| E1["Other APIs"]
        B1 -->|"Manual text parsing"| F1["Response"]
    end

    style A1 fill:#e1f5fe,stroke:#0288d1
    style B1 fill:#ffcdd2,stroke:#c62828
    style F1 fill:#ffcdd2,stroke:#c62828
```

**Problems:**
- Each provider has a different API format
- You must handle authentication, retries, and error handling for each
- Parsing responses requires custom code for each provider
- No built-in support for prompts, memory, or tool integration

---

## With LangChain

```mermaid
flowchart LR
    subgraph "With LangChain"
        A2["👤 User"] --> B2["Your Code"]
        B2 -->|"Simple interface"| C2["🔗 LangChain"]
        C2 -->|"Unified API"| D2["OpenAI"]
        C2 -->|"Unified API"| E2["Ollama"]
        C2 -->|"Unified API"| F2["Other Providers"]
    end

    style A2 fill:#e1f5fe,stroke:#0288d1
    style B2 fill:#c8e6c9,stroke:#388e3c
    style C2 fill:#fff9c4,stroke:#f9a825
```

**Benefits:**
- Same code works with any provider
- Built-in authentication, retries, and error handling
- Consistent interface for prompts, memory, and tools
- Easy to switch providers with minimal code changes

---

## Side-by-Side Code Comparison

### Direct API Call (Manual)
```python
import openai

client = openai.OpenAI(api_key="your-key")
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a data scientist."},
        {"role": "user", "content": "Explain feature engineering."}
    ]
)
print(response.choices[0].message.content)
```

### LangChain Approach
```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOpenAI(model="gpt-4o-mini")
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a data scientist."),
    ("human", "{question}")
])
chain = prompt | model | StrOutputParser()
print(chain.invoke({"question": "Explain feature engineering."}))
```

**Same result, but LangChain is modular, reusable, and provider-agnostic!**
