# Polyphemus project-rule acceptance — S5 relevance review

Status: experimental, non-normative.

Tracking issue: #82

Reviewed sources:

```text
opensiro/vsm-harness-profile@main (current S5 semantics)
opensiro/vsm-harness-index/assessments/polyphemus.md
polyphemus-ai/release-rehearsal@02020f3bc2829c350fd726273a7721254068925f
system-observations/polyphemus.json
vsm-projections/s5/post-closure-deltas/live-canonical-cohort-2026-09-29.json
vsm-projections/s5/matched-cell/s5-primary-search-closure.json
vsm-projections/benchmark-family-map/S5-WAKU-REVIEW.md
vsm-projections/benchmark-family-map/S5-PLATYPUS-REVIEW.md
BASELINE.md
```

Relevant exact-ref implementation/test surfaces:

```text
packages/core/src/projects.ts
packages/core/test/projects.test.ts
packages/core/src/polyphemus.ts
packages/core/test/polyphemus.test.ts
```

## Result

```text
function: S5
benchmark_fit: direct
system_linkage: canonical-native-descriptive
boundary: parent keep/discard of proposed project rules -> authoritative project AGENTS.md -> subsequent project-session context
canonical_harness_id: polyphemus
canonical S5 state: P
primary_reopen: no
primary_baseline: gap
```

The admitted Polyphemus observation is direct **descriptive S5 capability evidence at the canonical parent-owned project-rule boundary**.

A first-party native regression exercises the actual keep/discard surface with a concrete proposed project rule file, accepts `AGENTS.md`, and verifies that the project-root authoritative `AGENTS.md` contains the accepted `Real rules.` content. At the same exact canonical revision, a new project session resolves its project from `cwd`, reads that same project-root `AGENTS.md`, and first-party runtime regressions verify concrete project rules reach the later model/agent execution context.

This does not infer autonomous S5 ownership. The canonical Index independently classifies Polyphemus S5 as `P`: agents may propose durable rules, while the parent/operator retains the decisive keep/discard right over whether a proposal becomes authoritative.

## Function-first mapping

The direct fit comes from the exercised parent decision, authoritative enactment and same-state runtime return path, not from the filename `AGENTS.md` or from generic prompt injection:

```text
agent proposes project AGENTS.md
        ↓
parent/operator chooses keep or discard
        ↓
resolveInboxItem(..., "AGENTS.md", "accept")
        ↓
project-root AGENTS.md is replaced with accepted content
        ↓
first-party regression verifies concrete accepted rule bytes
        ↓
new project session resolves the same project
        ↓
session constructor reads project-root AGENTS.md
        ↓
project rules enter later model / agent execution context
```

At the canonical project recursion, this satisfies the narrow direct-descriptive threshold used by the current S5 post-closure reviews:

1. **identity / ultimate-policy object** — project `AGENTS.md` is the durable project rules surface that defines how work in the project is done, rather than a one-shot task argument;
2. **legitimate ultimate authority** — canonical ownership is `P`, and the ordinary native keep/discard path leaves the decisive acceptance decision with the parent/operator rather than the proposing agent;
3. **actual concrete enactment** — `packages/core/test/projects.test.ts` writes a proposed `AGENTS.md` containing `Real rules.`, calls `resolveInboxItem(..., 'accept')`, and verifies the project-root authoritative file contains that accepted content;
4. **durable authoritative state** — the accepted proposal replaces `<project-root>/AGENTS.md`, while discard removes a proposal without enacting it;
5. **return to subsequent operation** — `SessionRuntime` resolves the project from the session `cwd` and reads `<project-root>/AGENTS.md` during construction; separate first-party runtime regressions verify concrete project rules are delivered into later system context / agent `systemAppend` paths;
6. **ownership / mechanism separation** — the parent/operator owns the keep/discard decision; `resolveInboxItem`, file replacement and session prompt plumbing enact and transport that decision without becoming its ultimate owner.

## Why this clears the Platypus threshold

The evidentiary distinction from the current Platypus mechanism/proxy review is concrete authoritative mutation.

Platypus has an explicit source-level same-field bridge from persisted Workspace `context` to later `stream.system`, but its recovered owner/admin update regression does not exercise a concrete non-empty policy Context value through that authoritative persistence path. Its concrete prompt values occur in separate renderer fixtures, so the review correctly stops at mechanism/proxy.

Polyphemus supplies the missing empirical property:

