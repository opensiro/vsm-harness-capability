# SkillRevise — S4 evidence review

Status: experimental, non-normative.

Tracking issue: #32

Reviewed sources:

```text
opensiro/vsm-harness-profile@88d865f46ac93ec03b8fe0d58ef45054a64cead5
xuansenpa1/skillrevise@fb8042ac2415cb6d7f3a49db0c9a95ecb79edc6d
arXiv:2606.01139
system-observations/skillrevise.json
```

Profile basis:

```text
VSM Harness Profile v0.2.4
S4 = outside-and-then intelligence
```

## Result

```text
function_under_review: S4
fit: unsuitable-for-direct-s4
primary_reopen: no
post_closure_registration: no
```

The currently admitted SkillRevise observation does **not** establish a direct S4 capability family.

The Profile requires S4 to be externally and prospectively oriented: it must distinguish relevant external/future conditions, develop adaptation options, and provide a path by which those options affect present capability. It also explicitly states that generic learning, self-improvement, training, memory consolidation, or reaction to an external event are not S4 by themselves.

The admitted SkillRevise main-result protocol is narrower. For each task it:

1. executes the current task with the current skill;
2. diagnoses verifier-facing failure evidence from that execution;
3. proposes a revised persistent skill artifact;
4. re-executes the candidate on the **same task**;
5. selects the highest-utility observed candidate within the revision budget.

The pinned release is explicit that main-run candidate selection is current-task-only (`--max-heldout 0`) and that cross-task transfer is a separate analysis rather than part of selection. The public overview likewise states that candidate revision is re-executed on the same task.

That is strong evidence for execution-grounded current-task repair of a persistent artifact. It is not, in the admitted result surface, evidence that SkillRevise models a changing external environment or possible future and uses those prospective distinctions to select an adaptation for later operations.

## Why persistence is not enough

The returned skill is persistent and may be reused, but persistence alone does not create S4. The decisive measured selection signal in the admitted observation is success/utility on the task currently being repaired.

Likewise, the reported cross-model transfer result shows that a fixed revised skill can help other executors on the source-task subset. That is useful transfer evidence, but it is evaluated separately after revision; it does not make future/external performance part of the adaptation decision that generated the current admitted artifact.

Therefore the current evidence path is:

```text
current task execution
        ↓
current verifier failure
        ↓
skill revision option
        ↓
re-execution on the same task
        ↓
current-task utility selection
```

not the Profile-required direct-S4 path:

```text
external / future-relevant distinctions
        ↓
prospective adaptation options
        ↓
selection grounded in future/environment relation
        ↓
option returned into later present capability
```

## Separate frozen-bank studies

The release also documents separate calibration-then-freeze Principle Memory studies for ALFWorld and BFCL, followed by evaluation on held-out tasks. Those studies are potentially more relevant to an S4 question because they separate adaptation/calibration experience from later evaluation.

They are **not** part of the neutral observation admitted in Stage 1 of issue #32, whose empirical payload is the main SkillRevise result surface plus a cross-model-transfer summary. This review therefore does not silently import those domain-study result rows or treat documentation of a protocol as an admitted observation.

If a future task admits the frozen-bank calibration→held-out result surface with recoverable public provenance, it should receive a fresh neutral observation and an independent function review. That review must still establish the Profile's external-and-prospective closure rather than infer S4 from the words "learning", "memory", or "held-out" alone.

## Post-closure disposition

Because the admitted SkillRevise observation is not direct S4 evidence:

```text
new direct S4 family: no
post-closure extension entry: no
function-local S4 delta: no
S4 primary reopen: no
S4 primary baseline: unchanged gap
```

The generic Capability-native post-closure contract is intentionally not invoked. `post-closure.json` registers evidence additions; it is not a place to force every reviewed candidate into S4.

## Non-claims

This review does not claim that:

- SkillRevise is ineffective;
- persistent skill revision cannot support adaptation in another declared system boundary;
- the separately documented frozen-bank studies are unsuitable for all S4 interpretations;
- SkillRevise has no VSM-relevant role under any system-in-focus;
- current-task repair is unimportant to harness capability;
- the reported SkillRevise benchmark gains or transfer results are invalid.

It claims only that the **currently admitted public observation** does not satisfy the current Profile's direct S4 boundary.

## Mutation boundary

This review does not change raw evidence, `benchmark-family-map/post-closure.json`, frozen S4 closure counts, `baselines/primary-baselines.json`, the generated frontier, Profile semantics, Skills methodology, or canonical Index state.
