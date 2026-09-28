# Migration from `functional-capability-depth`

Status: **active migration record**

The predecessor of this repository is the public experiment:

```text
opensiro/vsm-harness-index/
  experiments/functional-capability-depth/
```

The migration is intentionally **lossless and staged**.

## Source boundary

Initial migration review boundary:

- source repository: `opensiro/vsm-harness-index`;
- source branch: `main`;
- reviewed source revision: `3446fe77e031878dc8ad4edfb857b608a7a6b26f` (2026-09-28);
- source path: `experiments/functional-capability-depth/`.

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

## Active artifacts to migrate

The active predecessor surfaces include:

- neutral `system-observations/`;
- public-evidence and registry contracts;
- S1–S5 function-specific derived evidence;
- primary-baseline selections and gaps;
- generated current evidence frontier;
- rendering / validation tooling.

These should become live repository-owned artifacts here only after content and generated-file consistency are checked.

## Historical artifacts

Historical research must be preserved rather than rewritten into the new active workflow, including:

- Batch 01;
- Batch 02 controlled-replication design / failed execution attempt;
- LoopX preregistration / execution-harness artifacts;
- frozen synthesis / experiment-state snapshots tied to the predecessor cycle.

Historical controlled-execution material is research history. It is not an active evidence-generation path.

## No double source of truth

During migration, the predecessor Index experiment remains provenance history and may temporarily remain the current copy of some artifacts.

After an artifact is explicitly migrated and validated here, future active maintenance should occur here, while the Index retains a migration pointer / frozen historical record rather than a second independently edited copy.

Canonical VSM assessments remain in the Index throughout. They are not migrated.

## Completion conditions

Migration is complete only when:

1. every active raw observation has a lossless counterpart here;
2. active function projections reference the migrated raw records;
3. current baseline/frontier outputs reproduce the predecessor state or document an intentional architecture-only change;
4. historical experiment artifacts remain recoverable with provenance;
5. repository-local validation passes;
6. the Index experiment is changed to a historical pointer rather than an active competing implementation.
