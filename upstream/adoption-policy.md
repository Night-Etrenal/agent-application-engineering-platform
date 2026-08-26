# Controlled Upstream Adoption Policy

AAEP never treats an upstream release, commit, UI change, plugin, dependency, or reference-fork delta as automatically adopted.

Required flow:

`DISCOVER → PIN SOURCE → PROVENANCE REVIEW → LICENSE REVIEW → SECURITY REVIEW → CAPABILITY MAPPING → COMPATIBILITY → DECISION → TEST → ACCEPTANCE EVIDENCE`

Decision values:

- `REUSE` — reuse with provenance/license obligations preserved.
- `ADAPT` — reuse with AAEP-specific adaptation.
- `REIMPLEMENT` — reproduce capability independently when justified and legally/technically appropriate.
- `DEFER` — postpone pending evidence or need.
- `REJECT` — explicitly reject adoption.

`UPSTREAM_CHANGE != AUTOMATIC_ADOPTION`
`FORK != PRODUCT_CANONICAL_STATE`
