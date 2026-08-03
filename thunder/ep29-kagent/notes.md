## Before kagent

- Knowledge lies only w domain experts (at first K8s networking knowledge)
- LLMs getting wide adoption (& MCP)
- folks using coding agents locally

kagent is open source programming framework for developers + platform engineers to build + run AI agents on Kubernetes

kagent also deploys Agents into your cluster
ex Istio, Cilium, Argo Rollouts, Prometheus Kubernetes troubleshooting

## K8s CRD = kagent config

you can say:
- type of agent
  ex use a kagent one or BYO, etc..
- prompt
- description
- which model
- tools
  BYO or kagent provides 100+ kubectl get, kubectl describe
  can specify "HUMAN IN THE LOOP"
  - AI Agent skills

BYO can be custom or 3rd party

Kagent has a CLI & WebUI + MCP interfaces

Agent Custom Resource creates Pod, Service, service acct — very customizable

## kagent controller watches:

- Agent CRD
- MCPServer CRD
- RemoteMcpServer CRD
- ModelConfig CRD
- etc.

↳ creates K8s resources to Run these things

## Agent Sandbox

- Kubernetes SIG
- sandbox within Kubernetes where you can run an AI agent
- in kagent, you can make your Agent CR a "sandbox" type

## Agent Runtimes

Default: Google Agent Development Kit
Also supports: Crewai & LangGraph

## Why run your agent on Kubernetes?

- for long-running agents
- to watch K8s (performance, cost, etc..)
- high availability
- integration w CNCF tooling

Declarative Experience

## AUTH

Identities, Policies are important
- context L8 layer
- L7 network layer

## How do people use kagent?

- creating agents to help share company-specific K8s/platform knowledge
  ex operate, troubleshoot underlying CNCF agents

kagent adds: connect to Slack or ticket system to find patterns & reduce toil

kagent adds: easily connect 3rd party tools w/o writing code

endorse open standards

kagent is a framework to help you make agents + run them in K8s w the YAML you already know — SIMPLICITY
