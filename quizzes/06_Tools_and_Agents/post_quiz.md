# Post-Quiz: Tools and Agents

**Purpose:** Test your understanding AFTER studying this topic.
**Time:** 10-15 minutes
**Questions:** 10

---

## Learning Objectives Tested

- Create tools with @tool
- Understand the agent loop
- Know when to use agents vs chains

---

### Q1: What decorator is used to create a LangChain tool?

- A) @chain
- B) @tool
- C) @agent
- D) @runnable

### Q2: What information does a tool schema provide to the LLM?

- A) The tool's source code
- B) Name, description, and input parameters
- C) The tool's execution history
- D) The tool's cost

### Q3: How does the LLM decide which tool to use?

- A) Random selection
- B) It reads tool schemas and matches the question to tool descriptions
- C) The user specifies the tool
- D) It uses all tools every time

### Q4: What happens after a tool returns its result?

- A) The result is shown to the user immediately
- B) The LLM receives the result and generates a final answer
- C) The tool is called again
- D) The conversation ends

### Q5: 🟡 Apply Why is tool input validation important?

- A) To make tools run faster
- B) To prevent the LLM from passing dangerous inputs to tools
- C) To reduce token usage
- D) To enable caching

### Q6: What is the advantage of using agents for Data Science tasks?

- A) They are always faster
- B) They can dynamically select appropriate analysis tools
- C) They don't need tools
- D) They are simpler to build

### Q7: 🔴 Evaluate When would an agent be unnecessary overhead?

- A) For a simple Q&A system
- B) For complex multi-step analysis
- C) When multiple tools are needed
- D) When dynamic routing is required

### Q8: What is a tool allow list?

- A) A list of blocked tools
- B) A restriction on which tools an agent can access
- C) A list of all available tools
- D) A pricing list for tools

### Q9: How do you log all tool calls in an agent?

- A) Print statements
- B) Use a logging framework to record tool name, input, and output
- C) Check the LLM provider's dashboard
- D) You cannot log tool calls

### Q10: 🔴 Evaluate What makes a good tool description?

- A) As short as possible
- B) Clear, specific description of what the tool does and its inputs
- C) Include the implementation details
- D) Use technical jargon


---

**Check your answers:** [Answer Key](answer_key.md)

**Back to:** [Quiz Index](../README.md)
