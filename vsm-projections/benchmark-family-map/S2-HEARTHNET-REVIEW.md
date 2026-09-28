# HearthNet Scene 2 conflict resolution — S2 evidence review

Status: experimental, non-normative.

Tracking issue: #41

Reviewed sources:

```text
opensiro/vsm-harness-profile@88d865f46ac93ec03b8fe0d58ef45054a64cead5
zhonghaozhan/hearthnet_framework@938fdd813e16c0d356c8e56685a8e1ce311d086a
zhonghaozhan/hearthnet@a0d1bfbad0a6576b32702d012e8e34875067971b
system-observations/hearthnet.json#hearthnet-scene2-conflict-resolution-5run-2026
```

Profile basis:

```text
VSM Harness Profile v0.2.4
S2 = coordination / attenuation of inter-S1 interference, conflict or oscillation
```

## Result

```text
function: S2
fit: direct
system_linkage: benchmark-scaffolded-noncanonical
primary_reopen: no
```

The reviewed HearthNet Scene 2 organization directly exercises an S2 disturbance-to-attenuation loop at the **benchmark/demo composed organization boundary**. This conclusion does not elevate the published Scene 2 result to native-system evidence: the experiment supplies the conflict stimulus and scripts the Dewey conflict alert and timeline response around real framework arbitration, lease, messaging and acknowledgement paths.

## Direct-S2 closure

The Profile requires four elements for a positive S2 mapping: distinct operational units, a concrete interaction disturbance, a coordination relation capable of attenuating it, and feedback that changes subsequent operational behaviour. The published HearthNet organization supplies those elements at the benchmark-scaffolded boundary.

1. **Distinct operational units.** Jeeves and Darcy are distinct device-manager operational units in the shared smart-home environment. Scene 1 establishes a common work-from-home operating mode across manager-controlled devices before Scene 2 introduces the scheduled wind-down requests.
2. **Concrete disturbance.** Scene 2 supplies incompatible scheduled changes while the cross-device WFH commitments remain active. The framework itself also contains a generic cross-sender conflict detector: Dewey compares incompatible desired-state values on the same target within a conflict window and ignores same-sender comparisons. The measured Scene 2 result must nevertheless be read more narrowly because its conflict alert and timeline evidence are benchmark-authored by the scene script.
3. **Attenuation relation.** Rupert receives the conflict context, applies the framework's `arbitrateConflict(...)` / `evaluateLeaseRequest(...)` paths under the active mode and policy, and issues lease denials that preserve the current shared operating commitment instead of allowing the scheduled requests to overwrite it.
4. **Closure into subsequent operation.** The denials return to Jeeves and Darcy; both acknowledge and defer the wind-down actions; the resolution broadcast records that the WFH mode and device commitments remain in force. The coordination result therefore changes subsequent operational behaviour: the proposed actuations are not performed.

```text
shared WFH operating commitments
        ↑                    ↑
     Jeeves                Darcy
        \                    /
         \ scheduled wind-down /
          \      requests     /
           ↓                 ↓
      benchmark-supplied conflict context
                    ↓
      Rupert arbitration / lease evaluation
                    ↓
              lease denials
                ↙       ↘
       Jeeves defers   Darcy defers
                \       /
             WFH state retained
```

This is direct S2 evidence because the reviewed outcome is explicitly about a concrete coordination disturbance and its attenuation, not a broad collaboration score or communication-efficiency proxy.

## Detection and ownership boundary

The published metric must not be over-read as autonomous native conflict-detection performance.

The framework implementation contains a real Dewey conflict detector and `sendConflictAlert(...)` path, but the released Scene 2 script itself constructs the conflict alert and the timeline response before calling the real arbitration and lease-evaluation functions. `run-metrics.js` then summarizes the repeated scene outcome from observed completion/denial behaviour. Therefore:

- **Rupert** owns the arbitration choice within the reviewed benchmark organization;
- **Jeeves and Darcy** are the operational units whose scheduled requests are regulated;
- **Dewey/framework conflict logic** provides relevant structural support for the broader implementation, but the five-run published result does not independently demonstrate that autonomous detector firing;
- **MQTT, Git persistence and lease machinery** transport, preserve or enforce the coordination result rather than owning the organizational choice;
- **the Scene 2 script** supplies material experimental stimulus and evidence context, which is why compatibility remains `benchmark-scaffolded` rather than `native-system`.

The direct classification belongs to this composed benchmark/demo boundary, not to any one model or component by name.

## Why this does not reopen the S2 primary

The frozen S2 primary-search closure explicitly says not to reopen for another benchmark-scaffolded direct S2 observation without canonical native or adapter-preserved linkage, and separately rejects another framework benchmark whose coordination organization is benchmark-authored.

HearthNet adds another explicit disturbance-to-attenuation family, but it remains:

- benchmark-scaffolded;
- non-canonical;
- not a materially matched comparison with the existing canonical direct S2 observations;
- not evidence that two or more canonical systems exercised their own native or adapter-preserved S2 paths under one common disturbance definition.

Therefore:

```text
new direct S2 evidence: yes
new canonical S2 observation: no
matched multi-canonical S2 cell: no
primary baseline: gap
```

The live family is registered only in the Capability-native post-closure extension. The frozen base family map, frozen S2 closure counts, selected baseline state and generated frontier remain unchanged.

## Raw-evidence ownership

The empirical repeated-run payload remains owned by:

```text
system-observations/hearthnet.json
  # hearthnet-scene2-conflict-resolution-5run-2026
```

This derived review does not duplicate those metrics and does not claim an OpenSiro reproduction of the published experiment.

## Non-claims

This review does not claim that:

- the five-run Scene 2 result measures native autonomous Dewey conflict detection;
- HearthNet is currently a canonical VSM Harness Index system;
- Rupert, Dewey, Jeeves or Darcy individually constitute a complete viable system;
- any central arbitration step is automatically S2;
- every lease denial is coordination evidence;
- the result generalizes to all conflicts, policies, devices or model configurations;
- the first-party aggregate was independently reproduced by OpenSiro;
- a matched S2 primary baseline has been found.

## Mutation boundary

This review does not change Profile semantics, Skills methodology, canonical Index ownership, raw evidence, frozen S2 closure counts, any comparison cell, or the current S2 primary gap.
