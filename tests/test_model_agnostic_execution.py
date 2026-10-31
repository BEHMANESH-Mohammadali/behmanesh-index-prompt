import json
from unittest.mock import patch

import pytest

from core.execution_contract import (
    ExecutionTrace, MANDATORY_STAGES, StageRecord, StageStatus,
)
from core.model_adapters import OpenAICompatibleChatAdapter, StaticModelRouter
from core.model_contracts import (
    ModelAdapterError, ModelCapabilities, ModelRequest, ModelResponse,
    TaskCapabilityRequirement, missing_capabilities,
)


def test_capability_requirements_are_explicit():
    actual = ModelCapabilities(structured_output=True, tool_calling=False)
    required = TaskCapabilityRequirement(
        frozenset({"structured_output", "tool_calling"}), "test"
    )
    assert missing_capabilities(actual, required) == ("tool_calling",)


def test_router_uses_semantic_roles_not_vendor_names():
    adapter = object()
    router = StaticModelRouter({"claim_extraction": adapter})
    assert router.resolve("claim_extraction") is adapter
    with pytest.raises(ModelAdapterError):
        router.resolve("evidence_synthesis")


def test_adapter_requires_endpoint_and_model(monkeypatch):
    monkeypatch.delenv("BSI_MODEL_BASE_URL", raising=False)
    monkeypatch.delenv("BSI_MODEL_NAME", raising=False)
    with pytest.raises(ModelAdapterError):
        OpenAICompatibleChatAdapter()


def test_adapter_normalizes_chat_completion_response():
    payload = {
        "id": "req-1",
        "model": "test-model",
        "choices": [{"message": {"content": "{\"ok\": true}"}, "finish_reason": "stop"}],
        "usage": {"total_tokens": 3},
    }

    class FakeResponse:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

        def read(self):
            return json.dumps(payload).encode()

    with patch("core.model_adapters.urlopen", return_value=FakeResponse()):
        adapter = OpenAICompatibleChatAdapter(
            base_url="https://example.invalid/v1",
            model="test-model",
            capabilities=ModelCapabilities(structured_output=True),
        )
        result = adapter.generate(ModelRequest(
            task="extract",
            system_instruction="Return JSON",
            input_text="source",
            output_schema={"type": "object"},
        ))

    assert isinstance(result, ModelResponse)
    assert result.content == '{"ok": true}'
    assert result.provider == "openai-compatible"
    assert result.model == "test-model"
    assert result.request_id == "req-1"


def test_completion_gate_fails_closed_for_missing_mandatory_stages():
    trace = ExecutionTrace(
        execution_id="test",
        stages=[StageRecord(stage="task_intake", status=StageStatus.COMPLETED)],
    )
    result = trace.completion_gate()
    assert result["authorized"] is False
    assert set(result["blockers"]) == set(MANDATORY_STAGES) - {"task_intake"}


def test_completion_gate_blocks_unresolved_t8():
    trace = ExecutionTrace(
        execution_id="test",
        stages=[
            StageRecord(stage=name, status=StageStatus.COMPLETED)
            for name in MANDATORY_STAGES
        ],
    )
    result = trace.completion_gate(unresolved_t8=True)
    assert result["authorized"] is False
    assert "unresolved_T8_claim_classification" in result["blockers"]
