#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
WORKFLOW = ROOT / ".github/workflows/ci.yml"
SELF = ROOT / "tools/validate_repository_foundation.py"

for path in (README, WORKFLOW, SELF):
    if not path.is_file():
        raise SystemExit(f"missing CI bootstrap file: {path.relative_to(ROOT)}")

readme = README.read_text(encoding="utf-8")
if "STATUS=BOOTSTRAP_ONLY" in readme:
    print("AAEP CI Bootstrap Validator: PASS")
    raise SystemExit(0)

required = [
    "README.zh.md",
    "PROJECT_CONTEXT.md",
    "AGENTS.md",
    "GOVERNANCE.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "LICENSE",
    "THIRD_PARTY_NOTICES.md",
    "state/CURRENT_STATE.json",
    "governance/UEGP_BINDING.md",
    "continuity/RECOVERY_POINTER.md",
    "upstream/source-registry.json",
    "upstream/adoption-policy.md",
    "docs/architecture/README.md",
    "docs/adr/0001-foundation-boundaries.md",
    "docs/roadmap/README.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/engineering-task.md",
    ".github/CODEOWNERS",
]
missing = [path for path in required if not (ROOT / path).is_file()]
if missing:
    raise SystemExit(f"missing required foundation files: {missing}")

state = json.loads((ROOT / "state/CURRENT_STATE.json").read_text(encoding="utf-8"))
if state.get("project_id") != "AAEP":
    raise SystemExit("project_id must be AAEP")
if state.get("primary_repository") != "Night-Etrenal/agent-application-engineering-platform":
    raise SystemExit("primary_repository mismatch")

onboarding = state.get("governance", {}).get("onboarding_status")
adoption = state.get("governance", {}).get("adoption_status")
managed = [
    ROOT / ".uceg/governance-profile.json",
    ROOT / ".uceg/governance-source.json",
    ROOT / ".uceg/projection-manifest.json",
]
if onboarding == "PENDING_CONSUMER_REGISTRATION":
    if any(path.exists() for path in managed):
        raise SystemExit("managed .uceg projection must remain absent before UEGP registration/onboarding")
    if adoption != "NOT_ADOPTED":
        raise SystemExit("pending onboarding cannot claim adoption")

license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
if state.get("license", {}).get("project_license_status") == "DECISION_REQUIRED":
    if "LICENSE_DECISION_REQUIRED=TRUE" not in license_text:
        raise SystemExit("pending license state must be explicit")

source = json.loads((ROOT / "upstream/source-registry.json").read_text(encoding="utf-8"))
repos = {item["repository"] for item in source.get("sources", [])}
for expected in {"deepseek-ai/deepseek-harness", "Night-Etrenal/Ai-deepseek-harness"}:
    if expected not in repos:
        raise SystemExit(f"missing upstream source: {expected}")

for marker in ["Agent Application Engineering Platform", "智能体应用工程平台", "CAPABILITY != AUTHORITY"]:
    if marker not in readme:
        raise SystemExit(f"README missing marker: {marker}")

print("AAEP Repository Foundation Validator: PASS")
