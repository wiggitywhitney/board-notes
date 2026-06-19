# What Is Network Service Mesh? Workload Connectivity at Layer 3

## Before Network Service Mesh...

Kubernetes networking model was new: L2 Ethernet layer, L3 IP address layer. Kubernetes starts here:

- In Kubernetes, every pod can talk to every other pod by IP.
- Can isolate pods through network policy, therefore labels/selectors.
- Kubernetes service can provide stable IP to a set of pods.

> K8s model is GREAT... except when it's not. No flexibility.

Service meshes were starting to be built at L7 (application problems):

- More expensive to process at L7.
- Hard to move traffic between workloads in different clusters and/or cloud providers.
- Workloads are tightly coupled with Kubernetes networking.
- Telecommunications companies want to process at the L2/L3 layers.

---

## A Network Service is

Something that processes IP packets (L3) and adds security, networking, and observability. Anything that accepts IP packets and does something.

---

## Network Service Mesh is

A technology that allows workloads to connect to zero or more network services, independent of where the workload is running.

**User experience:** add a single line annotation to a Kubernetes pod, for example, that names the network service I want to connect to. L4 is the transport layer (TCP/IP).

---

## The blessed thingy that is providing the Network Service could be:

- Pod that processes packets
- VMs or physical servers
- Physical routers and switches

> The client doesn't know or care where the Network Service is running.

---

## Use Cases for NSM

- Connect workloads only
- Connect inner organizational services (example: a car company and a parts supplier)
- Connect multi-cloud apps to, say, a database that uses a funky protocol, possibly by connecting to an application service mesh
- When a company wants to process packets (example: telecommunications)

Kubernetes setup is an easy `kubectl apply` command.

---

## Network Service Registry

- Easy to add a network service and make it discoverable
- Uses SPIFFE/SPIRE for workload authentication and OPA for authorization

---

## Application Service Meshes (Istio, Kuma, LinkerD) vs. NSM

- App mesh is mostly operating at L7 (HTTP, etc.)
- NSM is operating at L3, usually sometimes L2
- App meshes are only one per workload and typically one per cluster
- In NSM, a workload can connect to many network services
  - Can connect to services in different orgs
  - Mutually ignorant things coexisting

NSM scales fabulously well at internet scale.

---

## NSM and App Meshes Are Complementary

- L3 provides a single flat connectivity domain across systems, a hard problem to solve at L7
- L7 provides complex routing and fun HTTP reasoning
