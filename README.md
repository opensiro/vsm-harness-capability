# VSM Harness Capability

> **Status: experimental**

Experimental evidence-backed research on **general functional capability** of autonomous agent harnesses, compared one VSM function at a time.

This repository asks a different question from the canonical [VSM Harness Index](https://github.com/opensiro/vsm-harness-index):

```text
canonical VSM assessment:
Which organizational functions exist at the declared boundary,
and who owns their decisive closure?

general functional capability:
Given an established VSM function,
what empirical evidence supports how capable that function is
across systems under comparable conditions?
```

The distinction is deliberate:

```text
canonical closure / ownership
        ≠
general functional capability
        ≠
domain-specific assessment
```

`A`, `C`, `P`, `A(P)`, `C(P)`, `—`, and `?` are ownership / closure states, not performance scores. Benchmark performance does not create or change those states.

## Start here

- [`CONTRACT.md`](CONTRACT.md) — authoritative repository-local scope and architecture.
- [`PUBLIC-EVIDENCE.md`](PUBLIC-EVIDENCE.md) — public-evidence admission and provenance contract.
- [`EVIDENCE-REGISTRY.md`](EVIDENCE-REGISTRY.md) — neutral observation-layer responsibilities.
- [`BASELINE.md`](BASELINE.md) — per-function general-capability comparison rules.
- [`MIGRATION.md`](MIGRATION.md) — completed migration record from the original Index experiment.

Cross-repository responsibility and the relationship to future domain-specific repositories are documented in [`opensiro/vsm-oss-organization/ECOSYSTEM.md`](https://github.com/opensiro/vsm-oss-organization/blob/main/ECOSYSTEM.md).

## Ecosystem position

```text
vsm-harness-profile
    authoritative VSM semantics
        ↓
vsm-harness-skills
    canonical assessment methodology
        ↓
vsm-harness-index
    repository-relative closure / ownership corpus
        │
        └──────────────→ vsm-harness-capability
                         experimental general functional capability
```

Capability consumes Profile semantics and may link to canonical Index identities and assessments. It does not redefine either.

## Core comparison unit

Capability is compared **one VSM function at a time**:

```text
capability(system A, S1) ↔ capability(system B, S1)
capability(system A, S2) ↔ capability(system B, S2)
...
```

There is no universal harness capability score and no maturity ordering over ownership states.

## General means application-domain-independent scope

`general` is the default scope of this repository and therefore is not encoded in the repository name.

General capability does **not** mean averaging domain benchmarks. A specialized result remains specialized unless broader transfer is independently supported.

```text
strong SWE result
        ≠ automatically
strong general S1 capability
```

Raw observations may record their real task or operating domain as provenance. Domain-specific assessment, admission, autonomy requirements and evidence thresholds belong to separate downstream repositories.

## Evidence model

```text
public benchmark / paper / leaderboard /
repository result / operational witness
        ↓
evidence-surface identity
        ↓
concrete system identity
        ↓
neutral raw observation
        ↓
provenance + execution metadata
        ↓
optional VSM-function projection
        ↓
matched general-capability comparison where supportable
```

A raw result is stored once. Derived function mappings and comparison views reference the raw observation rather than copying the empirical payload.

OpenSiro does **not** run assessed harness benchmarks merely to manufacture missing capability evidence for this repository. A public-evidence gap remains a gap.

## Repository layout

```text
system-observations/   neutral public empirical observations
vsm-projections/      derived S1–S5 relevance mappings
comparison-cells/     materially comparable cross-system cells
baselines/            per-function baseline selections / rules
frontier/             current generated evidence frontier
historical/           frozen pre-repository experiment artifacts
scripts/              repository-local validation / rendering tooling
```

The extraction from `vsm-harness-index/experiments/functional-capability-depth` is complete for pinned source revision `3446fe77e031878dc8ad4edfb857b608a7a6b26f`. Active capability maintenance now occurs here; the Index retains a migration pointer and remains authoritative for canonical assessments. See [`MIGRATION.md`](MIGRATION.md).

## Source-of-truth boundaries

- **VSM semantics:** [`opensiro/vsm-harness-profile`](https://github.com/opensiro/vsm-harness-profile)
- **Canonical assessment methodology:** [`opensiro/vsm-harness-skills`](https://github.com/opensiro/vsm-harness-skills)
- **Canonical repository-relative assessments:** [`opensiro/vsm-harness-index`](https://github.com/opensiro/vsm-harness-index)
- **Cross-repository architecture:** [`opensiro/vsm-oss-organization`](https://github.com/opensiro/vsm-oss-organization)
- **This repository:** experimental general functional-capability evidence and derived comparisons

## Validation

```bash
python scripts/validate_repository.py
```

## License

Repository code and original documentation are licensed under the Apache License 2.0. Imported public evidence retains its source provenance and does not change the licensing of linked third-party artifacts.
