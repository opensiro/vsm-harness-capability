# WildClawBench — S1 general-capability review

Status: experimental, non-normative.

Tracking issue: #20

Reviewed source:

```text
InternLM/WildClawBench@8e1fde746584ae1a9c49b70526d49a7a572625cd
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

WildClawBench directly exercises an agent harness on end-to-end tasks in live task environments and grades the resulting operational outcome. The measured harness therefore performs the task-level primary transformation itself. Under Profile v0.2.4 this is a direct S1 performance surface, not an inference from a component name or from benchmark vocabulary such as planning, retrieval, safety, verification, or orchestration.

This review classifies the benchmark family only. A concrete displayed harness row still needs independent canonical identity and adapter-boundary provenance before it can become a system-level S1 observation.

## General-scope basis

The pinned benchmark contains 60 original tasks across six categories:

- Productivity Flow;
- Code Intelligence;
- Social Interaction;
- Search / Retrieval;
- Creative Synthesis;
- Safety / Alignment.

The tasks include text and multimodal work, browser/file/bash/API interaction, coding, information synthesis, communication and long-horizon workflows. The benchmark is therefore not restricted to one application vertical such as Coding/SWE or life sciences.

That heterogeneous task distribution is the explicit basis for treating the reviewed family as a **general S1** evidence surface in this repository. `general` means the intended comparison crosses multiple task/application contexts. It does not mean universal task coverage, domain-transfer proof, or a timeless scalar measure of harness quality.

## Matched-harness surface

WildClawBench publishes a harness-comparison surface in which the same GPT-5.4 model executes the same 60-task suite under the same benchmark grading protocol across:

- OpenClaw;
- Claude Code;
- Codex CLI;
- Hermes Agent.

The benchmark supplies a dedicated runtime path for each harness. Public code shows separate first-party-preserving execution adapters rather than display-label-only mappings: OpenClaw runs its CLI/gateway path, Codex invokes `codex exec`, Claude Code uses its dedicated runtime image/path, and Hermes executes its installed agent runtime.

The already-admitted raw observations therefore carry `adapter-preserved` compatibility while preserving the exact historical upstream harness revision as unknown where the benchmark does not publish it.

## Environment and reset limits

The task set and grading protocol are shared, but the benchmark publishes dedicated Docker images per harness. Those harness-specific images are part of the treatment boundary and prevent a claim that every execution-environment byte is identical across systems.

WildClawBench states that each task runs in an isolated Docker container. This supports task-level reset/isolation for the ordinary baseline, while exact hidden package/runtime differences inside the harness-specific images remain part of the harness comparison rather than a separately normalized control.

Budget/repetition details that are not established by the pinned public comparison remain unknown. They must not be filled by inference.

## Function-first non-claims

WildClawBench does not establish:

- S2 from social interaction, communication or multi-step workflow labels;
- S3 from planning or task-management behaviour;
- S3* from verification, grading or safety checking;
- S4 from search, recovery, adaptation or context use inside one task;
- S5 from safety/alignment labels or refusal behaviour;
- experimental self-organizing `S` from ordinary task execution;
- canonical `A`, `C`, `P`, `A(P)`, `C(P)`, `—`, or `?` ownership states from benchmark performance.

The family is direct for S1 because the harness performs end-to-end operational work in the task environment.

## Comparison consequence

The pinned GPT-5.4 four-harness surface is suitable for a secondary machine-readable S1 comparison cell because model, task set and benchmark family/grader are matched while the harness is the intended varying factor.

Unknown or only partially matched dimensions remain explicit in that cell. The cell does not replace the selected PawBench primary and must not be combined numerically with PawBench or other S1 evidence families into a universal score.

## Mutation boundary

This review does not change:

- Profile semantics;
- canonical Index assessments or ownership states;
- the four previously admitted WildClawBench raw observations;
- the selected PawBench S1 primary;
- any domain-specific assessment or capability grade;
- any overall harness ranking.
