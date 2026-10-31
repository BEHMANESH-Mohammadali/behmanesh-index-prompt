"""Validated BSI v3.5 scoring runtime.

This runtime connects the scoring primitives to an executable, explicit-input
contract. It deliberately does not infer D1-D7 or EIG values from raw text.
Those assessments must be produced by the analysis layer with traceable evidence.
"""
from __future__ import annotations

from typing import Mapping, Any

from core.bsi_scoring_v35 import (
    BSI_WEIGHTS,
    EIG_WEIGHTS,
    ScoringInputError,
    calculate_bsi,
    calculate_ecc_gaps,
    calculate_eig,
    calculate_reig,
)


def run_v35_scoring(assessment: Mapping[str, Any]) -> dict:
    """Run the v3.5 numerical scoring stage from evidence-backed assessments.

    Required assessment keys:
      dimension_scores: D1..D7 numeric scores on 0..100
      eig_gaps: MCG/CEG/FCG/LCG numeric gaps on 0..10
      lcg_interpretation: Evolution/Rupture/Unknown
      calculation_mode: explicitly linear or nonlinear
      ecc: claimed_confidence, supported_evidence, supported_method,
           supported_conclusion (each 0..100)
      reig: ERG/MRG/CRG/ARG/FRG integer scores (each 0..4)

    ECC aggregate and the automatic nonlinear threshold remain unresolved.
    REIG values must represent an audit of Draft Analysis, not the target text.
    """
    required = {
        "dimension_scores", "eig_gaps", "lcg_interpretation",
        "calculation_mode", "ecc", "reig",
    }
    missing = required - set(assessment)
    if missing:
        raise ScoringInputError(f"Missing assessment fields: {sorted(missing)}")

    eig = calculate_eig(
        assessment["eig_gaps"],
        lcg_interpretation=assessment["lcg_interpretation"],
    )
    bsi = calculate_bsi(
        assessment["dimension_scores"],
        eig["EIG_penalty"],
        calculation_mode=assessment["calculation_mode"],
    )

    ecc_input = assessment["ecc"]
    ecc_required = {
        "claimed_confidence", "supported_evidence",
        "supported_method", "supported_conclusion",
    }
    if not isinstance(ecc_input, Mapping):
        raise ScoringInputError("ecc must be an object containing four confidence values.")
    ecc_missing = ecc_required - set(ecc_input)
    if ecc_missing:
        raise ScoringInputError(f"Missing ECC fields: {sorted(ecc_missing)}")
    ecc = calculate_ecc_gaps(
        ecc_input["claimed_confidence"],
        ecc_input["supported_evidence"],
        ecc_input["supported_method"],
        ecc_input["supported_conclusion"],
    )

    reig_input = assessment["reig"]
    if not isinstance(reig_input, Mapping):
        raise ScoringInputError("reig must be an object with five Draft Analysis audit dimensions.")
    reig = calculate_reig(reig_input)

    return {
        "framework_version": "3.5",
        "engine_version": "3.5.0-explicit-input",
        "engine_status": "V3_5_SCORING_CONNECTED",
        "assessment_mode": "EXPLICIT_EVIDENCE_BACKED_INPUTS",
        "BSI": bsi,
        "EIG": eig,
        "ECC": ecc,
        "REIG": reig,
        "limitations": [
            "D1-D7 and EIG assessments are inputs; this endpoint does not infer them from raw text.",
            "Nonlinear activation threshold remains unresolved; calculation mode was explicitly supplied.",
            "ECC aggregate is omitted pending authoritative specification reconciliation.",
            "REIG scores must audit Draft Analysis, not the target text.",
        ],
    }
