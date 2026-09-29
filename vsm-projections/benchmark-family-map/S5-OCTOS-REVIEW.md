# Octos soul-policy mutation — S5 relevance review

Status: experimental, non-normative.

Tracking issue: #70

Reviewed sources:

```text
opensiro/vsm-harness-profile@main (Profile v0.2.4)
opensiro/vsm-harness-index/assessments/octos.md
octos-org/octos@9f6311afd4e00324cdb89d957461cf861f4f2630
octos-org/octos@379193861165e1ca3784c1c65927297fb42429c6
octos-org/octos@fb9247456d8f8b0a469aaeecfdb46e3f2b4866b8
system-observations/octos.json
vsm-projections/s5/matched-cell/s5-primary-search-closure.json
vsm-projections/benchmark-family-map/S5-DOTCRAFT-REVIEW.md
vsm-projections/benchmark-family-map/S5-HUGAGENTOS-REVIEW.md
vsm-projections/benchmark-family-map/S5-MARVEEN-REVIEW.md
BASELINE.md
```

## Result

```text
function: S5
benchmark_fit: direct
system_linkage: canonical-native-descriptive
boundary: parent-owned profile/chat soul-policy mutation -> durable effective state -> new-session runtime prompt input
canonical_harness_id: octos
canonical S5 state: P
primary_reopen: no
primary_baseline: gap
```

The admitted Octos observation is direct **descriptive S5 capability evidence at the canonical gateway soul-policy enactment boundary**. First-party tests exercise concrete parent/user-facing personality-policy changes, durable storage, precedence between profile-wide and per-chat policy state, reset, and effective-state readback. At the exact canonical revision the same profile-wide soul state is read during native system-prompt construction, while the command contract explicitly states that soul changes take effect in new sessions.

This review does not infer autonomous S5 ownership. The canonical Index assessment independently classifies Octos S5 as `P`; Capability preserves that ownership fact rather than re-assessing it.

## Function-first mapping

The direct fit comes from the exercised identity/personality change plus the native return path, not from the word `soul`, the existence of a file, or a generic writable prompt:

```text
parent/gateway user chooses profile or chat personality policy
        ↓
/soul writes durable policy state
        ↓
effective-state resolution applies per-chat override over profile-wide soul
        ↓
/soul readback exposes the currently effective policy
        ↓
reset removes the chat override and restores profile-wide policy
        ↓
new sessions consume soul state through native runtime prompt construction
```

At the declared Octos profile/workspace runtime recursion, the current Profile requires an identity- or ultimate-policy-level decision path, legitimate authority, ownership/enforcement separation, and return into subsequent operation. The evidence supports the narrow descriptive mapping:

1. **identity/policy level** — the exercised state is explicitly personality/soul guidance for how the runtime Agent operates, not a routine task argument, resource allocation or tool permission;
2. **legitimate parent boundary** — the mutation is exposed through the user-facing gateway command/API boundary; the canonical assessment separately establishes that ultimate identity/value authority belongs to the parent workspace/operator rather than to the autonomous Agent;
3. **actual enactment** — first-party tests write concrete soul values such as `coding helper`, `writing tutor`, `dashboard persona` and `chat persona`, then read the resulting effective state;
4. **precedence and reset** — a per-chat soul supersedes profile-wide soul for that chat, and reset removes only the override so the profile-wide soul becomes effective again;
5. **return path** — the command contract reports that updates take effect in new sessions, and the exact canonical `build_system_prompt(...)` path reads profile soul state and appends it as `## Soul` before later Agent execution;
6. **ownership/enforcement separation** — the user/operator supplies the semantic soul choice; storage, precedence resolution, command handling and prompt construction transport and enact that choice but do not become its ultimate owner.

That is stronger than a static identity file, parser, CRUD schema or policy-enforcement mechanism: a concrete personality-policy state is changed through a shipped native control path, persisted, resolved as effective state and wired into later native runtime context.

## Evidence boundary and the two soul surfaces

The admitted empirical witness and the canonical assessment must not be conflated into one file-level claim.

