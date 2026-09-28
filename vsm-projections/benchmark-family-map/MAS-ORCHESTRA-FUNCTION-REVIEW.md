# MAS-Orchestra — VSM-function relevance review

Status: experimental, non-normative.

Tracking issue: #46

Reviewed sources:

```text
opensiro/vsm-harness-profile@88d865f46ac93ec03b8fe0d58ef45054a64cead5
SalesforceAIResearch/MAS-Orchestra@0527c70a508eb49ed42d5dd49a91ea857551e242
arXiv:2601.14652
https://www.salesforceairesearch.com/mas-orchestra
system-observations/mas-orchestra.json
```

Profile basis:

```text
VSM Harness Profile v0.2.4
```

## Result

```text
S1: direct relevance at the end-to-end operational-outcome boundary
S2: unsuitable for direct attribution from the admitted observation
S3: unsuitable for direct attribution from the admitted observation
S3*: unsuitable for direct attribution from the admitted observation
S4: unsuitable for direct attribution from the admitted observation
S5: unsuitable for direct attribution from the admitted observation

machine_s1_projection_added: no
comparison_cell_added: no
post_closure_registration: no
primary_reopen: no
```

The admitted MAS-Orchestra observation is useful direct **S1 performance evidence** at the measured whole-system task-execution boundary, but it does not directly isolate S2, S3, S3*, S4 or S5 capability.

## S1 — direct operational relevance

The Profile defines S1 as the operational capability through which the system enacts its primary transformation. The admitted MAS-Orchestra result surface measures the assembled system producing final task outcomes on:

- AIME24;
- AIME25;
- HotpotQA;
- BrowseComp+;
- GPQA.

Those are end-to-end operational result surfaces. The measured system is not merely inspected for the presence of a planner, manager, router or training mechanism; it is evaluated on whether the resulting organization solves the task.

Therefore the function-first path is:

```text
input task / task environment
        ↓
MAS-Orchestra constructs and executes a task-specific multi-agent organization
        ↓
sub-agent work is combined into the system's task outcome
        ↓
benchmark grades the resulting operational output
```

That is direct S1 relevance at this declared measured boundary.

### Scope limitation

The five published rows span mathematical reasoning, multi-hop question answering and search-based question answering, including an OOD GPQA result. This is broader than one narrow application benchmark, but it is not treated here as a universal or selected general S1 baseline.

The public study uses task-specific training/checkpoint surfaces and heterogeneous benchmark definitions. The admitted observation does not establish a materially matched cross-harness cell in which the same model/configuration is held fixed while multiple canonical harnesses are varied.

The current machine-readable S1 projection path also requires canonical Index linkage and the existing single-benchmark/result raw schema. MAS-Orchestra is currently non-canonical and the neutral observation intentionally preserves one multi-benchmark publication surface. This review therefore does not weaken or rewrite the S1 projection contract merely to force this observation into `vsm-projections/s1/observations.jsonl`.

Consequently:

```text
direct S1 relevance: yes
canonical S1 system linkage: no
machine S1 observation projection: no
new S1 comparison cell: no
selected PawBench primary: unchanged
```

A future infrastructure task may generalize machine-readable S1 projection for non-canonical multi-benchmark observations if that is useful across more than one case. Such a change should be reviewed independently from this evidence interpretation.

## S2 — no direct disturbance-to-attenuation result

MAS-Orchestra composes multiple sub-agents and the broader MASBENCH study examines task structures including parallel and robustness conditions. However, the currently admitted observation is the public five-benchmark outcome table, not an isolated inter-operational-unit interference experiment.

The Profile requires a positive S2 mapping to identify distinct operational units, a specific interference/conflict/oscillation, a relation that attenuates that disturbance, and closure back into subsequent operational behaviour.

The admitted rows report final task scores. They do not isolate a concrete inter-S1 disturbance and a measured attenuation treatment. Multi-agent communication, parallelism or coordination vocabulary is therefore insufficient for direct S2 attribution.

## S3 — orchestration is not automatically current control

