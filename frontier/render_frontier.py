#!/usr/bin/env python3
"""Render the live general-capability evidence frontier from owning source artifacts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUTPUT = HERE / "EVIDENCE-FRONTIER.md"
BASELINES = ROOT / "baselines" / "primary-baselines.json"

FUNCTION_ORDER = ("S1", "S2", "S3", "S3*", "S4", "S5")
CLOSURE_PATHS = {
    "S2": ROOT / "vsm-projections" / "s2" / "matched-cell" / "s2-primary-search-closure.json",
    "S3": ROOT / "vsm-projections" / "s3" / "matched-cell" / "s3-primary-search-closure.json",
    "S3*": ROOT / "vsm-projections" / "s3star" / "matched-cell" / "s3star-primary-search-closure.json",
    "S4": ROOT / "vsm-projections" / "s4" / "matched-cell" / "s4-primary-search-closure.json",
    "S5": ROOT / "vsm-projections" / "s5" / "matched-cell" / "s5-primary-search-closure.json",
}


class FrontierError(ValueError):
    pass


def load_json(path: Path) -> dict:
    if not path.is_file():
        raise FrontierError(f"missing source artifact: {path.relative_to(ROOT)}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise FrontierError(f"{path.relative_to(ROOT)}: invalid JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise FrontierError(f"{path.relative_to(ROOT)}: expected JSON object")
    return data


def rel_link(path: Path) -> str:
    return "../" + path.relative_to(ROOT).as_posix()


def display_value(value: object) -> str:
    if isinstance(value, list):
        return ", ".join(str(item) for item in value)
    return str(value)


def table_depth(function: str, selection: dict, closure: dict | None) -> list[tuple[str, object]]:
    if function == "S1":
        primary = selection.get("primary")
        if not isinstance(primary, dict):
            raise FrontierError("S1 selected primary is missing")
        harnesses = primary.get("canonical_harness_ids")
        if not isinstance(harnesses, list):
            raise FrontierError("S1 primary canonical_harness_ids must be a list")
        return [
            ("task_count", primary.get("task_count")),
            ("canonical_harnesses", len(harnesses)),
        ]

    if closure is None:
        raise FrontierError(f"{function}: closure record is missing")
    evidence_depth = closure.get("evidence_depth")
    if isinstance(evidence_depth, dict) and evidence_depth:
        return list(evidence_depth.items())
    if function == "S4":
        observations = closure.get("canonical_native_observations")
        routes = closure.get("reviewed_routes")
        if not isinstance(observations, list) or not isinstance(routes, list):
            raise FrontierError("S4 closure requires canonical_native_observations and reviewed_routes lists")
        return [
            ("canonical_native_observations", len(observations)),
            ("reviewed_routes", len(routes)),
        ]
    raise FrontierError(f"{function}: closure has no evidence_depth")


def detail_depth(function: str, closure: dict) -> list[tuple[str, object]]:
    evidence_depth = closure.get("evidence_depth")
    if isinstance(evidence_depth, dict) and evidence_depth:
        return list(evidence_depth.items())
    if function == "S4":
        observations = closure.get("canonical_native_observations")
        routes = closure.get("reviewed_routes")
        if not isinstance(observations, list) or not isinstance(routes, list):
            raise FrontierError("S4 closure requires canonical_native_observations and reviewed_routes lists")
        return [
            ("canonical_native_observations", observations),
            ("reviewed_routes", len(routes)),
        ]
    raise FrontierError(f"{function}: closure has no evidence depth")


def validate_sources(baselines: dict, closures: dict[str, dict]) -> dict[str, dict]:
    functions = baselines.get("functions")
    if not isinstance(functions, dict):
        raise FrontierError("baselines/primary-baselines.json: functions must be an object")

    for function in FUNCTION_ORDER:
        selection = functions.get(function)
        if not isinstance(selection, dict):
            raise FrontierError(f"baseline selection missing for {function}")
        status = selection.get("status")
        if function == "S1":
            if status != "selected" or selection.get("scope") != "general":
                raise FrontierError("S1 frontier requires selected general primary")
            continue
        if status != "gap":
            raise FrontierError(f"{function}: expected baseline status=gap, got {status!r}")
        if not isinstance(selection.get("blocking_reason"), str) or not selection["blocking_reason"]:
            raise FrontierError(f"{function}: gap selection requires blocking_reason")

        closure = closures[function]
        if "experimental" not in str(closure.get("status", "")).lower():
            raise FrontierError(f"{function}: closure must remain experimental")
        if closure.get("disposition") != "evidence-backed-gap":
            raise FrontierError(f"{function}: closure disposition must remain evidence-backed-gap")
        if closure.get("primary_baseline") != "gap":
            raise FrontierError(f"{function}: closure primary_baseline must remain gap")
        for field in ("reviewed_at", "closure_claim", "non_claim"):
            if not isinstance(closure.get(field), str) or not closure[field]:
                raise FrontierError(f"{function}: closure requires {field}")
        for field in ("reopen_when", "do_not_reopen_for"):
            value = closure.get(field)
            if not isinstance(value, list) or not value or any(not isinstance(item, str) for item in value):
                raise FrontierError(f"{function}: closure requires non-empty string list {field}")
        table_depth(function, selection, closure)

    return functions


def render() -> str:
    baselines = load_json(BASELINES)
    closures = {function: load_json(path) for function, path in CLOSURE_PATHS.items()}
    functions = validate_sources(baselines, closures)

    lines = [
        "# Current Functional Capability Evidence Frontier",
        "",
        "Status: **generated, experimental, non-normative**",
        "",
        "Generated deterministically by `frontier/render_frontier.py` from `baselines/primary-baselines.json` and the S2–S5 primary-search closure records.",
        "",
        "This file is **not** the historical experiment synthesis. Frozen predecessor artifacts remain under `historical/`; this projection moves only when its owning current-state source artifacts move.",
        "",
        "It is also not a second evidence database: primary state, counts, blockers, closure claims and reopen rules below are rendered from existing source-of-truth artifacts.",
        "",
        "## Current frontier",
        "",
        "| Function | Primary state | Current evidence depth | Reviewed through | Source |",
        "| --- | --- | --- | --- | --- |",
    ]

    selected_at = baselines.get("selected_at")
    if not isinstance(selected_at, str) or not selected_at:
        raise FrontierError("baselines/primary-baselines.json: selected_at is required")

    for function in FUNCTION_ORDER:
        selection = functions[function]
        if function == "S1":
            primary = selection["primary"]
            state = f"`selected` — {primary['benchmark_name']} / `{primary['reference_model']}`"
            reviewed_at = selected_at
            source_path = BASELINES
            closure = None
        else:
            state = "`gap`"
            closure = closures[function]
            reviewed_at = closure["reviewed_at"]
            source_path = CLOSURE_PATHS[function]

        depth = " · ".join(
            f"`{key}`: `{display_value(value)}`"
            for key, value in table_depth(function, selection, closure)
        )
        source_name = source_path.name
        lines.append(
            f"| {function} | {state} | {depth} | `{reviewed_at}` | "
            f"[`{source_name}`]({rel_link(source_path)}) |"
        )

    lines.extend(
        [
            "",
            "A `gap` is an empirical evidence state, not a zero capability score and not a statement about canonical VSM ownership.",
            "",
            "## S1 — selected primary",
            "",
        ]
    )

    s1_primary = functions["S1"]["primary"]
    harnesses = s1_primary["canonical_harness_ids"]
    lines.extend(
        [
            f"- **Primary family:** {s1_primary['benchmark_name']} (`{s1_primary['benchmark_id']}`).",
            f"- **Reference model:** `{s1_primary['reference_model']}`.",
            f"- **Comparison design:** `{s1_primary['comparison_design']}`.",
            "- **Canonical harnesses in the first cell:** "
            + ", ".join(f"`{item}`" for item in harnesses)
            + ".",
            f"- **Primary source:** {s1_primary['primary_source']}.",
            f"- **Provenance note:** {s1_primary['provenance_note']}",
            f"- **Source:** [`{BASELINES.name}`]({rel_link(BASELINES)}).",
            "",
        ]
    )

    for function in FUNCTION_ORDER[1:]:
        closure = closures[function]
        selection = functions[function]
        source_path = CLOSURE_PATHS[function]
        lines.extend(
            [
                f"## {function} — current `gap` frontier",
                "",
                f"- **Reviewed through:** `{closure['reviewed_at']}`.",
                f"- **Primary blocking reason:** {selection['blocking_reason']}",
                f"- **Closure claim:** {closure['closure_claim']}",
                "- **Evidence depth:**",
            ]
        )
        for key, value in detail_depth(function, closure):
            lines.append(f"  - `{key}`: `{display_value(value)}`")

        lines.append("- **Reopen when:**")
        for index, item in enumerate(closure["reopen_when"], start=1):
            lines.append(f"  {index}. {item}")

        lines.append("- **Do not reopen for:**")
        for item in closure["do_not_reopen_for"]:
            lines.append(f"  - {item}")

        lines.extend(
            [
                f"- **Non-claim:** {closure['non_claim']}",
                f"- **Source:** [`{source_path.name}`]({rel_link(source_path)}).",
                "",
            ]
        )

    lines.extend(
        [
            "## Reading rule",
            "",
            "```text",
            "historical/",
            "        = immutable predecessor / closed-cycle artifacts",
            "",
            "baselines/primary-baselines.json",
            "        +",
            "current S2–S5 primary-search closure records",
            "        ↓",
            "frontier/EVIDENCE-FRONTIER.md",
            "        = generated live derived view",
            "```",
            "",
            "Raw observation admission alone does not force a frontier change. The frontier moves when the owning baseline selection or function closure record moves.",
            "",
            "## Generation contract",
            "",
            "Write the current frontier:",
            "",
            "```bash",
            "python frontier/render_frontier.py",
            "```",
            "",
            "Check that the committed frontier is current:",
            "",
            "```bash",
            "python frontier/render_frontier.py --check",
            "```",
            "",
            "Do not hand-edit `EVIDENCE-FRONTIER.md`; edit the owning baseline/closure source first and regenerate.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    try:
        expected = render()
    except FrontierError as exc:
        raise SystemExit(f"error: {exc}") from exc

    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != expected:
            raise SystemExit("error: frontier/EVIDENCE-FRONTIER.md is stale; run python frontier/render_frontier.py")
        print("ok: evidence frontier is current")
        return

    OUTPUT.write_text(expected, encoding="utf-8")
    print(f"wrote {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
