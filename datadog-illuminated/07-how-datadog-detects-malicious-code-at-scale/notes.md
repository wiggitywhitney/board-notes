# HOW DATADOG DETECTS MALICIOUS CODE AT SCALE

malicious code ≠ vulnerabilities

## The Attack Surface

**Vector 1** ⚡ pull request
example: exfiltrate secrets via CI config

**Vector 2** ⚡ packages
example: attacker compromises pkg maintainer, backdoor ships in next update

BewAIre is software that automatically analyzes pull requests and packages to detect malicious changes

## How It Works

```mermaid
flowchart TD
    PR["pull request event"] --> API
    PKG["3rd party package source code"] --> API
    subgraph API["BewAIre API"]
        direction TB
        F["① pre-filter — fast, cheap<br/>ex GPT mini<br/>&quot;Suspicious or not?&quot;<br/>(single-turn)"]
        E["② AI-powered escalation<br/>ex Claude Opus<br/>looks at author info, comments,<br/>metadata, dependencies, etc..<br/>(full agentic flow)"]
        F -- suspicious --> E
        F -- fine --> EXIT["exit — a bit exits here<br/>0.02% escalated to human review<br/>99.98% filtered out!!"]
    end
    E --> V["returns verdict + reason<br/>malicious or benign"]
    V --> H["human triage — security incident team / security research team"]
```

## How It Scales

✱ Scanning every PR event
✱ Scanning every package release

scales because of this fast + cost effective step
also scales because of this step's precision

## BewAIre Detects:

✱ token exfiltration!
✱ encoded payloads!
✱ backdoors!
✱ typosquatting!
AND MORE!

## What's Next:

- stronger enforcement
- improving + extending package scanning
