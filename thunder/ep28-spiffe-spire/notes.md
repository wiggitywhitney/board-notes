## Before SPIFFE Workloads Communicated

- Service tokens
  - need to be stored
  - sometimes hard coded
  - hackers can extract
- mTLS
  - certificates have to be managed/rotated

Tokens used to verify.

Certificates used to verify.

---

## SPIFFE Definition

**<u>S</u>**ecure **<u>P</u>**roduction **<u>I</u>**dentity **<u>F</u>**ramework **<u>F</u>**or **<u>E</u>**veryone (SPIFFE) is a standard for securing and identifying workloads in a production environment. It's a secure and automated way to manage identity.

---

## WHO + WHAT = POLICY

```mermaid
graph TD
    Who[WHO] --> Identity[IDENTITY] --> Spiffe[SPIFFE]
    What[WHAT] --> Action[ACTION] --> Frameworks["Typically managed by policy frameworks (like OPA)"]
    Spiffe --> Policy[POLICY]
    Frameworks --> Policy
```

Identity is best added to processes.

```mermaid
graph TB
    subgraph Machine["Machine (ex: VM)"]
        subgraph Host["Host (ex: Kubernetes)"]
            subgraph Pod1["Pod"]
                Proc1["process"]
            end
            subgraph Pod2["Pod"]
                Proc2["process"]
            end
            subgraph Pod3["Pod"]
                Proc3["process"]
            end
        end
    end
```

Identity can be added to any layer, but...
- Machine layer doesn't play well with other machines
- Host layer deals with IP addresses, but those can change

BEST TO ADD IDENTITY TO PROCESSES (WORKLOADS)

---

## SPIFFE Is Designed to Solve These Problems

- Standard for formatting an ID = SPIFFE ID (it looks like a URL)
- SPIFFE Verify = proves that a workload is what it claims to be

---

## SVID

**<u>S</u>**PIFFE **<u>V</u>**erifiable **<u>I</u>**dentity **<u>D</u>**ocument

- A bundle of PKI certs/keys
- SVIDs are short-lived
- If two workloads each have their own SVIDs, they can establish a secure connection between each other

---

## Workload API

- Workloads attest themselves in order to gain access to the Workload API
- Workload API gives SVIDs to workloads
- User configures how attestations are verified
- Workload API can verify the attestation by querying other stuff in the environment
  - Examples: might query kubelet, might query OS, might check SHA hash, plug-ins used here
- Once this process is complete, Workload API issues SVID
- Workload API rotates, revokes, distributes, and compartmentalizes the SVID

---

## Benefits of SPIFFE

- Well supported
- Neither your platform nor your workloads need certificates/tokens
  - There is no spoon
- SPIFFE manages a potentially complex cross-platform/cross-cloud identity layer
- No more need for secrets management
- Scales well
- Short lived SVIDs are more secure than long-lived X509 certs

---

## SPIRE Definition

**<u>S</u>****<u>P</u>****<u>I</u>**FFE **<u>R</u>**untime **<u>E</u>**nvironment (SPIRE) is a reference implementation.

- SPIRE Server talks to SPIRE Agent
- Each SPIRE Agent has its own Workload API
- SPIRE Server - typically a stateful set, this software stores and distributes SVIDs
- SPIRE Agents - typically a daemon set, receives SVIDs from server and exposes Workload API, and does the work of verifying workloads and giving them SVIDs
