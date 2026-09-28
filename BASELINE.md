# Per-function general-capability baseline rules

Status: **experimental, non-normative**

Public-evidence contract: [`PUBLIC-EVIDENCE.md`](PUBLIC-EVIDENCE.md).
Repository scope: [`CONTRACT.md`](CONTRACT.md).

This document defines a simple comparison baseline for **general functional capability** beside canonical VSM closure and ownership.

## Baseline shape

For the simple baseline view:

```text
1 VSM function → 1 primary benchmark / evidence family
```

This is a view rule, not a restriction on the underlying evidence model.

Each function may retain:

- one selected primary family where a valid matched cell exists;
- secondary evidence;
- mechanism-specific evidence;
- alternative environments;
- explicit gaps.

Do not average unrelated evidence families into a universal score.

## Rule 1 — compare one function at a time

```text
capability(system A, Sx) ↔ capability(system B, Sx)
```

Do not create one harness-wide capability score.

Canonical VSM ownership states remain a separate axis.

A function with canonical state `—` does not receive a low capability score merely because the canonical path is absent.

## Rule 2 — use materially matched comparison cells

Hold constant where public evidence permits:

- model and material model configuration;
- evidence family/version/task set;
- evaluator / grader;
- execution environment;
- budget / timeout / repetition policy;
- adaptation/reset policy.

The system/harness should be the intended varying factor.

Where those conditions are not matched, retain the evidence as observational, partially matched, descriptive or proxy rather than manufacturing a baseline comparison.

## Rule 3 — primary does not erase secondary evidence

Changing the selected primary family must not delete or rewrite historical observations.

A primary is a simple current view over the evidence corpus, not the corpus itself.

## Rule 4 — generality must be supported

A specialized-domain result is not automatically a general-capability result.

```text
strong SWE result
        ≠ automatically
strong general S1 capability
```

A general claim requires an explicit basis for application-domain-independent scope, such as function-focused evidence, cross-domain replication, supported transfer, or another reviewable argument.

Raw domain context remains available as provenance.

This repository does not publish domain-specific capability grades. A future domain-specific repository performs a fresh domain assessment under its own boundary and evidence contract.

## Rule 5 — ordinary baseline uses a frozen functional repertoire

Ordinary capability measures the quality of the current function repertoire, not persistent self-improvement across benchmark tasks.

Within-task reasoning, tool use, retry and recovery are allowed.

Persistent repertoire changes across tasks must be reset/isolated where the public protocol establishes such controls, or the observation must be marked adaptive / non-baseline-comparable.

If reset/adaptation state is unknown, keep it unknown.

## Rule 6 — self-organizing evaluation remains separate

Ordinary capability:

> How good is the current Sx repertoire?

Self-organizing experiment:

> Can Sx endogenously improve its own repertoire and later operate through the changed repertoire?

Do not infer self-organization from a high ordinary score and do not silently compare an adaptive run with a frozen baseline run.

## Rule 7 — raw observations stay shared

Store a published result once in `system-observations/`.

Function projections and comparison cells reference that raw observation ID.

## Rule 8 — preserve version/provenance identity

Historical evidence remains historical. Never relabel an old result as if it evaluated the current canonical Index revision.

## Gap semantics

A primary `gap` means only:

> the reviewed general-capability view does not currently support a selected materially matched primary comparison cell for that function.

It does not mean zero capability, no evidence, or a requirement for OpenSiro to run a benchmark.
