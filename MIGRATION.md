# Migration from `functional-capability-depth`

Status: **active migration record**

The predecessor of this repository is the public experiment:

```text
opensiro/vsm-harness-index/
  experiments/functional-capability-depth/
```

The migration is intentionally **lossless and staged**.

## Source boundary

Migration source:

- source repository: `opensiro/vsm-harness-index`;
- source branch: `main`;
- reviewed source revision: `3446fe77e031878dc8ad4edfb857b608a7a6b26f` (2026-09-28);
- source path: `experiments/functional-capability-depth/`.

The exact predecessor ref is also stored in [`historical/SOURCE-REF`](historical/SOURCE-REF), and the imported predecessor surface has a checksum inventory in [`historical/PREDECESSOR-SHA256SUMS.txt`](historical/PREDECESSOR-SHA256SUMS.txt).

Later source changes must be reconciled explicitly rather than silently assumed to be present here.

## Architecture change during migration

The predecessor experiment evolved from function-first benchmark mapping into a neutral-evidence-first model.

The new repository makes that later model explicit:

```text
public evidence
→ neutral raw observation
→ optional VSM projection
→ comparison cell
→ general capability view
```

It also makes one newer boundary explicit:

```text
general capability
        ≠
domain-specific assessment
```

Older predecessor wording that treated domain-specific views as an owned projection of the same capability repository is superseded by [`CONTRACT.md`](CONTRACT.md) and the cross-repository architecture note in `vsm-oss-organization`.

## Migrated active state

The branch `bootstrap/experimental-capability` now contains:

- the neutral `system-observations/` corpus;
- **53 raw observation IDs** copied losslessly from the pinned predecessor;
- raw registry rendering and validation tooling;
- S1–S5 derived projection surfaces under `vsm-projections/`;
- the benchmark-family mapping under `vsm-projections/benchmark-family-map/`;
- per-function baseline selections and explicit gaps under `baselines/`;
- the current evidence frontier under `frontier/`;
- repository-local validation and CI.

Canonical VSM assessments were deliberately **not** copied. Canonical identity/state remains owned by `opensiro/vsm-harness-index`; extracted derived validators resolve the current Index assessment when a live canonical-state check is required.

Active path references have been rebased from the predecessor directory layout to this repository layout.

## Intentional architecture-only normalization

The migration is not a blind rename of every predecessor concept.

The active repository contract intentionally changes two boundaries without changing raw evidence:

1. **Domain-specific assessment is external.** Factual domain context stays in raw evidence, but domain-specific admission/autonomy/evidence requirements belong to separate downstream repositories.
2. **OpenSiro-operated execution is historical only.** Controlled-execution artifacts do not form an active path for manufacturing capability evidence.

These changes are recorded as architecture changes, not empirical-result changes.

## Historical artifacts

Historical research is preserved rather than rewritten into the new active workflow, including:

- Batch 01;
- Batch 02 controlled-replication design / failed execution attempt;
- LoopX preregistration / execution-harness artifacts;
- frozen synthesis / experiment-state snapshots tied to the predecessor cycle;
- predecessor rendering / validation tooling where useful for provenance.

LoopX has been moved out of active S2 projections into `historical/`.

Historical controlled-execution material is research history. It is not an active evidence-generation path.

## No double source of truth

During bootstrap, the predecessor Index experiment remains provenance history.

After this repository's bootstrap is merged and validated, active capability maintenance belongs here. The Index should retain a migration pointer / frozen historical record rather than a second independently edited capability implementation.

Canonical VSM assessments remain in the Index throughout. They are not migrated.

## Remaining completion gates

Migration is complete only when:

1. the full derived S1–S5 validator suite passes from the extracted layout;
2. repository-local contract / raw-registry / generated-file validation passes;
3. the bootstrap branch is merged to `main`;
4. the predecessor Index experiment is changed to a historical pointer rather than an active competing implementation;
5. the cross-repository `vsm-oss-organization` documentation reflects the live experimental repository while preserving the current bounded organization boundary.

Until those gates close, this file remains an active migration record rather than a completion declaration.
