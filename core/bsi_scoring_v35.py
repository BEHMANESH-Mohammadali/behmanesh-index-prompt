"""BSI v3.5 deterministic scoring primitives.

This module calculates scores only from explicitly supplied, evidence-backed
inputs. It does not infer D1-D7 scores from keywords or fabricate longitudinal
evidence. See the canonical specification and implementation notes.
"""
from __future__ import annotations

from math import prod
from typing import Mapping, Sequence


BSI_WEIGHTS = {
    "D1": 0.22,  # ConditionalDepth
    "D2": 0.18,  # LongitudinalCoherence
    "D3": 0.18,  # AuthenticEthicalLayer
    "D4": 0.17,  # CreativeValueAdd
    "D5": 0.12,  # StrategicDepth
    "D6": 0.08,  # InterdisciplinaryBreadth
    "D7": 0.05,  # AntiPerformativeDrift
}

EIG_WEIGHTS = {
    "MCG": 0.30,
    "CEG": 0.35,
    "FCG": 0.15,
    "LCG": 0.20,
}

REIG_DIMENSIONS = ("ERG", "MRG", "CRG", "ARG", "FRG")


class ScoringInputError(ValueError):
    """Raised when a score cannot be calculated without inventing an input."""


def _bounded_number(value: object, name: str, low: float, high: float) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ScoringInputError(f"{name} must be a numeric value.")
    number = float(value)
    if not low <= number <= high:
        raise ScoringInputError(f"{name} must be within [{low}, {high}].")
    return number


def calculate_eig(
    gaps: Mapping[str, float],
    *,
    lcg_interpretation: str,
) -> dict:
    """Calculate EIG using official gap weights and Evolution/Rupture handling.

    lcg_interpretation is one of Evolution, Rupture, or Unknown.
    Unknown applies the documented 25% adjustment to the raw LCG value.
    """
    missing = set(EIG_WEIGHTS) - set(gaps)
    extra = set(gaps) - set(EIG_WEIGHTS)
    if missing or extra:
        raise ScoringInputError(
            f"EIG gaps must contain exactly {tuple(EIG_WEIGHTS)}; "
            f"missing={sorted(missing)}, extra={sorted(extra)}"
        )

    interpretation = lcg_interpretation.strip().lower()
    if interpretation not in {"evolution", "rupture", "unknown"}:
        raise ScoringInputError(
            "lcg_interpretation must be Evolution, Rupture, or Unknown."
        )

    raw = {key: _bounded_number(gaps[key], key, 0, 10) for key in EIG_WEIGHTS}
    lcg_factor = {"evolution": 0.50, "rupture": 1.0, "unknown": 0.75}[interpretation]
    adjusted = dict(raw)
    adjusted["LCG"] = raw["LCG"] * lcg_factor

    eig_avg = sum(EIG_WEIGHTS[k] * adjusted[k] for k in EIG_WEIGHTS)
    eig_score = 100.0 - (eig_avg * 10.0)

    # User-approved calibration decision (2026-10-03): EIG_avg / 20.
    penalty = eig_avg / 20.0
    return {
        "raw_gaps": raw,
        "adjusted_gaps": adjusted,
        "lcg_interpretation": interpretation.upper(),
        "lcg_adjustment_factor": lcg_factor,
        "EIG_avg": round(eig_avg, 6),
        "EIG_score": round(eig_score, 4),
        "EIG_penalty": round(penalty, 6),
        "penalty_formula": "EIG_avg / 20",
        "maximum_penalty": 0.5,
    }


