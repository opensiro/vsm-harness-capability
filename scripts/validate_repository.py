#!/usr/bin/env python3
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SOURCE_REF = "opensiro/vsm-harness-index@3446fe77e031878dc8ad4edfb857b608a7a6b26f"
EXPECTED_MIGRATED_OBSERVATION_COUNT = 53

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
    "comparison-cells/validate.py",
    "comparison-cells/s1-pawbench-v1-qwen3.6-35b-a3b.json",
    "baselines/README.md",
    "frontier/README.md",
    "historical/README.md",
    "historical/SOURCE-REF",
    "historical/MIGRATED-OBSERVATION-IDS.txt",
]

errors: list[str] = []

for rel in REQUIRED:
    if not (ROOT / rel).is_file():
        errors.append(f"missing required file: {rel}")

for rel in ("README.md", "CONTRACT.md", "PUBLIC-EVIDENCE.md", "BASELINE.md"):
    path = ROOT / rel
    if path.is_file() and "experimental" not in path.read_text(encoding="utf-8").lower():
        errors.append(f"{rel}: must explicitly state experimental status")

contract_path = ROOT / "CONTRACT.md"
contract = contract_path.read_text(encoding="utf-8") if contract_path.is_file() else ""
for phrase in (
    "general functional capability",
    "domain-specific assessment",
    "vsm-harness-profile",
    "vsm-harness-index",
    "does not run or reproduce benchmark experiments",
):
    if phrase.lower() not in contract.lower():
        errors.append(f"CONTRACT.md: missing contract phrase: {phrase}")

if (ROOT / "domain-projections").exists():
    errors.append("domain-projections/: domain-specific assessment is outside this repository boundary")

for active_loopx in (ROOT / "vsm-projections").glob("**/loopx*"):
    errors.append(
        f"{active_loopx.relative_to(ROOT)}: controlled-execution LoopX artifacts must live under historical/"
    )

active_files = [
    ROOT / "baselines" / "FUNCTION-BASELINES.md",
    ROOT / "baselines" / "PRIMARY-BASELINES.md",
    ROOT / "baselines" / "S1-BASELINE.md",
    ROOT / "frontier" / "EVIDENCE-FRONTIER.md",
]
forbidden = {
    "domain_projection": "active general layer must not own domain-specific projection state",
    "## Applied-domain projections": "active general layer must not publish domain-specific projection sections",
    "Opensiro-operated runs are optional": "active evidence contract forbids operated runs as evidence admission",
    "s2-system-benchmarks/": "old Index-local path leaked into active extracted view",
    "s3-system-benchmarks/": "old Index-local path leaked into active extracted view",
    "s3star-system-benchmarks/": "old Index-local path leaked into active extracted view",
    "s4-system-benchmarks/": "old Index-local path leaked into active extracted view",
    "s5-system-benchmarks/": "old Index-local path leaked into active extracted view",
}
for path in active_files:
    if not path.is_file():
        continue
    text = path.read_text(encoding="utf-8")
    for needle, why in forbidden.items():
        if needle in text:
            errors.append(f"{path.relative_to(ROOT)}: {why}: {needle}")

selection_path = ROOT / "baselines" / "primary-baselines.json"
if selection_path.is_file():
    data = json.loads(selection_path.read_text(encoding="utf-8"))
    s1 = data.get("functions", {}).get("S1", {})
    if "domains" in s1:
        errors.append(
            "baselines/primary-baselines.json: domain-specific derived state remains in active general layer"
        )
    if s1.get("scope") != "general":
        errors.append("baselines/primary-baselines.json: selected S1 baseline must declare scope=general")

registry = ROOT / "system-observations" / "registry.psv"
if registry.is_file():
    rows = [line for line in registry.read_text(encoding="utf-8").splitlines()[1:] if line.strip()]
    ids = [line.split("|", 1)[0] for line in rows]
    if len(set(ids)) != len(ids):
        errors.append(
            "system-observations/registry.psv: observation IDs must remain unique, "
            f"got {len(set(ids))}/{len(ids)} unique IDs"
        )

    migrated_manifest = ROOT / "historical" / "MIGRATED-OBSERVATION-IDS.txt"
    if migrated_manifest.is_file():
        migrated_ids = [
            line.strip()
            for line in migrated_manifest.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        ]
        if len(migrated_ids) != EXPECTED_MIGRATED_OBSERVATION_COUNT:
            errors.append(
                "historical/MIGRATED-OBSERVATION-IDS.txt: expected "
                f"{EXPECTED_MIGRATED_OBSERVATION_COUNT} migrated IDs, got {len(migrated_ids)}"
            )
        if len(set(migrated_ids)) != len(migrated_ids):
            errors.append("historical/MIGRATED-OBSERVATION-IDS.txt: migrated IDs must be unique")

        missing_migrated = sorted(set(migrated_ids) - set(ids))
        if missing_migrated:
            errors.append(
                "system-observations/registry.psv: migrated observation IDs disappeared from live corpus: "
                + ", ".join(missing_migrated)
            )

source_ref_path = ROOT / "historical" / "SOURCE-REF"
if source_ref_path.is_file():
    source_ref = source_ref_path.read_text(encoding="utf-8").strip()
    if source_ref != EXPECTED_SOURCE_REF:
        errors.append(
            f"historical/SOURCE-REF: expected {EXPECTED_SOURCE_REF}, found {source_ref!r}"
        )

tracked = subprocess.run(["git", "ls-files"], cwd=ROOT, text=True, capture_output=True)
if tracked.returncode:
    errors.append(f"git ls-files failed: {tracked.stderr}")
else:
    generated_python = [
        path
        for path in tracked.stdout.splitlines()
        if "/__pycache__/" in f"/{path}" or path.endswith((".pyc", ".pyo"))
    ]
    if generated_python:
        errors.append("generated Python cache must not be tracked: " + ", ".join(generated_python))

for cmd in (
    [sys.executable, str(ROOT / "system-observations" / "validate.py")],
    [sys.executable, str(ROOT / "system-observations" / "render_registry.py"), "--check"],
    [sys.executable, str(ROOT / "comparison-cells" / "validate.py")],
):
    if Path(cmd[1]).is_file():
        result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
        if result.returncode:
            errors.append(f"{' '.join(cmd)} failed:\n{result.stdout}{result.stderr}")

if errors:
    print("repository validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("repository validation passed")
