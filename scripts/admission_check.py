#!/usr/bin/env python3
"""Check one live public-evidence record against the local admission contract."""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "system-observations"
REGISTRY = RAW_DIR / "registry.psv"
PROJECTIONS = ROOT / "vsm-projections"
CELLS = ROOT / "comparison-cells"


class AdmissionError(ValueError):
    pass


def fail(message: str) -> None:
    raise AdmissionError(message)


def normalize_record_path(value: str) -> Path:
    candidate = Path(value)
    if not candidate.is_absolute():
        candidate = ROOT / candidate
    try:
        resolved = candidate.resolve(strict=True)
    except FileNotFoundError as exc:
        fail(f"record does not exist: {value}")
        raise AssertionError from exc

    if resolved.parent != RAW_DIR.resolve():
        fail("record must be a direct child of system-observations/")
    if resolved.suffix != ".json":
        fail("record must be a .json file")
    return resolved


def load_record(path: Path) -> tuple[dict, list[str]]:
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{path.name}: invalid JSON: {exc}")
        raise AssertionError from exc

    if not isinstance(record, dict):
        fail(f"{path.name}: raw record must be a JSON object")

    observations = record.get("observations")
    if not isinstance(observations, list) or not observations:
        fail(f"{path.name}: observations must be a non-empty list")

    ids: list[str] = []
    for index, observation in enumerate(observations):
        if not isinstance(observation, dict):
            fail(f"{path.name}: observations[{index}] must be an object")
        observation_id = observation.get("observation_id")
        if not isinstance(observation_id, str) or not observation_id:
            fail(f"{path.name}: observations[{index}] lacks observation_id")
        ids.append(observation_id)

    if len(set(ids)) != len(ids):
        fail(f"{path.name}: observation IDs must be unique within the record")

    return record, ids


def run_check(command: list[str], label: str) -> None:
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    if result.returncode:
        detail = (result.stdout + result.stderr).strip()
        fail(f"{label} failed" + (f":\n{detail}" if detail else ""))


def registry_rows() -> dict[str, dict[str, str]]:
    if not REGISTRY.is_file():
        fail("system-observations/registry.psv is missing")
    with REGISTRY.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="|"))
    result: dict[str, dict[str, str]] = {}
    for row in rows:
        observation_id = (row.get("observation_id") or "").strip()
        if observation_id:
            result[observation_id] = row
    return result


def projection_refs(observation_id: str) -> list[str]:
    refs: list[str] = []
    if not PROJECTIONS.is_dir():
        return refs
    for path in sorted(PROJECTIONS.rglob("*")):
        if not path.is_file() or path.suffix not in {".json", ".jsonl"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if observation_id in text:
            refs.append(path.relative_to(ROOT).as_posix())
    return refs


def comparison_cell_refs(observation_id: str) -> list[str]:
    refs: list[str] = []
    if not CELLS.is_dir():
        return refs
    for path in sorted(CELLS.glob("*.json")):
        try:
            cell = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        ids = cell.get("observation_ids") if isinstance(cell, dict) else None
        if isinstance(ids, list) and observation_id in ids:
            refs.append(path.relative_to(ROOT).as_posix())
    return refs


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate one system-observations JSON record through the live admission path."
    )
    parser.add_argument("record", help="path to one system-observations/*.json record")
    args = parser.parse_args()

    try:
        record_path = normalize_record_path(args.record)
        _, observation_ids = load_record(record_path)

        run_check(
            [sys.executable, str(RAW_DIR / "validate.py")],
            "neutral system-observation validation",
        )
        run_check(
            [sys.executable, str(RAW_DIR / "render_registry.py"), "--check"],
            "generated registry consistency check",
        )
        run_check(
            [sys.executable, str(CELLS / "validate.py")],
            "comparison-cell validation",
        )

        rows = registry_rows()
        for observation_id in observation_ids:
            row = rows.get(observation_id)
            if row is None:
                fail(f"{observation_id}: missing from system-observations/registry.psv")
            if row.get("record_ref") != record_path.name:
                fail(
                    f"{observation_id}: registry record_ref is {row.get('record_ref')!r}, "
                    f"expected {record_path.name!r}"
                )

    except AdmissionError as exc:
        raise SystemExit(f"error: {exc}") from exc

    print("ok: live public-evidence admission check passed")
    print(f"record: system-observations/{record_path.name}")
    print(f"observation ids: {len(observation_ids)}")
    print("registry: neutral corpus valid and generated views are current")
    print("downstream derived references (informational; not required for raw admission):")
    for observation_id in observation_ids:
        projections = projection_refs(observation_id)
        cells = comparison_cell_refs(observation_id)
        projection_text = ", ".join(projections) if projections else "none"
        cell_text = ", ".join(cells) if cells else "none"
        print(f"- {observation_id}")
        print(f"  projections: {projection_text}")
        print(f"  comparison cells: {cell_text}")
    print("derived review: VSM projection, baseline and frontier updates remain separate review steps")


if __name__ == "__main__":
    main()
