# Platypus Workspace Context — S5 relevance review

Status: experimental, non-normative.

Tracking issue: #79

Reviewed sources:

```text
opensiro/vsm-harness-profile@main (Profile v0.2.4)
opensiro/vsm-harness-index/assessments/platypus.md
willdady/platypus@5dda4dcdb92c209c8c8df953f0e9261cd018c2d7
system-observations/platypus.json
vsm-projections/s5/post-closure-deltas/live-canonical-cohort-2026-09-29.json
vsm-projections/s5/matched-cell/s5-primary-search-closure.json
vsm-projections/benchmark-family-map/S5-WAKU-REVIEW.md
vsm-projections/benchmark-family-map/S5-OCTOS-REVIEW.md
vsm-projections/benchmark-family-map/S5-DOTCRAFT-REVIEW.md
vsm-projections/benchmark-family-map/S5-HUGAGENTOS-REVIEW.md
BASELINE.md
```

Relevant exact-ref implementation/test surfaces:

```text
packages/schemas/index.ts
apps/backend/src/routes/workspace.ts
apps/backend/src/routes/workspace.test.ts
apps/frontend/components/workspace-form.test.tsx
apps/backend/src/system-prompt.ts
apps/backend/src/system-prompt.test.ts
apps/backend/src/services/chat-execution.ts
apps/backend/src/services/chat-execution.queries.test.ts
apps/docs/content/concepts/system-prompt.mdx
```

## Result

```text
function: S5
benchmark_fit: mechanism/proxy
system_linkage: canonical-native-mechanism
boundary: parent-owned Workspace Context configuration + native persistence/prompt-consumption wiring
canonical_harness_id: platypus
canonical S5 state: P
direct_descriptive_s5: no
primary_reopen: no
primary_baseline: gap
```

Platypus has a strong canonical S5-adjacent mechanism: a Workspace owner or Organization admin can update durable Workspace `context`, and the exact canonical runtime later reads that same persisted field while preparing a Chat turn and renders it into the model-visible `<workspace>` system-prompt fragment.

The missing piece for direct descriptive admission under #79 is not the source-level transport. That bridge is explicit. The missing piece is a first-party witness that actually exercises a **concrete non-empty identity/standing-policy change through the authoritative update boundary** and establishes that changed state as the one returned to subsequent operation.

The recovered first-party tests split that evidence across different fixtures:

- the backend Workspace route test exercises an owner-authorized update, but changes `name`, not a concrete non-empty `context`;
- the Workspace form test loads concrete `context: "Be brief"`, but its save regression submits an empty Context as `null` rather than changing one concrete policy value to another;
- the system-prompt test injects concrete `workspace.context = "We sell rare books."` directly into the renderer and verifies exact `<workspace>` output, but does not obtain that value through the owner/admin persistence path;
- the Drizzle-backed `prepareChatTurn` integration test exercises the native current-Workspace-row-to-`stream.system` path, but its Workspace fixture has `context: null`.

Under #79 those separate tests are not promoted into a synthetic empirical run. The result is therefore **mechanism/proxy**, while the canonical Index ownership remains `S5=P`.

## Function-first mapping

The canonical mechanism is structurally coherent:

```text
Workspace owner / Organization admin
        ↓
validated Workspace update includes `context`
        ↓
workspace row is persisted
        ↓
later prepareChatTurn() reads current Workspace row
        ↓
workspace.context enters SystemPromptStableContext
        ↓
renderSystemPrompt() emits <workspace>...</workspace>
        ↓
composed prompt becomes turn.stream.system
```

That is stronger than a static policy file, documentation-only claim, or disconnected CRUD field. It establishes a real native authority/persistence/return mechanism at the same canonical revision.

However, the current Capability direct-descriptive examples add one further empirical property: the policy/identity change itself is concretely exercised at the authoritative mutation/enactment boundary.

Examples already admitted as direct include:

- Waku: a concrete SOUL value is written through the shipped mutation path and exact durable bytes are asserted before the structural later-turn reread;
- Octos: concrete soul/personality values are written and recovered as effective state before the structural new-session prompt path;
- DotCraft: a concrete parent-authored profile is selected and materialized into the native persisted thread runtime contract;
- HugAgentOS: concrete project rules are written, persisted, and reread through native project-context assembly.

Platypus does not currently provide the equivalent concrete Context mutation witness at the reviewed revision. Treating the generic Workspace update test plus an independently injected prompt fixture as if they were one concrete owner-policy enactment would erase that evidentiary difference.

## Current Profile boundary

Profile v0.2.4 requires a positive S5 mapping to identify an identity- or ultimate-policy-level decision path, legitimate ultimate authority, and closure by which the resulting decision governs subsequent operation.

Platypus structurally exposes all of the relevant mechanism slots:

1. **potential identity/policy object** — Workspace Context is model-visible standing framing; the recovered fixtures include `Be brief` and `We sell rare books.`, both capable of expressing standing policy or identity rather than a one-shot task argument;
2. **legitimate parent boundary** — the Workspace update surface is available to the Workspace owner or Organization admin, with canonical ownership independently assessed as `P`;
3. **persistence mechanism** — validated Workspace update fields, including `context`, are written to the Workspace row;
4. **return mechanism** — every prepared Chat turn resolves the current Workspace row, feeds `workspace.context` to the prompt renderer, and returns the composed system prompt in `stream.system`.

