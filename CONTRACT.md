# VSM Harness Capability contract

Status: **experimental, non-normative**

This is the authoritative repository-local statement of what `opensiro/vsm-harness-capability` owns, consumes and explicitly does not own.

Cross-repository architecture is owned by `opensiro/vsm-oss-organization/ECOSYSTEM.md`. VSM semantics are owned by `opensiro/vsm-harness-profile`.

## 1. Object of study

The repository studies **general functional capability** of autonomous agent harnesses.

Canonical VSM assessment and functional capability answer different questions:

```text
canonical VSM assessment:
Which VSM functions are present at the declared system boundary,
and who owns each decisive organizational decision / feedback closure?

general functional capability:
Given an established VSM function,
what empirical evidence supports how capable that function is
across systems under materially comparable conditions?
```

Therefore:

```text
canonical closure / ownership
        ≠
general functional capability
        ≠
domain-specific assessment
```

The repository is experimental. It does not change released VSM semantics, canonical Index assessments, autonomy publication states, TLDR signatures or rankings.

## 2. Semantic authority

`opensiro/vsm-harness-profile` remains the sole authoritative definition of S1, S2, S3, S3*, S4, S5, recursion, autonomy, variety, escalation, organizational closure and evidence boundaries.

This repository may **apply** those semantics to empirical observations. It must not redefine them.

Invalid shortcuts remain invalid:

```text
delegation   → S2
manager      → S3
verifier     → S3*
learning     → S4
prompt       → S5
```

A benchmark label such as coordination, planning, verification, learning or governance is not sufficient VSM-function evidence.

## 3. Relationship to canonical assessment

`opensiro/vsm-harness-index` owns canonical repository-relative VSM assessment facts.

Capability may record references such as:

- canonical harness ID;
- canonical repository identity;
- assessment path / review reference;
- relationship between an empirical observation and the canonical reviewed revision.

Those are links, not duplicated authority.

Benchmark performance cannot assign or mutate `A`, `C`, `P`, `A(P)`, `C(P)`, `—`, or `?`.

Likewise, a canonical state does not imply an empirical capability result.

## 4. Unit of comparison

The unit is one established VSM function across two or more systems:

```text
capability(system A, Sx) ↔ capability(system B, Sx)
```

Do not collapse S1–S5 into one harness-wide capability score.

Do not interpret ownership states as a maturity ladder:

```text
— < C < P < A     # invalid
```

`A`, `C` and `P` describe different ownership arrangements.

## 5. Meaning of general capability

`general` is the default scope of this repository, not a fourth word in its repository name.

A general capability claim is an application-domain-independent claim about one VSM function whose broader intended validity is itself supported by evidence.

General capability is **not**:

- an average across domain-specific scores;
- the most common domain result;
- a specialized benchmark result relabelled as universal;
- a scalar score across all VSM functions.

A raw observation may be generated in a specialized environment and should preserve that fact as provenance.

```text
observation.task_domain = software-engineering
```

is factual context. It does not by itself establish a general S1 claim.

Evidence for broader generality may include, where supportable:

- function-focused evidence whose membrane is not tied to one application domain;
- materially comparable replication across multiple domains;
- independently supported transfer across environments;
- another explicit, reviewable argument for broader scope.

Unknown transfer remains unknown.

## 6. Domain-specific boundary

Domain-specific evaluation is outside this repository's ownership boundary.

A future domain-specific repository such as `vsm-harness-capability-swe` is a **fresh assessment system**, not a filtered view of this corpus.

A domain-specific system may consume:

- Profile semantics;
- canonical Index findings;
- reusable public observations from this repository;
- general-capability findings;
- additional domain-specific public evidence.

It then defines its own:

- operating purpose and system-in-focus;
- admission boundary;
- required or permitted ownership arrangements for that purpose;
- evidence requirements;
- capability requirements;
- assessment corpus and derived views.

A domain-specific autonomy requirement does not redefine `A`, `C`, `P` or any VSM function. It states which already-defined arrangements are required, permitted or insufficient for the domain's operating purpose.

Therefore a domain-specific assessment is not equivalent to:

```text
vsm-harness-capability WHERE task_domain = <domain>
```

## 7. Neutral evidence first

The empirical architecture is:

```text
public evidence
        ↓
evidence-surface identity
        ↓
concrete system identity
        ↓
neutral raw observation
        ↓
provenance + execution metadata
        ↓
optional derived interpretations
```

The neutral observation layer owns factual evidence identity. It does not need a canonical VSM-function interpretation before admission.

A later derived view may argue:

```text
observation X → direct S2 relevance
observation X → S2 + S3 proxy relevance
observation X → not direct S2
observation X → no useful VSM attribution
```

without rewriting the raw observation.

## 8. One result, one raw record

A published empirical result is stored once.

Function-specific projections and comparison cells reference the raw observation ID instead of copying numeric payloads into independently maintained databases.

This keeps factual provenance separable from interpretation.

## 9. Public-evidence-only operating model

OpenSiro does not run or reproduce benchmark experiments on assessed harnesses in order to create missing capability evidence for this repository.

```text
capability gap
        ↓
OpenSiro runs harness benchmark
        ↓
newly manufactured evidence
```

is not an active admission path.

A public-evidence gap remains a gap until suitable upstream or third-party evidence exists.

Historical controlled-execution work from the predecessor experiment may be preserved under `historical/`, but it must not be treated as an active evidence-generation workflow.

## 10. Evidence dimensions remain orthogonal

At minimum keep separate:

- evidence-source provenance;
- system compatibility;
- comparison quality;
- canonical VSM ownership state;
- VSM-function relevance;
- capability causal ownership;
- domain context;
- adaptation/reset state.

One dimension must not silently imply another.

## 11. Ordinary capability vs self-organization

Ordinary capability asks:

> How good is the current Sx repertoire under the admitted evidence membrane?

Experimental self-organization asks:

> Can Sx endogenously improve its own repertoire and later close relevant variety through the changed repertoire?

These remain separate research questions.

Persistent cross-task adaptation must not be silently mixed into a frozen ordinary baseline. A high ordinary benchmark result does not establish self-organization.

## 12. Historical vs live state

Frozen historical experiment snapshots remain immutable historical artifacts.

Current evidence, interpretations and frontiers evolve independently as new public evidence is admitted.

Do not rewrite historical synthesis merely because the live frontier changes.

## 13. Promotion boundary

This repository is experimental and non-normative.

If a reusable **procedure** for capability assessment becomes normative, the procedure belongs in `opensiro/vsm-harness-skills`.

If new organizational semantics are required, those semantics belong in `opensiro/vsm-harness-profile` first.

Creating or stabilizing this repository does not automatically admit it into the bounded `opensiro/vsm-oss-organization` viable system. That requires a separate explicit organizational-boundary change.
