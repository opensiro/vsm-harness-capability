# Bernstein governance-signature evidence — S5 relevance review

Status: experimental, non-normative.

Tracking issue: #76

Reviewed sources:

```text
opensiro/vsm-harness-profile@main (current public Profile)
opensiro/vsm-harness-index/assessments/bernstein.md
sipyourdrink-ltd/bernstein@c3d317385a058ae2b5f478399373d09d84d80962
sipyourdrink-ltd/bernstein@fd08e0aba89284e1476a5847abcab1dd2701ec38
system-observations/bernstein.json
vsm-projections/s5/post-closure-deltas/live-canonical-cohort-2026-09-29.json
vsm-projections/s5/matched-cell/s5-primary-search-closure.json
BASELINE.md
```

Relevant exact-ref implementation/test surfaces:

```text
src/bernstein/core/govern/proposal.py
src/bernstein/core/govern/apply.py
src/bernstein/cli/commands/governance_cmd.py
src/bernstein/cli/commands/govern_cmd.py
tests/unit/test_govern_proposal.py
tests/unit/core/govern/test_apply.py
tests/unit/core/govern/test_plan_artifact_is_applicable.py
docs/decisions/011-model-drafts-human-signs.md
```

## Result

```text
function: S5
benchmark_fit: mechanism/proxy
system_linkage: canonical-native-mechanism
boundary: human DraftProposal ratification + separate reviewed GovernPlan apply/receipt mechanics
canonical_harness_id: bernstein
canonical S5 state: P
direct_descriptive_s5: no
primary_reopen: no
primary_baseline: gap
```

Bernstein exposes two strong first-party governance mechanisms adjacent to S5, but the exact canonical revision does **not** evidence the executable bridge required by #76 to promote them into one direct descriptive S5 result.

The first mechanism is real human ratification: a concrete `DraftProposal` can move from `DRAFT` to `SIGNED` through `DraftProposal.sign(...)`, carries a concrete `human_signature`, preserves the proposal's findings/prompt/playbook/model/timestamp bindings, and `is_signed()` distinguishes signed from unsigned or rejected state.

The second mechanism is real reviewed-plan enforcement: `apply_plan(...)` can validate and execute a lineage-anchored `GovernPlan`, refuse stale or otherwise inadmissible plans before mutation, separately gate removal-class changes, record outcomes, and emit a signed apply receipt/projection.

Those mechanisms are not treated as one end-to-end authority decision. At the canonical ref the executable apply surface consumes `GovernPlan`; it does not consume `DraftProposal`, inspect `DraftProposal.is_signed()`, or verify `DraftProposal.human_signature`. No canonical source/test recovered in this review transports the same human-signed `DraftProposal` into the `GovernPlan` accepted by `apply_plan(...)` and then into a later governed Bernstein operation.

Therefore the Stage 1 observations remain useful **mechanism/proxy evidence**, not a direct S5 capability observation under the current post-closure contract.

This review does not re-assess ownership. The canonical Index assessment independently records Bernstein S5 as `P`; Capability preserves that parent-owned S5 state.

## Function-first mapping

The positive S5-adjacent evidence is:

```text
model/system can draft a governance proposal
        ↓
human ratification is represented explicitly by DraftProposal.sign(...)
        ↓
SIGNED state + human_signature are testable artifact properties
```

and, separately:

```text
playbook + inventory
        ↓
GovernPlan computed and lineage-anchored
        ↓
apply_plan validates reviewed world / journal binding / removal approval
        ↓
change set executes
        ↓
signed apply receipt/projection records the outcome
```

The missing direct bridge is:

```text
same human-signed DraftProposal
        ↓
verified as the authoritative input to apply
        ↓
that same ratified policy is enacted
        ↓
later Bernstein operation runs under the enacted state
```

Without that bridge, combining the signature regression and the apply regression would manufacture the exact synthetic end-to-end chain prohibited by #76.

## Exact canonical implementation boundary

### 1. Human ratification is explicit

`src/bernstein/core/govern/proposal.py` defines `ProposalStatus.DRAFT`, `SIGNED`, and `REJECTED`. `DraftProposal.is_signed()` requires both `status == SIGNED` and a non-null `human_signature`; `sign(signature)` returns a new signed artifact preserving the proposal content and source bindings.

The first-party proposal tests exercise that transition with a concrete human-signature fixture. Stage 1 therefore correctly admitted a neutral governance-signature observation.

### 2. Discover writes the proposal, but does not establish apply transport

At the exact canonical ref, `govern discover` builds and persists a `DraftProposal` from findings plus a model-drafted playbook. The command records the proposal on the lineage spine and writes `proposal.json`.

The reviewed command surface does not provide an evidenced conversion in which a signed `DraftProposal` becomes the reviewed `GovernPlan` later consumed by `apply_plan(...)`.

### 3. The executable apply object is GovernPlan

`src/bernstein/core/govern/apply.py` defines `apply_plan(...)` with a `GovernPlan` input. Its pre-mutation validation checks:

