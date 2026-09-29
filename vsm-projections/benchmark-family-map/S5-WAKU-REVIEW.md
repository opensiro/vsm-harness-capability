# Waku SOUL mutation — S5 relevance review

Status: experimental, non-normative.

Tracking issue: #73

Reviewed sources:

```text
opensiro/vsm-harness-profile@main (Profile v0.2.4)
opensiro/vsm-harness-index/assessments/waku-agent.md
ShenSeanChen/waku-agent@b8310c08029732475b68076df02a6cc44e3e41e7
system-observations/waku-agent.json
vsm-projections/s5/matched-cell/s5-primary-search-closure.json
vsm-projections/benchmark-family-map/S5-OCTOS-REVIEW.md
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
boundary: parent-owned SOUL persona/standing-rule mutation -> durable file state -> per-turn system-context return
canonical_harness_id: waku-agent
canonical S5 state: P
primary_reopen: no
primary_baseline: gap
```

The admitted Waku observation is direct **descriptive S5 capability evidence at the canonical parent-owned SOUL boundary**. A first-party deterministic regression exercises a real shipped dashboard mutation path against a concrete `SOUL.md` value and verifies its durable persisted bytes. At the same exact canonical revision, every `Session.build_system(...)` rebuild begins by reading that same `SOUL.md` through `load_soul(settings)`, so the changed persona/standing-rule surface has a native return path into later Waku operation.

This review does not infer autonomous S5 ownership. The canonical Index assessment independently classifies Waku S5 as `P`: the legitimate local owner/user retains ultimate rewrite authority, while agent-side `update_soul` persistence is constrained to standing preferences supplied by that parent.

## Function-first mapping

The direct fit comes from the exercised identity/standing-policy change plus the native return path, not from the filename `SOUL.md` or generic prompt editability:

```text
parent owner/user changes durable persona / standing rule
        ↓
shipped dashboard save_soul path writes SOUL.md
        ↓
first-party regression verifies exact persisted content
        ↓
next Session.build_system(...) rereads SOUL.md through load_soul
        ↓
SOUL content becomes the first component of later runtime system context
```

At the canonical single-assistant recursion, the current Profile requires an identity- or ultimate-policy-level decision path, legitimate authority, enactment and return into subsequent operation. Waku satisfies that narrow descriptive mapping:

1. **identity / standing-policy level** — `SOUL.md` is explicitly the editable persona and standing behavioural-rule surface for the assistant, not a routine task argument or tool parameter;
2. **legitimate parent boundary** — the local user/owner can rewrite the surface directly through the ordinary shipped dashboard, and the canonical assessment separately establishes the parent as ultimate authority;
3. **actual enactment** — `test_dashboard_soul_is_written_as_utf8` writes the concrete fixture `用户偏好中文回复 🚀` through the real `memory_action({"action": "save_soul", ...})` path and asserts exact durable UTF-8 content;
4. **durable state** — the mutation lands in the configured Waku home `SOUL.md`, the same persistent surface read by runtime session assembly;
5. **return path** — `Session.build_system(...)` calls `load_soul(self.settings)` on each turn and places the returned SOUL content first in the system context;
6. **ownership / enforcement separation** — the parent supplies the semantic identity or standing rule; dashboard/tool/file plumbing stores and transports that decision but does not become its ultimate owner.

That is stronger than a static persona file or generic configuration mechanism: a concrete owner-facing identity/standing-rule state is mutated through a shipped native path, verified as persisted, and wired into each later system-context rebuild.

## Evidence limitation

The empirical witness is a deterministic persistence regression, not a downstream behavioral benchmark.

The test verifies the mutation entrypoint and exact durable bytes. It does **not** invoke a later model turn after changing the fixture and does not measure whether the model then answers in Chinese or otherwise changes behaviour. The later-turn return claim comes from the exact canonical implementation path in the same revision: `Session.build_system(...)` rereads `SOUL.md` every turn.

Therefore the narrow direct claim is:

```text
parent-owned persona / standing-policy state was changed durably and the canonical runtime rereads that state into later per-turn system context
```

not:

```text
a public downstream task demonstrated behavioral compliance with the changed SOUL value
```

## Waku versus Octos: similar semantics, still not a matched primary cell

Waku is the closest current descriptive neighbor to Octos: both are canonical systems with parent/user-owned soul/personality state, a shipped mutation path, durable state and a native prompt/context return path.

That conceptual similarity still does not satisfy `BASELINE.md` Rule 2. The two witnesses do not share one materially matched comparison protocol:

- Waku uses its own deterministic dashboard UTF-8 persistence regression plus implementation-supported per-turn `load_soul` return;
- Octos uses its own gateway soul mutation/effective-state regression with profile-wide/per-chat precedence and separate canonical new-session prompt-consumption support;
- they do not hold constant one evidence family/version, fixture/task set, evaluator, execution environment, repetition policy or reset/adaptation policy;
- neither source publishes a common outcome metric under the same authority/change/subsequent-operation protocol.

Therefore Waku + Octos are **structurally analogous descriptive observations**, not a materially matched cross-harness comparison cell. Their resemblance is useful for evidence coverage but cannot be turned into a primary ranking or score without manufacturing comparability.

The same remains true against Marveen, DotCraft, HugAgentOS and Ouroboros, whose identity/policy objects and evidence protocols differ materially.

## Reopen gate

Under the frozen S5 closure contract:

```text
new live direct canonical S5 observation: yes
canonical native linkage: yes
second structurally similar canonical S5 witness: yes
second materially comparable canonical S5 observation under one matched protocol: no
matched multi-canonical authority/change/subsequent-operation protocol: no
adapter-preserved canonical rows from a direct family: no
primary_reopen: no
S5 primary_baseline: gap
```

This case therefore falls under the closure's explicit non-reopen class: another heterogeneous single-system descriptive policy/identity-change witness that cannot yet form a materially matched primary comparison.

A future common protocol that exercises the same owner-authority mutation, durable enactment and subsequent-operation surface across Waku and Octos (or another canonical S5 system), with matched evaluator/environment/reset conditions and recoverable provenance, would justify a deliberate closure review.

## Machine-readable placement

This observation is intentionally not inserted into frozen `vsm-projections/s5/canonical_observations.json`, because that file and its validator encode the historical S5 closure snapshot.

The live addition is represented through:

```text
vsm-projections/benchmark-family-map/post-closure.json
vsm-projections/s5/post-closure-deltas/waku-soul-state-return-2026-09-29.json
```

Here `benchmark_id` is the generic post-closure identity field; this review does **not** claim the Waku regression is a reusable benchmark family.

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

- Waku has autonomous S5 ownership;
- every writable system prompt is S5;
- the persistence regression executes a later model turn;
- the concrete Chinese/emoji fixture is observed affecting downstream model behavior;
- the regression is production deployment history;
- Waku and Octos are materially matched merely because both call their persona surface `soul`;
- Waku and the existing canonical S5 witnesses form a primary comparison cell;
- the S5 primary evidence gap is closed.

It claims only that, at the exact canonical Waku revision, first-party native evidence exercises a parent-owned persona/standing-rule mutation with exact durable persistence, while the same canonical runtime rereads that state into each later per-turn system-context build. This is direct descriptive S5 evidence at that declared boundary.