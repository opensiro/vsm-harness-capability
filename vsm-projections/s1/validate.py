#!/usr/bin/env python3
"""Validate the derived S1 projection against neutral JSON observations."""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OBS = HERE / "observations.jsonl"
RAW_DIR = ROOT / "system-observations"
RAW_PREFIX = "../../system-observations/"
FAMILY_MAP = ROOT / "vsm-projections" / "benchmark-family-map" / "map.json"

ALLOWED_COMPAT = {"native-system", "adapter-preserved"}
ALLOWED_REVISION = {"exact-historical", "version-known", "unknown"}
ALLOWED_COMPARE = {"matched-model", "partially-matched", "descriptive-only"}
PROJECTION_KEYS = {"record_id", "function", "raw_observation_ref"}


def fail(msg: str) -> None:
    raise SystemExit(f"error: {msg}")


def https(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def load_direct_s1_families() -> set[str]:
    if not FAMILY_MAP.is_file():
        fail("benchmark-family map is missing")
    try:
        data = json.loads(FAMILY_MAP.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"benchmark-family map is invalid JSON: {exc}")
    if not isinstance(data, dict):
        fail("benchmark-family map must be a JSON object")
    entries = data.get("entries")
    if not isinstance(entries, list):
        fail("benchmark-family map entries must be a list")

    families: set[str] = set()
    for index, entry in enumerate(entries, start=1):
        if not isinstance(entry, dict):
            fail(f"benchmark-family map entry {index} must be an object")
        if entry.get("function") != "S1" or entry.get("fit") != "direct":
            continue
        benchmark_id = entry.get("benchmark_id")
        if not isinstance(benchmark_id, str) or not benchmark_id.strip():
            fail(f"benchmark-family map direct S1 entry {index} has invalid benchmark_id")
        families.add(benchmark_id)

    if not families:
        fail("benchmark-family map contains no direct S1 families")
    return families


def load_jsonl(path: Path, id_key: str) -> list[dict]:
    out = []
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            rec = json.loads(raw)
        except json.JSONDecodeError as exc:
            fail(f"{path.name}:{lineno}: {exc}")
        if not isinstance(rec, dict) or not isinstance(rec.get(id_key), str) or not rec[id_key]:
            fail(f"{path.name}:{lineno}: missing {id_key}")
        out.append(rec)
    return out


def hydrate(ref: str, rid: str) -> dict:
    if not isinstance(ref, str) or not ref.startswith(RAW_PREFIX) or "#" not in ref:
        fail(f"{rid}: invalid raw_observation_ref")
    rel, oid = ref[len(RAW_PREFIX):].rsplit("#", 1)
    if oid != rid or not rel.endswith(".json") or "/" in rel:
        fail(f"{rid}: raw_observation_ref drift")
    path = RAW_DIR / rel
    if not path.is_file():
        fail(f"{rid}: neutral raw record missing: {rel}")
    record = json.loads(path.read_text(encoding="utf-8"))
    matches = [o for o in record.get("observations", []) if o.get("observation_id") == rid]
    if len(matches) != 1:
        fail(f"{rid}: expected exactly one raw observation in {rel}")
    obs = matches[0]
    return {
        "schema_version": record["schema_version"],
        "observation_id": rid,
        "evidence_source_class": record["evidence_source_class"],
        "system_name": record["system_name"],
        "canonical_harness_id": record.get("canonical_harness_id"),
        "canonical_assessment_ref": record.get("canonical_assessment_ref"),
        "canonical_review_ref": record.get("canonical_review_ref"),
        "canonical_repository": record.get("canonical_repository"),
        "published_implementation": obs["published_implementation"],
        "benchmark": obs["benchmark"],
        "result": obs["result"],
        "provenance": obs["provenance"],
        "comparison": obs["comparison"],
        "notes": obs["notes"],
    }


def validate_canonical_linkage(raw: dict, rid: str) -> str:
    """Validate recorded Index linkage without duplicating Index assessment state."""
    harness_id = raw.get("canonical_harness_id")
    if not isinstance(harness_id, str) or not harness_id:
        fail(f"{rid}: neutral raw observation missing canonical_harness_id")
    expected_ref = f"assessments/{harness_id}.md"
    if raw.get("canonical_assessment_ref") != expected_ref:
        fail(f"{rid}: canonical_assessment_ref drift")
    review_ref = raw.get("canonical_review_ref")
    if not isinstance(review_ref, str) or not review_ref:
        fail(f"{rid}: canonical_review_ref is required for canonical-linked S1 evidence")
    if not https(raw.get("canonical_repository")):
        fail(f"{rid}: canonical_repository must be an https URL")
    return harness_id


def main() -> None:
    allowed_families = load_direct_s1_families()
    records = load_jsonl(OBS, "record_id")
    if not records:
        fail("no S1 projection observations")

    seen = set()
    systems = set()
    groups: dict[str, list[dict]] = {}

    for rec in records:
        rid = rec["record_id"]
        if rid in seen:
            fail(f"duplicate record_id: {rid}")
        seen.add(rid)
        if set(rec) != PROJECTION_KEYS:
            fail(f"{rid}: S1 projection must not duplicate raw benchmark payload")
        if rec.get("function") != "S1":
            fail(f"{rid}: function must be S1")

        raw = hydrate(rec.get("raw_observation_ref"), rid)
        harness_id = validate_canonical_linkage(raw, rid)
        systems.add(harness_id)

        benchmark = raw.get("benchmark") or {}
        if benchmark.get("family_id") not in allowed_families:
            fail(f"{rid}: benchmark family is not a reviewed direct S1 family")
        for key in ("primary_source", "artifact_source"):
            if not https(benchmark.get(key)):
                fail(f"{rid}: benchmark.{key} must be https")

        result = raw.get("result") or {}
        if not isinstance(result.get("model"), str) or not result["model"]:
            fail(f"{rid}: model is required")
        if not isinstance(result.get("metric"), str) or not result["metric"]:
            fail(f"{rid}: metric is required")
        if not isinstance(result.get("value"), (int, float)):
            fail(f"{rid}: numeric metric value is required")

        identity = raw.get("published_implementation") or {}
        if identity.get("system_compatibility") not in ALLOWED_COMPAT:
            fail(f"{rid}: invalid system_compatibility")
        if identity.get("revision_match") not in ALLOWED_REVISION:
            fail(f"{rid}: invalid revision_match")

        comparison = raw.get("comparison") or {}
        mode = comparison.get("mode")
        group = comparison.get("group")
        if mode not in ALLOWED_COMPARE:
            fail(f"{rid}: invalid comparison mode")
        if not isinstance(group, str) or not group:
            fail(f"{rid}: comparison group required")
        groups.setdefault(group, []).append(raw)

        notes = raw.get("notes")
        if not isinstance(notes, str) or len(notes.strip()) < 20:
            fail(f"{rid}: explicit interpretation notes required")

    partially = 0
    for group, members in groups.items():
        modes = {m["comparison"]["mode"] for m in members}
        member_systems = {m["canonical_harness_id"] for m in members}
        if "matched-model" in modes and len(member_systems) < 2:
            fail(f"{group}: matched-model requires at least two systems")
        if "partially-matched" in modes and len(member_systems) >= 2:
            partially += 1

    print(f"ok: {len(records)} derived S1 observations across {len(systems)} canonical-linked systems")
    print(f"reviewed direct S1 families: {len(allowed_families)}")
    print("neutral raw source: system-observations/*.json")
    print("benchmark-family semantics: vsm-projections/benchmark-family-map/map.json")
    print("canonical assessment state: externally owned by opensiro/vsm-harness-index")
    print(f"comparison groups: {len(groups)}")
    print(f"cross-system partially-matched groups: {partially}")


if __name__ == "__main__":
    main()
