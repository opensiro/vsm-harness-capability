# Contributing

`vsm-harness-capability` is experimental public research on general per-function harness capability.

Before changing data or interpretation, read:

1. [`CONTRACT.md`](CONTRACT.md);
2. [`PUBLIC-EVIDENCE.md`](PUBLIC-EVIDENCE.md);
3. [`EVIDENCE-REGISTRY.md`](EVIDENCE-REGISTRY.md);
4. [`BASELINE.md`](BASELINE.md).

## Route changes by ownership

- VSM semantics → `opensiro/vsm-harness-profile`;
- canonical assessment procedure → `opensiro/vsm-harness-skills`;
- canonical repository assessment → `opensiro/vsm-harness-index`;
- cross-repository architecture / organization boundary → `opensiro/vsm-oss-organization`;
- general capability evidence / projections / comparison cells → this repository;
- domain-specific autonomy/evidence requirements → the owning future domain repository.

## Evidence rules

Prefer primary public evidence and immutable artifacts. Preserve unknowns. Do not infer function meaning from benchmark vocabulary. Do not operate assessed harness benchmarks merely to fill an evidence gap.

## Pull requests

Meaningful changes should use reviewable PRs. Keep raw evidence changes separate from semantic interpretation when practical so factual identity and derived claims can be reviewed independently.

Run:

```bash
python scripts/validate_repository.py
```