def calculate_bsi(
    dimension_scores: Mapping[str, float],
    eig_penalty: float,
    *,
    calculation_mode: str,
) -> dict:
    """Calculate BSI from explicitly supplied, evidence-backed scores.

    For a single-content analysis, D2 is assessed only for internal coherence;
    no longitudinal trajectory is inferred. The caller must supply the D2
    assessment under that rule. Missing D2 is not imputed or renormalized.

    The automatic nonlinear activation threshold remains intentionally
    unresolved. The caller must explicitly select linear or nonlinear mode.
    """
    missing = set(BSI_WEIGHTS) - set(dimension_scores)
    extra = set(dimension_scores) - set(BSI_WEIGHTS)
    if missing or extra:
        raise ScoringInputError(
            f"Dimension scores must contain exactly {tuple(BSI_WEIGHTS)}; "
            f"missing={sorted(missing)}, extra={sorted(extra)}. "
            "No missing dimension is imputed or renormalized."
        )

    scores = {
        key: _bounded_number(dimension_scores[key], key, 0, 100)
        for key in BSI_WEIGHTS
    }
    penalty = _bounded_number(eig_penalty, "EIG_penalty", 0, 0.5)
    mode = calculation_mode.strip().lower()
    if mode not in {"linear", "nonlinear"}:
        raise ScoringInputError(
            "calculation_mode must be explicitly 'linear' or 'nonlinear'; "
            "no automatic nonlinear threshold is specified."
        )

    if mode == "linear":
        raw_score = sum(BSI_WEIGHTS[k] * scores[k] for k in BSI_WEIGHTS)
    else:
        if any(scores[k] == 0 and BSI_WEIGHTS[k] > 0 for k in BSI_WEIGHTS):
            raw_score = 0.0
        else:
            raw_score = 100.0 * prod(
                (scores[k] / 100.0) ** BSI_WEIGHTS[k] for k in BSI_WEIGHTS
            )

    final_score = raw_score * (1.0 - penalty)
    return {
        "calculation_mode": mode.upper(),
        "dimension_scores": scores,
        "dimension_weights": dict(BSI_WEIGHTS),
        "weighted_base_score": round(raw_score, 4),
        "EIG_penalty": round(penalty, 6),
        "BSI_score": round(final_score, 4),
        "status": "CALCULATED",
    }


def calculate_ecc_gaps(
    claimed_confidence: float,
    supported_evidence: float,
    supported_method: float,
    supported_conclusion: float,
) -> dict:
    """Calculate ECC v2.0 signed component gaps and absolute-gap aggregate.

    Signed gaps preserve direction (overclaim vs. underclaim); ECC_Total
    follows the authoritative v2.0 arithmetic mean of their absolute values.
    """
    cc = _bounded_number(claimed_confidence, "CC-C", 0, 100)
    se = _bounded_number(supported_evidence, "SC-E", 0, 100)
    sm = _bounded_number(supported_method, "SC-M", 0, 100)
    sl = _bounded_number(supported_conclusion, "SC-L", 0, 100)
    gaps = {
        "EG": round(cc - se, 4),
        "MG": round(cc - sm, 4),
        "LG": round(cc - sl, 4),
    }
    directions = {
        key: (
            "OVERCLAIM" if value > 0
            else "UNDERCLAIM" if value < 0
            else "ALIGNED"
        )
        for key, value in gaps.items()
    }
    total = sum(abs(value) for value in gaps.values()) / 3.0
    return {
        "CC-C": cc,
        "SC-E": se,
        "SC-M": sm,
        "SC-L": sl,
        **gaps,
        "gap_directions": directions,
        "ECC_Total": round(total, 4),
        "aggregate_formula": "mean(abs(EG), abs(MG), abs(LG))",
        "aggregate_scale": "0-100",
        "aggregate_status": "CALCULATED_PER_ECC_V2.0",
    }


def calculate_reig(scores: Mapping[str, int]) -> dict:
    """Calculate REIG_Total from the five official 0-4 dimensions."""
    missing = set(REIG_DIMENSIONS) - set(scores)
    extra = set(scores) - set(REIG_DIMENSIONS)
    if missing or extra:
        raise ScoringInputError(
            f"REIG scores must contain exactly {REIG_DIMENSIONS}; "
            f"missing={sorted(missing)}, extra={sorted(extra)}"
        )
    checked = {}
    for key in REIG_DIMENSIONS:
        value = scores[key]
        if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value <= 4:
            raise ScoringInputError(f"{key} must be an integer from 0 to 4.")
        checked[key] = value
    total = sum(checked.values()) / len(REIG_DIMENSIONS)
    return {
        "dimensions": checked,
        "REIG_Total": round(total, 4),
        "scale": "0-4",
    }


D2_SI_WEIGHTS = {"I": 0.40, "D": 0.30, "C": 0.20, "R": 0.10}
D2_SI_NON_SCORE_STATES = {"N/A", "INSUFFICIENT_EVIDENCE", "NOT_ASSESSED"}


