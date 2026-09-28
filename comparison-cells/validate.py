#!/usr/bin/env python3
"""Validate machine-readable general-capability comparison cells."""

from __future__ import annotations

import csv
import io
import json
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
REGISTRY = ROOT / "system-observations" / "registry.psv"

FUNCTION_SLUGS = {
    "S1": "s1",
    "S2": "s2",
    "S3": "s3",
    "S3*": "s3star",
    "S4": "s4",
    "S5": "s5",
}
FORBIDDEN_METRIC_KEYS = {
    "score",
    "scores",
    "result",
    "results",
    "raw_score",
    "raw_result",
    "metric_value",
    "metric_values",
    "rank",
    "ranking",
}


class CellError(ValueError):
    pass


def _public_https(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def _registry_ids() -> set[str]:
    if not REGISTRY.is_file():
        raise CellError("system-observations/registry.psv is missing")
    rows = list(csv.DictReader(io.StringIO(REGISTRY.read_text(encoding="utf-8")), delimiter="|"))
    ids = {row.get("observation_id", "").strip() for row in rows}
    ids.discard("")
    if not ids:
        raise CellError("system-observations/registry.psv contains no observation IDs")
    return ids


def _projection_path(function: str) -> Path:
    return ROOT / "vsm-projections" / FUNCTION_SLUGS[function] / "observations.jsonl"


def _projection_ids(function: str) -> set[str]:
    path = _projection_path(function)
    if not path.is_file():
        raise CellError(f"{path.relative_to(ROOT)} is missing")

    ids: set[str] = set()
    for line_number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            row = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise CellError(f"{path.relative_to(ROOT)}:{line_number}: invalid JSON: {exc}") from exc
        if row.get("function") != function:
            raise CellError(
                f"{path.relative_to(ROOT)}:{line_number}: expected function={function!r}, got {row.get('function')!r}"
            )
        record_id = row.get("record_id")
        if not isinstance(record_id, str) or not record_id:
            raise CellError(f"{path.relative_to(ROOT)}:{line_number}: missing record_id")
        ids.add(record_id)
    return ids


def _reject_metric_payloads(value: object, path: str = "$") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            if key.lower() in FORBIDDEN_METRIC_KEYS:
                raise CellError(
                    f"{child_path}: comparison cells reference raw observations; metric/result payloads stay in system-observations/"
                )
            _reject_metric_payloads(child, child_path)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _reject_metric_payloads(child, f"{path}[{index}]")


def _validate_baseline_link(path: Path, cell: dict) -> None:
    ref = cell.get("selected_baseline_ref")
    if not isinstance(ref, str) or not ref.startswith("baselines/") or not ref.endswith(".md"):
        raise CellError(f"{path.name}: selected_baseline_ref must point to a baselines/*.md view")
    baseline = ROOT / ref
    if not baseline.is_file():
        raise CellError(f"{path.name}: selected baseline view is missing: {ref}")
    if path.name not in baseline.read_text(encoding="utf-8"):
        raise CellError(
            f"{path.name}: {ref} must link back to the machine-readable comparison cell"
        )


def _load_cells() -> dict[str, dict]:
    registry_ids = _registry_ids()
    cells: dict[str, dict] = {}

    for path in sorted(HERE.glob("*.json")):
        try:
            cell = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise CellError(f"{path.name}: invalid JSON: {exc}") from exc
        if not isinstance(cell, dict):
            raise CellError(f"{path.name}: cell must be a JSON object")

        _reject_metric_payloads(cell)

        if not isinstance(cell.get("schema_version"), int) or cell["schema_version"] < 1:
            raise CellError(f"{path.name}: schema_version must be an integer >= 1")
        if "experimental" not in str(cell.get("status", "")).lower():
            raise CellError(f"{path.name}: status must explicitly remain experimental")

        cell_id = cell.get("cell_id")
        if not isinstance(cell_id, str) or not cell_id:
            raise CellError(f"{path.name}: cell_id must be a non-empty string")
        if cell_id != path.stem:
            raise CellError(f"{path.name}: cell_id must match filename stem")
        if cell_id in cells:
            raise CellError(f"duplicate cell_id: {cell_id}")

        function = cell.get("function")
        if function not in FUNCTION_SLUGS:
            raise CellError(f"{path.name}: function must be one of {sorted(FUNCTION_SLUGS)}")
        if cell.get("scope") != "general":
            raise CellError(f"{path.name}: comparison-cell scope must be general")
        if cell.get("raw_metric_owner") != "system-observations":
            raise CellError(f"{path.name}: raw_metric_owner must be system-observations")

        expected_projection_ref = str(_projection_path(function).relative_to(ROOT)).replace("\\", "/")
        if cell.get("projection_ref") != expected_projection_ref:
            raise CellError(
                f"{path.name}: projection_ref must be {expected_projection_ref!r}"
            )

        evidence_family = cell.get("evidence_family")
        if not isinstance(evidence_family, dict):
            raise CellError(f"{path.name}: evidence_family must be an object")
        if not _public_https(evidence_family.get("primary_source")):
            raise CellError(f"{path.name}: evidence_family.primary_source must be public HTTPS")

        observation_ids = cell.get("observation_ids")
        if not isinstance(observation_ids, list) or len(observation_ids) < 2:
            raise CellError(f"{path.name}: observation_ids must contain at least two IDs")
        if any(not isinstance(item, str) or not item for item in observation_ids):
            raise CellError(f"{path.name}: observation_ids entries must be non-empty strings")
        if len(set(observation_ids)) != len(observation_ids):
            raise CellError(f"{path.name}: observation_ids must be unique within the cell")

        missing_raw = sorted(set(observation_ids) - registry_ids)
        if missing_raw:
            raise CellError(f"{path.name}: unknown raw observation IDs: {', '.join(missing_raw)}")

        projection_ids = _projection_ids(function)
        missing_projection = sorted(set(observation_ids) - projection_ids)
        if missing_projection:
            raise CellError(
                f"{path.name}: observation IDs missing from {function} projection: {', '.join(missing_projection)}"
            )

        comparability = cell.get("comparability")
        if not isinstance(comparability, dict) or not comparability:
            raise CellError(f"{path.name}: comparability must be a non-empty object")
        for dimension, statement in comparability.items():
            if not isinstance(statement, dict) or not isinstance(statement.get("status"), str):
                raise CellError(
                    f"{path.name}: comparability.{dimension} must explicitly declare status"
                )

        _validate_baseline_link(path, cell)
        cells[cell_id] = cell

    if not cells:
        raise CellError("no machine-readable comparison cells found")
    return cells


def main() -> None:
    try:
        cells = _load_cells()
    except CellError as exc:
        raise SystemExit(f"error: {exc}") from exc

    print(f"ok: validated {len(cells)} machine-readable comparison cell(s)")


if __name__ == "__main__":
    main()