MAS-Orchestra is explicitly designed for holistic orchestration. The trained orchestrator can generate an entire task-specific multi-agent design at once, selecting decomposition and sub-agent structure rather than building the system incrementally.

That is strong evidence for an orchestration mechanism, but the Profile explicitly rejects the shortcut `orchestrator/manager/delegation -> S3`. S3 requires whole-system current-operational regulation with relevant authority over resources, commitments, priorities or constraints; task allocation counts only when it is part of that regulation rather than ordinary decomposition of the parent task.

The admitted five-benchmark result does not isolate:

- a current whole-system exception or resource/commitment disturbance;
- a specific S3 decision right exercised over ongoing operations;
- a matched treatment showing that current-control intervention and its subsequent organizational effect;
- an owner/support decomposition for such a decision.

The paper's task-conditioned generation of a MAS may contain mechanisms that could participate in S3 under another declared boundary, but the published aggregate task scores do not directly measure that function.

Therefore:

```text
direct S3 family from this observation: no
S3 post-closure addition: no
S3 primary reopen: no
```

## S3* — verification effects do not establish complementary audit

The publication reports that MAS benefits depend partly on verification protocols, and some generated organizations may use verification/moderation behavior. That does not by itself establish S3*.

The admitted observation does not isolate a materially independent complementary-access path that challenges ordinary operational reporting and then returns findings into subsequent control. Benchmark grading is an external evaluation membrane, not automatically a system-owned complementary audit function.

Therefore no direct S3* family is registered from this observation.

## S4 — training and OOD generalization are not automatically outside-and-then intelligence

MAS-Orchestra uses reinforcement learning at training time and publishes OOD GPQA performance. Those facts are relevant to learned capability, but the Profile explicitly states that generic learning, self-improvement or training is not S4 by itself.

A direct S4 mapping requires an external-and-prospective loop:

```text
external / future-relevant distinctions
        ↓
prospective adaptation options
        ↓
selection / development of an adaptation
        ↓
return into later present capability
```

The admitted observation instead records a post-training benchmark result surface for trained orchestrator checkpoints. It does not separately measure a prospective adaptation cycle in which environmental/future distinctions generate organizational options and those options return into later operation.

OOD generalization is evidence that the trained system can perform outside an IID training surface; it is not, without the missing adaptation path, direct evidence that the operating system performs S4.

Therefore:

```text
direct S4 family from this observation: no
S4 post-closure addition: no
S4 primary reopen: no
```

A separate raw observation focused on a public training/adaptation experiment could receive an independent S4 review if it exposes a reconstructable external/prospective adaptation path rather than only final trained-model performance.

## S5 — no identity or ultimate-policy closure

The admitted result surface measures task execution and learned orchestration. It does not expose an identity- or ultimate-policy-level decision path with legitimate authority and return into subsequent operation. No S5 attribution follows.

## Comparison consequence

The published paper compares MAS-Orchestra with standalone agents and several orchestration baselines, but those rows are not a Capability comparison cell under the current contract merely because they appear in one table. The compared systems use different orchestration methods and, in several cases, materially different model/configuration surfaces.

The table remains useful first-party empirical context. It is not normalized into PawBench, WildClawBench or another existing S1 family, and it is not converted into a universal harness score.

## Mutation boundary

This review changes no empirical payload and does not modify:

- `system-observations/mas-orchestra.json`;
- `vsm-projections/benchmark-family-map/map.json`;
- `vsm-projections/benchmark-family-map/post-closure.json`;
- any S2-S5 frozen primary-search closure;
- `baselines/primary-baselines.json`;
- the generated evidence frontier;
- Profile semantics;
- Skills methodology;
- canonical Index state.

## Non-claims

This review does not claim that:

- MAS-Orchestra lacks coordination, control or adaptation mechanisms;
- its reinforcement-learning procedure is ineffective;
- its OOD result is not meaningful;
- holistic orchestration can never participate in S3;
- training-time learning can never participate in S4;
- MASBENCH cannot support separate function-specific observations if stronger isolated evidence is admitted later.

It claims only that the **currently admitted five-benchmark publication observation** directly supports S1 operational performance while not isolating direct S2-S5 capability under Profile v0.2.4.
