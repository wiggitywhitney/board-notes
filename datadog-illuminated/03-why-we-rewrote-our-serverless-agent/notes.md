# Why We Rewrote Our Serverless Agent

## The Problem Space

- AWS Lambda is weird
  - CPU gets frozen between requests
  - Very small resources
  - Isolated sandboxes
- Datadog Agent
  - Designed to be long-running
  - Large binary - 55mb
  - 400ms+ to start up

## Why Rewrite?

- Make agent lighter, ~20% of code needed
- Eliminate upstream bugs
- Switch to RUST
  - No garbage collection
  - Small binaries / low memory
  - Fast startup
  - Memory safety
- Also more reasons we'll say later *(Suspense)*

## Challenges

- No RUST knowledge

## Before / After

### Before

```text
|— 400ms init —|————— function runs —————|— send data to Datadog —|
```

### After

```text
|50ms init|——— function runs ———|   ← Continuous flushing
              ↓      ↓      ↓
     Send data to Datadog - during I/O waits!
```

## Results

- Improved startup time! 400ms → 50ms
- Decreased binary size! 55mb → 7mb
- Memory reduced by 50%
- 2x reduction in tail latency
- Safe rollout procedure
  - Ship RUST + GO binaries together
  - Failover to old GO version
- Rolled out in under a year!