```text
concrete proposed authoritative rule value
        ↓
actual native parent acceptance path
        ↓
exact authoritative target file changed and asserted
```

The later-return evidence is still split across native tests, but it is bound structurally to the **same authoritative file** that the mutation regression changes. That is the same kind of evidence composition already accepted for Waku: a concrete native mutation and exact durable-state assertion plus a canonical implementation path that rereads that state into later operation. A single end-to-end model turn is therefore not manufactured or claimed.

## Evidence limitation

The evidence is descriptive and deterministic, not a downstream behavioral benchmark.

The acceptance regression does **not** itself start a later project session after accepting `Real rules.`. The runtime regressions independently prepare concrete `AGENTS.md` fixtures such as `Always run npm test.` and `Keep it static.` and verify those project rules reach subsequent execution contexts.

Therefore the narrow direct claim is:

```text
parent/operator acceptance concretely changes the authoritative project-rule file,
and canonical later project sessions natively read that same file into operation
```

not:

```text
one public test accepted "Real rules." and then demonstrated model behavioral compliance with it
```

The review also does not claim production deployment history or quantify how reliably a downstream model obeys the accepted rule.

## Material comparability and primary reopen

Polyphemus adds another canonical-native direct descriptive S5 witness, but it does not create a materially matched cross-harness comparison cell under `BASELINE.md` Rule 2.

Its protocol is native to Polyphemus:

- project inbox proposal fixture;
- parent keep/discard action;
- project-root `AGENTS.md` replacement;
- project session construction and provider/agent context wiring;
- repository-local Vitest environment and fixtures.

The existing canonical direct witnesses use different first-party evidence families, objects and execution contracts: Waku SOUL persistence/per-turn assembly, Octos soul effective-state/new-session construction, HugAgentOS project instructions/context assembly, DotCraft profile-to-thread contract, Marveen installation identity mutation, and others.

These observations do not hold constant one evidence family/version, fixture/task set, evaluator, execution environment, budget/repetition policy, or reset/adaptation policy, and they do not publish a common outcome metric under one matched authority/change/subsequent-operation protocol.

Therefore:

```text
new live direct canonical S5 observation: yes
canonical native linkage: yes
concrete authoritative policy mutation: yes
native same-state subsequent-operation path: yes
second materially comparable canonical S5 observation under one matched protocol: no
matched multi-canonical authority/change/subsequent-operation protocol: no
adapter-preserved canonical rows from a direct family: no
primary_reopen: no
S5 primary_baseline: gap
```

Polyphemus is structurally analogous to several existing descriptive witnesses, especially Waku and HugAgentOS, but structural analogy is not material comparability.

## Machine-readable placement

The neutral Stage 1 observation remains in:

```text
system-observations/polyphemus.json
system-observations/registry.psv
system-observations/REGISTRY.md
```

This direct post-closure semantic addition is represented through:

```text
vsm-projections/benchmark-family-map/post-closure.json
vsm-projections/s5/post-closure-deltas/polyphemus-project-rule-state-return-2026-09-29.json
```

The generic `benchmark_id` field is only the post-closure identity key; this review does not claim the Polyphemus native regression is a reusable cross-system benchmark family.

## Mutation boundary

This review does not modify:

- the neutral Stage 1 observation;
- the historical live-canonical-cohort snapshot;
- the frozen S5 family map;
- `vsm-projections/s5/coverage.json`;
- frozen `vsm-projections/s5/canonical_observations.json`;
- the frozen S5 primary-search closure;
- `baselines/primary-baselines.json`;
- canonical Index ownership/state;
- Profile semantics or Skills methodology.

## Non-claims

This review does not claim that:

- Polyphemus has autonomous S5 ownership;
- every `AGENTS.md` edit is automatically an S5 decision;
- the acceptance regression itself executes a later model turn;
- the `Real rules.` fixture is empirically observed changing downstream model behavior;
- the separate acceptance and runtime tests form one end-to-end execution;
- the observation is production deployment history;
- Polyphemus and another canonical harness are materially matched because both use project-rule files;
- the S5 primary evidence gap is closed.

It claims only that, at `polyphemus-ai/release-rehearsal@02020f3bc2829c350fd726273a7721254068925f`, first-party native evidence exercises a concrete parent-governed project-rule acceptance into the authoritative project `AGENTS.md`, while the same canonical runtime reads that exact authoritative surface into subsequent project sessions. Under the current post-closure threshold, that is direct descriptive S5 evidence at the declared parent-owned boundary.