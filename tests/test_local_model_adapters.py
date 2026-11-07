import json
from unittest.mock import patch
import pytest
from urllib.error import URLError

from core.local_model_adapters import OllamaChatAdapter
from core.model_contracts import ModelAdapterError, ModelCapabilities, ModelRequest


def test_ollama_adapter_requires_local_model_name(monkeypatch):
    monkeypatch.delenv("BSI_OLLAMA_MODEL", raising=False)
    with pytest.raises(ModelAdapterError):
        OllamaChatAdapter()


def test_ollama_adapter_normalizes_local_response():
    payload = {
        "model": "qwen-local",
        "message": {"role": "assistant", "content": "local result"},
        "done": True, "eval_count": 12,
    }
    class FakeResponse:
        def __enter__(self): return self
        def __exit__(self, *args): return False
        def read(self): return json.dumps(payload).encode()

    with patch("core.local_model_adapters.urlopen", return_value=FakeResponse()):
        adapter = OllamaChatAdapter(
            host="http://127.0.0.1:11434", model="qwen-local",
            capabilities=ModelCapabilities(structured_output=True),
        )
        result = adapter.generate(ModelRequest(
            task="extract", system_instruction="Return structured data",
            input_text="source", output_schema={"type": "object"},
        ))
    assert result.content == "local result"
    assert result.provider == "ollama-local"
    assert result.model == "qwen-local"
    assert result.raw_metadata["eval_count"] == 12


def test_ollama_adapter_reports_connection_failure():
    with patch("core.local_model_adapters.urlopen", side_effect=URLError("offline")):
        adapter = OllamaChatAdapter(model="qwen-local")
        with pytest.raises(ModelAdapterError, match="unavailable"):
            adapter.generate(ModelRequest("task", "system", "input"))
