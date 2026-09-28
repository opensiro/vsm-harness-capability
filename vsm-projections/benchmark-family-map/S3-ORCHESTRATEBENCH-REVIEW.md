# OrchestrateBench policy-conditioned containment — S3 relevance review

Status: experimental, non-normative.

Tracking issue: #49

Reviewed sources:

```text
opensiro/vsm-harness-profile@88d865f46ac93ec03b8fe0d58ef45054a64cead5
anote-ai/Research-OrchestrateBench@5c3738c19d99cbe9aa152b0ea9b7d903ea4f93db
arXiv:2608.05263
system-observations/orchestratebench.json
```

Profile basis:

```text
VSM Harness Profile v0.2.4
```

## Result

```text
function: S3
benchmark_fit: direct
system_linkage: benchmark-scaffolded-noncanonical
boundary: benchmark-defined policy-conditioned current-control organization
primary_reopen: no
primary_baseline: gap
```

The admitted OrchestrateBench policy-conditioned containment study is direct **S3 capability evidence at the benchmark-defined control boundary**. It does not establish autonomous S3 ownership for Claude, a native deployed multi-agent system, or any canonical harness.

## Function-first mapping

The relevant measured path is not the benchmark's use of the words `orchestration`, `router`, or `recovery`. The direct fit comes from the concrete current-control relation:

```text
staged current operation
        ↓
benchmark injects a current failure/disturbance
        ↓
current-state distinction reaches the policy
        ↓
policy has a bounded right to revise the failed stage result
        ↓
revised result returns into later dependent stages
        ↓
downstream recovery / cascade provides observable closure
```

This satisfies the Profile's structural S3 requirements at the declared benchmark-defined boundary:

1. **current operation exists** — the measured system is already executing a staged dependency chain;
2. **a present disturbance matters to the larger operation** — a corrupted or ambiguous stage result can propagate into downstream commitments;
3. **the control path receives a current-state distinction** — the strongest LLM policy is explicitly supplied a trusted upstream value;
4. **the policy has an intervention right** — it may re-attempt and replace the failed stage result rather than merely observe it;
5. **the intervention returns into subsequent operation** — later stages consume the revised result;
6. **closure is measured** — the committed study records recovery and downstream cascade rather than only local classifier accuracy.

The intervention is therefore more than ordinary task decomposition or a static workflow. It regulates an already-running operation after a current exception appears.

## Trusted-state support is not autonomous ownership

The trusted-state ablation is essential to the interpretation. When the same correction-style LLM re-attempt is deprived of the trusted upstream state, the reported recovery gain collapses close to baseline. The paper itself therefore attributes most of the apparent containment benefit to the supplied trusted-state distinction rather than to autonomous fault detection.

That does **not** remove the S3 functional fit at the benchmark-defined composed boundary. S3 may be distributed across a decision path, and the Profile requires separating decision ownership from supporting sensing/enforcement machinery. Here:

- benchmark construction and failure injection supply the disturbance;
- the trusted upstream value supplies supporting current-state information;
- the LLM policy chooses a revised stage output under that information;
- later dependency-chain execution transports the returned decision and exposes its effect;
- the external benchmark grader measures closure.

The correct claim is therefore **direct benchmark-scaffolded S3 capability**, not autonomous native S3 ownership.

## Why this is stronger than an S3 proxy

A broad end-task orchestration score would remain proxy evidence because it would not isolate a current-control intervention. This observation instead contains a policy-conditioned treatment in which the relevant intervention repertoire changes while the controlled failure surface and staged workload are recoverable from committed artifacts.

The study directly measures whether the current-control treatment contains a disturbance and changes subsequent organizational outcome. That is the distinguishing feature that moves this surface beyond ordinary orchestration-performance proxy evidence.

## Boundary limitations

The direct fit is deliberately narrow:

- the organization is authored by the benchmark;
- the real measured run uses one Claude model over a controlled staged arithmetic dependency chain;
- failure modes are benchmark-injected;
- the strongest LLM treatment receives externally supplied trusted upstream state;
- the study is not evidence that a deployed MAS autonomously discovers its own current-control exceptions;
- no canonical Index harness is linked to this observation;
- no native canonical harness S3 implementation is exercised by the measured policy arms.

Accordingly, the direct S3 attribution belongs to the **benchmark-defined policy + supplied-state + staged-operation boundary**, not to any component in isolation.

## Relationship to the frozen S3 coverage review

The frozen S3 coverage already recorded `orchestrabench-failure-recovery-candidate` as `candidate-direct`, with the blocker that an authoritative public implementation/result source had not been recovered.

The first-party repository at the pinned revision now supplies:

- the real-Claude measurement implementation;
- committed measured policy CSVs;
- the paper table/analysis path;
- reproducibility documentation;
- a trusted-state ablation that clarifies what the treatment actually controls.

This resolves the old **public provenance / measured-boundary** blocker. It does not rewrite the frozen coverage artifact; the new evidence is represented as a Capability-native post-closure addition.

## Primary-baseline disposition

The S3 primary-search closure requires materially matched evidence across two or more canonical systems through their own native or adapter-preserved S3 paths before reopening.

OrchestrateBench supplies none of those missing properties:

```text
canonical harness linkage: no
multiple canonical systems: no
native canonical S3 paths active: no
materially matched cross-harness cell: no
```

The existing closure also explicitly says not to reopen for another direct composed or benchmark-scaffolded S3 observation without canonical native or adapter-preserved linkage.

Therefore:

```text
new live direct S3 family: yes
primary_reopen: no
S3 primary_baseline: gap
```

## Mutation boundary

This review does not modify:

- the frozen `benchmark-family-map/map.json`;
- the frozen `vsm-projections/s3/coverage.json` counts;
- the frozen S3 primary-search closure;
- `baselines/primary-baselines.json`;
- any canonical Index assessment;
- Profile semantics or Skills methodology.

The live addition is recorded only through the post-closure extension registry and its S3 delta.

## Non-claims

This review does not claim that:

- Claude autonomously owns S3;
- the trusted upstream signal is generated by an autonomous S3* path;
- OrchestrateBench is a native production multi-agent organization;
- the benchmark measures all aspects of S3;
- current public evidence supports a cross-harness S3 ranking;
- the S3 primary gap is closed.

It claims only that the admitted policy-conditioned containment study directly exercises a benchmark-defined current-control relation whose intervention changes subsequent operation, while the decisive current-state support remains externally supplied and the system remains non-canonical.