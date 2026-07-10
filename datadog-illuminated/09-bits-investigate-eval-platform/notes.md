**Bits Investigate** is an autonomous, end-to-end production investigation AI agent

Getting Bits Investigate Quality Right

☆ High Stakes
- critical to get right

☆ Huge Scope
- many domains in parallel
  ex app code, infra, DBs
- limitless incident shapes

☆ Interconnectivity
- many many surfaces
  ex API call, tool, skill, a Datadog product

Why EVALS (not tests)?
Evals understand scope + track behavior over time

---

```mermaid
flowchart LR
    EVAL["EVAL"] --> P["① PROBLEM"]
    EVAL --> T["② TELEMETRY"]
    EVAL --> R["③ ROOT CAUSE"]
    EVAL --> F["④ FIX"]

    P --> EXP["EX: order service latency spike"]
    T --> EXT["EX:<br/>• p95 metric<br/>• DB cpu maxed out<br/>• increased error rate"]
    R --> EXR["EX: missing index caused query latency under load"]
    F --> EXF["EX:<br/>• add index<br/>• cap query fanout<br/>• add alert on p95/cpu"]
```

Next to the TELEMETRY example: **"The world"** — Noise is good! ← PROD has noise so eval platform should too

PLATFORM should handle change
- eval collection built into platform
- user feedback spawns evals
- also technology landscape changes

---

**Running an eval**

```mermaid
flowchart LR
    PROBLEM["PROBLEM"] --> BI(("BITS<br/>INVESTIGATE"))
    TELEMETRY["TELEMETRY"] --> BI
    BI --> BRC["BITS' ROOT CAUSE"]
    BI --> BFIX["BITS' FIX"]
    BRC --> SCORING["SCORING"]
    BFIX --> SCORING
    SCORING --> STORING["STORING"]
```

inputs - "the world" (PROBLEM, TELEMETRY)
BITS INVESTIGATE does its thing!
outputs (BITS' ROOT CAUSE, BITS' FIX)
SCORING — did Bits do a good job?
STORING — store behavior of a bajillion eval runs

PERFORMANCE over time

**Segmentation** — metadata added to an eval
examples of segments: underlying failure mode, surface, complexity/difficulty. limitless

Helps stakeholders understand their piece of Bits Investigate

When scoring, look at:
- correctness
- reasoning
- what surfaces
- level of effort

Regression catching
- run evals regularly
- detect regressions
- alert
- surface early
