# UEGP Binding

`PROJECT_ID=AAEP`
`CANONICAL_GOVERNANCE_REPOSITORY=Night-Etrenal/universal-computing-governance`
`CONSUMER_ONBOARDING_ISSUE=Night-Etrenal/universal-computing-governance#33`
`UEGP_CURRENT_OBSERVED_HEAD=1f0b04bca164178b93584870f79d8d053f8f0639`
`CONSUMER_REGISTRATION_STATUS=COMPLETE`
`GOVERNANCE_PROFILE_STATUS=COMPLETE`
`ONBOARDING_STATUS=MANUAL_REVIEW_REQUIRED`
`ADOPTION_STATUS=NOT_ADOPTED`

AAEP consumes UEGP governance by reference and projection. Project-local documents explain how AAEP applies governance; they do not replace UEGP canonical policy.

UEGP PR #34 established AAEP as a unique Consumer Project（消费项目）, added `profiles/aaep-governance-profile.v1.json`, added an AAEP repository canary snapshot, and passed exact-head plus merged-main Governance CI.

The current UEGP Initial Consumer Onboarding V1 classifies the still-absent projection as:

`projection_state=ONBOARDING_REQUIRED`
`compatibility=COMPATIBLE`
`risk_classification=MEDIUM`
`candidate_state=MANUAL_REVIEW_REQUIRED`

The reviewed candidate may create only:

- `.uceg/governance-profile.json`
- `.uceg/governance-source.json`
- `.uceg/projection-manifest.json`

All three are `CREATE` operations with `expected_old_sha256=null`. No project-owned `AGENTS.md`, `SECURITY.md`, release, runtime, domain, contribution or upstream assets may be overwritten by onboarding.

Until explicit Manual Review approval is recorded and fresh exact-head/write/tool preflight passes, these managed `.uceg/` artifacts must remain absent.

`ONBOARDING_REQUIRED != ADOPTED`
`MANUAL_REVIEW != MERGE_AUTHORITY`
`REGISTRATION != REPOSITORY_WRITE_AUTHORITY`
`CAPABILITY != AUTHORITY`
