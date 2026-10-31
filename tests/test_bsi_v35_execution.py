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
