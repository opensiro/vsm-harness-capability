#!/usr/bin/env python3
from pathlib import Path
import csv
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "CONTRACT.md",
    "PUBLIC-EVIDENCE.md",
    "EVIDENCE-REGISTRY.md",
    "BASELINE.md",
    "MIGRATION.md",
    "LICENSE",
    "system-observations/README.md",
    "system-observations/registry.psv",
    "vsm-projections/README.md",
    "comparison-cells/README.md",
    "baselines/README.md",
    "frontier/README.md",
    "historical/README.md",
    "historical/SOURCE-REF",
]

errors = []
for rel in REQUIRED:
    if not (ROOT / rel).is_file():
        errors.append(f"missing required file: {rel}")

for rel in ("README.md", "CONTRACT.md", "PUBLIC-EVIDENCE.md", "BASELINE.md"):
    path = ROOT / rel
    if path.is_file() and "experimental" not in path.read_text(encoding="utf-8").lower():
        errors.append(f"{rel}: must explicitly state experimental status")

contract = (ROOT / "CONTRACT.md").read_text(encoding="utf-8") if (ROOT / "CONTRACT.md").is_file() else ""
for required_phrase in (
    "general functional capability",
    "domain-specific assessment",
    "vsm-harness-profile",
    "vsm-harness-index",
    "does not run or reproduce benchmark experiments",
):
    if required_phrase.lower() not in contract.lower():
        errors.append(f"CONTRACT.md: missing contract phrase: {required_phrase}")

if (ROOT / "domain-projections").exists():
    errors.append("domain-projections/: domain-specific assessment is outside this repository boundary")

for active_loopx in (ROOT / "vsm-projections").glob("**/loopx*"):
    errors.append(f"{active_loopx.relative_to(ROOT)}: controlled-execution LoopX artifacts must live under historical/")

registry_path = ROOT / "system-observations/registry.psv"
if registry_path.is_file():
    with registry_path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="|"))
    observation_ids = [row.get("observation_id", "") for row in rows]
    if len(observation_ids) != 53:
        errors.append(f"system-observations/registry.psv: expected migrated 53 observations, found {len(observation_ids)}")
    if len(set(observation_ids)) != len(observation_ids):
        errors.append("system-observations/registry.psv: duplicate observation_id values")

source_ref = ROOT / "historical/SOURCE-REF"
if source_ref.is_file():
    expected = "opensiro/vsm-harness-index@3446fe77e031878dc8ad4edfb857b608a7a6b26f"
    if source_ref.read_text(encoding="utf-8").strip() != expected:
        errors.append("historical/SOURCE-REF: predecessor revision drift")

if errors:
    print("repository validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("repository validation passed")
