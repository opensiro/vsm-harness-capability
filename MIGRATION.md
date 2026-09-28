# Migration from `functional-capability-depth`

Status: **completed migration record**

The predecessor of this repository was the public experiment:

```text
opensiro/vsm-harness-index/
  experiments/functional-capability-depth/
```

The extraction was completed losslessly at the pinned source boundary below, with intentional architecture-only normalization of the active layer documented in this repository.

## Source boundary

Migration source boundary:

- source repository: `opensiro/vsm-harness-index`;
- source branch: `main`;
- reviewed source revision: `3446fe77e031878dc8ad4edfb857b608a7a6b26f` (2026-09-28);
- source path: `experiments/functional-capability-depth/`.

Later historical changes to the Index must not be silently treated as part of this extraction. New active capability work belongs here.

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

## Migrated active artifacts

The extraction imported and validated:

- neutral `system-observations/`;
- public-evidence and registry contracts;
- S1–S5 function-specific derived evidence;
- primary-baseline selections and gaps;
- generated current evidence frontier;
- rendering / validation tooling.

The neutral corpus preserved **53 unique raw observation IDs** at extraction. Raw observation files were checked against the pinned predecessor source, and predecessor checksums/source provenance are preserved under `historical/`.

The exact migrated observation-ID set is frozen in [`historical/MIGRATED-OBSERVATION-IDS.txt`](historical/MIGRATED-OBSERVATION-IDS.txt). Repository validation treats that set as a migration floor: every migrated ID must remain present, while valid new public observations may be added to the live corpus after extraction.

This separates two invariants that should not be conflated:

```text
migration completeness
    = all 53 extracted observation IDs remain recoverable

live capability corpus
    = migration floor + later admitted public observations
```

The migration record therefore does not freeze the active corpus at 53 observations.

## Historical artifacts

Historical research was preserved rather than rewritten into the new active workflow, including:

- Batch 01;
- Batch 02 controlled-replication design / failed execution attempt;
- LoopX preregistration / execution-harness artifacts;
- frozen synthesis / experiment-state snapshots tied to the predecessor cycle;
- experiment-specific Index tests that lived outside the predecessor subtree, preserved under `historical/predecessor-tests/`.

Historical controlled-execution material is research history. It is not an active evidence-generation path.

## Source-of-truth state after extraction

Active capability maintenance now occurs in this repository.

The predecessor Index path has been reduced to a stable migration pointer rather than an independently maintained capability implementation. Capability-specific Index CI/tests were removed after their predecessor copies were preserved here where applicable.

Canonical VSM assessments, catalog state, TLDR, Rankings, Full-A and autonomy states remain in `opensiro/vsm-harness-index`. They were not migrated.

## Completion record

The migration completed the intended conditions:

1. every active raw observation at the pinned source boundary has a lossless counterpart here;
2. active function projections were migrated into the Capability-owned `vsm-projections/` layer;
3. current baseline/frontier outputs were migrated, with intentional removal of active domain-specific grading/projection ownership;
4. historical experiment artifacts remain recoverable with source/checksum provenance;
5. repository-local validation preserves the frozen 53-observation migration floor and checks neutral-registry regeneration while permitting later live-corpus growth;
6. the Index predecessor path is now a migration pointer rather than an active competing implementation.

This completion does not change the repository's status: `opensiro/vsm-harness-capability` remains **experimental and non-normative** and is not automatically admitted into the bounded `opensiro/vsm-oss-organization` viable system.
