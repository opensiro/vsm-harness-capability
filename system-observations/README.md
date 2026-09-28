# System observations

Neutral public empirical evidence layer.

This directory owns system/result/provenance/configuration identity, not VSM-function semantics.

Each active raw observation is stored once and referenced by derived projections and comparison cells.

The predecessor corpus was migrated losslessly from `opensiro/vsm-harness-index/experiments/functional-capability-depth/system-observations/`; see [`../MIGRATION.md`](../MIGRATION.md). New active public observations are admitted here under [`../ADMISSION.md`](../ADMISSION.md).

After changing a raw record, regenerate the neutral registry:

```bash
python system-observations/render_registry.py
```

Then check the changed record:

```bash
python scripts/admission_check.py system-observations/<record>.json
```

Raw admission remains VSM-neutral. A VSM-function projection is optional downstream interpretation, not a prerequisite for storing valid public evidence.
