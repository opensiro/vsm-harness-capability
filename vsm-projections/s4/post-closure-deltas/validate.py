#!/usr/bin/env python3
"""Validate post-closure S4 evidence additions without rewriting frozen closure snapshots."""

from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BASE_MAP = ROOT / "vsm-projections" / "benchmark-family-map" / "map.json"
EXTENSION = ROOT / "vsm-projections" / "benchmark-family-map" / "post-closure.json"
REVIEW = ROOT / "vsm-projections" / "benchmark-family-map" / "S4-AIRBNB-AHO-REVIEW.md"
DELTA = HERE / "airbnb-agent-harness-optimizer-2026-09-28.json"
RAW = ROOT / "system-observations" / "airbnb-agent-harness-optimizer.json"
CLOSURE = ROOT / "vsm-projections" / "s4" / "matched-cell" / "s4-primary-search-closure.json"
BASELINES = ROOT / "baselines" / "primary-baselines.json"

AHO_ID = "agent-harness-optimizer-prism"
OBSERVATION_ID = "airbnb-agent-harness-optimizer-prism-heldout-lift-2026"
SOURCE_REVISION = "0d7652b42296c8df07532fa3787fc956250741e7"
SOURCE_URL = f"https://github.com/airbnb/agent-harness-optimizer/tree/{SOURCE_REVISION}"


def fail(message: str) -> None:
    raise SystemExit(f"error: {message}")


