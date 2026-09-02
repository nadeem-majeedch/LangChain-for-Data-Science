# Post-Quiz: Models, Prompts & Messages

**Purpose:** Test your understanding AFTER studying this topic.
**Time:** 10-15 minutes
**Questions:** 10

---

## Learning Objectives Tested

- Understand chat models vs LLMs
- Use message types correctly
- Create prompt templates
- Implement structured output

---

### Q1: 🟢 Understand Which message type should come FIRST in a conversation?

- A) Human Message
- B) AI Message
- C) System Message
- D) Tool Message

### Q2: 🟡 Apply Given this prompt template, what happens if you forget the "topic" variable?

```
prompt = ChatPromptTemplate.from_messages([
    ("system", "Explain {topic}"),
    ("human", "Tell me about {topic}")
])
```

- A) It uses a default value
- B) It raises an error
- C) It ignores the missing variable
- D) It works but gives generic answers

### Q3: What is the purpose of few-shot prompting?

- A) To make the model respond faster
- B) To show examples of desired input-output patterns
- C) To reduce token usage
- D) To enable tool calling

### Q4: When should you use temperature=0 vs temperature=0.7?

- A) Always use 0.7
- B) Use 0 for factual tasks, 0.7 for creative tasks
- C) Temperature does not matter
- D) Use 0 for creative tasks

### Q5: 🟡 Apply What Pydantic model field type would you use for a difficulty level that must be "beginner", "intermediate", or "advanced"?

- A) str
- B) int
- C) Literal["beginner", "intermediate", "advanced"]
- D) List[str]

### Q6: A student creates a prompt template but forgets to include a system message. What is likely to happen?

- A) The LLM will refuse to answer
- B) The LLM has no behavior guidance and may give inconsistent answers
- C) The code will crash
- D) Nothing — system messages are optional

### Q7: Which is correct for creating a chat prompt with LangChain?

- A) PromptTemplate.from_messages(...)
- B) ChatPromptTemplate.from_messages([...])
- C) ChatModel.create(...)
- D) LLM.prompt(...)

### Q8: What does with_structured_output() do?

- A) Formats output as plain text
- B) Forces LLM to return data matching a Pydantic schema
- C) Parses the output into a dictionary
- D) Saves output to a file

### Q9: In a conversation, why include previous AI messages in the history?

- A) To make the prompt longer
- B) To maintain context across turns
- C) To reduce token usage
- D) To enable tool calling

### Q10: 🔴 Evaluate A quiz generator needs to produce questions with: question_text, options, correct_answer, difficulty. What is the best approach?

- A) Return plain text and parse it
- B) Use with_structured_output() with a Pydantic model
- C) Use multiple separate LLM calls
- D) Use a regex to extract fields


---

**Check your answers:** [Answer Key](answer_key.md)

**Back to:** [Quiz Index](../README.md)
