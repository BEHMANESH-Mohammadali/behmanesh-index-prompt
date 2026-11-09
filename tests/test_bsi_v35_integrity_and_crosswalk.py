import pytest

from core.execution_contract import MANDATORY_STAGES
from core.bsi_v35_execution import build_bsi_v35_handlers, task_intake, evidence_retrieval_or_gap_record


def test_canonical_registry_has_exact_handler_coverage_and_gate_is_external():
    handlers = build_bsi_v35_handlers()
    assert tuple(handlers) == MANDATORY_STAGES
    assert len(MANDATORY_STAGES) == 17
    assert "completion_gate" not in MANDATORY_STAGES
    assert "final_answer" not in MANDATORY_STAGES


def test_task_intake_candidate_artifacts_are_reused_by_retrieval(monkeypatch):
    calls = {"claim": 0, "assumptions": 0, "domain": 0}

    def claim(text):
        calls["claim"] += 1
        return "candidate claim"

    def assumptions(text):
        calls["assumptions"] += 1
        return ["candidate assumption"]

    def domain(text):
        calls["domain"] += 1
        return "general"

    monkeypatch.setattr("core.bsi_v35_execution.extract_core_claim", claim)
    monkeypatch.setattr("core.bsi_v35_execution.excavate_assumptions", assumptions)
    monkeypatch.setattr("core.bsi_v35_execution.detect_domain", domain)
    monkeypatch.setattr(
        "core.bsi_v35_execution.evaluate_claim_with_rag",
        lambda value: {"enabled": True, "retrieved_sources": 0, "source_refs": []},
    )

    text = "A sufficiently long text for candidate extraction reuse."
    intake = task_intake({"task": {"text": text}})
    context = {"task": {"text": text}, "task_intake": intake.output}
    retrieval = evidence_retrieval_or_gap_record(context)

    assert retrieval.output["candidate_core_claim"] == "candidate claim"
    assert calls == {"claim": 1, "assumptions": 1, "domain": 1}
