# 02 — Models, Prompts and Messages

> 📓 **Hands-on Notebook:** [02 — Models, Prompts and Messages](../notebooks/02_Models_Prompts_and_Messages.ipynb)

**Level:** Beginner → Intermediate | **Reading time:** 30-40 minutes

## Learning Objectives

- Understand the difference between LLMs and Chat Models
- Learn the three message types: System, Human, AI
- Master prompt templates and few-shot prompting
- Understand structured output with Pydantic
- Know when to use different prompting strategies

## Prerequisites

- Reading 01 (LangChain Introduction)
- Basic Python knowledge

---

## 1. Chat Models

A **Chat Model** is an LLM that works with structured messages rather than raw text. Each message has a role (system, user, assistant) that tells the model who said what.

**Why Chat Models over raw LLMs?**

| Aspect | Raw LLM | Chat Model |
|--------|---------|-----------|
| Input | Plain text string | List of messages with roles |
| Context | Implicit | Explicit (system message sets behavior) |
| Control | Limited | High (system message guides behavior) |
| Multi-turn | Manual | Natural conversation flow |

**Key parameters:**

| Parameter | Effect | Typical Values |
|-----------|--------|---------------|
| `temperature` | Controls randomness | 0.0 (deterministic) to 1.0 (creative) |
| `max_tokens` | Limits response length | 100-4000 |
| `model` | Selects the specific model | gpt-4o-mini, gpt-4o, llama3.2 |

## 2. Messages

LangChain uses three message types:

### System Message
Sets the AI's behavior, personality, and constraints. The user never sees this in a real application.

```
"You are a Data Science tutor. Answer questions concisely."
```

### Human Message
The user's input or question.

```
"What is linear regression?"
```

### AI Message
The model's previous response. Used for multi-turn conversations to maintain context.

```
"Linear regression models relationships between variables."
```

### Conversation Flow

```
System: "You are a Data Science tutor."
Human:  "What is PCA?"
AI:     "PCA reduces dimensionality..."
Human:  "How do I choose the number of components?"
AI:     "Use explained variance ratio..."
```

Each message builds on the previous ones, creating context.

## 3. Prompt Templates

A **prompt template** is a reusable text pattern with variables that get filled in at runtime.

**Why templates matter:**
- Separate prompt design from application logic
- Reuse the same prompt with different inputs
- Version and test prompts independently
- Share prompts across applications

**Two types:**

### String Prompt Template
Simple string with `{variable}` placeholders.

### Chat Prompt Template
Structured messages with roles and variables. This is the standard for chat models.

```python
ChatPromptTemplate.from_messages([
    ("system", "You are a {role}."),
    ("human", "{question}")
])
```

## 4. Few-Shot Prompting

**Few-shot prompting** provides the model with examples of the desired input-output pattern before asking it to generate a response.

**Why it works:** The model learns the pattern from examples rather than needing explicit instructions.

**When to use:**
- Classification tasks
- Specific output formatting
- Domain-specific terminology
- Consistent response style

**When NOT to use:**
- Simple questions (overkill)
- When examples would be too long
- When the task is self-explanatory

## 5. Structured Output

**Structured output** forces the LLM to return data in a specific format (like JSON) rather than free-form text.

**Why it matters:**
- Downstream code can process the output programmatically
- Consistent format across all responses
- Enables validation and error handling
- Makes the output machine-readable

**Pydantic models** define the expected structure:

```python
class MLConcept(BaseModel):
    name: str
    definition: str
    difficulty: str
    use_case: str
```

The LLM fills in these fields, and you get a Python object you can use directly.

### Unstructured vs Structured Output

| Unstructured | Structured |
|-------------|-----------|
| "Random Forest is an ensemble method that reduces overfitting..." | `{"name": "Random Forest", "definition": "...", "difficulty": "intermediate"}` |
| Free-form text | Validated Python object |
| Requires parsing | Ready to use |
| Good for explanations | Good for data processing |

## 6. Data Science Applications

| Application | Technique Used |
|------------|---------------|
| Concept explainer | System message + prompt template |
| Quiz generator | Few-shot prompting + structured output |
| Code generator | System message with code instructions |
| Algorithm comparison | Structured output with comparison fields |
| Study plan creator | Multi-variable prompt template |

## 7. Practical Considerations

- **Temperature 0** for factual/consistent responses
- **Temperature 0.7+** for creative/generative tasks
- **System message first** — it sets the context for everything
- **Keep prompts focused** — one task per prompt
- **Test with edge cases** — empty input, long input, adversarial input

## 8. Common Mistakes

- **Confusing LLMs and Chat Models:** Always use Chat Models in LangChain
- **Missing system message:** Without it, the model has no behavior guidance
- **Too many variables:** Keep templates simple and focused
- **Not validating structured output:** Always handle parsing failures
- **Ignoring token limits:** Long prompts + long responses can exceed limits

## 9. Key Takeaways

- Chat Models work with structured messages, not raw text
- System messages control behavior; human messages are user input
- Prompt templates make prompts reusable and testable
- Few-shot prompting teaches patterns through examples
- Structured output with Pydantic makes LLM output programmable

## 10. Before You Run the Notebook

1. Ensure your `.env` file has `OPENAI_API_KEY` set (or Ollama running)
2. The notebook is self-contained — no prior notebook variables needed
3. All imports are at the top of the notebook

## 11. Further Reading

**Official Documentation:**
- [Chat Models (LangChain)](https://python.langchain.com/docs/concepts/chat_models/)
- [Prompt Templates (LangChain)](https://python.langchain.com/docs/concepts/prompt_templates/)
- [Structured Output (LangChain)](https://python.langchain.com/docs/concepts/structured_outputs/)

---

**Previous:** [01 — LangChain Introduction](01_LangChain_Introduction.md)
**Next:** [03 — LCEL and Chains](03_LCEL_and_Chains.md)

**Back to:** [Reading Index](README.md)
