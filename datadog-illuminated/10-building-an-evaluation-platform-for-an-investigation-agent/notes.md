## Bits Investigation

Bits Investigation autonomous, end-to-end production investigation agent

### Why are Investigation Evals unique???

- **High Stakes**
  - critical to get right
- **Ginormous Scope**
  - many domains in parallel
  - ex hardware, app, infrastructure
- **Interconnectivity**
  - many many surfaces
  - ex tool calls, networking, etc, traces, API calls, other Datadog products

### Why EVALs (not tests)?

Discrete tests of tools, etc goes stale fast & don't give full picture

Helps stakeholders understand their part

---

## EVAL

```mermaid
flowchart LR
    EVAL[EVAL] --> P["① PROBLEM"]
    EVAL --> T["② TELEMETRY"]
    EVAL --> R["③ ROOT CAUSE"]
    EVAL --> F["④ FIX"]

    P --> EX1["EX: order service latency spike"]
    T --> EX2["EX:<br/>• p95 metric<br/>• errors increasing<br/>• DB cpu maxing out"]
    R --> EX3["EX: missing index caused query latency under load<br/>(ground truth)"]
    F --> EX4["EX:<br/>• add index<br/>• cap the query fanout<br/>• make a p95 alert"]

    EX2 -.-> NOISE["+ INJECT NOISE<br/>recreate 'the world'"]
```

**SCALABLE EVAL creation system**
- real use powers EVAL creations
- internal incidents
- this captures new tech

---

## Running an eval

```mermaid
flowchart LR
    Problem["① PROBLEM"] --> Bits(("Bits Investigation<br/>does its thing!"))
    Telemetry["② TELEMETRY"] --> Bits
    Bits --> RootCause["③ BITS' ROOT CAUSE"]
    Bits --> Fix["④ BITS' FIX"]
    RootCause --> Score["SCORE<br/>Did Bits do a good job?"]
    Fix --> Score
    Score --> Store["STORE<br/>Store behavior of a bajillion eval runs<br/>(Performance over time)"]
```

"the world" — Problem + Telemetry (inputs)

**When scoring, look at:**
- correctness
- reasoning
- what surfaces
- level of effort

**catching regressions**
- run evals regularly
- detect regressions
- alert
- surface problems early

**"Slice n-dice" evals using metadata**
- EX: product area
- surfaces
- complexity — limitless!
