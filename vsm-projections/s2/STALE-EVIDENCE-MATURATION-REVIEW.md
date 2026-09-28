# STALE semantic-coordination — S2 evidence-maturation review

Status: **reviewed evidence maturation; frozen closure preserved**

Tracking issue: #53  
Neutral admission: #59  
Repository: `illinoisdata/STALE-bench`  
Reviewed revision: `f7bc831e4eff08b9652acd893553824636ae3985`  
Paper: `arXiv:2609.25396`  
Raw observation: `system-observations/stale-bench.json#stale-semantic-interference-communication-2026`

## Decision

The newly admitted neutral observation supports the **already-existing** direct S2 family:

```text
benchmark_id: stale-semantic-coordination
function: S2
fit: direct
system_linkage: benchmark-scaffolded
```

This is an **evidence-maturation review**, not a new benchmark-family admission.

Accordingly:

```text
new family: no
base family identity change: no
frozen family-count change: no
frozen observation-count change: no
canonical observation added: no
primary_reopen: no
S2 primary_baseline: gap
```

## Why the existing direct S2 mapping is supported

The direct chain remains the one already recorded by the frozen family review:

```text
parallel workers act from stale local assumptions
        ↓
individually acceptable patches interact after composition
        ↓
silent semantic interference appears only in the composed state
        ↓
coordination changes what concurrent state is visible to a worker
        ↓
a precise message exposes the finalized concurrent change
        ↓
interference is attenuated in the controlled communication condition
```

The relevant variety is relational rather than ordinary single-worker task failure: each patch can satisfy its solo condition while the composed result fails because the two workers acted on mutually stale semantic assumptions. The benchmark then changes only the information available across that relation and measures whether the composed failure is reduced.

That is the same direct S2 boundary already owned by `stale-semantic-coordination` in the frozen benchmark-family map. The raw admission adds recoverable public result provenance; it does not create a second S2 family.

## Evidence tiers that must remain separate

The raw observation deliberately preserves three materially different public surfaces.

### 1. Synthetic controlled tier

The synthetic benchmark plants known semantic coupling/staleness and reports that blind interference tracks the planted disturbance. A precise message describing the concurrent finalized change removes almost all of that interference in the reported communication study.

This is the cleanest controlled disturbance-to-attenuation surface, but it is benchmark-authored and therefore remains benchmark-scaffolded rather than a native canonical harness result.

### 2. Corrected mined-real tier

The corrected 417-pair Django corpus is a **negative control**, not supporting evidence for a high natural interference rate. Under the corrected protocol the first-party report finds essentially no observable composed interference, including no both-solved-and-break cases; the stronger-model corrected run likewise reports no interference in its valid sample.

This negative result is part of the evidence and must remain visible. It prevents the synthetic/real-derived result from being generalized into a claim that ordinary mined real-world patch pairs frequently exhibit the same failure mode.

### 3. Real-derived anchored tier

The real-derived tier starts from helpers anchored to validated real Django pull-request pairs and deliberately instantiates semantic-interference mechanisms around them. In that surface the first-party gpt-5.5 runs report high blind interference and substantial recovery when one precise message is supplied.

This tier increases ecological grounding relative to the purely synthetic suite, while still being a constructed benchmark condition rather than an estimate of natural incidence in the mined-real corpus.

## Measurement correction is part of the claim boundary

The repository documents that an earlier naive real-tier metric over-reported interference for two methodological reasons:

1. agent test edits plus permissive three-way application could make solo validation vacuously pass while the clean merged condition received tests that the solo did not actually exercise;
2. solo conditions and the merged condition were graded against asymmetric test sets, allowing cross-task failures to appear only after composition.

The corrected protocol discards agent test edits, grades every condition on the union test set, and requires both workers to solve their own task before composed breakage is observable.

Therefore the following historical surfaces are explicitly **excluded from capability claims** in the admitted raw record:

- `results/real_delta_blind.jsonl`;
- `results/openhands.jsonl`;
- `results/comm_real.jsonl`;
- `results/readwrite.json`.

They may document measurement history, but they must not be substituted for the corrected mined-real or real-derived evidence.

## Boundary and ownership

The result belongs to the **benchmark-defined parallel-work and information-sharing organization**.

It does not establish native S2 ownership for mini-swe-agent, OpenHands, a model used in the runs, or any canonical Index harness. The benchmark controls the stale-snapshot/composition relation and the communication treatment, so `system_compatibility = benchmark-scaffolded` remains the correct classification.

The raw evidence is first-party reported. OpenSiro has not independently rerun the stochastic model-backed experiments.

## Why the S2 primary does not reopen

The frozen S2 primary-search closure explicitly says not to reopen for another benchmark-scaffolded direct S2 observation without canonical native or adapter-preserved linkage.

This maturation changes provenance depth for an already-counted benchmark family; it does not add a materially matched canonical cell. Squad and thClaws remain the frozen canonical descriptive direct observations, and their surfaces remain heterogeneous.

Therefore the new raw STALE observation cannot satisfy any current reopen route:

- it is not a native or adapter-preserved canonical harness observation;
- it does not form a materially matched cell with an existing canonical direct observation;
- it is not a multi-canonical benchmark comparison with recoverable canonical system provenance.

The correct disposition remains:

```text
S2 primary_baseline: gap
```

## Frozen-state boundary

This review intentionally does **not** modify:

- `vsm-projections/benchmark-family-map/map.json`;
- `vsm-projections/benchmark-family-map/post-closure.json`;
- `vsm-projections/s2/coverage.json`;
- `vsm-projections/s2/observations.json`;
- the frozen S2 primary-search closure;
- `baselines/primary-baselines.json`.

The historical closure still records 8 direct S2 families and 6 frozen direct observations. STALE was already one of those 8 families; the post-closure neutral raw admission matures its evidence provenance without rewriting the frozen six-observation snapshot.

## Non-claims

This review does not claim that:

- the uncorrected historical real-tier metric is valid capability evidence;
- the corrected mined-real corpus has a high semantic-interference rate;
- the real-derived benchmark estimates natural real-world incidence;
- a participating model or task-solving harness owns S2;
- the result is independently reproduced;
- the frozen S2 observation count should be incremented;
- the S2 primary evidence gap is closed.

It claims only that the corrected and explicitly bounded public STALE evidence now has a neutral raw observation supporting the already-existing direct benchmark-scaffolded `stale-semantic-coordination` S2 family.