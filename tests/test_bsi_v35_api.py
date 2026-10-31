from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_v35_version_reports_explicit_input_runtime():
    response = client.get("/bsi/version")
    assert response.status_code == 200
    payload = response.json()
    assert payload["engine_version"] == "3.5.0-explicit-input"
    assert payload["engine_status"] == "V3_5_SCORING_CONNECTED"
    assert payload["scoring_endpoints_are_v3_5"] is True


def test_v35_score_rejects_missing_assessment_instead_of_legacy_heuristics():
    response = client.post("/bsi/score", json={"text": "A sufficiently long input text for the API."})
    assert response.status_code == 422
    assert response.json()["detail"]["code"] == "MISSING_V35_ASSESSMENT"


def test_v35_score_accepts_explicit_assessment():
    payload = {
        "text": "A sufficiently long input text for the API.",
        "assessment": {
            "dimension_scores": {f"D{i}": 80 for i in range(1, 8)},
            "eig_gaps": {"MCG": 2, "CEG": 4, "FCG": 2, "LCG": 6},
            "lcg_interpretation": "Rupture",
            "calculation_mode": "linear",
            "ecc": {
                "claimed_confidence": 80,
                "supported_evidence": 60,
                "supported_method": 70,
                "supported_conclusion": 50,
            },
            "reig": {"ERG": 0, "MRG": 1, "CRG": 2, "ARG": 3, "FRG": 4},
        },
    }
    response = client.post("/bsi/score", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert body["engine_version"] == "3.5.0-explicit-input"
    assert body["BSI"]["BSI_score"] < 80
    assert body["EIG"]["penalty_formula"] == "EIG_avg / 20"
    assert "ECC_Total" not in body["ECC"]
    assert body["REIG"]["REIG_Total"] == 2


def test_v35_score_rejects_missing_d2():
    payload = {
        "text": "A sufficiently long input text for the API.",
        "assessment": {
            "dimension_scores": {f"D{i}": 80 for i in range(1, 8) if i != 2},
            "eig_gaps": {"MCG": 2, "CEG": 4, "FCG": 2, "LCG": 6},
            "lcg_interpretation": "Rupture",
            "calculation_mode": "linear",
            "ecc": {
                "claimed_confidence": 80,
                "supported_evidence": 60,
                "supported_method": 70,
                "supported_conclusion": 50,
            },
            "reig": {"ERG": 0, "MRG": 1, "CRG": 2, "ARG": 3, "FRG": 4},
        },
    }
    response = client.post("/bsi/score", json=payload)
    assert response.status_code == 422
