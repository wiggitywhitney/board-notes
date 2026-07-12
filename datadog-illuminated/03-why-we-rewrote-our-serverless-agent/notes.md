# Why We Rewrote Our Serverless Agent

## The Problem Space

- AWS Lambda is weird
  - CPU gets frozen btwn requests
  - very small resources
  - isolated sandboxes
- Datadog Agent
  - designed to be long-running
  - large binary - 55mb
  - 400ms+ to start up

### Before

```text
|— 400ms init —|————— function runs —————|— send data to Datadog —|
```

### After

```text
|50ms init|— function runs —|
     ↓          ↓         ↓
     send data to Datadog - during I/O waits!
```

← Continuous flushing

## Why Rewrite?

- make agent lighter, ~20% of code needed
- eliminate upstream bugs
- switch to RUST
  - no garbage collection
  - small binaries / low memory
  - fast startup
  - memory safety
- Also more reasons we'll say later *(Suspense)*

## Challenges

- no RUST knowledge

## Results

- improved startup time! 400ms → 50ms
- decreased binary size! 55mb → 7mb
- memory reduced by 50%
- 2x reduction in tail latency
- safe rollout procedure
  - ship RUST + GO binaries together
  - failover to old GO version
- rolled out in under a year!
