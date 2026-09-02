# Final Capstone Rubric

**Total Marks:** 100 (+ 40 bonus)

## Grading Scale

| Grade | Percentage | Description |
|-------|-----------|-------------|
| A | 90-100% | Excellent — exceeds expectations |
| B+ | 80-89% | Strong — meets all requirements well |
| B | 70-79% | Good — meets most requirements |
| C+ | 60-69% | Satisfactory — meets minimum requirements |
| C | 50-59% | Passing — some requirements missing |
| F | <50% | Failing — does not meet minimum requirements |

## Rubric

### Architecture (15 marks)

| Criterion | Excellent (15-13) | Good (12-10) | Satisfactory (9-7) | Needs Improvement (<7) |
|-----------|-------------------|--------------|---------------------|----------------------|
| **Design** | Clean, modular, scalable architecture with clear separation of concerns | Well-structured with minor issues | Functional but some design problems | Poorly structured, hard to understand |
| **Components** | All components properly integrated | Most components integrated | Some components missing | Major components missing |
| **Data flow** | Clear, documented data flow | Mostly clear flow | Some unclear paths | Confusing data flow |

### LLM & Prompt Design (10 marks)

| Criterion | Excellent (10-9) | Good (8-7) | Satisfactory (6-5) | Needs Improvement (<5) |
|-----------|-------------------|------------|---------------------|----------------------|
| **Prompts** | Well-crafted, tested, effective prompts | Good prompts with minor issues | Basic prompts that work | Poor prompts, inconsistent results |
| **Configuration** | Provider-agnostic, configurable | Mostly configurable | Some configuration | Hardcoded settings |

### RAG (15 marks)

| Criterion | Excellent (15-13) | Good (12-10) | Satisfactory (9-7) | Needs Improvement (<7) |
|-----------|-------------------|--------------|---------------------|----------------------|
| **Knowledge base** | 15+ well-structured documents with metadata | 10+ documents with some metadata | 10+ documents, no metadata | Few documents, poor quality |
| **Retrieval** | High-quality retrieval with filtering | Good retrieval | Basic retrieval | Poor retrieval |
| **Generation** | Grounded, accurate, cited answers | Mostly accurate | Sometimes accurate | Often inaccurate |

### Tools & Agent (10 marks)

| Criterion | Excellent (10-9) | Good (8-7) | Satisfactory (6-5) | Needs Improvement (<5) |
|-----------|-------------------|------------|---------------------|----------------------|
| **Tool design** | Well-designed, validated, documented tools | Good tools with validation | Basic tools | Poor or missing tools |
| **Agent routing** | Smart, accurate routing | Mostly accurate routing | Basic routing | No routing or poor routing |

### Data Science Functionality (15 marks)

| Criterion | Excellent (15-13) | Good (12-10) | Satisfactory (9-7) | Needs Improvement (<7) |
|-----------|-------------------|--------------|---------------------|----------------------|
| **DS relevance** | Highly relevant to Data Science | Mostly relevant | Somewhat relevant | Generic, not DS-specific |
| **Dataset** | Real, meaningful dataset with analysis | Good dataset | Basic dataset | No dataset or trivial |
| **Insights** | Provides actionable insights | Mostly insightful | Some insights | No meaningful insights |

### Evaluation (10 marks)

| Criterion | Excellent (10-9) | Good (8-7) | Satisfactory (6-5) | Needs Improvement (<5) |
|-----------|-------------------|------------|---------------------|----------------------|
| **Test coverage** | 15+ test cases, all types | 10+ test cases | 5+ test cases | <5 test cases |
| **Metrics** | Multiple metrics, automated | Some metrics | Basic metrics | No metrics |
| **Results** | Comprehensive analysis | Good analysis | Basic analysis | No analysis |

### Security (10 marks)

| Criterion | Excellent (10-9) | Good (8-7) | Satisfactory (6-5) | Needs Improvement (<5) |
|-----------|-------------------|------------|---------------------|----------------------|
| **Input validation** | Comprehensive validation | Good validation | Basic validation | No validation |
| **Output validation** | Data leakage prevention | Mostly secure | Some checks | No output checks |
| **Secrets** | Proper secrets management | Environment variables | .env file | Hardcoded secrets |

### Code Quality (5 marks)

| Criterion | Excellent (5) | Good (4) | Satisfactory (3) | Needs Improvement (<3) |
|-----------|---------------|----------|-------------------|----------------------|
| **Clean code** | Well-organized, PEP 8, documented | Mostly clean | Some issues | Messy, hard to read |

### Documentation (5 marks)

| Criterion | Excellent (5) | Good (4) | Satisfactory (3) | Needs Improvement (<3) |
|-----------|---------------|----------|-------------------|----------------------|
| **README** | Complete setup, architecture, usage | Good README | Basic README | Missing or incomplete |

### Presentation (5 marks)

| Criterion | Excellent (5) | Good (4) | Satisfactory (3) | Needs Improvement (<3) |
|-----------|---------------|----------|-------------------|----------------------|
| **Demo** | Clear, impressive demonstration | Good demo | Basic demo | Poor or missing demo |

## Bonus Marks (up to 40)

| Feature | Marks |
|---------|-------|
| LangGraph workflow | +5 |
| MCP integration | +3 |
| Advanced RAG (query rewriting, reranking) | +5 |
| Evaluation framework | +5 |
| Observability (logging, metrics, tracing) | +5 |
| Production features (caching, rate limiting) | +5 |
| Creative/innovative features | +5 |
| Exceptional documentation | +3 |
| Exceptional testing | +4 |

## Submission Checklist

- [ ] Source code submitted
- [ ] README with setup instructions
- [ ] Architecture diagram included
- [ ] Evaluation report with 10+ test cases
- [ ] Security documentation
- [ ] Demo working
- [ ] Code clean and documented
- [ ] No hardcoded secrets

---

**Back to:** [Final Capstone](README.md) | [Assignment Index](../README.md)
