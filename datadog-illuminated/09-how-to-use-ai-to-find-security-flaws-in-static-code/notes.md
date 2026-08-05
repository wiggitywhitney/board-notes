## Static Application Security Testing (SAST)

- Scans source code to find vulnerabilities
- Uses pattern matching

**PROBLEMS**
- High false positive rate
- Doesn't have context of surrounding files

---

AI-Native SAST uses LLMs to reason about code instead of relying on patterns

Finds vulnerabilities without so many false positives & with more context

**UNDERSTANDS**
- Code semantics, data/execution flow, code usage, context

---

**EXAMPLE USE CASE**
Devs make a service that feeds app logs to an LLM for sentiment analysis & categorization

---

**OWASP** - Open Web Application Security Project

**Benchmark** → Industry standard

AI-Native SAST improved Datadog's OWASP score by 50%

## AI-Native SAST

*Triggered by Git operations*

### Step 1: Identify Relevant Files

(NO LLM)

- ★ Doesn't Analyze whole repo
- ★ Uses cached results
- Use heuristics, keywords
- **EX**: Flags a file w an input going straight to LLM

## How It Works

### Step 2: Get Context

(NO LLM)

- Builds context for data flow analysis
- Cross-file context
- **EX**: Build context for the file that was flagged in step 1. Sees that user logs direct to LLM

### Step 3: AI Analysis

**A** — Fast + Cheap LLM pass
- Yes or no, smaller model
- More false positives
- **EX**: Sees no sanitization → (FLAG)

**B** — Thorough LLM pass
- Reasoning model
- Deep analysis
- Output: yes or no with reasoning
- What, Where, Why, When
- **EX**: Traces full flow. Confirms issue & says why

### Step 4: Post-processing

(output: SARIF file)

**FIRST: CACHE RESULTS** ★
- If Benign → Drop it
- If Vulnerable → Keep, and...
- , Output SARIF file
- Use SARIF file to surface issues to users as alert, in IDE, in pull request in Datadog UI
- **EX**: Results surfaced to devs w/ reasoning + actionable steps

**OPTIMIZING COST** ★ = cost optimizing
- ★ Full repo scanned only at onboarding

```mermaid
flowchart LR
    Step1["Step 1: Identify Relevant Files (No LLM)"] --> Step2["Step 2: Get Context (No LLM)"]
    Step2 --> Step3["Step 3: AI Analysis (A: Fast+Cheap pass / B: Thorough pass)"]
    Step3 --> Step4["Step 4: Post-processing"]
    Step4 --> SARIF["Output: SARIF File"]
```
