# Airbnb Agent Harness Optimizer — S4 evidence review

Status: experimental, non-normative.

Tracking issue: #26

Reviewed sources:

```text
airbnb/agent-harness-optimizer@0d7652b42296c8df07532fa3787fc956250741e7
arXiv:2609.05736
```

Profile basis:

```text
opensiro/vsm-harness-profile v0.2.4
```

## Result

```text
function: S4
fit: direct
system_linkage: external-native-noncanonical
primary_reopen: no
```

The reviewed Agent Harness Optimizer (AHO) boundary directly exercises a prospective adaptation loop rather than only retrying the current task. A fixed task-solving model is run on benchmark cases; execution failures are analyzed by the optimizer; persistent edits are proposed to the system prompt and tool-boundary middleware; candidate harness states are evaluated on separate repair/holdout surfaces; and the selected changed harness is then scored on later held-out cases.

That sequence closes the evidence → adaptation option → persistent capability change → later operation path. The direct classification belongs to the public AHO optimizer plus its evolving harness state. It does **not** belong to the fixed inner model, BFCL, τ²-bench, or the outer proposer model by association.

## Ordinary-S4 boundary

The experiment freezes the adaptation regulator sufficiently for an ordinary S4 reading:

- optimizer algorithm/configuration and benchmark protocol are fixed for a run;
- the task-solving inner model is fixed;
- train/holdout resource budgets and split rules are fixed by the published protocol;
- the declared adaptation target is the surrounding harness: system prompt and guarded tool-boundary middleware;
- persistent candidate harness state changes across generations/iterations and is later re-evaluated.

The evidence therefore concerns adaptation of an operational harness under a fixed optimizer/evaluation regulator. It is not evidence for recursive improvement of the optimizer itself or for the separate self-organizing-S evidence class.

## Published result surface

The first-party paper reports PRISM mean held-out lift under fixed-model harness optimization of:

- `+14.2` percentage points on BFCL multi-round;
- `+14.9` percentage points on τ²-Retail;
- `+10.1` percentage points on τ²-Telecom.

The public code release pins the paper experiment models, split sizes, resource budgets, optimizer flags and reproduction commands. It intentionally gitignores local `runs/`, `experiment_runs/` and related run-output directories, so these values remain **first-party published results**, not an independently reproduced raw-run ledger in this repository.

Numeric payload remains owned by `system-observations/airbnb-agent-harness-optimizer.json`; this derived review does not duplicate it into a second result database.

## Why this does not reopen the S4 primary

The frozen S4 primary-search closure explicitly says not to reopen for another heterogeneous single-system S4 result or another non-canonical evolving-system study without matched canonical-native linkage.

AHO materially strengthens the public direct-S4 evidence set, but it still evaluates one optimizer/evolving-harness organization rather than two or more independently canonical-linkable S4 systems in one materially matched comparison cell.

Therefore:

```text
new direct S4 evidence: yes
new canonical S4 observation: no
matched multi-canonical S4 cell: no
primary baseline: gap
```

## Non-claims

This review does not claim that:

- AHO is currently a canonical VSM Harness Index system;
- the fixed inner model owns the adaptation loop;
- positive aggregate lift transfers to every task domain or model;
- prompt/middleware optimization establishes any other VSM function by terminology alone;
- the first-party paper results were independently reproduced by OpenSiro;
- this evidence creates a global harness score or ranking.

## Mutation boundary

This review does not change Profile semantics, canonical Index ownership, the selected S1 primary, any domain-specific grade, or the frozen S4 primary closure disposition.
