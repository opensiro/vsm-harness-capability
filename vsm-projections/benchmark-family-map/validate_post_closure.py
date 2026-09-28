#!/usr/bin/env python3
"""Validate Capability-native post-closure no-reopen additions.

This validator intentionally ignores heterogeneous migrated predecessor delta
files. It owns only additions explicitly registered in
vsm-projections/benchmark-family-map/post-closure.json.
"""

from __future__ import annotations

import json
from pathlib import Path, PurePosixPath
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASE_MAP = HERE / "map.json"
EXTENSION = HERE / "post-closure.json"
BASELINES = ROOT / "baselines" / "primary-baselines.json"

FUNCTION_DIR = {
    "S2": "s2",
    "S3": "s3",
    "S3*": "s3star",
    "S4": "s4",
    "S5": "s5",
}
CLOSURE_FILE = {
    "S2": "s2-primary-search-closure.json",
    "S3": "s3-primary-search-closure.json",
    "S3*": "s3star-primary-search-closure.json",
    "S4": "s4-primary-search-closure.json",
    "S5": "s5-primary-search-closure.json",
}
FITS = {"direct", "proxy", "unsuitable", "unknown"}
EMPIRICAL_PAYLOAD_KEYS = {
    "result",
    "results",
    "benchmark_results",
    "metrics",
    "reported_metrics",
    "scores",
    "score",
}


def fail(message: str) -> None:
    raise SystemExit(f"error: {message}")


def load_object(path: Path) -> dict:
    if not path.is_file():
        fail(f"missing required file: {path.relative_to(ROOT)}")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")
    if not isinstance(value, dict):
        fail(f"expected JSON object: {path.relative_to(ROOT)}")
    return value


