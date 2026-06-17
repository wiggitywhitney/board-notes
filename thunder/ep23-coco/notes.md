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

---

## ISOLATION

The secure place can be called:
- guest
- enclave
- realm
- Trusted Execution Env (TEE)

Attestation supplies evidence that the secure place is secure

- For example, secrets are only supplied to guest after guest is attested
- KBS (key broker service) in a trusted place

Architecture diagram:

VM:
- imageRS
- CDH
- AA
- KATA AGENT
- WORKLOAD POD

K8s:
- KATA SHIM
- KUBELET

CC - ENABLED HARDWARE

3 things:
① put 1 pod in VM
② pull image inside VM
③ decrypt image/get secrets

---

## Components of Confidential Containers

Virtual machine(s)

- KATA shim on the host
  - receives container requests
  - makes a VM
  - forwards container request into VM

- KATA Agent in VM
  - receives container requests
  - does whatever ex CRUD

- one pod in the VM

- CoCo snapshotter talks to imageRS on the host
- imageRS downloads the image inside VM

- KBS = key broker service - runs in another location - receives evidence from CDH/AA, verifies it, releases keys to unpack image or whatever secrets

- Confidential data hub (CDH) & Attestation Agent (AA) run on VM
  work together to get hardware evidence from the guest, then
  sets up a secure connection w KBS
  → makes the attestation
