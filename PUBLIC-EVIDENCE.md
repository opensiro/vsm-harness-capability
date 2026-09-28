# Public-evidence capability ingestion

Status: **experimental, non-normative**

This document defines the active evidence-ingestion contract for `vsm-harness-capability`.

The repository is an evidence and interpretation layer, **not a benchmark operator**.

**OpenSiro does not run or reproduce benchmark experiments on assessed harnesses to create capability evidence for this repository.** A public-evidence gap remains a gap until suitable public upstream or third-party evidence exists.

## Active flow

```text
public benchmark / paper / leaderboard /
repository result / operational witness
        ↓
evidence-surface identity
        ↓
concrete system identity
        ↓
raw system-linked observation
        ↓
provenance + execution metadata
        ↓
optional derived VSM / capability interpretation
```

Raw observation admission does not require OpenSiro to first decide which VSM function the evidence measures.

## Admission sequence

For each public result:

1. identify the public source and preserve an immutable revision/artifact where available;
2. identify the evidence surface: benchmark family/version/task set or a named non-benchmark paper/repository/operational witness;
3. identify the concrete system exercised by the evidence;
4. link to a canonical Index harness only when public provenance supports the linkage;
5. classify system compatibility where supportable;
6. preserve the raw result and historical execution identity;
7. record comparison metadata and known confounders without manufacturing comparability;
8. record factual task/operating-domain context where available;
9. store the raw observation once.

Unknown values remain unknown.

## Evidence-source classes

- `external-reproduced` — result published by an evaluator or research/benchmark operator independent of the measured project;
- `first-party-reported` — result published by the measured project or its maintainers;
- `mechanism-only` — public executable/repository evidence establishes a mechanism or path but no admitted numeric performance observation exists.

Source class describes provenance, not VSM meaning or comparison quality.

## System compatibility

Typical values:

- `native-system`;
- `adapter-preserved`;
- `benchmark-scaffolded`;
- `unclear`.

Compatibility describes what system boundary the public evidence actually exercised.

## Comparison quality

A direct cross-system comparison should keep materially constant, as far as the public record permits:

- benchmark family/version/task set;
- model and materially relevant model configuration;
- evaluator / grader;
- execution environment;
- budget / timeout / repetition policy;
- adaptation/reset policy.

Use explicit weaker classes such as `partially-matched` or `descriptive-only` when these are not materially matched.

Do not normalize unrelated benchmark families into one universal score.

## Required provenance

Preserve where available:

- system / harness display identity;
- canonical harness ID when linkable;
- repository and historical revision/version/configuration;
- relation to the current canonical assessment revision;
- evidence-surface identity;
- model and model configuration;
- metric and raw result;
- task / replicate count;
- result date;
- publisher;
- primary and immutable source;
- execution environment;
- evaluator / grader;
- budget / timeout / repetition settings;
- evidence-source class;
- system compatibility;
- comparison group and quality;
- adaptation/reset state;
- factual domain context;
- known discrepancies and confounders.

Current repository state must not be used to invent historical run metadata.

## System linkage

A display label is not enough to establish canonical harness linkage.

Support linkage using public evidence such as:

- an adapter that installs or invokes the first-party harness;
- exact repository / revision / version in result metadata;
- first-party artifact identifying the implementation;
- another reconstructable public provenance chain.

If the benchmark authors supply the material organization and no canonical harness identity is supportable, preserve the observation as benchmark-scaffolded / non-canonical rather than inventing a mapping.

## Non-benchmark evidence

The registry may admit public non-benchmark evidence such as immutable repository history, public operational incidents/case studies, or publication witnesses.

Use explicit evidence-surface identity rather than inventing a benchmark label.

## VSM relevance is downstream

The raw registry does not own a canonical `benchmark → VSM function` taxonomy.

Function relevance is a reviewable derived interpretation under Profile semantics.

## Domain context is provenance, not domain assessment

A raw observation may record `software-engineering`, `browser-use`, `scientific-research` or another task/operating domain because that describes where the evidence was produced.

This repository does not turn those labels into domain-specific admission, autonomy or capability grades. Those belong to separate downstream domain-specific assessment systems.

## Capability causal ownership

Where independently supported, a derived interpretation may describe causal capability ownership as:

- `native`;
- `inherited`;
- `mixed`;
- `unclear`.

A score alone does not establish causal ownership.

## Historical observations

Public results are temporal evidence. Preserve historical run identity even when the canonical Index assessment later moves to a newer revision.

New releases may justify new observations; they do not invalidate older correctly identified evidence.

## Non-goals

- no benchmark-driven mutation of canonical VSM assessments;
- no global harness winner;
- no scalar score across S1–S5;
- no maturity ladder over `A`, `C`, `P`;
- no forced normalization across unrelated benchmark families;
- no OpenSiro-operated runs to manufacture missing evidence;
- no domain-specific assessment contract in this repository.
