# Agent Application Engineering Platform

**AAEP — 智能体应用工程平台**

Agent Application Engineering Platform (AAEP) is a public engineering platform intended for open-source collaboration around high-value AI agent applications. It provides a governed structure for application discovery, architecture, implementation, validation, productization, and long-term evolution while using DeepSeek Harness only as a controlled upstream technology source.

AAEP keeps project architecture, governance binding, security boundaries, continuity, product ownership, and release decisions independent from the upstream project.

> **License status:** the repository is public, but the AAEP project-owned license grant is still pending an explicit project-owner decision. Public source availability does not itself create an open-source license grant.

## Current Project State

| Area | State | Evidence |
|---|---|---|
| Repository Foundation | `IN_PROGRESS` | AAEP Issue #1, branch `agent/aaep-repository-foundation-v1-r2` |
| CI Bootstrap | `ESTABLISHED` | `main@d6fac90ca647381f19e779860d100c1d65e43d0e` |
| UEGP Governance Onboarding | `PENDING_CONSUMER_REGISTRATION` | `Night-Etrenal/universal-computing-governance#33` |
| Upstream Source | `OBSERVED_NOT_ADOPTED` | `deepseek-ai/deepseek-harness@b150a551b8d465e31e418e1b2eaf5e79bbb7d28e` |
| Reference Fork | `REFERENCE_ONLY` | `Night-Etrenal/Ai-deepseek-harness@04ae6a52d4e52eae73e3414d620908d01b389143` |
| Runtime | `NOT_ESTABLISHED` | repository-foundation phase only |
| Live Execution | `NOT_AUTHORIZED` | no production/runtime authority |
| AAEP License | `DECISION_REQUIRED` | `LICENSE` |

`DECLARED != OBSERVED` · `PLAN != IMPLEMENTED` · `CI_PASS != COMPLETE` · `CAPABILITY != AUTHORITY`

## Architecture Direction

`DeepSeek Harness Upstream` → `Controlled Source / Compatibility` → `AEHP Shared Harness Foundation` → `AAEP Application Engineering` → `Independent High-Value Applications`

Upstream changes are classified before adoption:

`REUSE / ADAPT / REIMPLEMENT / DEFER / REJECT`

No automatic upstream merge or trust inheritance is allowed.

## Repository Governance

- Canonical engineering state: this repository after Repository Foundation acceptance.
- Project control: `Night-Etrenal/agent-application-engineering-platform#1`.
- Launch/discovery pointer: `Night-Etrenal/universal-project-launch-execution-center#7`.
- P01 execution contract: `Night-Etrenal/universal-project-launch-execution-center#8`.
- Canonical governance owner: `Night-Etrenal/universal-computing-governance` (UEGP).
- Governance onboarding request: `Night-Etrenal/universal-computing-governance#33`.
- Continuity provider: `Night-Etrenal/Engineering-Continuity`.

AAEP does not create a second universal engineering governance, authorization, security, or continuity system.

## Engineering Rules

- State Before Action（行动前确认状态）
- Verify Before Mutate（修改前先核验）
- Evidence First（证据优先）
- Root Cause Before Patch（补丁前先找根因）
- Smallest Coherent Change（最小完整变更）
- Recovery Instead of Restart（恢复而不是重做）
- Branch → PR → Review → CI → Merge → exact-head revalidation
- no direct `main` writes after the consumed empty-repository bootstrap exception
- no secrets, credentials, private customer data, or private production topology in this public repository

## Repository Map

- `PROJECT_CONTEXT.md` — project identity and authority/state pointers
- `AGENTS.md` — AI/Agent engineering contract
- `GOVERNANCE.md` — UEGP binding and onboarding state
- `SECURITY.md` — security boundary and reporting rules
- `CONTRIBUTING.md` — contribution workflow
- `state/` — machine-readable project state
- `governance/` — project-local governance pointers, never duplicate universal governance
- `continuity/` — Engineering-Continuity recovery pointer
- `upstream/` — upstream provenance and controlled-adoption policy
- `docs/architecture/` — architecture documentation
- `docs/adr/` — Architecture Decision Records
- `docs/roadmap/` — evidence-backed roadmap

---

# 中文说明

**Agent Application Engineering Platform（AAEP，智能体应用工程平台）** 是一个面向高价值 AI 智能体应用的公开工程平台，目标是形成从应用发现、架构设计、开发实现、验证验收、产品化到长期演进的专业工程体系。DeepSeek Harness 只作为受控上游技术来源，AAEP 保持自己的架构、治理绑定、安全边界、连续性、产品所有权和发布决策。

当前仓库已经公开，但 **AAEP 自身开源许可证尚未由项目所有者正式确定**；公开可见不等于已经授予开源使用、修改和分发权利。

当前阶段重点是建立完整 Repository Foundation（仓库基础）并完成 UEGP Governance Onboarding（治理接入）。在 UEGP #33 完成 Consumer Registration（消费者登记）和治理 Profile（配置）前，AAEP 不会伪造 `.uceg/` 已采用状态。

任何上游能力、UI、插件或源码进入 AAEP 前，都必须经过来源、许可证、安全、兼容性和工程价值审查，并明确选择 `REUSE / ADAPT / REIMPLEMENT / DEFER / REJECT`。
