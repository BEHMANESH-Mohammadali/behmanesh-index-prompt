import pytest
from fastapi.testclient import TestClient

from api.main import app
from core.bsi_v35_execution import configured_model_router, execute_bsi_v35
from core.model_contracts import ModelAdapterError

client = TestClient(app)


def test_execute_endpoint_rejects_short_text():
    response = client.post("/bsi/execute", json={"text": "short"})
    assert response.status_code == 422
    assert response.json()["detail"]["code"] == "TEXT_TOO_SHORT"


def test_execute_endpoint_requires_explicit_model_configuration(monkeypatch):
    for key in (
        "BSI_OLLAMA_MODEL", "BSI_OLLAMA_MODEL_ANALYST", "BSI_OLLAMA_MODEL_AUDITOR",
        "BSI_MODEL_BASE_URL", "BSI_MODEL_NAME", "BSI_MODEL_NAME_ANALYST",
        "BSI_MODEL_NAME_AUDITOR",
    ):
        monkeypatch.delenv(key, raising=False)
    response = client.post("/bsi/execute", json={
        "text": "A sufficiently long text for a guarded execution test."
    })
    assert response.status_code == 503
    assert response.json()["detail"]["code"] == "MODEL_ROUTER_NOT_CONFIGURED"


def test_model_router_supports_role_specific_local_models(monkeypatch):
    monkeypatch.setenv("BSI_OLLAMA_MODEL_ANALYST", "local-analyst")
    monkeypatch.setenv("BSI_OLLAMA_MODEL_AUDITOR", "local-auditor")
    monkeypatch.delenv("BSI_OLLAMA_MODEL", raising=False)
    router = configured_model_router()
    assert router.resolve("analyst").model == "local-analyst"
    assert router.resolve("auditor").model == "local-auditor"


def test_execution_blocks_when_required_stages_are_unavailable(monkeypatch):
    monkeypatch.setattr(
        "core.bsi_v35_execution.evaluate_claim_with_rag",
        lambda claim: {"enabled": False, "retrieved_sources": 0},
    )
    result = execute_bsi_v35({"text": "A sufficiently long target text for integration."})
    assert result["status"] == "BLOCKED"
    assert result["completion"]["authorized"] is False
    assert any(stage["status"] == "BLOCKED" for stage in result["trace"])
    assert result["scoring"] is None


def test_source_level_verification_requires_inspected_text_and_reference():
    from core.bsi_v35_execution import verification
    result = verification({
        "task": {"text": "A sufficiently long target text."},
        "structural_analysis": {"core_claim": "a claim"},
        "evidence_retrieval_or_gap_record": {"source_count": 2, "retrieval_signal": {}},
    })
    assert result.output["blocked"] is True
    assert result.verification_state == "NOT_EXTERNALLY_VERIFIABLE"


class _FakeAdapter:
    capabilities = None

    def generate(self, request):
        from core.model_contracts import ModelResponse
        instruction = request.system_instruction.lower()
        if "find counterevidence" in instruction:
            output = {"counterevidence": [], "searched_sources": ["fixture:source-1"], "unresolved_gaps": [], "sufficient": True}
        elif "generate materially distinct interpretations" in instruction:
            output = {"interpretations": ["Interpretation A", "Interpretation B"], "evidence_for_each": [], "evidence_against_each": [], "preferred_interpretation": "A", "uncertainty": "fixture"}
        elif "perform bsi v3.5 structural analysis" in instruction:
            output = {"core_claim": "Fixture claim", "manifest_layer": [], "latent_layer": [], "meta_layer": [], "mechanisms": [], "feedback_loops": [], "leverage_points": [], "claim_evidence_inference_graph": [], "uncertainty": "fixture", "limitations": []}
        elif "audit each material claim" in instruction:
            output = {"verified_claims": [], "unverified_claims": ["Fixture claim"], "contradictions": [], "verification_state": "SOURCE_TEXT_REVIEWED_MODEL_ASSISTED", "unresolved_gaps": []}
        elif "excavate explicit and implicit assumptions" in instruction:
            output = {"assumptions": [], "counterfactual_tests": [], "author_stated": [], "analyst_inferred": [], "uncertainty": "fixture"}
        elif "assess eig components" in instruction:
            output = {"raw_gaps": {"MCG": 2, "CEG": 3, "FCG": 2, "LCG": 4}, "lcg_interpretation": "Unknown", "evidence_for_each_gap": ["fixture"], "missing_evidence": [], "ready_for_scoring": True}
        elif "calibrate the confidence" in instruction:
            output = {"claimed_confidence": 70, "supported_evidence": 60, "supported_method": 60, "supported_conclusion": 55, "evidence_basis": ["fixture"], "uncertainty": "fixture", "ready_for_scoring": True}
        elif "apply official reig dimensions" in instruction:
            output = {"scores": {"ERG": 1, "MRG": 1, "CRG": 1, "ARG": 1, "FRG": 1}, "evidence_for_each_dimension": ["fixture"], "defects": [], "needs_reanalysis": False, "ready_for_scoring": True}
        elif "final re-read" in instruction:
            output = {"passed": True, "defects": [], "unresolved_gaps": [], "ready_for_final": True}
        else:
            raise AssertionError(f"Unexpected model instruction: {request.system_instruction}")
        import json
        return ModelResponse(content=json.dumps(output), provider="test", model="fixture")


def test_full_orchestration_connects_existing_stages_and_scores_only_explicit_inputs(monkeypatch):
    from core.model_adapters import StaticModelRouter
    from core.bsi_v35_execution import execute_bsi_v35

    monkeypatch.setattr(
        "core.bsi_v35_execution.evaluate_claim_with_rag",
        lambda claim: {
            "enabled": True, "retrieved_sources": 1, "external_support": 0.4,
            "external_conflict": 0.0, "external_coverage": 0.3,
            "external_status": "underdetermined",
        },
    )
    router = StaticModelRouter({"analyst": _FakeAdapter(), "auditor": _FakeAdapter()})
    result = execute_bsi_v35({
        "text": "A sufficiently long fixture text containing a claim for structural analysis.",
        "model_router": router,
        "source_materials": [{"source_ref": "fixture:source-1", "text": "Inspected source text for a fixture claim."}],
        "dimension_scores": {f"D{i}": 75 for i in range(1, 8)},
        "calculation_mode": "linear",
        "content_scope": "single_content",
    })
    assert result["status"] == "COMPLETED_WITH_EXPLICIT_ASSESSMENTS"
    assert result["completion"]["authorized"] is True
    assert result["scoring"]["engine_version"] == "3.5.0-explicit-input"
    assert result["scoring"]["D2_assessment_basis"] == "internal_coherence_only"
    assert len(result["trace"]) == 17
