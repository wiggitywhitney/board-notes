## The Problem

```mermaid
flowchart TB
    GitHub["GitHub<br/>source of truth"]
    Backend["Datadog Git<br/>Backend"]
    Runners["CI Runners"]

    GitHub -- internal sync --> Backend
    Backend -- git clone/fetch --> Runners
```

- ★ CI slow + many outages
- ★ AI coding agents 10x Git traffic
- ★ Tried:
  - add backend nodes ✗
  - add CDN/cache ✗
  - have CI fetch straight from GitHub ✗

---

## How Git Fetch Works

**client - CI runner:** "This is what I *have* in my Git. This is what I *want* from your Git"

**server - Datadog Git backend:** "Okay! I'll compute what changed + send it in a Packfile"

reference (ref) = pointer to a commit

---

## GitRetriever = self-hosted Git Mirror

```mermaid
flowchart TB
    GitHub["GitHub<br/>source of truth"]
    subgraph GitRetriever["GitRetriever"]
        Mirror1["Mirror<br/>(sync + resolve changes)"]
        Mirror2["Mirror<br/>(sync + resolve changes)"]
        subgraph Relays["Relays scale out the reads (autoscaling)"]
            Relay1["Relay<br/>(stay up to date w mirror)"]
            Relay2["Relay<br/>(stay up to date w mirror)"]
        end
        LB["GitRetriever Load Balancer<br/>one single endpoint"]
    end
    CI["CI JOBS"]

    GitHub -- changes as packfiles --> Mirror1
    Mirror1 -- poll for changes --> GitHub
    GitHub <--> Mirror2
    Mirror1 --> Relay1
    Mirror2 --> Relay2
    Relays ~~~ LB
    LB ~~~ CI
    LB --> Relays
    CI -- "git clone/git fetch<br/>new upstream" --> LB
    CI -- "lookup API<br/>file/SHA/Diff<br/>no clone needed" --> LB
```

---

## mirror: a closer look

| changed refs | parallel fetches | thin packfile | resolve once | resolved packfile |
|---|---|---|---|---|
| fetch changed refs in parallel + save to memory | | trade higher mirror CPU for speed | | reused by relays |

---

## relay: closer look*

```mermaid
sequenceDiagram
    participant mirror
    participant Relay
    mirror->>Relay: gRPC: "Hey theres a new packfile X"
    Relay->>mirror: HTTP: "yo I want packfile X"
    mirror->>Relay: "Here you go!" (Resolved packfile)
```

- Relay: Auto-scaling
- \* this happens in parallel

---

## Results!

- ~20x traffic flat latency
- 100m+ req/week
- ~10 ms lookup
- ~5500 repos
- 3-4x lower CPU
- sec → ms sync
