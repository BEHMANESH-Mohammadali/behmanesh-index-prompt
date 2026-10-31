"""Local-first model adapters; no hosted API key or vendor SDK is required.

Ollama's native HTTP API is an optional local transport. The BSI execution
contracts remain provider-neutral and can also be implemented by other
local runtimes.
"""
from __future__ import annotations

import json
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from core.model_contracts import (
    ModelAdapterError, ModelCapabilities, ModelRequest, ModelResponse,
)


class OllamaChatAdapter:
    """Adapter for a locally running Ollama server (default localhost:11434)."""

    def __init__(
        self, *, host: str | None = None, model: str | None = None,
        timeout_seconds: float = 180.0,
        capabilities: ModelCapabilities | None = None,
    ) -> None:
        self.host = (host or os.getenv("BSI_OLLAMA_HOST", "http://127.0.0.1:11434")).rstrip("/")
        self.model = model or os.getenv("BSI_OLLAMA_MODEL", "")
        self.timeout_seconds = timeout_seconds
        self._capabilities = capabilities or ModelCapabilities()
        if not self.model:
            raise ModelAdapterError("BSI_OLLAMA_MODEL must name an installed local model.")

    @property
    def capabilities(self) -> ModelCapabilities:
        return self._capabilities

    def generate(self, request: ModelRequest) -> ModelResponse:
        body = {
            "model": self.model, "stream": False,
            "messages": [
                {"role": "system", "content": request.system_instruction},
                {"role": "user", "content": request.input_text},
            ],
            "options": {"temperature": request.temperature},
        }
        if request.output_schema is not None and self.capabilities.structured_output:
            body["format"] = dict(request.output_schema)
        http_request = Request(
            f"{self.host}/api/chat", data=json.dumps(body).encode("utf-8"),
            headers={"Content-Type": "application/json"}, method="POST",
        )
        try:
            with urlopen(http_request, timeout=self.timeout_seconds) as response:
                payload = json.loads(response.read().decode("utf-8"))
        except HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")[:2000]
            raise ModelAdapterError(f"Local Ollama returned HTTP {exc.code}: {detail}") from exc
        except (URLError, TimeoutError, OSError) as exc:
            raise ModelAdapterError(f"Local Ollama is unavailable: {exc}") from exc
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ModelAdapterError("Local Ollama returned invalid JSON.") from exc

        try:
            content = payload["message"]["content"]
        except (KeyError, TypeError) as exc:
            raise ModelAdapterError("Response does not satisfy Ollama chat response contract.") from exc
        if not isinstance(content, str) or not content.strip():
            raise ModelAdapterError("Local model returned empty or non-text content.")
        return ModelResponse(
            content=content, provider="ollama-local",
            model=str(payload.get("model", self.model)),
            request_id=None,
            raw_metadata={
                "done": payload.get("done"),
                "prompt_eval_count": payload.get("prompt_eval_count"),
                "eval_count": payload.get("eval_count"),
            },
        )
