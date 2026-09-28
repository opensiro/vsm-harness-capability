# S1 General Capability Baseline

Status: **experimental, non-normative**

This is the current selected **general** S1 comparison cell. It is not a global harness ranking and does not change canonical VSM ownership. Rows are ordered by harness ID, never by score.

## Function baseline availability

| Function | Status | Primary family | Reference model |
| --- | --- | --- | --- |
| S1 | `selected` | PawBench v1.0 | `qwen3.6-35b-a3b` |
| S2 | `gap` | — | — |
| S3 | `gap` | — | — |
| S3* | `gap` | — | — |
| S4 | `gap` | — | — |
| S5 | `gap` | — | — |

A `gap` means no materially matched canonical-harness general-capability primary has been selected for that function. It is not a zero score and does not mean relevant public evidence is absent.

## S1 selected general primary

**PawBench v1.0** · model `qwen3.6-35b-a3b` · comparison `matched-model-cross-harness`

| Harness | Canonical S1 | Historical benchmark identity | Result | Compatibility |
| --- | --- | --- | ---: | --- |
| Hermes Agent (`hermes-agent`) | `A` | `2026.4.23` · version-known | `0.5674` | `adapter-preserved` |
| OpenClaw (`openclaw`) | `A` | `2026.4.24` · version-known | `0.6779` | `adapter-preserved` |
| QwenPaw (`qwenpaw`) | `A` | `1.1.3` · version-known | `0.6828` | `adapter-preserved` |

The raw numeric results remain owned by `system-observations/`; this file is a derived comparison view. Historical benchmark identity must not be relabelled as the current canonical Index revision.

## Specialized-domain evidence

The raw registry also contains evidence from specialized environments such as software engineering. Those observations remain available as provenance/evidence, but this repository does not publish a Coding/SWE capability grade or domain-specific primary.

A specialized-domain repository may later consume those observations and perform a fresh assessment under its own domain contract.

## Reading rule

```text
canonical VSM state
        ≠
general functional capability
        ≠
domain-specific assessment
```

Do not average PawBench with unrelated benchmark families into one S1 or overall harness score. Adaptive/self-organizing evidence remains a separate evidence class.
