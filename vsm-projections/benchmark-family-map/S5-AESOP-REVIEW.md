# Aesop target-project rule evidence — S5 relevance review

Status: experimental, non-normative.

Tracking issue: #88

Reviewed sources:

```text
opensiro/vsm-harness-profile@main (current public Profile)
opensiro/vsm-harness-index/assessments/aesop.md
matt82198/aesop@2a661c12007c5484f964176da3d5532c6bdf070d
system-observations/aesop.json
vsm-projections/s5/post-closure-deltas/live-canonical-cohort-2026-09-29.json
vsm-projections/s5/matched-cell/s5-primary-search-closure.json
BASELINE.md
```

Relevant exact-ref target-project surfaces:

```text
tools/init_project.py
tests/test_init_project.py
skills/power/SKILL.md
tests/demo-e2e.test.mjs
```

Explicitly excluded from this target-project evidence boundary:

```text
Aesop's own LANE-CONTRACT.md development history and other self-repository amendment traces
```

## Result

```text
function: S5
benchmark_fit: mechanism/proxy
system_linkage: canonical-native-mechanism
boundary: target-project CLAUDE.md scaffolding plus declared init-prime/write and already-primed/read procedure, without an executed concrete ultimate-policy amendment through /power
canonical_harness_id: aesop
canonical S5 state: A(P)
direct_descriptive_s5: no
primary_reopen: no
primary_baseline: gap
```

The admitted Aesop observations are useful **S5 mechanism/proxy evidence** at the target-project recursion, but they do not meet the current direct-descriptive S5 threshold.

At the canonical revision, the native project initializer creates a project-root `CLAUDE.md` carrying a project name, a domain map and a dispatch rule. First-party regressions exercise creation, ordinary idempotent non-overwrite, and explicit `force=True` overwrite; the force-overwrite regression verifies that the resulting root file contains the concrete replacement project-name fixture `proj-v2`.

The same revision's `/power` skill defines the stronger semantic lifecycle that matters for S5: on an unprimed target project it instructs the orchestrator to inspect the repository, synthesize project-root and domain `CLAUDE.md` rule state, write a durable `STATE.md`, and commit/push the new layer; on an already-primed target it reads the project-root `CLAUDE.md` as authoritative project rules and proceeds under the loaded dispatch model.

However, the recovered public first-party tests do **not** execute that `/power` synthesis path against a concrete target project and do not verify that a concrete identity/ultimate-policy decision produced through that authority path became the state returned to later operation. The test named `Complete init-prime-demo flow succeeds` does not run `/power`; it scaffolds a harness and checks generated artifacts and basic commands. Treating its name as an executed init-prime policy-change witness would overstate what the test actually does.

The tested `force=True` overwrite does not close the gap by itself. It demonstrates a native parent-invoked replacement mechanism over the authoritative root file, but the concrete changed value asserted by the regression is the scaffold project-name fixture `proj-v2`. The regression does not exercise a concrete project rule, constitutional constraint, standing behavioral policy, or another clearly ultimate-policy-level decision being authored/ratified through the `/power` path and then returned to subsequent governed operation.

Therefore the evidence directly establishes **authoritative file mutation capability plus a structurally coherent policy write/read procedure**, not a direct empirical S5 decision instance.

This review does not re-assess ownership. The canonical Index independently records Aesop S5 as `A(P)`: bounded autonomous amendment exists under a legitimate parent boundary. Capability preserves that canonical state while keeping the current public observation classification separate.

## Function-first mapping

The supported target-project mechanism is:

```text
parent/user invokes project initialization or /power
        ↓
target-project root CLAUDE.md is the durable project rule surface
        ↓
initializer can create / explicitly force-replace that root file
        ↓
/power init-prime procedure can synthesize root + domain CLAUDE.md state
        ↓
already-primed /power procedure reads root CLAUDE.md as authoritative rules
        ↓
later orchestration proceeds under the loaded dispatch model
```

That is substantive S5-adjacent machinery. In particular, it is stronger than a static documentation file because the canonical system includes native creation/replacement logic and a declared later-operation read path over the same target-project rule surface.