The canonical Index assessment's original positive S5 path emphasizes the workspace bootstrap identity/value files, including `.octos/IDENTITY.md` and `.octos/SOUL.md`, and their hot-reload into model-visible context. The admitted raw observation instead exercises the gateway/profile `soul.md` and per-chat override path introduced through `/soul`.

They are distinct storage/control surfaces on the same canonical runtime lineage. This review credits the admitted `/soul` path because it independently exercises an identity/personality policy mutation and effective-state transition, while using the canonical assessment only to anchor the parent-owned S5 recursion and ownership state. It does not claim that the `/soul` test edits `.octos/SOUL.md` or `.octos/IDENTITY.md`.

## Evidence limitation

The observation is a controlled first-party regression witness, not production history or a downstream behavioral benchmark.

The test verifies mutation, effective-state readback, precedence and reset. It does **not** start a later model turn and demonstrate changed model behavior under `dashboard persona` or `chat persona`. The exact canonical implementation supplies the native prompt-consumption path for profile soul state, but that implementation evidence is not a second empirical task result.

The per-chat override test likewise demonstrates effective-state resolution but is not independently promoted into a claim that a later model call consumed that exact `chat persona` fixture.

Therefore the narrow direct claim is:

```text
parent-owned soul/personality policy was changed durably, resolved as effective runtime state, and has a canonical new-session prompt-consumption path
```

not:

```text
a public downstream model task demonstrated behavioral compliance with the changed soul
```

## Relationship to the existing S5 witnesses and reopen gate

Octos adds another canonical native descriptive S5 witness, but it does not satisfy the frozen primary reopen condition.

The current canonical descriptive witnesses share only an abstract authority/change/return shape:

- **Octos**: parent/user-facing soul-policy mutation, effective-state precedence/readback, and canonical new-session prompt-consumption path;
- **Marveen**: parent-owned installation display/persona identity mutation plus native runtime identity readback;
- **DotCraft**: parent-authored Agent Profile selected and resolved into a persisted thread runtime contract;
- **HugAgentOS**: authorized durable project rules persisted and returned through native project-context assembly;
- **Ouroboros**: immutable repository-history witness of a parent-governed constitutional/runtime policy change with executable return and later canonical lineage.

These evidence surfaces do not hold constant one evidence family/version, authority/change treatment, policy object, task/evaluator, execution environment, repetition policy or reset/adaptation policy. Structural resemblance is therefore not a materially matched comparison cell under `BASELINE.md`.

Therefore:

```text
new live direct canonical S5 observation: yes
canonical native linkage: yes
second materially comparable canonical S5 surface: no
matched multi-canonical authority/change/subsequent-operation protocol: no
adapter-preserved canonical rows from a direct family: no
primary_reopen: no
S5 primary_baseline: gap
```

A future common authority/change/subsequent-operation protocol exercised across Octos and another canonical S5 system, or adapter-preserved canonical rows from a direct S5 family, would justify a deliberate closure review.

## Machine-readable placement

This observation is intentionally not inserted into frozen `vsm-projections/s5/canonical_observations.json`, because that file and its validator encode the historical S5 closure snapshot.

The live addition is represented through:

```text
vsm-projections/benchmark-family-map/post-closure.json
vsm-projections/s5/post-closure-deltas/octos-soul-policy-state-return-2026-09-29.json
```

Here `benchmark_id` is the generic post-closure identity field; this review does **not** claim the Octos regression test is a benchmark family.

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

- Octos has autonomous S5 ownership;
- the `/soul` regression edits the separate `.octos/SOUL.md` or `.octos/IDENTITY.md` bootstrap files;
- the regression executes a later model turn under the changed soul;
- the per-chat `chat persona` fixture is directly observed inside a later model prompt;
- the test is production deployment history or a cross-harness benchmark;
- Octos and the existing canonical S5 witnesses are materially matched enough to select a primary;
- the S5 primary evidence gap is closed.

It claims only that, at the exact canonical Octos revision, first-party native evidence exercises a parent/user-facing identity-personality policy mutation, durable/effective-state resolution and reset, with the same canonical runtime providing a new-session prompt-consumption path for soul state. This is direct descriptive S5 evidence at that declared boundary.