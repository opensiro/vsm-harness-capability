# Capability-native post-closure evidence

Status: **experimental, non-normative**

This document defines the live post-closure path for new `vsm-harness-capability` evidence discovered after a function's primary-search closure has already been frozen as an evidence-backed gap.

It applies to **Capability-native** additions registered in:

```text
vsm-projections/benchmark-family-map/post-closure.json
```

It does not retroactively normalize or rewrite heterogeneous `post-closure-deltas/` artifacts migrated from the predecessor Index experiment.

## Why this layer exists

For S2, S3, S3*, S4 and S5, the repository already has frozen primary-search closure artifacts. New public evidence may strengthen a function's evidence set without satisfying the closure's primary-reopen gate.

Those two facts must coexist:

```text
new evidence exists
        +
frozen primary search remains a gap
        ↓
post-closure addition
```

The addition must not be inserted into historical closure counts as though it had been reviewed before the closure date.

## Artifact split

A live no-reopen addition has three derived artifacts after any neutral raw admission:

```text
addition-specific human review
        ↓
benchmark-family-map/post-closure.json entry
        ↓
function-local post-closure delta JSON
```

The human review explains the VSM interpretation and boundary. The extension registry gives the addition a machine-readable family identity. The function-local delta evaluates the current reopen gates and records why the frozen primary state remains unchanged.

The frozen sources remain separate:

```text
benchmark-family-map/map.json
function primary-search closure
baselines/primary-baselines.json
```

A no-reopen addition does not rewrite those historical closure counts or silently change the primary baseline.

## Supported functions

This workflow is for functions with a frozen gap closure:

```text
S2
S3
S3*
S4
S5
```

S1 does not use this path. S1 already has a selected general primary and follows the normal family-map, projection, comparison-cell and baseline-review path.

## Extension entry contract

Every addition in `post-closure.json` declares:

- `function`;
- `benchmark_id`;
- `benchmark_name`;
- `fit`;
- `primary_source`;
- `evaluated_object`;
- `evaluation_mode`;
- `system_linkage`;
- `tracking_issue`;
- `review_ref`;
- `delta_ref`;
- `non_claim`.

The `(function, benchmark_id)` pair must be unique and must not duplicate the frozen base `map.json`.

`review_ref` must point to an addition-specific review under `vsm-projections/benchmark-family-map/`.

`delta_ref` must point to the matching function-local directory:

```text
vsm-projections/<function>/post-closure-deltas/*.json
```

with `S3*` represented on disk as `s3star`.

## No-reopen delta contract

A Capability-native no-reopen delta must include at least:

- `schema_version: 1`;
- `status: experimental-non-normative`;
- the same tracking issue, function, benchmark ID, fit and system linkage as the extension entry;
- `reviewed_at`;
- `primary_reopen: false`;
- a non-empty `reopen_gate_status` object whose values are all `false`;
- `disposition: retain-evidence-backed-gap`;
- an explicit `reason`;
- an explicit `non_claim`.

If the delta references a neutral raw observation, `observation_id` and `raw_observation_ref` must be supplied together and resolve exactly once into a direct child of `system-observations/`.

Numeric empirical payload remains in the neutral raw record. The delta records interpretation, boundary and reopen disposition rather than copying result tables into another database.

## Fail-closed reopen boundary

This workflow is deliberately unable to approve a primary reopen.

If any relevant reopen gate becomes true, do **not** encode the change as another ordinary `post-closure.json` no-reopen addition.

Instead open a separate task to re-review the owning primary-search closure and baseline. That task may need to update:

- the function's primary-search closure;
- `baselines/primary-baselines.json`;
- comparison cells;
- generated frontier state.

This separation prevents a new evidence row from silently turning a frozen gap into a selected primary.

## Validation

Run:

```bash
python vsm-projections/benchmark-family-map/validate_post_closure.py
```

The generic validator checks:

- extension schema and unique identities;
- separation from the frozen base family map;
- review and delta reference existence/boundaries;
- the common no-reopen delta contract;
- the owning closure still has `primary_baseline=gap` and `disposition=evidence-backed-gap`;
- the live baseline still has `status=gap`;
- optional raw-observation references resolve exactly once;
- common empirical result containers are not copied into the derived delta.

Addition-specific validators may impose stronger provenance or semantic invariants. The Airbnb AHO S4 validator is the first such specialization and remains authoritative for AHO-specific model, benchmark and source bindings.

## Historical boundary

Predecessor-era delta files under function-local `post-closure-deltas/` are preserved historical artifacts with heterogeneous schemas. They are not made invalid merely because they do not conform to this new live contract.

The generic validator owns only entries explicitly registered in `benchmark-family-map/post-closure.json` after extraction into this standalone Capability repository.

## Non-goals

This workflow does not:

- manufacture new evidence;
- change canonical Index ownership;
- redefine Profile semantics;
- normalize heterogeneous function metrics;
- select or rank a primary automatically;
- rewrite frozen closure history;
- convert migrated predecessor artifacts into a new schema;
- permit a true reopen condition to be hidden inside a no-reopen delta.
