# DotCraft Agent Profile enactment — S5 relevance review

Status: experimental, non-normative.

Tracking issue: #61

Reviewed sources:

```text
opensiro/vsm-harness-profile@main (Profile v0.2.4)
opensiro/vsm-harness-index/assessments/dotcraft.md
DotHarness/dotcraft@a08c8b35497f6ba9148f6ede80839835dcc8812a
system-observations/dotcraft.json
vsm-projections/s5/matched-cell/s5-primary-search-closure.json
```

## Result

```text
function: S5
benchmark_fit: direct
system_linkage: canonical-native-descriptive
boundary: parent-authored Agent Profile -> resolved native thread runtime contract
canonical_harness_id: dotcraft
canonical S5 state: P
primary_reopen: no
primary_baseline: gap
```

The admitted DotCraft observation is direct **descriptive S5 capability evidence at the native profile-to-thread enactment boundary**. The canonical Index assessment independently establishes the owner: a legitimate parent operator authors, saves and selects Agent Profiles, while DotCraft runtime mechanisms resolve and enforce the selected profile. The integration test at the exact canonical review revision demonstrates that this durable policy is returned into a new native thread configuration and persists after the source profile is removed.

This review does not infer autonomous S5 ownership. DotCraft remains canonical `S5=P` unless the Index independently changes that assessment.

## Function-first mapping

The direct fit comes from the exercised authority/change/return path, not from the existence of a profile file:

```text
parent-authored durable Agent Profile
        ↓
profile carries role + tool + approval policy
        ↓
parent selects profile for a new native DotCraft thread
        ↓
DotCraft resolves the profile into the persisted thread runtime contract
        ↓
role instructions + denied tool + approval policy are present in that contract
        ↓
source profile is removed
        ↓
thread reread retains the enacted profile identity/fingerprint/role state
```

The current Profile requires identity/ultimate-policy-level authority, legitimate ownership, an actual decision/change path, separation of ownership from enforcement, and return into subsequent operation. At the declared DotCraft recursion:

1. **policy level** — Agent Profiles define durable role, instructions, model/runtime defaults, capability policy and approval behavior for subsequent work;
2. **legitimate authority** — the canonical assessment assigns authoritative save/edit/select rights to the parent operator, not to the child thread;
3. **actual enactment** — the test creates `reviewer-lite`, selects it on `ThreadStart`, and observes the resolved runtime configuration;
4. **ownership/enforcement separation** — the parent-authored profile supplies the policy while DotCraft compilation, thread configuration, tool filtering and approval machinery support enforcement;
5. **return and persistence** — the selected policy is materialized into a native thread snapshot and remains there after the source profile is deleted.

That is stronger than a static profile schema, CRUD test, or policy parser. A concrete durable policy is selected and enacted into a subsequent native runtime object.

## Evidence limitation

The observation is still a **controlled integration-test witness**, not a production-history or benchmark outcome.

The test stops after the native thread configuration is created and reread. It does not send a subsequent model turn or attempt `WriteFile` to produce an observable denial under the enacted policy. The first-party Agent Profile specification states that the persisted thread configuration is the runtime contract and that agents, tool filtering, approvals and prompt rendering consume it, but that specification is mechanism evidence rather than an additional empirical result.

Therefore the narrow direct claim is:

```text
parent policy was enacted into and persisted as the native runtime contract
```

not:

```text
a public task run demonstrated downstream behavioral impact under that policy
```

## Relationship to Ouroboros and the S5 reopen gate

The frozen S5 closure contains one canonical direct observation, Ouroboros PR #855. DotCraft now adds another canonical native descriptive S5 observation, but the two evidence surfaces are not materially matched enough to reopen the primary:

- **Ouroboros**: immutable repository-history witness of a parent-governed constitutional/runtime policy change, owner enactment, executable return and persistence into later canonical lineage;
- **DotCraft**: controlled integration-test witness of a parent-authored Agent Profile being compiled into a persisted native thread runtime contract, without a subsequent public task/tool execution result.

They share the abstract parent-authority → changed policy → returned runtime-state shape, but differ materially in intervention, execution and observation surface. Treating them as one matched cross-harness cell would erase those differences.

The frozen closure explicitly says not to reopen for another heterogeneous single-system descriptive policy-change witness that cannot be materially compared with the existing canonical observation.

Therefore:

```text
new live direct canonical S5 observation: yes
second materially comparable canonical S5 surface: no
matched multi-canonical protocol: no
primary_reopen: no
S5 primary_baseline: gap
```

A future DotCraft public witness that executes a task/tool path after profile enactment, or a common adapter-preserved authority/change/subsequent-operation protocol exercised across DotCraft and another canonical S5 system, could justify a new closure review.

## Machine-readable placement

This observation is intentionally not inserted into frozen `vsm-projections/s5/canonical_observations.json`, because that file and its validator encode the historical S5 closure snapshot.

The live addition is represented through:

```text
vsm-projections/benchmark-family-map/post-closure.json
vsm-projections/s5/post-closure-deltas/dotcraft-agent-profile-enactment-2026-09-29.json
```

Here `benchmark_id` is the generic post-closure identity field; this review does **not** claim the DotCraft integration test is a benchmark family.

## Mutation boundary

This review does not modify:

- the frozen S5 family map;
- `vsm-projections/s5/coverage.json`;
- frozen `vsm-projections/s5/canonical_observations.json`;
- the frozen S5 primary-search closure;
- `baselines/primary-baselines.json`;
- canonical Index ownership/state;
- Profile semantics or Skills methodology.

## Non-claims

This review does not claim that:

- DotCraft has autonomous S5 ownership;
- the integration test is a production deployment history or cross-harness benchmark;
- the test directly observes a model turn or tool denial after profile enactment;
- DotCraft and Ouroboros are materially matched enough to form a primary comparison;
- the S5 primary evidence gap is closed.

It claims only that, at the exact canonical DotCraft revision, first-party native integration evidence exercises a parent-owned durable profile being selected, compiled into the thread runtime contract and persisted for subsequent operation, which is direct descriptive S5 evidence at that declared boundary.