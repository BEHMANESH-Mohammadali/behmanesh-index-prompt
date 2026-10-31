"""Generic adapters for model APIs; no vendor SDK is required.

OpenAI-compatible chat-completions is treated only as a transport protocol.
It is not the BSI model contract: provider-specific behavior stays inside this
adapter and can be replaced without changing the BSI core.
"""
from __future__ import annotations

import json
import os
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from core.model_contracts import (
    ModelAdapterError, ModelCapabilities, ModelRequest, ModelResponse,
)


class OpenAICompatibleChatAdapter:
    """Adapter for any service implementing the chat-completions wire format."""

    def __init__(
        self,
        *,
        base_url: str | None = None,
        api_key: str | None = None,
        model: str | None = None,
        timeout_seconds: float = 90.0,
        provider_label: str = "openai-compatible",
        capabilities: ModelCapabilities | None = None,
    ) -> None:
        self.base_url = (base_url or os.getenv("BSI_MODEL_BASE_URL", "")).rstrip("/")
        self.api_key = api_key or os.getenv("BSI_MODEL_API_KEY", "")
        self.model = model or os.getenv("BSI_MODEL_NAME", "")
        self.timeout_seconds = timeout_seconds
        self.provider_label = provider_label
        self._capabilities = capabilities or ModelCapabilities()
        if not self.base_url or not self.model:
            raise ModelAdapterError(
                "BSI_MODEL_BASE_URL and BSI_MODEL_NAME must be configured."
            )

    @property
    def capabilities(self) -> ModelCapabilities:
        return self._capabilities

    def generate(self, request: ModelRequest) -> ModelResponse:
        body: dict[str, Any] = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": request.system_instruction},
                {"role": "user", "content": request.input_text},
            ],
            "temperature": request.temperature,
        }
        if request.max_output_tokens is not None:
            body["max_tokens"] = request.max_output_tokens
        # Only request JSON mode when the adapter has explicitly declared support.
        if request.output_schema is not None and self.capabilities.structured_output:
            body["response_format"] = {"type": "json_object"}

        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        url = f"{self.base_url}/chat/completions"
        http_request = Request(
            url, data=json.dumps(body).encode("utf-8"),
            headers=headers, method="POST",
        )
        try:
            with urlopen(http_request, timeout=self.timeout_seconds) as response:
                payload = json.loads(response.read().decode("utf-8"))
        except HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")[:2000]
            raise ModelAdapterError(
                f"Model endpoint returned HTTP {exc.code}: {detail}"
            ) from exc
        except (URLError, TimeoutError, OSError) as exc:
            raise ModelAdapterError(f"Model endpoint unavailable: {exc}") from exc
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ModelAdapterError("Model endpoint returned invalid JSON.") from exc

        try:
            content = payload["choices"][0]["message"]["content"]
        except (KeyError, IndexError, TypeError) as exc:
            raise ModelAdapterError(
                "Response does not satisfy chat-completions response contract."
            ) from exc
        if not isinstance(content, str) or not content.strip():
            raise ModelAdapterError("Model returned empty or non-text content.")

        return ModelResponse(
            content=content,
            provider=self.provider_label,
            model=str(payload.get("model", self.model)),
            request_id=payload.get("id"),
            raw_metadata={
                "finish_reason": payload.get("choices", [{}])[0].get("finish_reason"),
                "usage": payload.get("usage"),
            },
        )


class StaticModelRouter:
    """Small role-to-adapter router; roles are configuration, not model identities."""

    def __init__(self, adapters: dict[str, Any]) -> None:
        self._adapters = dict(adapters)

    def resolve(self, role: str):
        try:
            return self._adapters[role]
        except KeyError as exc:
            raise ModelAdapterError(f"No model adapter configured for role: {role}") from exc
