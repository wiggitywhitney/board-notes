## The Problem

```mermaid
flowchart LR
    UI["Release Engineering UI"] -- GraphQL --> GW["GraphQL Gateway<br/>written in NODE"]
    subgraph INT["34 Integrations"]
        D["Deployments"] --- HTTP["HTTP"]
        N["Notifications"] --- GRPC["gRPC"]
        F["Feature flags"] --- GQL["GraphQL"]
    end
    GW -- resolvers --> D
    GW -- resolvers --> N
    GW -- resolvers --> F
```

- **Most integrations are in GO**
- custom protocol plumbing
- custom auth
- maintenance burden

## Port vs. Rewrite

| Port | Rewrite |
|---|---|
| ✅ new language | ❌ changing language + behavior |
| ✅ architecture unchanged | ❌ hard to debug |

- Change one thing at a time
- Improvement comes later

## The Astounding Results!

- **FULL PARITY IN ONE WEEK!** AH-MAZING
- **SIZE:** ~10,000 lines of code (WOW)
- **COST:** $513.40 (Huzzah!!!)

## First: Comparison Harness

(one-shot PORT FAILED)

```mermaid
flowchart LR
    Q["GraphQL Query"] --> NODE["Node<br/>(reference)"]
    Q --> GO["GO<br/>(being tested)"]
    NODE --> C["Compare<br/>Query results are<br/>exactly the same"]
    GO --> C
    C --> M["✅ match"]
    C --> X["❌ mismatch<br/>returns error + diff<br/>shows what to fix"]
```

- **local harness:** mocked downstream services
- **integration harness:** real services + full path
- **rollout harness:** real services, full path, real production traffic

## Now do the thing! PORT

```mermaid
flowchart LR
    W["WORKING REQUEST PATH<br/>GraphQL request resolves"]
    subgraph PW["parallel workstreams"]
        H["HTTP"] --> LH1["run local harness"]
        LH1 -. "❌" .-> H
        G["gRPC"] --> LH2["run local harness"]
        LH2 -. "❌" .-> G
        QL["GraphQL"] --> LH3["run local harness"]
        LH3 -. "❌" .-> QL
    end
    W --> H
    W --> G
    W --> QL
    LH1 -- "✅" --> S["Shared integration branch"]
    LH2 -- "✅" --> S
    LH3 -- "✅" --> S
    S --> DS["deploy to staging"]
    DS --> IH["run integration harness"]
    IH -- "❌" --> FIX1["fix"]
    FIX1 --> S
    IH -- "✅" --> RO["run rollout"]
    RO -- "❌" --> FIX2["fix"]
    FIX2 --> RO
    RO -- "✅" --> DONE["YAY<br/>WE ARE DONE"]
```

> **Agents do well with concrete failures**