def calculate_d2_si(scores: Mapping[str, object]) -> dict:
    """Calculate the proposed, non-canonical single-input D2-SI research metric.

    This helper is not used by the canonical scoring runtime and its result
    must not be submitted as the official D2 input.

    Values for I/D/C/R must be numeric 0..4 or one of the explicit states
    N/A, INSUFFICIENT_EVIDENCE, NOT_ASSESSED. This arithmetic helper cannot
    validate the quality of textual evidence; evidence binding remains the
    responsibility of the assessment layer. Canonical longitudinal D2 is
    not calculated or replaced here.
    """
    missing = set(D2_SI_WEIGHTS) - set(scores)
    extra = set(scores) - set(D2_SI_WEIGHTS)
    if missing or extra:
        raise ScoringInputError(
            f"D2-SI scores must contain exactly {tuple(D2_SI_WEIGHTS)}; "
            f"missing={sorted(missing)}, extra={sorted(extra)}"
        )

    checked = {}
    applicable = {}
    for key, weight in D2_SI_WEIGHTS.items():
        value = scores[key]
        if isinstance(value, str):
            state = value.strip().upper()
            if state not in D2_SI_NON_SCORE_STATES:
                raise ScoringInputError(f"Invalid D2-SI state for {key}: {value!r}.")
            checked[key] = state
            applicable[key] = state != "N/A"
        else:
            checked[key] = _bounded_number(value, f"D2-SI {key}", 0, 4)
            applicable[key] = True

    if not any(applicable.values()):
        return {
            "status": "NOT_SCORABLE",
            "D2-SI": None,
            "dimension_scores": checked,
            "applicable_weights": {},
            "renormalized": False,
        }

    unresolved = [
        key for key, value in checked.items()
        if value in {"INSUFFICIENT_EVIDENCE", "NOT_ASSESSED"}
    ]
    if unresolved:
        state = "INSUFFICIENT_EVIDENCE" if "INSUFFICIENT_EVIDENCE" in [checked[k] for k in unresolved] else "NOT_ASSESSED"
        return {
            "status": state,
            "D2-SI": None,
            "dimension_scores": checked,
            "applicable_weights": {k: w for k, w in D2_SI_WEIGHTS.items() if applicable[k]},
            "renormalized": any(not applicable[k] for k in D2_SI_WEIGHTS),
            "unresolved_dimensions": unresolved,
        }

    active_weights = {k: w for k, w in D2_SI_WEIGHTS.items() if applicable[k]}
    denominator = sum(active_weights.values())
    score = sum(active_weights[k] * float(checked[k]) for k in active_weights) / denominator
    return {
        "status": "CALCULATED",
        "D2-SI": round(score, 6),
        "dimension_scores": checked,
        "applicable_weights": active_weights,
        "renormalized": len(active_weights) != len(D2_SI_WEIGHTS),
        "weight_denominator": round(denominator, 6),
        "scale": "0-4",
        "canonical_D2_modified": False,
    }



def d2_si_to_normalized_score(d2_si_result: Mapping[str, object]) -> float:
    """Research-only scale conversion; not authorized for canonical D2 scoring.

    The canonical runtime rejects D2-SI and does not accept this conversion as
    an official D2 input.

    This is a scale conversion only. It does not assert that D2-SI is the
    canonical longitudinal D2 formula. The BSI engine then applies the
    unchanged official D2 weight (0.18) as part of its normal aggregation.
    """
    if d2_si_result.get("status") != "CALCULATED":
        raise ScoringInputError("D2-SI must have CALCULATED status before normalization.")
    value = _bounded_number(d2_si_result.get("D2-SI"), "D2-SI", 0, 4)
    return round((value / 4.0) * 100.0, 6)



def validate_d2_si_penalty_attribution(records: Sequence[Mapping[str, str]]) -> dict:
    """Audit whether a single identified defect is penalized across dimensions.

    Reuse of one defect_id across multiple D2-SI dimensions is accepted only
    when each dimension entry cites a distinct evidence_id and supplies its
    own non-empty rationale. This is a traceability guard, not a semantic
    judgment that the cited evidence truly establishes distinct failures.
    """
    allowed = set(D2_SI_WEIGHTS)
    normalized = []
    for index, record in enumerate(records):
        if not isinstance(record, Mapping):
            raise ScoringInputError(f"Penalty record {index} must be a mapping.")
        required = {"defect_id", "dimension", "evidence_id", "rationale"}
        if required - set(record):
            raise ScoringInputError(f"Penalty record {index} is missing required fields.")
        item = {key: str(record[key]).strip() for key in required}
        if not all(item.values()):
            raise ScoringInputError(f"Penalty record {index} contains an empty required field.")
        if item["dimension"] not in allowed:
            raise ScoringInputError(f"Invalid D2-SI dimension in penalty record {index}.")
        normalized.append(item)

    by_defect = {}
    for item in normalized:
        by_defect.setdefault(item["defect_id"], []).append(item)
    for defect_id, items in by_defect.items():
        dimensions = {item["dimension"] for item in items}
        if len(dimensions) > 1:
            evidence_ids = [item["evidence_id"] for item in items]
            if len(set(evidence_ids)) != len(evidence_ids):
                raise ScoringInputError(
                    f"Potential double penalty for {defect_id}: cross-dimension entries require distinct evidence_id values."
                )
    return {"status": "TRACEABILITY_CHECK_PASSED", "records_checked": len(normalized)}
