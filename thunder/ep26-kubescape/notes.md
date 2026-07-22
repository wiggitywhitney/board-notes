# Before Kubescape...

- Kubernetes security standards were starting to emerge
- Desire for a tool that automates testing a cluster against these standards

National Security Agency (NSA) came out w/ K8s security standards

**Kubescape is a tool to help you discover risks & threats in your K8s system.**

KUBESCAPE IS A
- Good security starting point
  - helps you solve configuration problems
  - helps filter out false positives (non-exploitable vulnerabilities)
  - easy to use/integrate
  - covers many aspects of security

# Threats in Kubernetes

- Managed K8s has a good default setup but has some security threats

THREAT: supply chain attack
- ex, build process exploit

THREAT: network vulnerabilities
- ex, exploit K8s control plane endpoint

**the main two attack vectors**

# Kubescape can do a lot!

- scan Kubernetes infrastructure setup
  - control plane config
  - kubelet config
  - cloud provider API config
  - ex - whether kube-API uses TLS
  - whether secrets are encrypted at rest in etcd
- scanning workload config
  - ex - whether running as root
  - permissions
  - filesystem level
  - kernel level
- scan role based access control (RBAC) configuration
  - ensures least-privilege access

Scanning uses Open Policy Agent (OPA) + their own rules

- vulnerability scanning in workloads
  - both container images & running workloads
  - uses a project called GRYPE
  - gives hardening/remediation proposals
  - uses CNCF project "Inspektor Gadget" (eBPF-powered observability)

ex - give you a least-privilege NetworkPolicy proposal

**GRYPE** does heavy lifting, Kubescape enriches data

**many vulnerabilities are irrelevant & Kubescape can help filter them out**

Config scanning vs Vulnerability scanning
- one-and-done (config is unlikely to change)
- needs constant monitoring

**hardening** = reducing attack surface

**posture** = risks & threats in the system

**least-privilege** = giving a human/process the least amount of access — this is a hard problem

**vulnerability** = a bug that, in some cases, can be exploited by an attacker

# Kubescape User Experience

1. CLI - scans YAML, Helm charts
   - good for CI/CD
   - good for investigating issues
2. Operator - installs Kubescape as a microservice & can monitor your posture
   - uses eBPF
   - produces findings as CRDs
   - can use Prometheus exporter
   - other integrations too
3. GitHub Action
   - integrate Kubescape into GitHub
   - wrapper for CLI
   (GitLab one too)

KUBESCAPE CREATED A LIBRARY OF Kubernetes Validating Admission Policies
- written in Common Expression Language (CEL)
- helps folks easily make policies that will improve security posture & least-privilege access
