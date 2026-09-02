# Common Student Mistakes

## Notebook 01: LangChain Introduction

### Mistake: Confusing LLM with LangChain
**Why:** Students think LangChain IS the LLM.
**Correct:** LangChain is a FRAMEWORK that helps you BUILD applications using LLMs.
**Explanation:** "LangChain is like Flask for LLMs — it's a framework, not the server itself."

### Mistake: API Key Problems
**Why:** Students forget to set environment variables or hardcode keys.
**Correct:** Always use `load_dotenv()` and `.env` files.
**Explanation:** "Never put API keys in code. Use environment variables."

### Mistake: Not Understanding Temperature
**Why:** Students don't realize temperature affects output randomness.
**Correct:** Temperature 0 = deterministic; Temperature 1 = creative.
**Explanation:** "Think of temperature as 'creativity dial' — lower is more factual."

---

## Notebook 02: Models, Prompts & Messages

### Mistake: Missing System Message
**Why:** Students forget the system message sets behavior.
**Correct:** Always include a system message first.
**Explanation:** "The system message is like giving the LLM a job description."

### Mistake: Hardcoding Prompt Text
**Why:** Students write prompts as strings instead of templates.
**Correct:** Use `ChatPromptTemplate` with variables.
**Explanation:** "Templates make prompts reusable and testable."

### Mistake: Confusing LLM and Chat Model
**Why:** Students use raw LLMs instead of Chat Models.
**Correct:** Always use Chat Models in LangChain.
**Explanation:** "Chat Models work with messages (system, human, AI). Raw LLMs are for raw text."

---

## Notebook 03: LCEL and Chains

### Mistake: Forgetting StrOutputParser
**Why:** Students get raw model output instead of text.
**Correct:** Add `| StrOutputParser()` at the end.
**Explanation:** "Without the parser, you get metadata. With it, you get clean text."

### Mistake: Not Understanding Pipe Operator
**Why:** Students don't see how `|` connects components.
**Correct:** The pipe operator passes output to the next component.
**Explanation:** "Think of it like Unix pipes: `cat file | grep pattern | sort`"

---

## Notebook 04: Embeddings & Vector Stores

### Mistake: Confusing Embeddings with LLMs
**Why:** Students think embeddings generate text.
**Correct:** Embeddings convert text to vectors. LLMs generate text.
**Explanation:** "Embeddings are like a search index — they help you FIND text, not generate it."

### Mistake: Poor Chunking
**Why:** Students use wrong chunk sizes.
**Correct:** Experiment with different sizes (200-1000 tokens).
**Explanation:** "Too small loses context. Too large adds noise."

### Mistake: Ignoring Metadata
**Why:** Students don't add metadata to documents.
**Correct:** Add topic, difficulty, source as metadata.
**Explanation:** "Metadata is like tags — it helps filter search results."

---

## Notebook 05: RAG Applications

### Mistake: Thinking RAG Eliminates Hallucination
**Why:** Students believe RAG makes LLMs always correct.
**Correct:** RAG reduces but doesn't eliminate hallucination.
**Explanation:** "RAG gives the LLM references, but it can still make things up."

### Mistake: Retrieving Too Many Documents
**Why:** Students think more is always better.
**Correct:** Optimize top-k (usually 3-5).
**Explanation:** "Too many documents confuse the LLM and waste tokens."

### Mistake: Not Chunking Documents
**Why:** Students pass entire documents to the LLM.
**Correct:** Always chunk documents before embedding.
**Explanation:** "LLMs have limited context windows. Chunking fits documents within limits."

---

## Notebook 06: Tools and Agents

### Mistake: Assuming Agents Are Always Better
**Why:** Students think agents are more advanced.
**Correct:** Chains are better for fixed workflows; agents for dynamic tasks.
**Explanation:** "Agents add overhead. Use chains when you know the exact steps."

### Mistake: Not Validating Tool Inputs
**Why:** Students trust user input blindly.
**Correct:** Always validate and sanitize tool inputs.
**Explanation:** "Users might enter malicious data. Validate everything."

### Mistake: Too Many Tools
**Why:** Students create tools for everything.
**Correct:** Start with 2-3 essential tools.
**Explanation:** "More tools = more complexity. Start simple."

---

## Notebook 08: Advanced RAG

### Mistake: Not Experimenting with Chunk Sizes
**Why:** Students use default sizes without testing.
**Correct:** Always experiment and measure.
**Explanation:** "Different data needs different chunk sizes. Test and compare."

### Mistake: Ignoring Metadata Filtering
**Why:** Students don't use metadata for precision.
**Correct:** Add and filter by metadata.
**Explanation:** "Metadata filtering is like adding WHERE clauses to your search."

---

## Notebook 10: SQL & Databases

### Mistake: Trusting Generated SQL Blindly
**Why:** Students execute LLM-generated SQL without checking.
**Correct:** Always show SQL before execution.
**Explanation:** "LLMs can generate dangerous SQL. Always review first."

### Mistake: Using Write Access
**Why:** Students give LLMs full database access.
**Correct:** Use read-only database connections.
**Explanation:** "Never let an LLM modify your database."

---

## Notebook 12: LangGraph

### Mistake: Infinite Loops
**Why:** Students don't add exit conditions.
**Correct:** Always add max iteration limits.
**Explanation:** "Graphs can loop forever. Always add a safety limit."

### Mistake: Confusing State with Variables
**Why:** Students don't understand state management.
**Correct:** State is a dictionary that flows through the graph.
**Explanation:** "State is like a backpack — it carries information from node to node."

---

## Notebook 14: Security

### Mistake: Treating Retrieved Content as Trusted
**Why:** Students assume retrieved documents are safe.
**Correct:** Always treat retrieved content as untrusted data.
**Explanation:** "Retrieved text is DATA, not INSTRUCTIONS. Never follow it blindly."

### Mistake: Not Sanitizing Outputs
**Why:** Students don't check what the LLM returns.
**Correct:** Always validate and sanitize outputs.
**Explanation:** "The LLM might accidentally include sensitive information."

---

**Back to:** [Instructor Guide](README.md) | [Teaching Roadmap](teaching_roadmap.md)