def valid_https(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def nonempty_text(value: object, *, minimum: int = 1) -> bool:
    return isinstance(value, str) and len(value.strip()) >= minimum


def repository_path(ref: object, *, prefix: str, suffix: str) -> Path:
    if not isinstance(ref, str) or not ref:
        fail(f"repository reference must be a non-empty string under {prefix}")
    posix = PurePosixPath(ref)
    if posix.is_absolute() or ".." in posix.parts or "." in posix.parts:
        fail(f"repository reference must be normalized and relative: {ref!r}")
    normalized = posix.as_posix()
    if not normalized.startswith(prefix) or not normalized.endswith(suffix):
        fail(f"repository reference outside expected boundary {prefix}*{suffix}: {ref!r}")
    path = ROOT.joinpath(*posix.parts)
    if not path.is_file():
        fail(f"referenced file does not exist: {ref}")
    return path


def closure_path(function: str) -> Path:
    folder = FUNCTION_DIR[function]
    filename = CLOSURE_FILE[function]
    return ROOT / "vsm-projections" / folder / "matched-cell" / filename


def resolve_raw_observation(delta_path: Path, delta: dict) -> None:
    observation_id = delta.get("observation_id")
    raw_ref = delta.get("raw_observation_ref")

    if observation_id is None and raw_ref is None:
        return
    if not nonempty_text(observation_id) or not nonempty_text(raw_ref):
        fail(
            f"{delta_path.relative_to(ROOT)}: observation_id and raw_observation_ref "
            "must be supplied together"
        )

    raw_ref = str(raw_ref)
    if "#" not in raw_ref:
        fail(f"{delta_path.relative_to(ROOT)}: raw_observation_ref requires #observation_id")
    path_part, fragment = raw_ref.rsplit("#", 1)
    if fragment != observation_id:
        fail(f"{delta_path.relative_to(ROOT)}: raw observation fragment does not match observation_id")

    candidate = (delta_path.parent / path_part).resolve()
    raw_root = (ROOT / "system-observations").resolve()
    if candidate.parent != raw_root or candidate.suffix != ".json":
        fail(
            f"{delta_path.relative_to(ROOT)}: raw_observation_ref must resolve to a direct "
            "system-observations/*.json child"
        )

    raw = load_object(candidate)
    observations = raw.get("observations")
    if not isinstance(observations, list):
        fail(f"{candidate.relative_to(ROOT)}: observations must be a list")
    matches = [
        row
        for row in observations
        if isinstance(row, dict) and row.get("observation_id") == observation_id
    ]
    if len(matches) != 1:
        fail(
            f"{delta_path.relative_to(ROOT)}: raw observation {observation_id!r} "
            f"resolved {len(matches)} times"
        )

    duplicated = EMPIRICAL_PAYLOAD_KEYS & set(delta)
    if duplicated:
        fail(
            f"{delta_path.relative_to(ROOT)}: derived delta duplicates neutral empirical "
            f"payload containers: {sorted(duplicated)}"
        )


def validate_delta(entry: dict, delta_path: Path, baselines: dict) -> None:
    function = entry["function"]
    delta = load_object(delta_path)

    required = {
        "schema_version",
        "status",
        "tracking_issue",
        "reviewed_at",
        "function",
        "benchmark_id",
        "benchmark_fit",
        "system_linkage",
        "primary_reopen",
        "reopen_gate_status",
        "disposition",
        "reason",
        "non_claim",
    }
    missing = required - delta.keys()
    if missing:
        fail(f"{delta_path.relative_to(ROOT)}: missing fields: {sorted(missing)}")

    expected = {
        "schema_version": 1,
        "status": "experimental-non-normative",
        "tracking_issue": entry["tracking_issue"],
        "function": function,
        "benchmark_id": entry["benchmark_id"],
        "benchmark_fit": entry["fit"],
        "system_linkage": entry["system_linkage"],
        "primary_reopen": False,
        "disposition": "retain-evidence-backed-gap",
    }
    for key, value in expected.items():
        if delta.get(key) != value:
            fail(
                f"{delta_path.relative_to(ROOT)}: {key} must be {value!r}, "
                f"found {delta.get(key)!r}"
            )

    if not nonempty_text(delta.get("reviewed_at"), minimum=10):
        fail(f"{delta_path.relative_to(ROOT)}: reviewed_at is required")
    if not nonempty_text(delta.get("reason"), minimum=40):
        fail(f"{delta_path.relative_to(ROOT)}: explicit reason is required")
    if not nonempty_text(delta.get("non_claim"), minimum=40):
        fail(f"{delta_path.relative_to(ROOT)}: explicit non_claim is required")

    gates = delta.get("reopen_gate_status")
    if not isinstance(gates, dict) or not gates:
        fail(f"{delta_path.relative_to(ROOT)}: reopen_gate_status must be a non-empty object")
    if any(value is not False for value in gates.values()):
        fail(
            f"{delta_path.relative_to(ROOT)}: this no-reopen path requires every "
            "reopen_gate_status value to be false"
        )

    closure = load_object(closure_path(function))
    if closure.get("status") != "experimental-non-normative":
        fail(f"{function}: owning primary-search closure status drift")
    if closure.get("primary_baseline") != "gap":
        fail(f"{function}: post-closure no-reopen path requires primary_baseline=gap")
    if closure.get("disposition") != "evidence-backed-gap":
        fail(f"{function}: owning closure disposition must remain evidence-backed-gap")
    for field in ("reopen_when", "do_not_reopen_for"):
        value = closure.get(field)
        if not isinstance(value, list) or not value or any(not nonempty_text(row) for row in value):
            fail(f"{function}: owning closure requires non-empty {field}")
    if not nonempty_text(closure.get("non_claim"), minimum=40):
        fail(f"{function}: owning closure requires an explicit non_claim")

    function_view = (baselines.get("functions") or {}).get(function)
    if not isinstance(function_view, dict) or function_view.get("status") != "gap":
        fail(f"{function}: live primary-baselines view must remain status=gap")

    resolve_raw_observation(delta_path, delta)


def main() -> None:
    base_map = load_object(BASE_MAP)
    extension = load_object(EXTENSION)
    baselines = load_object(BASELINES)

    if extension.get("schema_version") != 1:
        fail("post-closure extension schema_version must be 1")
    if extension.get("status") != "experimental-non-normative":
        fail("post-closure extension must remain experimental-non-normative")
    if extension.get("base_map_ref") != "vsm-projections/benchmark-family-map/map.json":
        fail("post-closure extension base_map_ref drift")
    if not nonempty_text(extension.get("purpose"), minimum=40):
        fail("post-closure extension requires an explicit purpose")

    base_pairs = {
        (entry.get("function"), entry.get("benchmark_id"))
        for entry in base_map.get("entries", [])
        if isinstance(entry, dict)
    }

    additions = extension.get("additions")
    if not isinstance(additions, list) or not additions:
        fail("post-closure additions must be a non-empty list")

    required_entry = {
        "function",
        "benchmark_id",
        "benchmark_name",
        "fit",
        "primary_source",
        "evaluated_object",
        "evaluation_mode",
        "system_linkage",
        "tracking_issue",
        "review_ref",
        "delta_ref",
        "non_claim",
    }

    seen: set[tuple[str, str]] = set()
    function_counts = {function: 0 for function in FUNCTION_DIR}

    for index, entry in enumerate(additions, start=1):
        if not isinstance(entry, dict):
            fail(f"post-closure addition {index} must be an object")
        missing = required_entry - entry.keys()
        if missing:
            fail(f"post-closure addition {index} missing fields: {sorted(missing)}")

        function = entry["function"]
        benchmark_id = entry["benchmark_id"]
        pair = (function, benchmark_id)

        if function not in FUNCTION_DIR:
            fail(f"post-closure addition {index} has unsupported function: {function!r}")
        if not nonempty_text(benchmark_id):
            fail(f"post-closure addition {index} benchmark_id must be non-empty")
        if pair in seen:
            fail(f"duplicate post-closure function/benchmark pair: {pair}")
        if pair in base_pairs:
            fail(f"post-closure pair duplicates frozen base map: {pair}")
        seen.add(pair)
        function_counts[function] += 1

        if entry["fit"] not in FITS:
            fail(f"{pair}: invalid fit {entry['fit']!r}")
        if not valid_https(entry["primary_source"]):
            fail(f"{pair}: primary_source must be an https URL")
        for field in ("benchmark_name", "evaluated_object", "evaluation_mode", "system_linkage"):
            if not nonempty_text(entry[field]):
                fail(f"{pair}: {field} must be non-empty")
        if not isinstance(entry["tracking_issue"], int) or entry["tracking_issue"] < 1:
            fail(f"{pair}: tracking_issue must be a positive integer")
        if not nonempty_text(entry["non_claim"], minimum=40):
            fail(f"{pair}: explicit non_claim is required")

        review_path = repository_path(
            entry["review_ref"],
            prefix="vsm-projections/benchmark-family-map/",
            suffix=".md",
        )
        if review_path.name in {"NOTE.md", "REVIEW.md"}:
            fail(f"{pair}: review_ref must point to an addition-specific review")

        function_dir = FUNCTION_DIR[function]
        delta_prefix = f"vsm-projections/{function_dir}/post-closure-deltas/"
        delta_path = repository_path(entry["delta_ref"], prefix=delta_prefix, suffix=".json")
        validate_delta(entry, delta_path, baselines)

    print("ok: Capability-native post-closure contract validated")
    print(f"registered additions: {len(additions)}")
    for function, count in function_counts.items():
        print(f"  {function}: {count}")


if __name__ == "__main__":
    main()
