# superharness project-rule evidence — S5 relevance review

Status: experimental, non-normative.

Tracking issue: #85

Reviewed sources:

```text
opensiro/vsm-harness-profile@main (current public Profile)
opensiro/vsm-harness-index/assessments/superharness.md
artificemachine/superharness@8bd54bc1ea7db2391190de25087bc638d503e549
system-observations/superharness.json
vsm-projections/s5/post-closure-deltas/live-canonical-cohort-2026-09-29.json
vsm-projections/s5/matched-cell/s5-primary-search-closure.json
BASELINE.md
```

Relevant exact-ref implementation/test surfaces:

```text
src/superharness/commands/rules.py
src/superharness/commands/init_project.py
src/superharness/commands/delegate.py
src/superharness/engine/handoff_generator.py
tests/unit/test_rules.py
tests/unit/test_rules_injection.py
```

## Result

```text
function: S5
benchmark_fit: mechanism/proxy
system_linkage: canonical-native-mechanism
boundary: project-rule representation, parsing and downstream injection without an exercised legitimate owner policy-mutation decision
canonical_harness_id: superharness
canonical S5 state: P
direct_descriptive_s5: no
primary_reopen: no
primary_baseline: gap
```

The admitted superharness observation is useful **S5 mechanism/proxy evidence**, but it does not meet the current direct-descriptive S5 threshold.

At the canonical revision, first-party native tests create concrete `.superharness/rules/*.md` fixtures, including an active rule whose body says that it covers `state backend policy`. The rule parser, adapter payload and handoff-loading paths then recover or expose those concrete rules to later consumers. Project initialization also creates the rule directory and instruction surfaces used by the harness.

The missing direct-S5 element is the decisive policy-change path. The concrete rules in the recovered regressions are written directly by test setup. They are not produced by an exercised owner/operator keep, approve, edit, reject or amendment action over a concrete proposed rule. The shipped `shux rules` command at this exact revision provides `list`, `show` and `search`; it does not itself supply the missing authoritative mutation path.

Therefore the evidence directly exercises **rule-state representation and transport**, but not a concrete legitimate ultimate-policy decision that changes authoritative state and then returns that changed state to operation.

This review does not re-assess ownership. The canonical Index independently records superharness S5 as `P`, and Capability preserves that parent-owned state.

## Function-first mapping

The positive evidence is:

```text
project rule files exist in .superharness/rules/
        ↓
first-party fixtures contain concrete rule IDs and bodies
        ↓
all_rules_text(...) parses project rule state
        ↓
adapter / handoff paths expose the rule state to later work
```

That is relevant to how an already-authoritative policy state is represented and transported.

The direct-S5 path required by #85 would additionally need evidence equivalent to:

```text
legitimate parent/operator policy choice
        ↓
concrete rule accepted / edited / rejected through the native authority surface
        ↓
authoritative project rule state changes
        ↓
that exact changed state is later used by superharness operation
```

The exact-ref tests recovered in this review begin after the decisive authority step: fixture setup writes the rule files directly. Treating fixture construction as the owner/operator's policy decision would manufacture the missing S5 decision boundary rather than observe it.

## Why this is mechanism/proxy rather than direct

The current direct-descriptive S5 precedent requires more than a durable policy-like object plus downstream injection.

For Polyphemus, for example, a first-party regression exercised the actual parent keep/accept path with a concrete proposed `AGENTS.md`, asserted the resulting authoritative project file, and the canonical runtime rereads that same authoritative surface into later sessions. Waku similarly combines a concrete native authoritative mutation with an exact same-state return path.

Superharness currently supplies the latter half strongly — concrete rule representation plus downstream consumption — but not the former half through a legitimate authority decision path. The relevant native regression does not show who decided that `state backend policy` became authoritative or exercise the mechanism by which that decision was accepted into project policy.

Accordingly:

```text
concrete policy-like rule fixture: yes
native parsing / downstream transport: yes
legitimate authority owner identified canonically: yes (P)
concrete owner decision exercised in the admitted evidence: no
authoritative policy mutation through that decision: no
same-decision return to subsequent operation: no
```

The fail-closed classification is therefore **mechanism/proxy**.

## Why this is not no-fit

`no-fit` would throw away genuine S5-adjacent machinery:

- a durable project rule corpus exists;
- concrete active/deprecated rule semantics are exercised;
- the harness parses the rule state through first-party code;
- adapter and handoff paths expose the state to later work;
- project initialization establishes the policy/instruction surfaces at the assessed project recursion;
- canonical ownership is parent/operator `P`, consistent with an owner-governed policy surface.

These are substantive implementation mechanisms for carrying project policy. They simply do not, on the admitted public evidence, exercise the decisive ultimate-policy mutation itself.

## Relationship to the S5 reopen gate

Because this result is not direct, #85 does not promote it into the frozen S5 reopen search.

Therefore:

```text
new direct canonical S5 observation: no
concrete authoritative owner policy mutation: no evidenced native decision path
same-decision return to subsequent operation: no
materially matched cross-harness protocol: not evaluated for promotion
primary_reopen: no
S5 primary_baseline: gap
```

No comparison cell is created by treating direct test-fixture writes as a matched authority/change protocol.

## Machine-readable placement

Stage 1 already records the factual surfaces in:

```text
system-observations/superharness.json
system-observations/registry.psv
system-observations/REGISTRY.md
```

This Stage 2 review adds **no** direct entry to:

```text
vsm-projections/benchmark-family-map/post-closure.json
vsm-projections/s5/post-closure-deltas/
```

The post-closure additions registry represents admitted direct additions. Adding superharness there would contradict the evidence boundary above.

## Mutation boundary

This review does not modify:

- Stage 1 neutral observations;
- the historical live-canonical-cohort snapshot;
- the frozen S5 family map;
- `vsm-projections/s5/coverage.json`;
- frozen `vsm-projections/s5/canonical_observations.json`;
- the frozen S5 primary-search closure;
- `baselines/primary-baselines.json`;
- canonical Index ownership/state;
- Profile semantics or Skills methodology.

## Reassess if

Re-open superharness's semantic disposition if public first-party evidence at the relevant supported boundary supplies a concrete native authority path that, without treating fixture setup as the decision itself:

- accepts, edits, rejects or otherwise ratifies a concrete project rule under the legitimate parent/operator boundary;
- persists the resulting decision into the authoritative `.superharness/rules/` state; and
- demonstrates that changed authoritative state returning to subsequent superharness operation.

A new parser test, another directly written rule fixture, or stronger prose describing owner control is not by itself sufficient.

## Non-claims

This review does not claim that:

- superharness lacks S5 structurally;
- its project rules are ineffective;
- its parsing/injection tests are invalid;
- project owners cannot edit rule files outside the tested harness path;
- a direct S5 path cannot exist in another revision;
- superharness has autonomous S5 ownership;
- direct test-fixture writes are evidence of a legitimate ultimate-policy decision;
- the S5 primary evidence gap is closed.

It claims only that, at `artificemachine/superharness@8bd54bc1ea7db2391190de25087bc638d503e549`, first-party evidence directly exercises concrete project-rule representation, parsing and downstream transport, but does not exercise the legitimate parent/operator decision that makes a concrete rule authoritative. Under #85, that is mechanism/proxy rather than direct descriptive S5.