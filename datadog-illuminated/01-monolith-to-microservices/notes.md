## Problem

Datadog WebApp Monolith
- thousands of HTTP routes
- need to be migrated to Services Framework

**Goal:** Decommission Datadog monolith! Rewriting and/or getting rid of

**Technologies:** Python, Claude Code, GPT5, LangGraph, Temporal

---

## Workflow

```mermaid
flowchart TD
    A["① Gather + Plan\n──────────────\ninput: current monolith docs,\nservices framework docs,\ninstructions (prompt),\ndestination repo\n──────────────\noutput: PLAN\n[Claude Code]"] --> B

    B["② DO THE THING! Execute the Plan\n──────────────\n[Claude Code]\ninput: prompts to write code,\nprompts for test, organization, etc.\naccess to monolith + Services Framework\n──────────────\noutput: CODE!!!! + tests\n(probably not good yet)"] --> VP1

    subgraph VP1["Verification Process"]
        C["③ Run typechecker + fix issues"] --> D
        D["④ Run tests + fix issues"] --> E
        E["⑤ Start Server + fix issues"]
        E -- fails --> C
        D -- fails --> C
    end

    VP1 --> F["⑥ Code review by GPT5\n──────────────\ninput: code diff, prompts,\ngoal of migration,\naccess to monolith +\nservices framework\n──────────────\noutput: 1 of 2 things:\n• PASSES  -or-\n• discrepancies"]

    F -- passes --> K
    F -- discrepancies --> G

    G["⑦ Address discrepancies\n──────────────\n[Claude Code]\ninput: context, prompts, discrepancies\n──────────────\noutput: Code + tests"] --> VP2

    subgraph VP2["Verification Process"]
        H["⑧ run typechecker + fix issues"] --> I
        I["⑨ run tests + fix issues"] --> J
        J["⑩ start server + fix issues"]
        I -- fails --> H
        J -- fails --> H
    end

    VP2 --> K["⑪ open PR"]
    K --> L["⑫ deploy to staging"]
    L --> M["⑬ HUMAN REVIEW"]
    M --> N["MERGED & DEPLOYED!!! HUZZAH!!! WOO HOO!!!"]
```

---

## Room for Improvement

- not always passing integration testing
- How to measure success? + consistency
- modernize while migration

## What's Good

- exploratory + validating THIS WORKFLOW HAS GREAT POTENTIAL
- continuous improvement
- Workflow has run successfully
