**kagent is an open-source programming framework for developers and platform engineers to build and run AI agents on Kubernetes.**

## Before kagent

- Knowledge lies only with domain experts (at first Kubernetes networking knowledge)
- LLMs getting wide adoption (and MCP)
- folks using coding agents locally

kagent also deploys agents into your cluster

Example: Istio, Cilium, Argo Rollouts, Prometheus, Kubernetes troubleshooting

## kagent config

### Kubernetes CRD

You can define:

1. type of agent
   - example: use a kagent one or BYO, etc.
2. prompt
3. description
4. which model
5. tools
   - BYO or kagent provides hundreds
     - example: kubectl get, kubectl describe
   - BYO can be custom or third-party
6. can specify human in the loop
7. AI agent skills

Kagent has a CLI, WebUI, and MCP interfaces

## kagent controller watches: Agent CRD (described above)

- MCP Server CRD
- Remote MCP Server CRD
- Model Config CRD
- etc.

Creates Kubernetes resources to run these things

- example: Agent Custom Resource creates Pod, Service, Service Account (very customizable)

## Agent Sandbox

- Kubernetes SIG
- sandbox within Kubernetes where you can run an AI agent
- in kagent, you can make your Agent CR a "sandbox" type

## Agent Runtimes

- Default: Google Agent Development Kit
- Also supports: CrewAI and LangGraph

## Why run your agent on Kubernetes?

1. for long-running agents
2. to watch Kubernetes (performance, cost, etc.)
3. high availability
4. integration with CNCF tooling
5. declarative experience

## AUTH

Identities, Policies are important

- new context layer
- L7
  - network layer

## How do people use kagent?

1. Creating agents to help share company-specific Kubernetes/platform knowledge
   - example: operate/troubleshoot underlying CNCF agents
2. What kagent adds:
   - Connect to Slack or ticket system to find patterns and reduce toil
   - kagent easily connects third-party tools without writing code

kagent is a framework to help you make agents and run them in Kubernetes with the YAML you already know — Simplicity
