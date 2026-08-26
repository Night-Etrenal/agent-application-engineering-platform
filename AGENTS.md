# AAEP Agent Engineering Contract

This file defines project-local execution rules for AI / Agent contributors. It does not replace UEGP governance.

## Source Priority

1. Current verified runtime/evidence when runtime exists.
2. Current Git / policy / ADR / runbook / repository governance.
3. Current UEGP canonical governance.
4. Project control / Issue / checkpoint / handoff.
5. AI memory / chat summary.
6. Raw chat.

## Mandatory Rules

- State Before Action（行动前确认状态）.
- Verify Before Mutate（修改前先核验）.
- Evidence First（证据优先）.
- Root Cause Before Patch（先找根因再补丁）.
- Smallest Coherent Change（最小完整变更）.
- Reuse Before Duplicate（优先复用）.
- Recovery Instead of Restart（恢复优先）.
- `UNKNOWN != DOWN`, `MISSING != ZERO`, `STALE != HEALTHY`.
- `DECLARED != OBSERVED`, `PLAN != IMPLEMENTED`, `CI_PASS != COMPLETE`.

## Git Contract

The one-time empty-repository bootstrap exception is consumed.

All normal mutations require:

`exact main/HEAD → active Issue → Single Writer → Branch → change → validation → PR → Review → CI → Merge gate → exact merged-head revalidation`

Do not write directly to `main` for normal engineering work.

## Public Repository Boundary

Never commit secrets, credentials, private customer data, personal data, private production topology, signing material, or private operational evidence.

## High-Risk Authority

Project work does not grant Production, Runtime Mutation, Secret/Credential, Network Mutation, Administrative, Signing, Package Publication, Financial, or Trading authority. Request the minimum required authorization only when the real gate is reached.

## Upstream Rule

DeepSeek Harness and any other upstream source must be treated as untrusted capability supply until provenance, license, security, compatibility, and validation checks complete.

`UPSTREAM_CHANGE != AUTOMATIC_ADOPTION`
