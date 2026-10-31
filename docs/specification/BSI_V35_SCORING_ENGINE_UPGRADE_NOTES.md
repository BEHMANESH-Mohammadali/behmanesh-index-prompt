# BSI v3.5 scoring-engine upgrade — implementation notes

Status: **draft on branch `feat/bsi-v3.5-scoring-engine`; not merged**

## Scope of this first implementation slice

Adds `core/bsi_scoring_v35.py` as a deterministic scoring module separate from the legacy v3.4.1 engine. Adds unit tests in `tests/test_bsi_scoring_v35.py`.

The existing `core/bsi_engine.py`, pipeline, API wiring, prompt, ontology, and official criteria are not replaced or modified in this slice.

## Preserved semantics

- Single-content D2: evaluate internal coherence only; do not infer longitudinal development or treat absence of longitudinal evidence as a defect. This clarification implements the user's confirmation that the rule was already settled.

- Official BSI dimension weights D1-D7: 0.22, 0.18, 0.18, 0.17, 0.12, 0.08, 0.05.
- Official EIG gap weights: MCG 0.30, CEG 0.35, FCG 0.15, LCG 0.20.
- EIG's Evolution/Rupture/Unknown distinction, including documented LCG adjustments (0.50 / 1.00 / 0.75).
- User's previously recorded EIG penalty decision dated 2026-10-03: `EIG_penalty = EIG_avg / 20`, which caps the penalty at 0.5. This differs from the current canonical matrix's `EIG_avg / 10` and is intentionally made explicit in code rather than silently overwriting either record.
- Official linear and nonlinear equations.
- Official five-dimension REIG aggregate where all five dimensions are provided.

## Fail-closed behavior

- No keyword-derived D1-D7 score is produced by this new scoring module.
- All seven dimension scores must be supplied. Missing D2 is not imputed, set to zero, or silently renormalized.
- Calculation mode must be explicitly supplied as `linear` or `nonlinear`. The unresolved automatic nonlinear threshold is not invented.
- ECC component gaps can be calculated, but `ECC_Total` is deliberately omitted because ECC v2.0 and the canonicalization matrix are inconsistent about whether aggregation is unresolved.
- Missing/extra EIG or REIG dimensions and out-of-range values raise explicit input errors.

## Known integration work still required

1. Resolve the authoritative EIG penalty conflict: the user's 2026-10-03 decision says `/20`, while `docs/specification/CANONICAL_SPECIFICATION_MATRIX_v3.5.md` and `BSI_Calculation_Formula_Hybrid_v3x.md` currently say `/10`. Do not silently choose one for production integration.
2. Resolve ECC aggregation authority by reviewing the complete SOP and architectural invariants alongside ECC v2.0.
3. Single-content D2 handling is now explicit: assess internal coherence only, do not infer longitudinal trajectory, and do not treat unavailable longitudinal evidence as a defect. The D2 score must still be evidence-backed; no automatic imputation or weight renormalization is performed.
4. Decide an authoritative nonlinear-selection rule or keep mode explicit at the caller.
5. Review the new module against the entire canonical output contract, engine/pipeline/API call paths, and existing regression suite before wiring it into production.
6. Run CI / unit tests in the repository environment and inspect diff, status, and regression results before proposing a merge.

## Non-goals

This change does not redefine BIO v1.0, CORE_BEHMANESH, D1-D7 constructs, weights, ontology, or output contract. It does not add benchmark/judge behavior and does not modify `main`.
