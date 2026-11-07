"""Provider-neutral contracts for model-backed BSI execution.

The BSI core depends on these contracts, never on a vendor SDK or model name.
Adapters may implement the same contract over local, hosted, or self-hosted APIs.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping, Protocol, Sequence


@dataclass(frozen=True)
class ModelCapabilities:
    """Declared capabilities; declarations must be verified by adapter probes."""
    structured_output: bool = False
    tool_calling: bool = False
    long_context: bool = False
    multimodal_input: bool = False
    streaming: bool = False
    max_context_tokens: int | None = None
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class ModelRequest:
    task: str
    system_instruction: str
    input_text: str
    output_schema: Mapping[str, Any] | None = None
    temperature: float = 0.0
    max_output_tokens: int | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class ModelResponse:
    content: str
    provider: str
    model: str
    request_id: str | None = None
    raw_metadata: Mapping[str, Any] = field(default_factory=dict)


class ModelAdapterError(RuntimeError):
    """A normalized adapter failure; never silently treated as model output."""


class ModelAdapter(Protocol):
    @property
    def capabilities(self) -> ModelCapabilities: ...

    def generate(self, request: ModelRequest) -> ModelResponse: ...


class ModelRouter(Protocol):
    def resolve(self, role: str) -> ModelAdapter: ...


@dataclass(frozen=True)
class TaskCapabilityRequirement:
    required: frozenset[str]
    description: str


def missing_capabilities(
    actual: ModelCapabilities, requirement: TaskCapabilityRequirement
) -> tuple[str, ...]:
    """Return unmet boolean capabilities without guessing from provider/model names."""
    return tuple(
        name for name in sorted(requirement.required)
        if not bool(getattr(actual, name, False))
    )