- the plan's lineage decision record and anchored bytes;
- environment/input digest stability;
- duplicate surfaces;
- unread surfaces;
- approval for removal-class entries.

`apply_plan(...)` additionally receives an `approver` identity string and, where relevant, a separate removal approval. It does **not** receive a `DraftProposal`, call `is_signed()`, or verify `human_signature`.

The first-party `test_plan_artifact_is_applicable.py` strengthens this conclusion rather than bridging it: it connects the artifact written by `govern plan` to `validate_apply(...)` as a `GovernPlan`. It does not route a human-signed `DraftProposal` through the gate.

### 4. Documentation intent is not substituted for executable evidence

`proposal.py` and ADR/documentation describe the intended property that `govern apply` refuses an unsigned proposal. That is relevant design evidence, but under #76 it cannot replace the missing source/test bridge at the canonical ref.

Where prose says the signed proposal is the apply authority object while the executable apply surface demonstrably accepts `GovernPlan`, this review follows the recoverable implementation/test boundary and does not infer an unobserved adapter or conversion.

### 5. Return to subsequent operation is also not evidenced for the same ratified object

The apply regressions demonstrate mutation plus receipt/projection behavior. They do not demonstrate a later Bernstein run consuming policy state that is provenance-linked back to the same human-signed `DraftProposal` exercised by the signature regression.

That missing same-decision return path independently prevents `direct` classification under #76.

## Why this is mechanism/proxy rather than no-fit

The evidence is still substantively relevant to S5 mechanics:

1. the drafting component is explicitly non-authoritative;
2. human ratification is represented as a distinct signed artifact state;
3. reviewed governance changes have a real validation/enforcement path;
4. apply produces provenance-bearing receipts over actual change outcomes;
5. canonical ownership remains parent/operator `P`, which is consistent with the authority split represented by these mechanisms.

So `no-fit` would discard genuine authority and governance machinery. The correct fail-closed classification is **mechanism/proxy**: strong implementation evidence for pieces of an S5 authority/enactment loop, but not direct evidence of the complete same-decision S5 loop.

## Relationship to the S5 reopen gate

Because the result is not direct, #76 says not to evaluate it as a candidate for reopening the frozen S5 closure.

Therefore:

```text
new direct canonical S5 observation: no
same signed authority object carried through apply: no evidenced bridge
return to subsequent operation for that same object: no
materially matched cross-harness protocol: not evaluated for promotion
primary_reopen: no
S5 primary_baseline: gap
```

No comparison cell is created by treating Bernstein's proposal-signature test, GovernPlan apply tests, or receipt projection as if they were one matched benchmark protocol.

## Machine-readable placement

Stage 1 already records the two factual surfaces separately in:

```text
system-observations/bernstein.json
system-observations/registry.psv
system-observations/REGISTRY.md
```

This Stage 2 review adds **no** direct entry to:

```text
vsm-projections/benchmark-family-map/post-closure.json
vsm-projections/s5/post-closure-deltas/
```

The post-closure additions registry currently represents admitted direct additions. Creating a Bernstein direct delta would contradict this review's classification and #76's fail-closed boundary.

## Mutation boundary

This review does not modify:

- Stage 1 neutral observations;
- the frozen S5 family map;
- `vsm-projections/s5/coverage.json`;
- frozen `vsm-projections/s5/canonical_observations.json`;
- the frozen S5 primary-search closure;
- `baselines/primary-baselines.json`;
- canonical Index ownership/state;
- Profile semantics or Skills methodology;
- the historical live-canonical-cohort snapshot.

## Reassess if

Re-open Bernstein's semantic disposition if first-party evidence at the canonical/current supported boundary supplies one of the following without inference:

- an executable path/test that accepts a human-signed `DraftProposal`, verifies that exact ratification, enacts the proposal's policy, and proves the enacted state is the one later used by Bernstein; or
- an immutable first-party run/case study binding the same signed governance artifact through apply and into subsequent governed operation.

A merely stronger prose statement, a separate `approver` label on `GovernPlan` apply, or another independently constructed apply fixture is not sufficient.

## Non-claims

This review does not claim that:

- Bernstein lacks S5 structurally;
- Bernstein's governance design is ineffective;
- the human signature test is synthetic or invalid;
- the GovernPlan apply/receipt tests are synthetic or invalid;
- documentation intent is false;
- a bridge can never exist in another Bernstein revision;
- the drafting model owns S5;
- Bernstein has autonomous S5 ownership;
- the two Stage 1 observations form one end-to-end run;
- the S5 primary evidence gap is closed.

It claims only that, at `sipyourdrink-ltd/bernstein@c3d317385a058ae2b5f478399373d09d84d80962`, the recovered first-party evidence directly exercises human proposal ratification and separately exercises reviewed `GovernPlan` application/receipt mechanics, but does not evidence the same human-signed `DraftProposal` flowing through apply and back into subsequent operation. Under #76, that is mechanism/proxy rather than direct descriptive S5.