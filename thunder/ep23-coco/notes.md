# Confidential Containers (CoCo) — Board Notes

## Basics: Confidential Containers (CoCo)

### Background: Confidential Computing (CC)
- Confidential Computing (CC) was very new
- CC was hard to integrate in Kubernetes
- CoCo solves it: integrating CC in K8s → standardization
- Reaches the Pod level; about the control Plane
- Confidential Containers is a technology that has big momentum — a paradigm shift

### What is Confidential Computing?
- Different trust model
- It is hardware
- Usually implemented as VMs + extra layer of security — cannot be breached by [the hypervisor/cloud provider]

### Confidential Computing Protects:
- Data at rest: is protected
- Data in motion: is protected
- Data in use: is **vulnerable**

**The adversary model:** the physical machine owner  
For example: **WHOEVER owns the KERNEL SEES ALL**

---

## Isolation and Attestation

- attestation: [illegible]
- isolation: [illegible]

For example, secrets are only supplied if the secure place is attested

Flow: IMAGES → COI → [illegible] → K8s → WORKLOAD SECRET

---

## The Importance of Using CoCo

**SOLUTION — NEED THE RIGHT MECHANISM**
- Run K8s operator
- Download + install CoCo
- Add a runtime class to your workload

---

## The Confidential Computing Trust Model
### DON'T TRUST THE HOST

**Confidential VM** (inside the host)

KATA:
- KATA runs on the host
- KATA agent in VM receives requests [from K8s control plane]
- One process called KATA [illegible]
- CoCo puts each pod in its own microVM (KATA microVM)
- [Everything about the VM is inside the confidential boundary]

---

## Components of a Confidential VM

**Virtual Machine — KATA agent:**
- Receives commands from [K8s/control plane]
- Executes [workloads inside the VM]
- CoCo [something] downloads the image

**3 things** [the VM does]:
1. Put pod in VM
2. Pull image [in VM, not on host]
3. [Deploy/run] image in VM

---

## Attestation and Keys

- [illegible — multiple lines about attestation, key sources, and data hub]
- attestation: checks whether the secure environment can be trusted before supplying secrets
- confidential data hub [?]
