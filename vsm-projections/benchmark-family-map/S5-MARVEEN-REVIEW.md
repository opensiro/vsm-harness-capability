# Marveen installation identity mutation — S5 relevance review

Status: experimental, non-normative.

Tracking issue: #67

Reviewed sources:

```text
opensiro/vsm-harness-profile@main (Profile v0.2.4)
opensiro/vsm-harness-index/assessments/marveen.md
Szotasz/marveen@b3f6574a76488b3367b26684f9065acca695a00f
Szotasz/marveen PR #615 / 6b6b8c960da18f25dc8a70a887b8ca0953a3dd5f
Szotasz/marveen PR #758 / 12890105aed9f76d8d19a742f90c988e8799767f
system-observations/marveen.json
vsm-projections/s5/matched-cell/s5-primary-search-closure.json
vsm-projections/benchmark-family-map/S5-DOTCRAFT-REVIEW.md
vsm-projections/benchmark-family-map/S5-HUGAGENTOS-REVIEW.md
BASELINE.md
```

## Result

```text
function: S5
benchmark_fit: direct
system_linkage: canonical-native-descriptive
boundary: parent-owned installation identity mutation -> durable persona/display state -> native runtime identity readback
canonical_harness_id: marveen
canonical S5 state: P
primary_reopen: no
primary_baseline: gap
```

The admitted Marveen observation is direct **descriptive S5 capability evidence at the canonical installation-identity enactment boundary**. The first-party live-install witness exercises a parent-facing identity decision that changes durable assistant display/persona state while deliberately preserving the installation's internal plumbing identifiers. A later first-party repair on the same canonical lineage makes the changed display identity visible through native runtime label routes via fresh per-call reads.

This review does not infer autonomous S5 ownership. The canonical Index assessment independently classifies Marveen S5 as `P`; Capability preserves that ownership fact rather than re-assessing it.

## Function-first mapping

The direct fit comes from the exercised identity-change and return path, not from the existence of persona files, an onboarding form, or a skill named `self-rename`:

```text
parent owner chooses installation identity
        ↓
identity-save path mutates durable display/owner/persona state
        ↓
internal MAIN_AGENT_ID / SERVICE_ID plumbing remains stable
        ↓
changed identity persists in installation state
        ↓
later canonical runtime uses fresh identity readers
        ↓
changed display identity is returned on native runtime label routes
```

At the declared Marveen installation recursion, the current Profile requires an identity- or ultimate-policy-level decision path, legitimate authority, ownership/enforcement separation, and return into subsequent operation. The admitted evidence supports the narrow descriptive mapping:

1. **identity level** — the owner-facing installation path changes the assistant's durable displayed identity and persona state rather than an ordinary task parameter;
2. **legitimate parent authority** — the canonical assessment assigns ultimate identity authority to the parent owner (`P`); the empirical witness exercises the owner-facing onboarding/admin path rather than a child runtime independently redefining its own ultimate identity;
3. **actual enactment** — PR #615 reports a live test installation where `BRAND_NAME`, `OWNER_NAME`, `IDENTITY_CONFIRMED` and `CLAUDE.md` persona content change, with the previous persona token reduced to zero occurrences;
4. **identity/plumbing separation** — `MAIN_AGENT_ID`, `SERVICE_ID` and tmux session names remain unchanged in the services-up live test, so the semantic/display identity change is not confused with transport/service identifiers;
5. **return path** — commit #758, an ancestor of the exact canonical assessment revision, adds fresh per-call identity readers to native label routes and reports isolated E2E verification that a newly saved display name is visible there before a process restart;
6. **ownership/enforcement separation** — the parent supplies the semantic identity choice; the onboarding endpoint, durable files/env state, validation logic and fresh-read helpers transport, persist and expose that decision but do not become the owner of it.

That is stronger than a static persona file, rename procedure, CRUD schema or validation test because a concrete identity change is exercised on a live installation and the same canonical lineage supplies a native runtime readback path for the changed identity.

## Evidence boundary and recursion

The credited boundary is the **installed Marveen system**, not the upstream repository-development organization.

