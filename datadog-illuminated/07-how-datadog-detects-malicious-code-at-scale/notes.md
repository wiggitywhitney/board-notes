# HOW DATADOG DETECTS MALICIOUS CODE AT SCALE

malicious code ≠ vulnerabilities

## The Attack Surface

- **Vector 1** ⚡ pull request
  - example: exfiltrate secrets via CI config
- **Vector 2** ⚡ packages
  - example: attacker compromises package maintainer, backdoor ships in next update

BewAIre is software that automatically analyzes <u>pull requests</u> and <u>packages</u> to detect <u>malicious changes</u>

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
        F -- "fine — 99.98% filtered out" --> EXIT["exit"]
    end
    E -- "0.02% escalated to human review" --> V["returns verdict + reason<br/>malicious or benign"]
    V --> H["human triage — security incident team / security research team"]
```

## How It Scales

☆ Scanning every PR event<br/>
☆ Scanning every package release<br/>

scales because of the fast + cost effective step 1 ↑<br/>
also scales because of step 2's precision ↑

## BewAIre Detects:

☆ token exfiltration!<br/>
☆ encoded payloads!<br/>
☆ backdoors!<br/>
☆ typosquatting!<br/>
AND MORE!

## What's Next:

- stronger enforcement
- improving + extending package scanning
