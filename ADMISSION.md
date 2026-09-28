# Live public-evidence admission

Status: **experimental, non-normative**

This document defines the contributor workflow for adding new public evidence to the live `vsm-harness-capability` corpus after the completed predecessor migration.

It operationalizes [`PUBLIC-EVIDENCE.md`](PUBLIC-EVIDENCE.md) and [`EVIDENCE-REGISTRY.md`](EVIDENCE-REGISTRY.md). It does not redefine their evidence contract.

## Admission boundary

Raw observation admission answers only:

> Is this a reconstructable public observation about a concrete system/evidence surface, with sufficient identity and provenance to store once in the neutral evidence layer?

It does **not** require an answer to:

- which VSM function the observation measures;
- whether the observation belongs in a comparison cell;
- whether it changes a selected general-capability baseline;
- whether it changes the current evidence frontier;
- whether it supports a domain-specific assessment.

Those are downstream derived-review questions.

## Live path

```text
public upstream / third-party evidence
        ↓
new or updated system-observations/*.json record
        ↓
neutral-record validation
        ↓
regenerate registry.psv + REGISTRY.md
        ↓
admission check for the changed raw record
        ↓
merge raw evidence
        ↓
optional derived review
    ├── VSM projection
    ├── comparison-cell eligibility
    ├── baseline selection/replacement
    └── evidence-frontier update
```

A raw observation may be admitted with no VSM projection. Absence of a downstream interpretation is a valid state, not a validation failure.

## 1. Establish the public evidence identity

Before editing the repository, identify:

- the public evidence surface;
- the concrete system that was actually exercised;
- primary public source(s), preferably pinned/immutable where available;
- publisher and evidence-source class;
- historical execution/version/revision identity where public;
- system compatibility;
- raw result/outcome and metric identity where applicable;
- material comparison metadata and known confounders;
- adaptation/reset state when publicly established;
- factual task or operating-domain context where useful.

Do not fill unknown historical metadata from current repository state.

Do not run an assessed harness merely to create missing evidence.

## 2. Add the neutral raw record

Add or extend a JSON record directly under:

```text
system-observations/
```

Each published result receives one globally unique `observation_id`.

Canonical Index linkage is optional. Use it only when public provenance supports the mapping. A useful public observation may remain non-canonical.

The raw record must remain VSM-neutral. Function relevance belongs downstream under `vsm-projections/`.

## 3. Regenerate the neutral registry

After changing raw observations, run:

```bash
python system-observations/render_registry.py
```

Commit both generated projections when they change:

```text
system-observations/registry.psv
system-observations/REGISTRY.md
```

Do not edit those generated files independently of the raw JSON records.

## 4. Run the record-specific admission check

Run:

```bash
python scripts/admission_check.py system-observations/<record>.json
```

The check is intentionally local and reproducible. It verifies that:

- the supplied path is an active raw JSON record;
- the record contains unique observation IDs;
- the complete neutral corpus validates;
- committed generated registry views match the raw corpus;
- every observation ID in the supplied record is present in `registry.psv` and points back to that record;
- existing machine-readable comparison cells remain valid.

It also reports downstream machine-readable VSM projection and comparison-cell references when present. Their absence is informational, not an admission failure.

## 5. Run repository validation

Before opening the PR, run:

```bash
python scripts/validate_repository.py
```

The root validator preserves repository-wide boundaries such as migration-floor integrity, general-vs-domain scope, generated registry consistency and comparison-cell integrity.

## 6. Review downstream interpretation separately

After factual admission, review whether the new observation justifies any derived change.

### VSM projection

Add a VSM projection only when Profile semantics support a reviewable function interpretation. Benchmark vocabulary alone is insufficient.

### Comparison cell

Add or modify a comparison cell only when two or more observations are materially comparable under [`BASELINE.md`](BASELINE.md). Do not normalize missing environment, budget or reset metadata by assumption.

### Baseline

A new observation does not automatically replace or create a selected primary. Baseline selection remains a separate current-view decision over the evidence corpus.

### Frontier

`frontier/` is a live derived view, but this repository currently has no repository-local frontier generator. Therefore frontier review is an explicit derived-maintenance step rather than part of mechanical raw admission.

Do not describe frontier refresh as automatic until a generator/check contract actually exists.

## Review split

When practical, keep factual admission and semantic interpretation separable in the diff:

```text
raw evidence identity/provenance
        ↓ review first
optional VSM/capability interpretation
        ↓ review separately
```

This makes disagreement about interpretation possible without losing a valid public observation.

## Non-goals

This workflow does not:

- run or reproduce assessed harness benchmarks;
- assign canonical `A`, `C`, `P`, `A(P)`, `C(P)`, `—` or `?` states;
- infer VSM function relevance from benchmark names;
- require canonical Index linkage for raw admission;
- create a global harness score;
- create domain-specific capability grades;
- manufacture a comparison cell when public conditions are not materially matched.
