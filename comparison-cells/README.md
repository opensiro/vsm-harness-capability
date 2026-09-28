# Comparison cells

Materially comparable groups of public observations used for cross-system per-function capability analysis.

A cell makes comparability constraints explicit: evidence family/version, model/configuration, evaluator, environment, budget/repetition and reset/adaptation policy where known. Unknown dimensions stay explicit rather than being normalized by assumption.

Weak or unmatched evidence remains useful evidence but must not be promoted into a matched cell by normalization guesswork.

## Storage rule

Machine-readable cells are JSON files in this directory. They reference raw `observation_id` values and the applicable `vsm-projections/<function>/observations.jsonl` view.

They must **not** duplicate raw score/result payloads. Numeric benchmark results remain owned by `system-observations/`; a baseline Markdown view may render them for humans while the cell keeps only identity, provenance and comparability structure.

A comparison cell does not assign canonical ownership state, create a domain-specific grade, or define a global harness ranking.

## Current selected cell

- [`s1-pawbench-v1-qwen3.6-35b-a3b.json`](s1-pawbench-v1-qwen3.6-35b-a3b.json) — the existing PawBench v1.0 / `qwen3.6-35b-a3b` matched-model S1 primary, materialized without introducing new evidence.

## Validation

```bash
python comparison-cells/validate.py
```

Validation checks that referenced raw observations exist, that each observation is present in the declared VSM-function projection, that selected baseline linkage is reciprocal, and that metric/result payload keys are not duplicated into the comparison-cell layer.
