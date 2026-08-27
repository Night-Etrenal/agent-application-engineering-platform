# Upstream Capability Map V1

## Purpose（目的）

This document maps the current DeepSeek Harness capability surface into AAEP adoption decisions. It is an engineering-control artifact, not an implementation claim.

本文件把当前 DeepSeek Harness 的能力面映射为 AAEP 的受控采用决策。它是工程控制资料，不代表相关能力已经实现或采用。

## Verified Source Snapshot（已验证来源快照）

- Official upstream（官方上游）: `deepseek-ai/deepseek-harness@b150a551b8d465e31e418e1b2eaf5e79bbb7d28e`
- Release generation（发布代际）: `dsh@0.1.1-rc.2`
- Upstream state（上游状态）: `DEVELOPER_PREVIEW`
- Reference fork（参考分叉）: `Night-Etrenal/Ai-deepseek-harness@04ae6a52d4e52eae73e3414d620908d01b389143`

Mutable source state must be revalidated before actual source-code or dependency adoption.

## Decision Vocabulary（决策词汇）

- `REUSE` — reuse a capability substantially as-is after license/security/compatibility validation.
- `ADAPT` — retain the engineering idea or seam but integrate it into AAEP-owned contracts and boundaries.
- `REIMPLEMENT` — build an AAEP-owned implementation using upstream only as reference/evidence.
- `DEFER` — intentionally postpone until maturity or a concrete product need justifies work.
- `REJECT` — explicitly exclude from AAEP scope.

A decision is not an implementation state and does not grant execution authority.

## Current Capability Direction（当前能力方向）

| Capability | Decision | AAEP intent |
|---|---|---|
| Cordis plugin composition | `ADAPT` | Preserve replaceable composition without inheriting product ownership. |
| Profiles / bundles | `ADAPT` | Use layered capability composition for multiple AAEP applications. |
| Session event log | `ADAPT` | Preserve reconstructable model-visible context and integrate with Engineering-Continuity. |
| Model adapter seam | `ADAPT` | Maintain model/provider independence. |
| Scoped tool execution | `ADAPT` | Bind tool capability to UEGP/project authority gates. |
| Sandbox / approval | `ADAPT` | Keep confinement and human-approval seams without expanding authority. |
| Filesystem / subprocess execution world | `ADAPT` | Keep execution backend replaceable and separately authorized. |
| Subagent provider seam | `ADAPT` | Reuse provider-neutral orchestration concepts; concrete providers are separately reviewed. |
| Web UI primitives | `ADAPT` | Reuse safe interaction/rendering ideas under AAEP-owned UX. |
| Headless profile | `ADAPT` | Support automation and validation without requiring a Web UI. |
| Experimental Agent Teams | `DEFER` | Do not make an experimental feature foundational without independent validation. |
| Product visual identity | `REIMPLEMENT` | AAEP owns visual language, information architecture and branding. |

The machine-readable authority is `upstream/capability-registry.v1.json`.

## UI Adoption Rule（UI 采用规则）

Upstream UI changes are engineering changes, not automatic cosmetic upgrades. Workspace ordering, error/retry presentation, reference interactions, client boot seams, rendering primitives and visual identity are reviewed independently.

`UPSTREAM_UI_CHANGE != AAEP_PRODUCT_UI_CHANGE`

The machine-readable UI decisions are in `upstream/ui-adoption-register.v1.json`.

## Safety Boundary（安全边界）

P02 V1 imports no upstream source code and installs no upstream dependency. It only records verified source pins, capability evidence and adoption decisions.

Before actual code reuse or dependency adoption, AAEP must separately verify:

1. current upstream exact head / tag;
2. license and third-party notices;
3. security and supply-chain implications;
4. compatibility with AAEP architecture and UEGP governance;
5. deterministic tests and acceptance evidence;
6. project authority for the concrete mutation.

`DISCOVERED != ADOPTED`
`PLAN != IMPLEMENTED`
`CAPABILITY != AUTHORITY`
