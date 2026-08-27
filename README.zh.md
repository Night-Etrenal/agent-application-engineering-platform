# Agent Application Engineering Platform

## AAEP — 智能体应用工程平台

AAEP 是一个面向高价值 AI 智能体应用的专业公开工程平台，用于组织应用发现、架构设计、开发实现、验证验收、产品化、发布协调与长期演进。

平台以 `deepseek-ai/deepseek-harness` 作为受控上游技术来源，但不把上游仓库、品牌、权限或信任直接继承为 AAEP 的规范状态。

## 当前状态

- Repository Foundation（仓库基础）：`IN_PROGRESS`
- UEGP Governance Onboarding（治理接入）：`PENDING_CONSUMER_REGISTRATION`
- UEGP 接入任务：`Night-Etrenal/universal-computing-governance#33`
- DeepSeek Harness 当前观测：`b150a551b8d465e31e418e1b2eaf5e79bbb7d28e`
- Reference Fork（参考分叉）：`04ae6a52d4e52eae73e3414d620908d01b389143`
- Runtime（运行时）：`NOT_ESTABLISHED`
- Live Execution（真实执行）：`NOT_AUTHORIZED`
- AAEP License（AAEP 自身许可证）：`DECISION_REQUIRED`

## 工程边界

AAEP 负责应用工程体系和共享工程能力协调；UEGP 继续负责通用工程治理；Engineering-Continuity 继续负责工程连续性；下游产品负责自己的业务目标与业务决策。

必须保持：

- `Governance != Business`
- `Capability != Authority`
- `Chat != Project State`
- `AI Memory != Project State`
- `Upstream Change != Automatic Adoption`
- `Public Repository != Public Secrets / Operations`

## Git 工作流

空仓库一次性 bootstrap 已消耗。后续仓库修改统一执行：

`Branch → PR → Review → CI → Merge → exact-head revalidation`

禁止把正常开发重新退化为直接修改 `main`。

## 上游采用

任何 DeepSeek Harness 能力进入 AAEP 前必须完成：

`DISCOVER → PROVENANCE → LICENSE → SECURITY → COMPATIBILITY → DECISION → VALIDATION`

最终只能进入：

`REUSE / ADAPT / REIMPLEMENT / DEFER / REJECT`

## 许可证状态

AAEP 目标是公开、可协作的工程平台，但 AAEP 自身许可证仍需要项目所有者明确决定。当前 `LICENSE` 文件不会伪造 MIT、Apache-2.0 或其他授权。第三方代码仍分别遵循其原始许可证。