The direct-descriptive threshold used by current post-closure admissions requires one further property:

```text
legitimate identity / ultimate-policy decision
        ↓
concrete changed authoritative state through the native decision path
        ↓
durable enactment
        ↓
that same changed policy state returns to subsequent operation
```

The exact-ref evidence does not directly exercise that complete decision instance.

## Why the scaffold regression is not direct S5

`tests/test_init_project.py` is real native evidence and should not be dismissed. It proves that:

- `init_project(...)` creates root `CLAUDE.md` in a target repository;
- the generated root contains a dispatch rule;
- a normal repeat does not overwrite existing state;
- explicit `force=True` does overwrite it;
- the replacement is concretely asserted through `proj-v2`.

But the empirically changed fixture is scaffolding metadata embedded in a fixed template. The test does not show a parent choosing or ratifying a new ultimate project policy. Nor does it show an autonomous Aesop policy proposal being accepted under the parent boundary. A generic ability to replace a policy-bearing file is not equivalent to observing a policy decision at the required semantic level.

Promoting this test to direct S5 solely because `CLAUDE.md` also contains standing rules would collapse the distinction already used elsewhere in Capability between:

- tested transport/configuration machinery; and
- a tested concrete identity/ultimate-policy decision through legitimate authority.

That distinction is why Platypus and superharness remain mechanism/proxy despite strong source-level policy transport paths.

## Why the /power procedure does not complete direct admission

`skills/power/SKILL.md` supplies the missing semantic intent very clearly. Its init-prime path directs Aesop to derive project and domain rule state from repository investigation, write that state durably, and later load it on the already-primed path.

What is missing is execution evidence at the reviewed revision. The recovered tests do not invoke the skill and then assert a concrete synthesized standing rule in the resulting target-project root `CLAUDE.md`. They also do not bind such a changed rule to a later `/power` run or model/agent operation.

Accordingly the review credits `/power` as first-party canonical procedure/source support, but does not transform procedure text into an empirical run.

## The demo E2E naming trap

`tests/demo-e2e.test.mjs` describes itself as an `init-prime-demo` flow and contains a final test named:

```text
Complete init-prime-demo flow succeeds
```

The executed body does not run `/power`. It:

- creates a toy repository;
- scaffolds an Aesop fleet harness;
- checks generated config/state surfaces;
- checks the generated `CLAUDE.md`;
- exercises basic doctor/watchdog invocation; and
- verifies expected scaffold artifacts exist.

That is useful installation evidence, but not a `/power` target-project policy-synthesis witness. The semantic classification therefore follows executed behavior, not the test label.

## Recursion boundary: why LANE-CONTRACT.md is excluded

Aesop's own repository contains richer governance/change history, including `LANE-CONTRACT.md`. That history concerns development and governance of the **Aesop repository itself**.

The canonical assessment considered Aesop's S5 at the target-project recursion: the project-level rule/identity surface that Aesop initializes, amends and later consumes while operating on another project. Importing self-repository contract amendments as if they were enacted target-project policy would cross recursion boundaries and manufacture a stronger target-project observation than the public evidence supplies.

This review therefore preserves the earlier cohort safeguard: self-repository development traces are not used to close the target-project direct S5 path.

## Why this is mechanism/proxy rather than no-fit

`no-fit` would understate the evidence. Aesop has a coherent canonical S5 mechanism at the target-project recursion:

- durable project-root and domain `CLAUDE.md` rule surfaces;
- native project initialization that creates and can explicitly replace the root surface;
- ordinary non-overwrite protection unless force is requested;
- a first-party `/power` init-prime procedure for synthesizing project policy/context state;
- a first-party already-primed procedure that reads the root state as authoritative rules;
- canonical parent legitimacy and bounded autonomous amendment reflected by `S5=A(P)`.

Those are real mechanisms for forming and carrying project identity/policy state. The public evidence simply stops short of a direct executed concrete ultimate-policy decision instance under the current Capability threshold.