The live PR #615 verification occurred on a test installation and is admissible because it exercises the product's installation identity path. This review does not treat maintainer choices about the Marveen repository, release naming, commit authorship or product branding as the installed system's S5.

The shipped `seed-skills/self-rename/SKILL.md` is also not promoted into the empirical observation. It documents a supported owner-triggered procedure and helps explain the construction, but the public PR #615 live verification did not establish that the shipped skill itself was the actor that executed the observed rename. The direct evidence therefore rests on the exercised parent-facing identity mutation and native readback path, not on the name or existence of that skill.

## Evidence limitation

The public witness does **not** run a later model turn after the persona mutation and measure whether the model talks or acts differently under the changed `CLAUDE.md` identity. It also does not provide a downstream task score under the new identity.

The later #758 evidence is narrower: native runtime label routes fresh-read the changed display identity immediately. This is enough for a descriptive identity **return-to-runtime** claim, but not for a behavioral-compliance claim about the model.

Therefore the narrow direct claim is:

```text
parent-owned installation identity was changed durably and returned through native runtime identity-readback surfaces
```

not:

```text
a subsequent public model task demonstrated behavioral compliance with the changed persona
```

## Relationship to DotCraft, HugAgentOS, Ouroboros and the S5 reopen gate

Marveen adds another canonical native descriptive S5 witness, but it does not satisfy the frozen primary reopen condition.

The current live/frozen witnesses have only an abstract authority/change/return shape in common:

- **Marveen**: parent-owned installation display/persona identity mutation plus native runtime identity readback;
- **DotCraft**: parent-authored Agent Profile selected and resolved into a persisted thread runtime contract;
- **HugAgentOS**: authorized durable project rules persisted and returned through native project-context assembly;
- **Ouroboros**: immutable repository-history witness of a parent-governed constitutional/runtime policy change with executable return and later canonical lineage.

These surfaces differ materially in policy object, intervention, execution path and observation protocol. They do not hold constant a common evidence family/version, authority/change treatment, task/evaluator, execution environment or reset/adaptation policy. Treating them as one matched primary cell would manufacture comparability from structural analogy.

Therefore:

```text
new live direct canonical S5 observation: yes
canonical native linkage: yes
second materially comparable canonical S5 surface: no
matched multi-canonical authority/change/subsequent-operation protocol: no
primary_reopen: no
S5 primary_baseline: gap
```

A future common authority/change/subsequent-operation protocol exercised across Marveen and another canonical S5 system — or adapter-preserved rows from an existing direct family — would justify deliberate closure review.

## Machine-readable placement

This observation is intentionally not inserted into frozen `vsm-projections/s5/canonical_observations.json`, because that file and its validator encode the historical S5 closure snapshot.

The live addition is represented through:

```text
vsm-projections/benchmark-family-map/post-closure.json
vsm-projections/s5/post-closure-deltas/marveen-installation-identity-mutation-2026-09-29.json
```

Here `benchmark_id` is the generic post-closure identity field; this review does **not** claim the Marveen live-install witness is a benchmark family.

## Mutation boundary

This review does not modify:

- the frozen S5 family map;
- `vsm-projections/s5/coverage.json`;
- frozen `vsm-projections/s5/canonical_observations.json`;
- the frozen S5 primary-search closure;
- `baselines/primary-baselines.json`;
- canonical Index ownership/state;
- Profile semantics or Skills methodology;
- neutral raw evidence admitted in Stage 1.

## Non-claims

This review does not claim that:

- Marveen has autonomous S5 ownership;
- the shipped `self-rename` skill executed the PR #615 live-install witness;
- Claude Code `/rename`, `MAIN_AGENT_ID`, `SERVICE_ID` or upstream repository-maintainer naming changes are part of the credited observation;
- a later model turn or public task demonstrated behavioral compliance with the changed persona;
- the test installation is production deployment history;
- Marveen, DotCraft, HugAgentOS and Ouroboros are materially matched enough to select an S5 primary;
- the S5 primary evidence gap is closed.

It claims only that first-party public evidence on the exact canonical Marveen lineage exercises a legitimate parent-owned installation identity change, durable identity-state mutation and native runtime readback of the changed display identity, which is direct descriptive S5 evidence at that declared boundary.