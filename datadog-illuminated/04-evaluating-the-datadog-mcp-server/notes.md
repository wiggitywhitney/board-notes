## Why eval MCP server?

- A: "How many errors are checkout?" → "42 errors"
- → Agent (LLM)
- ↕ Datadog MCP
- → Datadog Backend / "42 errors"

## How eval MCP server?

eval = Agent harness + MCP server + Q & A pair

Actual ≈ expected response (if passing)

## Automate eval generation

- ★ start w seed query
  - ex: Service: checkout / status: 500
  - → Datadog API ↓ "42 errors"
- → FUZZING — make questions
  - ex "How many errors in checkout?"
  - " " show checkout errors"
- ★ one seed → many Q/A pairs
- ★ re-run to update answers

## Benefits of Great Evals

easy to make → high quality, lots of 'em → good coverage, fast to run

### ① SPEED

- ★ fast to generate: docs → seed queries → evals (a few hundred in a day)
- ★ fast to run ~2 mins to run 200 evals
- ★ See impact quickly

### ② VISIBILITY INTO PROGRESS

High quantity of evals

- ★ see overall server progress
- ★ Tag each eval ex "boolean", "wildcard"
- ★ Traces

### ③ MUTUAL BENEFIT

Datadog AI Agents use Datadog MCP

- ex. BITS AI SRE, BITS AI ASSISTANT
- ★ Better MCP server = better agents
- ★ AI Agents team give MCP team feedback

### ④ Devs like writing evals

- ★ fast evals = fast feedback
- ★ use evals to show impact
- ★ use evals to prevent regression
