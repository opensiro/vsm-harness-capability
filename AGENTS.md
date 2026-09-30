# Agent guidance

This repository is an **experimental, non-normative** capability research layer.

Read in this order:

1. `CONTRACT.md` — local scope / ownership boundary;
2. `PUBLIC-EVIDENCE.md` — evidence admission;
3. `EVIDENCE-REGISTRY.md` — raw vs derived ownership;
4. `BASELINE.md` — comparison rules;
5. `MIGRATION.md` — predecessor provenance.

Authoritative upstreams:

- VSM semantics: `opensiro/vsm-harness-profile`;
- canonical assessment methodology: `opensiro/vsm-harness-skills`;
- canonical repository assessments: `opensiro/vsm-harness-index`;
- cross-repository architecture: `opensiro/vsm-oss-organization`.

Core rules:

- map organizational function before any capability interpretation;
- never treat `A/C/P/...` as performance or maturity grades;
- store one public result once in the neutral observation layer;
- keep factual provenance separate from VSM interpretation;
- do not manufacture capability evidence with OpenSiro-operated benchmark runs;
- general capability is not an average over domains;
- domain-specific assessment is a separate downstream system-in-focus;
- preserve historical experiment artifacts as history rather than active workflow.

## Track A downstream queue

For the active observational paper study, repetitive W2→W3→W4 routing is owned by the non-normative cross-repository queue in `opensiro/vsm-harness-research`:

```text
paper/studies/obs-harness-assoc/v0.2.0/TRACK_A_QUEUE.md
paper/studies/obs-harness-assoc/v0.2.0/track-a-queue.v0.5.json
```

The prospective successor rule is:

> **Assessment owns structure; W3 only projects historical run mode.**

Canonical Assessment artifacts/history in the frozen Assessment universe are the structural source of truth for successor W3. W3 must not perform a mini-reassessment from harness source code. If the benchmarked historical revision cannot be bound to an applicable canonical Assessment, preserve it as `structurally-unprojectable` / `?` according to the successor authority rather than creating a new historical Assessment.

Existing `OBS-HARNESS-ASSOC v0.1.0` W3/W4 artifacts remain immutable old-method provenance. W1 neutral evidence and valid W2 historical linkage may be reused; successor W3/W4 migration is owned by the research repository and must be uniform before W5/Gate B/W6.

Active queue semantics remain **bounded same-stage batches of up to 5 handoffs with handoff-local busy-skip parallelism**. Every handoff keeps its own exact input binding; W2/W3/W4 roles must not be mixed in one chat. A claimed/executing handoff is busy and may be skipped for routing to another free handoff; scientific/control blockers remain global STOP conditions.

Stable fresh-chat prompt:

```text
Execute the next admitted Track A queue batch in opensiro/vsm-harness-research.
Follow paper/studies/obs-harness-assoc/v0.2.0/TRACK_A_QUEUE.md exactly.
Use a fresh independent context, claim and execute exactly one role-homogeneous batch, then stop at its defined boundary.
```

The queue does not change this repository's ownership boundary. W1 remains capability-owned, W2 remains bounded historical-linkage work under issue #94, and raw observations remain stored only here. W2 does not classify VSM structure. W3/W4 and successor migration are research-repository work. The queue is routing/control only and must not be treated as scientific evidence or as authority to perform W5/Gate B/W6.