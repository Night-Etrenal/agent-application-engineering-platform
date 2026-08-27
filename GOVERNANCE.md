# AAEP Governance Binding

AAEP consumes UEGP — Universal Engineering Governance Platform（通用工程治理平台） as its canonical engineering-governance source.

`CANONICAL_GOVERNANCE=Night-Etrenal/universal-computing-governance`
`UEGP_ONBOARDING_ISSUE=Night-Etrenal/universal-computing-governance#33`
`FOUNDATION_START_UEGP_HEAD=08a57a7dea45e8388d92538f0b21a25207a1caed`
`CURRENT_OBSERVED_UEGP_HEAD=1f0b04bca164178b93584870f79d8d053f8f0639`

## Current State

`CONSUMER_REGISTRATION_STATUS=COMPLETE`
`GOVERNANCE_PROFILE_STATUS=COMPLETE`
`GOVERNANCE_ONBOARDING_STATUS=MANUAL_REVIEW_REQUIRED`
`GOVERNANCE_ADOPTION_STATUS=NOT_ADOPTED`

UEGP PR #34 registered AAEP as a unique Consumer Project（消费项目）, added its canonical Governance Profile（治理配置）, and established a read-only repository canary snapshot with exact-head and merged-main Governance CI evidence.

The remaining Initial Consumer Onboarding V1 transition is a create-only projection of exactly:

- `.uceg/governance-profile.json`
- `.uceg/governance-source.json`
- `.uceg/projection-manifest.json`

The candidate is `ONBOARDING_REQUIRED / COMPATIBLE / MEDIUM / MANUAL_REVIEW_REQUIRED`. No managed file may be created before explicit Manual Review approval plus fresh exact-head/write/tool preflight.

AAEP is therefore still not entitled to claim UEGP adoption.

## Separation of Responsibility

UEGP owns universal governance. AAEP owns application-engineering/project decisions. Engineering-Continuity owns continuity mechanisms.

AAEP must not create a second Engineering Constitution, Action Class model, authorization model, universal security governance, or independent continuity framework.

`ONBOARDING_REQUIRED != ADOPTED`
`COMPATIBLE != ADOPTION`
`MANUAL_REVIEW != MERGE_AUTHORITY`
`CAPABILITY != AUTHORITY`
`GOVERNANCE_CHANGE != AUTOMATIC_ADOPTION`
