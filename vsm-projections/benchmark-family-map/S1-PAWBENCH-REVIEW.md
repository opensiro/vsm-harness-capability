# PawBench v1.0 — S1 general-capability review

Status: experimental, non-normative.

Tracking issue: #18

Reviewed source:

```text
agentscope-ai/PawBench@0f794a8bb6c27aa9ee4091b2691fa30e4ed9cc8f
```

Profile basis:

```text
opensiro/vsm-harness-profile v0.2.4
```

## Result

```text
function: S1
fit: direct
scope: general
system_linkage: observation-specific
```

PawBench directly exercises the operational loop of an agent harness on end-to-end tasks and grades the resulting task outcome. Under Profile v0.2.4, that is an S1 performance surface: the harness is performing the primary transformation in a relevant task environment rather than merely exposing a component label, tool call, planner, reviewer or controller.

This review classifies the benchmark family only. Canonical S1 existence and ownership for a concrete harness remain separate Index facts, and a displayed PawBench harness row requires its own identity/provenance review before it can become a system observation.

## Why the selected scope is general

PawBench v1.0 contains 150 tasks assembled from multiple benchmark families and self-built tasks. Its published taxonomy spans several application contexts rather than a single vertical, including:

- office productivity and automation;
- software engineering;
- information retrieval;
- safety alignment;
- long-horizon skill/domain automation;
- text and multimodal tasks;
- closed reproducible and open live-service environments.

The source corpus includes `claweval`, `qwenclawbench`, `pinchbench`, `skillsbench`, `wildclawbench`, and PawBench self-built tasks.

That breadth is the explicit basis for treating the selected PawBench comparison cell as a **general S1 capability** surface in this experimental repository. `general` here means that the comparison claim is intentionally cross-domain and supported by a heterogeneous task distribution. It does **not** mean universal task coverage, a global harness-quality score, or proof that the observed ordering transfers to every application domain.

## Matched-harness design

PawBench is explicitly designed as a model × harness co-evaluation benchmark. It can hold the model fixed while varying the harness across the same task suite and grading surface.

The selected current primary cell uses:

```text
model: qwen3.6-35b-a3b
tasks: 150
harnesses:
  - QwenPaw
  - OpenClaw
  - Hermes Agent
```

The corresponding raw observations and comparison cell retain the empirical payload and historical harness identity. This family review does not duplicate those scores.

The benchmark controls task/environment setup and grading while the admitted rows preserve the corresponding first-party harness runtime behind that evaluation membrane. Those system-level rows are therefore reviewed separately as `native-system` or `adapter-preserved`; benchmark-family fit alone does not grant that compatibility class.

## Frozen-repertoire compatibility

The selected baseline already records the available task-isolation evidence and unknowns. This family review does not strengthen that provenance by inference.

Ordinary S1 capability permits within-task reasoning, tool use, retry and recovery, but persistent cross-task repertoire improvement must not be silently credited into the ordinary baseline. If later PawBench evidence changes the reset/adaptation boundary, comparability must be re-reviewed rather than assumed.

## Function-first non-claims

PawBench task and slice labels do not redefine VSM functions.

In particular:

- `Planning` does not establish S3;
- `Self_Verification` does not establish S3*;
- `Skill_Use` does not establish S4 or experimental self-organizing `S`;
- orchestration-labelled tasks do not establish S2 or S3 ownership;
- safety-labelled tasks do not establish S5;
- benchmark performance does not determine `A`, `C`, `P`, `A(P)`, `C(P)`, `—`, or `?` ownership states.

PawBench is direct for S1 because it measures operational task execution by the harness, not because of those vocabulary labels.

## Generality non-claim

Cross-domain breadth is enough to support the repository's current general S1 comparison view, but it is not evidence for a timeless or universal scalar capability.

The selected PawBench primary must therefore remain one evidence-family view. It must not be numerically averaged with Coding/SWE, scientific, or other evidence families into a single harness-wide score.

## Mutation boundary

This review materializes the semantic basis already assumed by the selected PawBench S1 primary. It does not change:

- Profile semantics;
- canonical Index assessments or ownership states;
- PawBench raw observations or scores;
- the selected S1 primary;
- comparison-cell results;
- any domain-specific assessment.
