"""Provider-neutral, fail-closed BSI execution lifecycle.

This module orchestrates supplied stage handlers. It deliberately does not
invent evidence, derive BSI scores from raw text, or treat model output as
external verification. Missing handlers block completion.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Mapping
from uuid import uuid4

from core.execution_contract import (
    ExecutionTrace, MANDATORY_STAGES, StageRecord, StageStatus,
)


@dataclass(frozen=True)
class StageResult:
    output: Any = None
    evidence_refs: tuple[str, ...] = ()
    verification_state: str | None = None
    limitation: str | None = None
    not_applicable: bool = False


StageHandler = Callable[[Mapping[str, Any]], StageResult]


@dataclass
class ExecutionResult:
    execution_id: str
    trace: ExecutionTrace
    outputs: dict[str, Any]
    completion: dict[str, Any]


class BSIExecutionOrchestrator:
    """Execute lifecycle handlers in canonical order and fail closed."""

    def __init__(self, handlers: Mapping[str, StageHandler], *, max_correction_rounds: int = 2):
        if max_correction_rounds < 1:
            raise ValueError("max_correction_rounds must be at least 1.")
        self.handlers = dict(handlers)
        self.max_correction_rounds = max_correction_rounds

    def run(self, task: Mapping[str, Any]) -> ExecutionResult:
        execution_id = str(uuid4())
        trace = ExecutionTrace(execution_id=execution_id, stages=[])
        outputs: dict[str, Any] = {"task": dict(task)}
        unresolved_t8 = False

        for stage in MANDATORY_STAGES:
            handler = self.handlers.get(stage)
            if handler is None:
                trace.stages.append(StageRecord(
                    stage=stage, status=StageStatus.BLOCKED,
                    limitation="No executable handler is configured for this mandatory stage.",
                ))
                continue
            try:
                context = {**outputs, "execution_id": execution_id, "stage": stage}
                result = (
                    self._run_correction(handler, context)
                    if stage == "correction_and_reanalysis"
                    else handler(context)
                )
                if not isinstance(result, StageResult):
                    raise TypeError("Stage handler must return StageResult.")
                correction_unresolved = (
                    stage == "correction_and_reanalysis"
                    and isinstance(result.output, Mapping)
                    and bool(result.output.get("needs_reanalysis") or result.output.get("correction_limit_reached"))
                )
                explicit_block = (
                    isinstance(result.output, Mapping)
                    and bool(result.output.get("blocked", False))
                )
                invalid_output = (
                    not result.not_applicable
                    and (
                        not isinstance(result.output, Mapping)
                        or not bool(result.output)
                    )
                )
                execution_status_not_ready = (
                    stage == "execution_status"
                    and (
                        not isinstance(result.output, Mapping)
                        or result.output.get("ready_for_completion") is not True
                    )
                )
                status = (
                    StageStatus.BLOCKED
                    if correction_unresolved or explicit_block or invalid_output or execution_status_not_ready
                    else StageStatus.NOT_APPLICABLE if result.not_applicable
                    else StageStatus.COMPLETED
                )
                limitation = result.limitation
                if invalid_output and not limitation:
                    limitation = "Stage returned no structured output; completion is blocked."
                if execution_status_not_ready and not limitation:
                    limitation = "Execution status did not explicitly authorize readiness for completion."
                if correction_unresolved and not limitation:
                    limitation = "Correction/reanalysis remains unresolved; completion is blocked."
                if explicit_block and not limitation:
                    limitation = str(result.output.get("block_reason") or "Stage explicitly blocked completion.")
                trace.stages.append(StageRecord(
                    stage=stage, status=status,
                    evidence_refs=list(result.evidence_refs),
                    verification_state=result.verification_state,
                    limitation=limitation, output=result.output,
                ))
                outputs[stage] = result.output
                if isinstance(result.output, Mapping):
                    unresolved_t8 = unresolved_t8 or bool(result.output.get("unresolved_t8", False))
            except Exception as exc:
                trace.stages.append(StageRecord(
                    stage=stage, status=StageStatus.BLOCKED,
                    limitation=f"Stage execution failed: {type(exc).__name__}: {exc}",
                ))

        completion = trace.completion_gate(unresolved_t8=unresolved_t8)
        return ExecutionResult(execution_id, trace, outputs, completion)

    def _run_correction(self, handler: StageHandler, context: Mapping[str, Any]) -> StageResult:
        """Bounded correction loop; handlers must preserve source evidence and scores."""
        result = handler(context)
        if not isinstance(result, StageResult):
            raise TypeError("Correction handler must return StageResult.")
        rounds = 1
        while isinstance(result.output, Mapping) and result.output.get("needs_reanalysis"):
            if rounds >= self.max_correction_rounds:
                return StageResult(
                    output={**result.output, "correction_limit_reached": True},
                    evidence_refs=result.evidence_refs,
                    verification_state=result.verification_state,
                    limitation="Correction loop reached its configured maximum; unresolved defects remain.",
                )
            context = {**context, "previous_correction": result.output, "correction_round": rounds + 1}
            result = handler(context)
            if not isinstance(result, StageResult):
                raise TypeError("Correction handler must return StageResult.")
            rounds += 1
        return result
