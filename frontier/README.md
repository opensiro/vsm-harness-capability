# Evidence frontier

Generated current-state view of the experimental general-capability corpus.

The frontier is live and may change as owning baseline selections or function closure records change. It remains distinct from frozen historical synthesis snapshots preserved under `historical/`.

## Source boundary

`EVIDENCE-FRONTIER.md` is derived from:

- `baselines/primary-baselines.json` for current primary state and gap blockers;
- S2–S5 `vsm-projections/<function>/matched-cell/*-primary-search-closure.json` records for reviewed dates, evidence depth, closure claims and reopen rules.

Raw public-evidence admission alone does not automatically change the frontier. A newly admitted neutral observation may remain unprojected and therefore may require no baseline/closure change.

## Generation

Write the derived view:

```bash
python frontier/render_frontier.py
```

Check committed consistency:

```bash
python frontier/render_frontier.py --check
```

Do not hand-edit `EVIDENCE-FRONTIER.md`. Change the owning current-state source artifact and regenerate.
