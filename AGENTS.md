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
paper/studies/obs-harness-assoc/v0.1.0/TRACK_A_QUEUE.md
paper/studies/obs-harness-assoc/v0.1.0/track-a-queue.v0.1.json
```

Stable fresh-chat prompt:

```text
Execute the next admitted Track A queue item in opensiro/vsm-harness-research.
Follow paper/studies/obs-harness-assoc/v0.1.0/TRACK_A_QUEUE.md exactly.
Use a fresh independent context, claim and execute exactly one item, then stop at its defined boundary.
```

The queue does not change this repository's ownership boundary. W1 remains capability-owned, W2 remains bounded historical-linkage work under issue #94, and raw observations remain stored only here. W3/W4 are research-repository work. The queue is routing/control only and must not be treated as scientific evidence or as authority to perform W5/Gate B/W6.
