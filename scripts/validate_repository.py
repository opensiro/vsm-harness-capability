#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "CONTRACT.md",
    "PUBLIC-EVIDENCE.md",
    "EVIDENCE-REGISTRY.md",
    "BASELINE.md",
    "MIGRATION.md",
    "system-observations/README.md",
    "vsm-projections/README.md",
    "comparison-cells/README.md",
    "baselines/README.md",
    "frontier/README.md",
    "historical/README.md",
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

if errors:
    print("repository validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("repository validation passed")
