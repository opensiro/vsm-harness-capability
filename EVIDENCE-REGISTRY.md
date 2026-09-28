# Neutral system-evidence registry

Status: **experimental, non-normative**

The neutral registry is the factual evidence layer beneath VSM-function and capability interpretations.

Its first responsibility is **identity and provenance**, not semantic classification.

## Core responsibilities

For each admitted observation preserve, where public evidence permits:

1. evidence-surface identity;
2. concrete system identity;
3. execution identity;
4. result identity;
5. source provenance;
6. system compatibility;
7. comparison metadata;
8. historical relation to canonical Index review state;
9. adaptation/reset state;
10. factual task / operating-domain context.

Unknown values remain unknown.

## Core flow

```text
public evidence
        ↓
raw observation
        ├── VSM-function projection
        ├── comparison-cell membership
        ├── general-capability view
        └── downstream domain-specific consumer
```

The branches above are consumers. They do not rewrite raw evidence identity.

## Raw / derived ownership rule

The raw layer owns:

- system/result identity;
- benchmark or other evidence-surface identity;
- raw metrics / outcomes;
- public source provenance;
- execution/configuration metadata;
- factual environment/domain context;
- compatibility and comparison metadata where directly supportable.

Derived layers own:

- VSM-function relevance;
- direct vs proxy interpretation;
- function-specific boundary classification;
- capability causal-ownership interpretation;
- comparison-cell eligibility;
- generality claims.

Do not copy numeric result payloads into function projections.

## One result, one record

One published result must have one raw observation ID even when it is relevant to multiple functions or downstream domains.

## Canonical linkage

Canonical harness linkage is optional and evidence-backed. A valid raw observation may remain non-canonical when its system identity is public and useful but cannot be linked to an Index harness.

`assessment boundary ≠ observation boundary`.

## Domain boundary

Factual domain metadata is allowed in the neutral registry. Domain-specific assessment semantics are not.

A downstream domain repository may consume the same observation under its own evidence contract without changing the raw record.
