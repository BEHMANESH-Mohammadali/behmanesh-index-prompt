import pytest

from core.bsi_scoring_v35 import (
    BSI_WEIGHTS,
    EIG_WEIGHTS,
    ScoringInputError,
    calculate_bsi,
    calculate_ecc_gaps,
    calculate_eig,
    calculate_reig,
)
from core.bsi_v35_runtime import run_v35_scoring


def test_official_weights_sum_to_one():
    assert sum(BSI_WEIGHTS.values()) == pytest.approx(1.0)
    assert sum(EIG_WEIGHTS.values()) == pytest.approx(1.0)


def test_eig_uses_user_approved_divide_by_twenty_penalty():
    result = calculate_eig(
        {"MCG": 2, "CEG": 4, "FCG": 2, "LCG": 6},
        lcg_interpretation="Rupture",
    )
    expected = 2 * .30 + 4 * .35 + 2 * .15 + 6 * .20
    assert result["EIG_avg"] == pytest.approx(expected)
    assert result["EIG_penalty"] == pytest.approx(expected / 20)
    assert result["maximum_penalty"] == .5


@pytest.mark.parametrize(
    ("interpretation", "factor"),
    [("Evolution", .5), ("Rupture", 1.0), ("Unknown", .75)],
)
def test_lcg_interpretation_adjustment_is_explicit(interpretation, factor):
    result = calculate_eig(
        {"MCG": 1, "CEG": 1, "FCG": 1, "LCG": 8},
        lcg_interpretation=interpretation,
    )
    assert result["lcg_adjustment_factor"] == factor
    assert result["adjusted_gaps"]["LCG"] == pytest.approx(8 * factor)


def test_eig_rejects_missing_or_extra_gap():
    with pytest.raises(ScoringInputError):
        calculate_eig({"MCG": 1, "CEG": 2, "FCG": 3}, lcg_interpretation="Unknown")


def test_bsi_linear_formula_and_penalty():
    scores = {key: 80 for key in BSI_WEIGHTS}
    result = calculate_bsi(scores, .25, calculation_mode="linear")
    assert result["weighted_base_score"] == pytest.approx(80)
    assert result["BSI_score"] == pytest.approx(60)


def test_bsi_nonlinear_formula_with_equal_scores():
    scores = {key: 64 for key in BSI_WEIGHTS}
    result = calculate_bsi(scores, .125, calculation_mode="nonlinear")
    assert result["weighted_base_score"] == pytest.approx(64)
    assert result["BSI_score"] == pytest.approx(56)


def test_missing_d2_is_not_imputed_or_renormalized():
    scores = {key: 80 for key in BSI_WEIGHTS if key != "D2"}
    with pytest.raises(ScoringInputError, match="No missing dimension is imputed"):
        calculate_bsi(scores, .1, calculation_mode="linear")


def test_mode_must_be_explicit():
    with pytest.raises(ScoringInputError, match="explicitly"):
        calculate_bsi({key: 80 for key in BSI_WEIGHTS}, .1, calculation_mode="auto")


def test_eig_penalty_is_bounded():
    with pytest.raises(ScoringInputError):
        calculate_bsi({key: 80 for key in BSI_WEIGHTS}, .51, calculation_mode="linear")


def test_ecc_calculates_v2_absolute_gap_aggregate_and_preserves_direction():
    result = calculate_ecc_gaps(80, 60, 70, 50)
    assert result["EG"] == 20
    assert result["MG"] == 10
    assert result["LG"] == 30
    assert result["gap_directions"] == {
        "EG": "OVERCLAIM", "MG": "OVERCLAIM", "LG": "OVERCLAIM"
    }
    assert result["ECC_Total"] == pytest.approx(20)
    assert result["aggregate_formula"] == "mean(abs(EG), abs(MG), abs(LG))"
    assert result["aggregate_status"] == "CALCULATED_PER_ECC_V2.0"


def test_ecc_negative_gaps_are_preserved_as_underclaim():
    result = calculate_ecc_gaps(50, 70, 60, 80)
    assert result["EG"] == -20
    assert result["MG"] == -10
    assert result["LG"] == -30
    assert set(result["gap_directions"].values()) == {"UNDERCLAIM"}
    assert result["ECC_Total"] == pytest.approx(20)


def test_ecc_mixed_gap_directions_and_zero_alignment():
    result = calculate_ecc_gaps(60, 50, 60, 70)
    assert result["EG"] == 10
    assert result["MG"] == 0
    assert result["LG"] == -10
    assert result["gap_directions"] == {
        "EG": "OVERCLAIM", "MG": "ALIGNED", "LG": "UNDERCLAIM"
    }
    assert result["ECC_Total"] == pytest.approx(20 / 3)


def test_reig_uses_five_official_dimensions():
    result = calculate_reig({"ERG": 0, "MRG": 1, "CRG": 2, "ARG": 3, "FRG": 4})
    assert result["REIG_Total"] == 2


def test_reig_rejects_missing_dimension():
    with pytest.raises(ScoringInputError):
        calculate_reig({"ERG": 0, "MRG": 1, "CRG": 2, "ARG": 3})


def test_reig_rejects_out_of_range_values():
    with pytest.raises(ScoringInputError):
        calculate_reig({"ERG": 0, "MRG": 1, "CRG": 2, "ARG": 3, "FRG": 5})



def test_runtime_integrates_all_scoring_stages():
    result = run_v35_scoring({
        "dimension_scores": {f"D{i}": 80 for i in range(1, 8)},
        "eig_gaps": {"MCG": 2, "CEG": 4, "FCG": 2, "LCG": 6},
        "lcg_interpretation": "Rupture",
        "calculation_mode": "linear",
        "content_scope": "single_content",
        "d2_assessment_basis": "internal_coherence_only",
        "ecc": {
            "claimed_confidence": 80,
            "supported_evidence": 60,
            "supported_method": 70,
            "supported_conclusion": 50,
        },
        "reig": {"ERG": 0, "MRG": 1, "CRG": 2, "ARG": 3, "FRG": 4},
    })
    assert result["engine_status"] == "V3_5_SCORING_CONNECTED"
    assert result["EIG"]["penalty_formula"] == "EIG_avg / 20"
    assert result["REIG"]["REIG_Total"] == 2
    assert result["ECC"]["ECC_Total"] == pytest.approx(20)


def test_runtime_rejects_missing_assessment_fields():
    with pytest.raises(ScoringInputError, match="Missing assessment fields"):
        run_v35_scoring({"dimension_scores": {}})


def test_runtime_rejects_longitudinal_basis_for_single_content():
    assessment = {
        "dimension_scores": {f"D{i}": 80 for i in range(1, 8)},
        "eig_gaps": {"MCG": 2, "CEG": 4, "FCG": 2, "LCG": 6},
        "lcg_interpretation": "Rupture",
        "calculation_mode": "linear",
        "content_scope": "single_content",
        "d2_assessment_basis": "longitudinal_evidence",
        "ecc": {"claimed_confidence": 80, "supported_evidence": 60, "supported_method": 70, "supported_conclusion": 50},
        "reig": {"ERG": 0, "MRG": 1, "CRG": 2, "ARG": 3, "FRG": 4},
    }
    with pytest.raises(ScoringInputError, match="D2 assessment basis"):
        run_v35_scoring(assessment)
