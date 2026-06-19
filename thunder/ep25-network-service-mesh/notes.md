# What Is Network Service Mesh? Workload Connectivity at Layer 3

## Before Network Service Mesh...

- K8s networking model was never designed for:
  - L2 - ethernet layer
  - L3 - IP address layer — K8s addresses this
    - K8s can handle Pod-to-Pod by IP
    - Network Policy
    - K8s can provide public IPs

K8s model is GREAT — especially with [illegible]

Service meshes were starting to be built at L7 (applications)

Problems:
- workloads in different [illegible]
- Workloads tightly coupled
- [illegible — telecommunications context]
- Workloads needing to process packets at the L3 layer

---

## A Network Service is

Something that:
- processes packets [?]
- adds security, Networking, observability
- Anything that accepts IP packets & does *something*

The cloud doesn't know if a Network Service is running

### The blessed things providing the Network Service could be:
- pod that processes packets
- VM or physical server

*The cloud doesn't know if a Network Service is running*

---

## Network Service Mesh is

A technology that allows Workloads to connect to Zero or more Network Services while the workload is running

---

## User Experience

- add a single line annotation to K8s pod (for example)
- that says: I want to connect to [a network service]
- L4 is transparent layer [?]

---

## Use Cases for NSM

Examples:
- connect [inter-organizational] Services
- Connect multi-cloud apps
- when a company wants to process packets at [?]
- K8s [gives] an easy API [?]

---

## Network Service Registry

- easy to add a Network Service
- makes it discoverable
- Uses SPIFFE/SPIRE for [identity]

---

## Application Service Meshes (Istio, Kuma, Linkerd?)

- operating at: L7 — TCP, UDP
- NSM operating at: L3, L2
- APP meshes are designed [if deployed the same way]

In NSM, a workload can:
- Connect to zero or more Network Services
- possibly by [illegible]
- designed to [connect across different or same cluster]

L3 provides a single flat [unified network]
- NSM provides the same
- HTTP provides [illegible]

---

## NSM + APP meshes ARE COMPLEMENTARY