def https(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def load(path: Path) -> dict:
    if not path.is_file():
        fail(f"missing required file: {path.relative_to(ROOT)}")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")
    if not isinstance(value, dict):
        fail(f"expected JSON object: {path.relative_to(ROOT)}")
    return value


def main() -> None:
    base_map = load(BASE_MAP)
    extension = load(EXTENSION)
    delta = load(DELTA)
    raw = load(RAW)
    closure = load(CLOSURE)
    baselines = load(BASELINES)

    if not REVIEW.is_file():
        fail("missing AHO human review")
    review_text = REVIEW.read_text(encoding="utf-8")
    for phrase in (
        "function: S4",
        "fit: direct",
        "system_linkage: external-native-noncanonical",
        "primary_reopen: no",
        "primary baseline: gap",
    ):
        if phrase not in review_text:
            fail(f"AHO review missing invariant: {phrase}")

    base_pairs = {
        (entry.get("function"), entry.get("benchmark_id"))
        for entry in base_map.get("entries", [])
        if isinstance(entry, dict)
    }
    if ("S4", AHO_ID) in base_pairs:
        fail("AHO must remain a post-closure extension, not rewrite the frozen base map")

    if extension.get("schema_version") != 1:
        fail("post-closure map schema_version must be 1")
    if extension.get("status") != "experimental-non-normative":
        fail("post-closure map must remain experimental-non-normative")
    if extension.get("base_map_ref") != "vsm-projections/benchmark-family-map/map.json":
        fail("post-closure base_map_ref drift")

    additions = extension.get("additions")
    if not isinstance(additions, list) or not additions:
        fail("post-closure additions must be a non-empty list")
    pairs: set[tuple[str, str]] = set()
    for entry in additions:
        if not isinstance(entry, dict):
            fail("post-closure additions must contain objects")
        pair = (entry.get("function"), entry.get("benchmark_id"))
        if pair in pairs:
            fail(f"duplicate post-closure pair: {pair}")
        if pair in base_pairs:
            fail(f"post-closure pair duplicates base map: {pair}")
        pairs.add(pair)
        if entry.get("fit") not in {"direct", "proxy", "unsuitable", "unknown"}:
            fail(f"invalid post-closure fit: {entry.get('fit')!r}")
        if not https(entry.get("primary_source")):
            fail(f"invalid post-closure primary_source for {pair}")
        if not isinstance(entry.get("non_claim"), str) or len(entry["non_claim"].strip()) < 40:
            fail(f"post-closure entry requires explicit non_claim: {pair}")

    aho = [entry for entry in additions if entry.get("function") == "S4" and entry.get("benchmark_id") == AHO_ID]
    if len(aho) != 1:
        fail("expected exactly one AHO post-closure family entry")
    aho = aho[0]
    expected_aho = {
        "fit": "direct",
        "primary_source": SOURCE_URL,
        "evaluation_mode": "published-heldout-harness-optimization",
        "system_linkage": "external-native-noncanonical",
        "tracking_issue": 26,
        "review_ref": "vsm-projections/benchmark-family-map/S4-AIRBNB-AHO-REVIEW.md",
        "delta_ref": "vsm-projections/s4/post-closure-deltas/airbnb-agent-harness-optimizer-2026-09-28.json",
    }
    for key, expected in expected_aho.items():
        if aho.get(key) != expected:
            fail(f"AHO post-closure family {key} drift")

    expected_delta = {
        "function": "S4",
        "benchmark_id": AHO_ID,
        "benchmark_fit": "direct",
        "system_linkage": "external-native-noncanonical",
        "boundary_class": "external-native-evolving-harness-system",
        "canonical_harness_id": None,
        "canonical_system_eligible": False,
        "observation_id": OBSERVATION_ID,
        "raw_observation_ref": "../../../system-observations/airbnb-agent-harness-optimizer.json#" + OBSERVATION_ID,
        "primary_reopen": False,
        "disposition": "retain-evidence-backed-gap",
    }
    for key, expected in expected_delta.items():
        if delta.get(key) != expected:
            fail(f"AHO post-closure delta {key} drift")
    gates = delta.get("reopen_gate_status")
    if not isinstance(gates, dict) or not gates or any(value is not False for value in gates.values()):
        fail("AHO reopen gates must all remain false")

    if raw.get("evidence_source_class") != "first-party-reported":
        fail("AHO raw evidence provenance drift")
    if raw.get("canonical_harness_id") is not None:
        fail("AHO raw evidence must remain non-canonical")
    implementation = raw.get("published_implementation")
    if not isinstance(implementation, dict) or implementation.get("system_compatibility") != "native-system":
        fail("AHO raw system compatibility drift")
    if implementation.get("source_revision") != SOURCE_REVISION:
        fail("AHO raw source revision drift")
    observations = raw.get("observations")
    matches = [row for row in observations or [] if isinstance(row, dict) and row.get("observation_id") == OBSERVATION_ID]
    if len(matches) != 1:
        fail("AHO raw observation linkage must resolve exactly once")
    observation = matches[0]
    if observation.get("publication_id") != "arXiv:2609.05736" or observation.get("optimizer") != "PRISM":
        fail("AHO publication/optimizer binding drift")
    if observation.get("inner_model") != "openai/gpt-5.4-mini":
        fail("AHO fixed inner-model binding drift")
    results = observation.get("benchmark_results")
    if not isinstance(results, list) or {row.get("benchmark") for row in results if isinstance(row, dict)} != {
        "BFCL multi-round",
        "tau2-Retail",
        "tau2-Telecom",
    }:
        fail("AHO benchmark result surface drift")

    if closure.get("primary_baseline") != "gap" or closure.get("disposition") != "evidence-backed-gap":
        fail("frozen S4 primary closure no longer remains a gap")
    if "another heterogeneous single-system S4 result" not in closure.get("do_not_reopen_for", []):
        fail("frozen S4 single-system non-reopen rule drift")

    s4 = (baselines.get("functions") or {}).get("S4")
    if not isinstance(s4, dict) or s4.get("status") != "gap":
        fail("live S4 primary baseline status must remain gap")
    frozen_ids = {
        row.get("benchmark_id")
        for row in s4.get("reviewed_direct_families", [])
        if isinstance(row, dict)
    }
    if frozen_ids != {
        "a-evolve-harness-evolution",
        "skillevolbench",
        "evoharnessbench-self-evolving",
        "evo-bench",
    }:
        fail("frozen S4 reviewed_direct_families snapshot drift")

    print("ok: post-closure S4 evidence validated")
    print(f"base S4 closure families: {len(frozen_ids)}")
    print(f"post-closure additions: {len(additions)}")
    print("AHO direct S4 family: admitted as external-native-noncanonical")
    print("S4 primary baseline: gap")


if __name__ == "__main__":
    main()