## Relationship to direct S5 precedents

The distinction is visible against currently admitted direct descriptive cases:

- **Waku**: a concrete SOUL/standing-rule value is changed through the shipped mutation path, exact durable bytes are asserted, and the same canonical runtime rereads that SOUL state into later system context.
- **Polyphemus**: a concrete proposed root `AGENTS.md` value (`Real rules.`) is accepted through the actual keep/accept authority path and asserted in the authoritative file; later session construction rereads that same root surface.
- **Aesop** here: the concrete native mutation regression proves scaffold replacement (`proj-v2`), while the semantically stronger rule-synthesis/return path is specified in `/power` procedure text but not executed by the recovered tests.

The gap is therefore evidentiary, not architectural.

## S5 reopen gate

Because #88's Stage 2 result is not direct, it is not admitted as a new live direct S5 observation and does not enter the frozen primary reopen comparison.

Therefore:

```text
new direct canonical S5 observation: no
canonical target-project S5 mechanism: yes
concrete native root CLAUDE.md mutation: yes, scaffold/template replacement
concrete executed identity/ultimate-policy amendment: no
executed /power policy synthesis witness: no
same changed policy empirically returned to later operation: no
materially matched cross-harness protocol: not evaluated for promotion
primary_reopen: no
S5 primary_baseline: gap
```

No comparison cell is created by combining the scaffold mutation regression with the unexecuted `/power` procedure or with Aesop's self-repository governance history.

## Machine-readable placement

Stage 1 records the factual target-project surfaces in:

```text
system-observations/aesop.json
system-observations/registry.psv
system-observations/REGISTRY.md
```

This Stage 2 review adds **no** direct entry to:

```text
vsm-projections/benchmark-family-map/post-closure.json
vsm-projections/s5/post-closure-deltas/
```

The direct post-closure registry remains reserved for admitted direct additions. Adding Aesop there under the current evidence would contradict the fail-closed disposition above.

## Mutation boundary

This review does not modify:

- Stage 1 neutral Aesop observations;
- the historical live-canonical-cohort snapshot;
- the frozen S5 family map;
- `vsm-projections/s5/coverage.json`;
- frozen `vsm-projections/s5/canonical_observations.json`;
- the frozen S5 primary-search closure;
- `baselines/primary-baselines.json`;
- canonical Index ownership/state;
- Profile semantics or Skills methodology.

## Reassess if

Re-open Aesop's semantic disposition if first-party public evidence at the relevant supported target-project boundary supplies a concrete native witness such as:

```text
parent-authorized /power init-prime or amendment
        ↓
concrete identity / standing-policy rule X is synthesized or changed
        ↓
root/domain CLAUDE.md durably contains X
        ↓
later /power / orchestration operation rereads X as authoritative state
```

A single monolithic test is not mandatory if first-party evidence concretely binds the same changed policy state across the legitimate decision, persistence and later-operation boundary. What is not sufficient is another scaffold-name replacement, an independently written fixture, stronger prose describing `/power`, or Aesop-self contract history at a different recursion.

## Non-claims

This review does not claim that:

- Aesop lacks S5 structurally;
- Aesop lacks bounded autonomous amendment;
- target-project `CLAUDE.md` is not a policy-bearing surface;
- the `/power` init-prime or already-primed paths are fictional;
- a later Aesop operation would fail to use project rules;
- explicit parent `--force` authority is irrelevant;
- every project-name change is necessarily below S5 in every context;
- Aesop's own `LANE-CONTRACT.md` history is invalid evidence for questions at the Aesop-self recursion;
- the S5 primary evidence gap is closed.

It claims only that, at `matt82198/aesop@2a661c12007c5484f964176da3d5532c6bdf070d`, first-party public evidence directly exercises target-project rule scaffolding/replacement and separately specifies a coherent `/power` policy write/read lifecycle, but does not execute a concrete identity/ultimate-policy amendment through that lifecycle and return the same changed decision to later operation. Under #88, that is mechanism/proxy rather than direct descriptive S5.
