# Confidential Containers (CoCo) — Board Notes

## Before Confidential Containers (CoCo)

- Confidential Computing (CC) was very new
- CC was hard to integrate in any environment

CoCo solves the problem of integrating CC into K8s = standardization
for adding CC at the Pod level
←don't trust the K8s control plane
Confidential Computing is a new technology that has big momentum
- paradigm shift
- needs different hardware

KATA encapsulates VMs in containers

## Confidential Computing protects data while it is in use

- data at rest is protected
- data in motion is protected
- data in use is vulnerable
  - it can be seen by the physical machine owner, for example

WHOMEVER OWNS THE KERNEL SEES ALL

---

## What is Confidential Computing?

- has a different trust model
- it is hardware
- In practice, usually implemented as VMs w extra layers of security - cannot be breached by host

---

## The experience of using CoCos

ASSUMPTION: NEED THE RIGHT HARDWARE
- Run K8s operator to install CoCo (easy to use!)
- add a runtime class to your workload

---

## The Confidential Computing Trust Model

DONT TRUST THE HOST

- defined by what goes inside vs outside the enclave  } ISOLATION
- CoCo puts each pod in its own VM (K8s control plane is not in there)
  - uses a project called KATA

- The owner of the VM should know what is running     } ATTESTATION
  everything about the VM itself
