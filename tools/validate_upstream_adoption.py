#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_REGISTRY = ROOT / "upstream/source-registry.json"
CAPABILITY_REGISTRY = ROOT / "upstream/capability-registry.v1.json"
UI_REGISTER = ROOT / "upstream/ui-adoption-register.v1.json"

SHA40 = re.compile(r"^[0-9a-f]{40}$")
ALLOWED_DECISIONS = {"REUSE", "ADAPT", "REIMPLEMENT", "DEFER", "REJECT"}


def load(path: Path) -> dict:
    if not path.is_file():
        raise SystemExit(f"missing upstream control file: {path.relative_to(ROOT)}")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid JSON in {path.relative_to(ROOT)}: {exc}") from exc
    if not isinstance(value, dict):
        raise SystemExit(f"root must be an object: {path.relative_to(ROOT)}")
    return value


def require_sha(value: object, field: str) -> str:
    if not isinstance(value, str) or not SHA40.fullmatch(value):
        raise SystemExit(f"{field} must be an exact 40-character lowercase SHA")
    return value


source = load(SOURCE_REGISTRY)
capabilities = load(CAPABILITY_REGISTRY)
ui = load(UI_REGISTER)

if source.get("mutable_source_state_revalidation_required") is not True:
    raise SystemExit("source registry must require mutable-source revalidation")

sources = source.get("sources")
if not isinstance(sources, list) or not sources:
    raise SystemExit("source registry must contain sources")

by_role = {}
by_repo = {}
for item in sources:
    if not isinstance(item, dict):
        raise SystemExit("source entries must be objects")
    role = item.get("role")
    repo = item.get("repository")
    if not isinstance(role, str) or not isinstance(repo, str):
        raise SystemExit("source role/repository must be strings")
    if role in by_role or repo in by_repo:
        raise SystemExit("source role/repository must be unique")
    require_sha(item.get("observed_head"), f"source[{role}].observed_head")
    if item.get("automatic_adoption") is not False:
        raise SystemExit(f"source[{role}] must disable automatic adoption")
    by_role[role] = item
    by_repo[repo] = item

for required_role in ("OFFICIAL_UPSTREAM", "REFERENCE_FORK"):
    if required_role not in by_role:
        raise SystemExit(f"missing source role: {required_role}")

official = by_role["OFFICIAL_UPSTREAM"]
reference = by_role["REFERENCE_FORK"]
if official.get("repository") != "deepseek-ai/deepseek-harness":
    raise SystemExit("unexpected official upstream repository")
if reference.get("repository") != "Night-Etrenal/Ai-deepseek-harness":
    raise SystemExit("unexpected reference fork repository")

snapshot = capabilities.get("source_snapshot")
if not isinstance(snapshot, dict):
    raise SystemExit("capability registry missing source_snapshot")
if snapshot.get("official_repository") != official["repository"]:
    raise SystemExit("capability snapshot official repository mismatch")
if snapshot.get("official_head") != official["observed_head"]:
    raise SystemExit("capability snapshot official head mismatch")
if snapshot.get("reference_fork") != reference["repository"]:
    raise SystemExit("capability snapshot reference fork mismatch")
if snapshot.get("reference_fork_head") != reference["observed_head"]:
    raise SystemExit("capability snapshot reference fork head mismatch")
if snapshot.get("upstream_stage") != "DEVELOPER_PREVIEW":
    raise SystemExit("P02 V1 expects upstream stage DEVELOPER_PREVIEW")
if snapshot.get("compatibility_breaking_changes_expected") is not True:
    raise SystemExit("developer-preview compatibility risk must be explicit")
if capabilities.get("adoption_scope") != "CONTROL_METADATA_ONLY_NO_SOURCE_IMPORT":
    raise SystemExit("P02 V1 must remain metadata-only")

records = capabilities.get("capabilities")
if not isinstance(records, list) or not records:
    raise SystemExit("capability registry must contain records")

seen = set()
decisions = {}
for record in records:
    if not isinstance(record, dict):
        raise SystemExit("capability records must be objects")
    capability_id = record.get("id")
    if not isinstance(capability_id, str) or not capability_id:
        raise SystemExit("capability id must be non-empty")
    if capability_id in seen:
        raise SystemExit(f"duplicate capability id: {capability_id}")
    seen.add(capability_id)
    decision = record.get("decision")
    if decision not in ALLOWED_DECISIONS:
        raise SystemExit(f"invalid decision for {capability_id}: {decision}")
    decisions[capability_id] = decision
    if record.get("implementation_status") != "NOT_STARTED":
        raise SystemExit(f"P02 metadata-only record cannot claim implementation: {capability_id}")
    if not isinstance(record.get("rationale"), str) or not record["rationale"].strip():
        raise SystemExit(f"missing rationale: {capability_id}")
    evidence = record.get("evidence")
    if not isinstance(evidence, list) or not evidence:
        raise SystemExit(f"missing evidence: {capability_id}")
    for item in evidence:
        if not isinstance(item, dict):
            raise SystemExit(f"invalid evidence object: {capability_id}")
        repo = item.get("repository")
        if repo not in by_repo:
            raise SystemExit(f"unregistered evidence repository for {capability_id}: {repo}")
        require_sha(item.get("ref"), f"evidence[{capability_id}].ref")
        if not isinstance(item.get("path"), str) or not item["path"].strip():
            raise SystemExit(f"evidence path required: {capability_id}")

if decisions.get("experimental-agent-teams") != "DEFER":
    raise SystemExit("experimental Agent Teams must remain DEFER in P02 V1")
if decisions.get("product-visual-identity") != "REIMPLEMENT":
    raise SystemExit("AAEP product visual identity must remain independently reimplemented")

if ui.get("official_repository") != official["repository"]:
    raise SystemExit("UI register official repository mismatch")
if ui.get("observed_under_head") != official["observed_head"]:
    raise SystemExit("UI register source head mismatch")
if ui.get("adoption_scope") != "CONTROL_METADATA_ONLY_NO_SOURCE_IMPORT":
    raise SystemExit("UI register must remain metadata-only")

items = ui.get("items")
if not isinstance(items, list) or not items:
    raise SystemExit("UI register must contain items")
ui_seen = set()
for item in items:
    if not isinstance(item, dict):
        raise SystemExit("UI items must be objects")
    item_id = item.get("id")
    if not isinstance(item_id, str) or not item_id:
        raise SystemExit("UI item id must be non-empty")
    if item_id in ui_seen:
        raise SystemExit(f"duplicate UI item id: {item_id}")
    ui_seen.add(item_id)
    require_sha(item.get("source_commit"), f"ui[{item_id}].source_commit")
    if item.get("decision") not in ALLOWED_DECISIONS:
        raise SystemExit(f"invalid UI decision: {item_id}")
    if item.get("implementation_status") != "NOT_STARTED":
        raise SystemExit(f"P02 UI metadata cannot claim implementation: {item_id}")
    if not isinstance(item.get("rationale"), str) or not item["rationale"].strip():
        raise SystemExit(f"missing UI rationale: {item_id}")

visual = next((item for item in items if item.get("id") == "visual-language-and-branding"), None)
if visual is None or visual.get("decision") != "REIMPLEMENT":
    raise SystemExit("UI register must preserve AAEP-owned visual identity")

print("AAEP Upstream Adoption Validator: PASS")
