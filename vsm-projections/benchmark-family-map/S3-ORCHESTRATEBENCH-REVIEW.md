# OrchestrateBench policy-conditioned containment — S3 evidence review

Status: experimental, non-normative.

Tracking issue: #49

Reviewed sources:

```text
opensiro/vsm-harness-profile@88d865f46ac93ec03b8fe0d58ef45054a64cead5
anote-ai/Research-OrchestrateBench@5c3738c19d99cbe9aa152b0ea9b7d903ea4f93db
arXiv:2608.05263
system-observations/orchestratebench.json#orchestratebench-policy-conditioned-containment-2026
```

Profile basis:

```text
VSM Harness Profile v0.2.4
S3 = inside-and-now control with whole-system current-state visibility and authority to regulate current commitments, priorities or constraints
```

## Result

```text
function: S3
fit: direct
system_linkage: benchmark-scaffolded-noncanonical
primary_reopen: no
```

The reviewed OrchestrateBench policy-conditioned containment study directly exercises an S3 current-control relation at the **benchmark-defined composed control boundary**. The direct fit is narrow: the benchmark injects a current operational disturbance into a staged dependency chain, exposes a trusted upstream-state distinction to the strongest repair policy, grants that policy authority to correct the current stage, and measures whether the intervention changes subsequent downstream operation.

This does **not** establish autonomous S3 ownership for Claude, a canonical harness, or an ordinary router. The critical no-upstream ablation shows that most of the apparent containment gain depends on the benchmark-supplied trusted-state signal.

## Direct-S3 closure

The Profile requires a whole-system view of current operations together with actual authority over relevant current commitments or constraints. OrchestrateBench supplies that relation at its benchmark-scaffolded boundary.

1. **Current operational disturbance.** The benchmark injects prompt-level failures into an active staged dependency chain. The latent/semantic modes can corrupt the current stage and then propagate into later stages.
2. **Current-state distinction.** For the strongest `llm` policy, the benchmark supplies the trusted upstream result at the injected stage and explicitly licenses the policy to treat ambiguity, contradiction or inconsistency as a current-control exception. This is material current-state support, not autonomous detection.
3. **Corrective authority.** The policy may re-attempt the current stage and replace the stage result before downstream stages consume it. The Oracle arm makes the upper-bound authority explicit by deterministically repairing the current stage to the trusted correct value.
4. **Closure into subsequent operation.** The repaired or unrepaired current-stage result becomes the upstream value for later stages. Recovery and cascade radius therefore measure whether the control intervention changed subsequent operation rather than merely produced an advisory judgment.

```text
seeded current-stage disturbance
            ↓
 current staged operation
            ↓
 trusted upstream state ──→ repair policy
                              ↓
                     corrective re-attempt
                              ↓
                 current-stage result changed
                              ↓
             later stages consume new state
                              ↓
                 recovery / cascade outcome
```

This is direct S3 evidence because the measured treatment is an intervention on current operation with observable downstream closure. It is not direct merely because the paper uses routing or orchestration terminology.

## Trusted-state boundary and ownership

The ablation is essential to the interpretation.

The published study reports that the trusted-state LLM repair policy materially improves latent-failure containment, but the separate `llm_noupstream` arm removes the trusted upstream value while keeping the correction-style re-attempt. Recovery then collapses near the baseline level. Therefore the direct S3 relation must be attributed to the **composed benchmark control arrangement**, which combines:

- benchmark-supplied current-state truth;
- a policy/model capable of choosing a corrective re-attempt from that distinction;
- authority to replace the current-stage result before downstream execution;
- a staged execution path in which the intervention has observable operational consequences.

Ownership must not be over-read:

- **the benchmark organization** supplies the decisive current-state support and control rights;
- **the LLM policy** participates in choosing the repair when trusted state is supplied;
- **Claude Sonnet 4.6** does not thereby acquire native autonomous S3 ownership;
- **the Oracle arm** is an experimental ceiling, not an autonomous system claim;
- **failure injection, exact-match grading and the trusted-state feed** are benchmark machinery, not native harness control-plane evidence.

The evidence therefore remains `benchmark-scaffolded-noncanonical`.

## Why this does not reopen the S3 primary

The frozen S3 primary-search closure requires materially matched evidence across two or more canonical systems exercising their own native or adapter-preserved S3 paths, or a new direct benchmark binding comparable immutable results to multiple canonical native S3 implementations.

OrchestrateBench does not satisfy those gates:

- it evaluates one benchmark-defined composed control organization;
- `canonical_harness_id` is null;
- the trusted-state repair path is authored by the benchmark rather than activating a canonical harness's own S3 implementation;
- no second canonical system is evaluated under the same native/adapter-preserved S3 membrane;
- the experiment does not create a matched canonical cross-harness cell.

Therefore:

```text
new direct S3 evidence: yes
new canonical S3 observation: no
matched multi-canonical S3 cell: no
primary baseline: gap
```

The live family is registered only in the Capability-native post-closure extension. The frozen base family map, frozen S3 closure counts, canonical S3 observations, selected baseline state and generated frontier remain unchanged.

## Raw-evidence ownership

The empirical payload remains owned by:

```text
system-observations/orchestratebench.json
  # orchestratebench-policy-conditioned-containment-2026
```

This derived review does not duplicate the raw metrics and does not claim an OpenSiro rerun of the Claude API experiments.

## Resolution of the earlier S3 candidate

The frozen S3 coverage snapshot recorded `orchestrabench-failure-recovery-candidate` as `candidate-direct` because an authoritative public implementation/result source had not been recovered at review time.

The pinned first-party repository now supplies:

- the real-Claude measurement implementation;
- committed measured CSV inputs for the policy-conditioned study and ablation;
- paper-facing aggregate claims tied to those files;
- explicit reproducibility and limitation documentation.

That historical candidate blocker is therefore resolved for the live evidence layer without rewriting the frozen coverage snapshot.

## Non-claims

This review does not claim that:

- Claude Sonnet 4.6 autonomously detects or owns S3 current control;
- supplying trusted upstream ground truth is equivalent to a deployable production control plane;
- an ordinary router, retry loop, manager, orchestrator or supervisor is S3 by name;
- the benchmark result is native capability evidence for AutoGen, LangGraph, CrewAI, Anthropic Agents SDK or any other framework named in the paper;
- the controlled arithmetic-chain probe generalizes quantitatively to arbitrary production organizations;
- OpenSiro independently reproduced the first-party API measurements;
- a matched S3 primary baseline has been found.

## Mutation boundary

This review does not change Profile semantics, Skills methodology, canonical Index ownership, raw evidence, frozen S3 coverage or closure counts, any comparison cell, or the current S3 primary gap.