What the admitted first-party evidence does not directly exercise is the complete changed-decision instance across those slots.

## Why this is mechanism/proxy rather than no-fit

`no-fit` would understate the recovered evidence. Platypus is not merely a system with a writable prompt field:

- the field belongs to a durable Workspace object at the declared recursion;
- update authority is explicitly owner/admin bounded;
- the field is part of the validated canonical Workspace update schema;
- the persisted row is reread by the native Chat-turn preparation path;
- the renderer has a dedicated Workspace fragment;
- first-party tests independently pin both authority/update plumbing and concrete Context rendering;
- canonical documentation states that Workspace Context is part of the composed system prompt for Chat turns.

So this is meaningful S5 mechanism evidence. It simply stops short of the direct-descriptive threshold used by the current live post-closure additions.

## Evidence limitation

The limitation is narrower than Bernstein's.

Bernstein lacked an evidenced executable object bridge between its human-signed `DraftProposal` and the separate `GovernPlan` consumed by apply. Platypus **does** have a source-level same-field bridge from persisted Workspace `context` to later `stream.system`.

Platypus fails direct admission for a different reason: the public first-party regressions recovered at `5dda4dc...` do not concretely exercise a non-empty identity/standing-policy Context mutation through the authoritative route and then establish that changed persisted state as the returned state.

Accordingly this review does **not** claim that the source path is hypothetical or disconnected. It claims only that source connectivity plus separate test fixtures is insufficient, under #79's fail-closed boundary, to manufacture a direct empirical policy-change witness.

## Relationship to the historical live-cohort snapshot

The historical live-canonical-cohort artifact recorded Platypus as having a structural owner/admin Workspace Context path but no recovered reusable concrete Context-amendment-to-subsequent-run witness.

Stage 1 materially improves the evidence record by pinning three exact canonical first-party surfaces:

- authorized configuration/persistence plumbing;
- concrete Context rendering;
- native persisted-row-to-turn wiring.

That improves mechanism coverage, but it does not invalidate the historical snapshot by retroactively turning those separate surfaces into one direct run. The historical cohort artifact therefore remains unchanged.

## S5 reopen gate

Because #79's Stage 2 result is not direct, it is not admitted as a new live direct S5 observation and does not trigger the frozen primary reopen analysis.

Therefore:

```text
new direct canonical S5 observation: no
canonical same-field authority/persistence/return mechanism: yes
concrete non-empty authoritative Context mutation witness: no
same changed policy empirically returned to later operation: no
materially matched cross-harness protocol: not evaluated for promotion
primary_reopen: no
S5 primary_baseline: gap
```

No comparison cell is created by treating Platypus's generic Workspace update regression, separate concrete prompt-rendering fixture, and null-Context turn integration fixture as one matched direct protocol.

## Machine-readable placement

Stage 1 already records the factual surfaces separately in:

```text
system-observations/platypus.json
system-observations/registry.psv
system-observations/REGISTRY.md
```

This Stage 2 review adds **no** direct entry to:

```text
vsm-projections/benchmark-family-map/post-closure.json
vsm-projections/s5/post-closure-deltas/
```

The post-closure additions registry currently represents admitted direct additions. Creating a Platypus direct delta would contradict #79's fail-closed disposition.

## Mutation boundary

This review does not modify:

- the Stage 1 neutral Platypus observations;
- the historical live-canonical-cohort snapshot;
- the frozen S5 family map;
- `vsm-projections/s5/coverage.json`;
- frozen `vsm-projections/s5/canonical_observations.json`;
- the frozen S5 primary-search closure;
- `baselines/primary-baselines.json`;
- canonical Index ownership/state;
- Profile semantics or Skills methodology.

## Reassess if

Re-open Platypus's semantic disposition if first-party evidence at the canonical/current supported boundary supplies a concrete identity/standing-policy Context change through the authoritative native path, for example a regression that:

```text
owner/admin sets Workspace context to concrete policy X
        ↓
Workspace row persists X
        ↓
a later prepareChatTurn() rereads the Workspace
        ↓
turn.stream.system contains X in the <workspace> fragment
```

A single integration test is not mandatory if the first-party evidence otherwise concretely binds the same changed state across the authoritative mutation and return boundary. What is not sufficient is another independently injected renderer fixture or another generic Workspace update that never exercises `context`.

## Non-claims

This review does not claim that:

- Platypus lacks S5 structurally;
- Workspace Context is irrelevant to identity or standing policy;
- the canonical update-to-turn source path is disconnected;
- a later Chat turn would fail to read a persisted Context value;
- every Workspace Context value is necessarily an S5 decision;
- Platypus has autonomous S5 ownership;
- the owner/admin update test and prompt-rendering test form one end-to-end run;
- the S5 primary evidence gap is closed.

It claims only that, at `willdady/platypus@5dda4dcdb92c209c8c8df953f0e9261cd018c2d7`, first-party evidence establishes a strong parent-governed Workspace Context authority/persistence/return mechanism, but does not concretely exercise the same non-empty identity/standing-policy mutation across that full path. Under #79, that is mechanism/proxy rather than direct descriptive S5.