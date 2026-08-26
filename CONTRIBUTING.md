# Contributing to AAEP

Thank you for contributing to Agent Application Engineering Platform（AAEP，智能体应用工程平台）.

## Workflow

For non-trivial changes:

1. Confirm the current repository state and open/identify an Issue.
2. Confirm ownership / Single Writer for the mutation slice.
3. Create a focused branch from the exact current base.
4. Make the smallest coherent change.
5. Run deterministic validation.
6. Open a PR with objective, scope, evidence, risks and completion conditions.
7. Complete review and CI.
8. Merge only after the applicable merge gate.
9. Revalidate the merged `main` exact head.

## Branch Naming

Prefer descriptive branches such as:

- `agent/<issue>-<slice>`
- `feat/<capability>`
- `fix/<problem>`
- `docs/<topic>`

## Public Data Rules

Do not include secrets, credentials, private data, private infrastructure topology or confidential operational evidence.

## Licensing Gate

AAEP's project-owned license is currently `DECISION_REQUIRED`. Substantial code contributions should not be merged under an assumed license until the project owner makes an explicit license decision. Third-party contributions and reused source must always preserve their original license/provenance obligations.
