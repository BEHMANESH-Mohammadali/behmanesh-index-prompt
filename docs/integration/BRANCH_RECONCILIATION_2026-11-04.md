# BSI v3.5 Branch Reconciliation — 2026-11-04

**Target integration branch:** `integration/bsi-v3.5-reconciled`
**Integration baseline:** `feat/d2-single-input-scoring`
**Status:** staged; not merged to `main` or `develop/v3.5`.

## Branch topology and disposition

- `feat/bsi-v3.5-scoring-engine` → `feat/model-agnostic-execution-adapters` → `feat/d2-single-input-scoring` is a cumulative technical lineage (41 commits, then 32 commits, each fast-forward relative to its predecessor). Use the D2 branch as the integrated technical baseline; do not merge these three branches independently.
- `migration/bsi-v3.5-canonical` is a divergent prompt-packaging/canonicalization line. Its PR #5 targets this integration branch as a draft staging PR. GitHub currently reports it non-mergeable; do not force-merge. Reconcile file-level conflicts and rerun CI before merging.
- `conceptual-refactor-volume1` is a separate research/publication stream. Preserve it as a distinct branch and retain its monograph under the research/documentation boundary. Do not fold it into runtime or the Master Prompt as if its future-work claims were implemented or empirically validated.
- `feature/core-behmanesh-v1` is historical/lineage material, not a current implementation stream.
- `main` is an older baseline and should not be used as the integration base for v3.5.

## Canonical conflict decisions

### EIG penalty denominator

**Resolved:** `EIG_penalty = EIG_avg / 20`, with `EIG_avg` on the 0–10 weighted-gap scale and maximum penalty 0.5. This is supported by the owner-confirmed decision recorded in the D2 branch's canonical specification matrix and scoring-engine upgrade notes (2026-10-31; notes also record an earlier owner decision dated 2026-10-03). The older `/10` mapping in `develop/v3.5` and the legacy calculation-formula document is superseded for the v3.5 implementation. Preserve the older rule in history; do not erase its provenance.

### ECC v2.0 aggregation

**Resolved:** `ECC_Total = mean(|EG|, |MG|, |LG|)`. Preserve signed component gaps and their OVERCLAIM / UNDERCLAIM / ALIGNED direction in the report. The aggregate magnitude must not erase direction. Authority: ECC v2.0 source document; canonicalization matrix records the source-based resolution.

### D2 with one content item

**Resolved:** assess internal coherence only; do not infer longitudinal trajectory, historical development, persistence, or continuity from one item. Absence of longitudinal evidence is not itself a defect. The D2-SI 0.40/0.30/0.20/0.10 operationalization remains a proposed constrained single-input aid and must not be presented as the canonical longitudinal D2 definition or as empirically calibrated. Preserve D2 official weight 0.18.

### ECC / REIG boundaries

- ECC is calibration, not truth adjudication; report absolute aggregate and signed component directions.
- REIG audits Draft Analysis and retains all five official dimensions; it is not an independent external validation.
- Model-generated analysis, self-audit, and RAG leads are not source evidence or independent validation.

### Nonlinear activation

**Unresolved by design:** no automatic threshold for switching to nonlinear scoring. Require explicit calculation-mode selection; do not invent a threshold.

## Integration boundaries

- Prompt-First standalone execution is a supported path; API/runtime/provider adapters are optional automation, not prerequisites.
- Keep prompt-only external-verification limits explicit.
- Keep explicit-input scoring separate from autonomous evidence analysis. Do not claim the runtime derives defensible D1–D7/EIG/ECC/REIG scores from raw text unless that layer is implemented and validated.
- Do not claim durable execution-trace persistence, independent human/third-party validation, or independent-interface portability testing without evidence.
- No new BSI criteria, weights, ontology, or scoring dimensions are introduced by this reconciliation.

## Validation gates before promotion

1. Resolve PR #5's file-level merge conflicts without overwriting the newer D2 branch Master Prompt or scoring/runtime work.
2. Reconcile the standalone Master Prompt and calculation formula to the decisions above.
3. Run full repository CI and prompt-package tests on the integration head.
4. Perform and record the independent-interface Prompt-Only portability test.
5. Review the final diff and confirm no unintended changes to BIO v1.0, CORE_BEHMANESH, official weights, or protected rubrics.

## Audit note

This document records the current branch-level decisions and known limits. It does not claim that all files in every branch have been reviewed line by line, that PR #5 has been merged, or that the integration branch is production-ready.
