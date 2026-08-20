## Before SPIFFE...

workloads communicated:

w/ service tokens
- need to be stored
- sometimes hard coded
- hackers can extract

via mTLS
- certificates have to be managed/rotated

tokens used to verify / certificates used to verify

Secure Production Identity Framework For Everyone (SPIFFE) is a standard for securing + identifying workloads in a production environment (secure + automated way to manage identity)

SPIFFE Runtime Environment (SPIRE) is a reference implementation

SPIRE SERVER talks to SPIRE AGENT

EACH SPIRE AGENT has its own WORKLOAD API

---

## WHO + WHAT = POLICY

IDENTITY → ACTION → (typically managed by policy frameworks (like OPA))

SPIFFE

Identity best added to processes

[diagram: three boxes labeled PODS connecting down to a HOST layer (ex K8s), connecting down to a Machine layer (ex VM)]

Identity can be added to any layer, but...

- Machine layer doesn't play well w/ other machines
- Host layer deals w/ IP Addresses, but those can change

BEST TO ADD IDENTITY TO PROCESSES (WORKLOADS)

---

## SPIFFE is designed to solve these problems:

- standard for formatting an ID = SPIFFE ID
  It looks like a URL

- SPIFFE Verify = proves that a workload is what it claims to be
  SVID PKI bundle of certs/keys

- WORKLOAD API gives SVIDS to workloads

  First, WORKLOADS ATTEST themselves in order to gain access to the WORKLOAD API

  (USER configures how attestations are verified)

- WORKLOAD API can verify the attestation by querying other stuff in the env
  ex - might query kubelet
  - might query OS
  - might check SHA hash
  - plug-ins used here

SVID = SPIFF VERIFIABLE IDENTY DOCUMENT

---

## Once this process is complete,

WORKLOAD API issues SVID

Also rotating, revoking, distributing, compartmentalizing SVID

SVIDS ARE short lived

IF 2 workloads each have their own SVIDS they can establish a secure connection between each other

## Benefits of SPIFFE

- well supported
- Neither your platform nor your workloads need certificates/tokens
  THERE IS NO SPOON
- SPIFFE manages potentially complex cross-platform/cross-cloud identity layer
- No more need for secrets management
- scales well
- short lived SVIDs are more secure than long-lived X509 certs

SPIRE SERVER - typically a stateful set, this software stores + distributes SVIDs

SPIRE AGENTS - typically a daemon set, receives SVIDs from server and exposes WORKLOAD API + does the work of verifying workloads + giving them SVIDs
