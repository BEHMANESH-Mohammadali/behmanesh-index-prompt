# BSI v3.5 scoring-engine upgrade — implementation notes

Status: **draft on branch `feat/bsi-v3.5-scoring-engine`; not merged**

## Scope of this first implementation slice

Adds `core/bsi_scoring_v35.py` as a deterministic scoring module separate from the legacy v3.4.1 engine. Adds unit tests in `tests/test_bsi_scoring_v35.py`.

The legacy `core/bsi_engine.py` and `core/bsi_pipeline.py` remain intact for traceability, but the `/bsi/score`, `/bsi/analyze`, and `/bsi/compare` routes now use the new explicit-input v3.5 runtime. API scoring requires evidence-backed assessment objects; it no longer silently turns raw text into legacy heuristic scores.

## Preserved semantics

- Single-content D2: evaluate internal coherence only; do not infer longitudinal development or treat absence of longitudinal evidence as a defect. This clarification implements the user's confirmation that the rule was already settled.

- Official BSI dimension weights D1-D7: 0.22, 0.18, 0.18, 0.17, 0.12, 0.08, 0.05.
- Official EIG gap weights: MCG 0.30, CEG 0.35, FCG 0.15, LCG 0.20.
- EIG's Evolution/Rupture/Unknown distinction, including documented LCG adjustments (0.50 / 1.00 / 0.75).
- User's previously recorded EIG penalty decision dated 2026-10-03: `EIG_penalty = EIG_avg / 20`, which caps the penalty at 0.5. The owner confirmed this mapping on 2026-10-31. The canonicalization matrix is updated on this branch to use `/20`; maximum penalty is 0.5.
- Official linear and nonlinear equations.
- Official five-dimension REIG aggregate where all five dimensions are provided.

## Fail-closed behavior

- No keyword-derived D1-D7 score is produced by this new scoring module.
- All seven dimension scores must be supplied. Missing D2 is not imputed, set to zero, or silently renormalized.
- Calculation mode must be explicitly supplied as `linear` or `nonlinear`. The unresolved automatic nonlinear threshold is not invented.
- ECC component gaps can be calculated, but `ECC_Total` is deliberately omitted because ECC v2.0 and the canonicalization matrix are inconsistent about whether aggregation is unresolved.
- Missing/extra EIG or REIG dimensions and out-of-range values raise explicit input errors.

## Known integration work still required

1. The EIG penalty decision is resolved for this upgrade: use `EIG_avg / 20`, confirmed by the owner on 2026-10-31. The older formula reference still needs reconciliation before production integration; the canonicalization matrix records the approved mapping on this branch.
2. Resolve ECC aggregation authority by reviewing the complete SOP and architectural invariants alongside ECC v2.0.
3. Single-content D2 handling is resolved by the owner: assess internal coherence only, do not infer longitudinal trajectory, and do not treat unavailable longitudinal evidence as a defect. The D2 score must still be evidence-backed; no automatic imputation or weight renormalization is performed.
4. Decide an authoritative nonlinear-selection rule or keep mode explicit at the caller.
5. Review the new runtime against the entire canonical output contract and expand integration tests. The API now calls the explicit-input runtime, but a separate evidence-analysis layer that derives defensible D1-D7/EIG/ECC/REIG inputs from source content is not yet implemented; raw-text-only scoring is intentionally rejected.
6. Run CI / unit tests in the repository environment and inspect diff, status, and regression results before proposing a merge.

## Non-goals

This change does not redefine BIO v1.0, CORE_BEHMANESH, D1-D7 constructs, weights, ontology, or output contract. It does not add benchmark/judge behavior and does not modify `main`.
