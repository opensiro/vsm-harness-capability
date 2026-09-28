# TeamBench verifier-remediation — S3* evidence review

Status: experimental, non-normative.

Tracking issue: #40

Reviewed sources:

```text
opensiro/vsm-harness-profile@88d865f46ac93ec03b8fe0d58ef45054a64cead5
ybkim95/TeamBench@d185aef1916fd86a9ba554d581fd256319a973af
system-observations/teambench.json#teambench-gpt54mini-verifier-remediation-lb90-2026
```

Profile basis:

```text
VSM Harness Profile v0.2.4
S3* = complementary audit
```

## Result

```text
function: S3*
fit: direct
system_linkage: benchmark-scaffolded-noncanonical
primary_reopen: no
```

The reviewed TeamBench `full` organization directly exercises complementary audit at the **benchmark-defined composed organization boundary**. This classification belongs to the Planner → Executor → Verifier organization plus the remediation closure implemented by TeamBench. It does not belong to the underlying model, the external task grader, or any canonical harness by association.

## Direct-S3* closure

The Profile requires more than a component named `Verifier`: the audit path must add sufficiently independent access to operational reality, challenge an ordinary operational claim, and return findings into subsequent control or operation.

The TeamBench full organization establishes that chain:

1. **Ordinary operational path.** The Executor receives a brief plus Planner messages, edits and executes in the workspace, and reports completion to the Verifier.
2. **Complementary access.** The Verifier is a separately configured role with the full task specification, direct read access to the workspace/reports/messages/submission, and command execution for tests or behavioural checks. It cannot permanently modify the workspace; its write access is limited to the submission/attestation surface.
3. **Independent audit judgment.** The Verifier is instructed to check each requirement against the full specification and observed workspace, produce a pass/fail attestation, and send specific failure evidence back to the Executor. The decisive audit judgment is therefore not merely the Executor's own completion claim or self-check.
4. **Return into operation.** A failed Verifier judgment causes the orchestrator to re-run the Executor with the audit feedback for targeted remediation, after which a fresh Verifier pass is executed. A passing judgment closes the loop and terminates remediation.
5. **Matched removal control.** The `team_no_verify` arm removes the Verifier and verifier-triggered remediation while retaining the Planner → Executor path. The neutral raw observation preserves the matched public aggregate without turning the result magnitude into a VSM definition.

```text
Planner guidance
      ↓
Executor changes workspace ── completion claim
      ↓                         │
      └───────────────┐         │
                      ↓         │
Verifier: full spec + direct workspace/tests
                      ↓
                audit judgment
                 ↙           ↘
             fail             pass
               ↓                ↓
feedback → Executor          close run
   remediation
       ↓
  re-verification
```

The role is mandatory in the benchmark's `full` protocol, but that does not make it S3* merely by workflow position. The direct fit follows from its materially different evidence access, separately constrained decision role, and corrective return path. This is stronger than a routine checker that only repeats the producing unit's own report or controlled test.

## Ownership and supporting mechanisms

The **Verifier agent role** owns the audit judgment within the benchmark-defined organization: it interprets the full specification and observed workspace/test evidence and chooses the attestation verdict and feedback.

Supporting mechanisms remain separate:

- TeamBench's deterministic orchestrator sequences phases, parses the attestation, bounds remediation loops, and invokes the next Executor/Verifier phase;
- OS/tool permissions enforce role separation and restrict workspace mutation;
- the post-run task-specific grader scores benchmark artifacts after the run.

The deterministic task grader is an external evaluation surface common to the benchmark arms. It does not supply the runtime audit judgment that closes the Verifier → remediation → re-verification loop and therefore does not inherit S3* ownership from this review.

## Benchmark-defined boundary

This is a **benchmark-scaffolded** composed organization, not evidence that GPT-5.4 Mini or another model intrinsically implements S3*. TeamBench supplies the role decomposition, permissions, prompts, message path, remediation controller and experiment conditions.

Likewise, the result cannot be transferred to an external harness merely because that harness could use the same model. A separate native or adapter-preserved implementation would require its own boundary evidence.

## Why this does not reopen the S3* primary

The frozen S3* primary-search closure explicitly says not to reopen for another benchmark-supplied external reviewer loop. Its reopen gate requires materially matched evidence in which multiple independently canonical-linkable native or adapter-preserved S3* paths are active.

TeamBench strengthens the direct evidence set, but it remains:

- one benchmark-defined non-canonical organization;
- benchmark-scaffolded rather than a canonical native or adapter-preserved audit path;
- not a matched comparison across multiple canonical S3* implementations.

Therefore:

```text
new direct S3* evidence: yes
new canonical S3* observation: no
matched multi-canonical S3* cell: no
primary baseline: gap
```

The family is registered only in the live post-closure extension. The frozen base family map, frozen S3* closure counts, selected baseline state and generated frontier remain unchanged.

## Raw-evidence ownership

The empirical payload remains owned by:

```text
system-observations/teambench.json
  # teambench-gpt54mini-verifier-remediation-lb90-2026
```

This derived review does not duplicate benchmark scores and does not claim an OpenSiro reproduction of the public TeamBench run.

## Non-claims

This review does not claim that:

- GPT-5.4 Mini, or any other underlying model, intrinsically owns S3*;
- the external deterministic task grader is the runtime S3* owner;
- every mandatory verifier or QA stage is S3*;
- the published matched result proves that verifier/remediation always improves outcomes;
- TeamBench is a canonical VSM Harness Index system;
- the first-party aggregate was independently reproduced by OpenSiro;
- a matched S3* primary baseline has been found.

## Mutation boundary

This review does not change Profile semantics, Skills methodology, canonical Index ownership, raw evidence, frozen S3* closure counts, any comparison cell, or the current S3* primary gap.
