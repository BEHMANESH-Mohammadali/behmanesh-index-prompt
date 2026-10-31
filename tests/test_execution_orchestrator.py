from core.execution_contract import MANDATORY_STAGES
from core.execution_orchestrator import BSIExecutionOrchestrator, StageResult


def complete_handler(context):
    return StageResult(output={"stage": context["stage"]}, verification_state="INTERNAL")


def test_orchestrator_blocks_when_any_mandatory_handler_is_missing():
    handlers = {stage: complete_handler for stage in MANDATORY_STAGES[:-1]}
    result = BSIExecutionOrchestrator(handlers).run({"text": "A sufficiently long target text."})
    assert result.completion["authorized"] is False
    assert MANDATORY_STAGES[-1] in result.completion["blockers"]


def test_orchestrator_completes_only_when_all_stages_have_handlers():
    handlers = {stage: complete_handler for stage in MANDATORY_STAGES}
    result = BSIExecutionOrchestrator(handlers).run({"text": "A sufficiently long target text."})
    assert result.completion["authorized"] is True
    assert len(result.trace.stages) == len(MANDATORY_STAGES)


def test_unresolved_t8_blocks_completion():
    def intake(_):
        return StageResult(output={"unresolved_t8": True})
    handlers = {stage: complete_handler for stage in MANDATORY_STAGES}
    handlers["task_intake"] = intake
    result = BSIExecutionOrchestrator(handlers).run({"text": "A sufficiently long target text."})
    assert result.completion["authorized"] is False
    assert "unresolved_T8_claim_classification" in result.completion["blockers"]


def test_correction_loop_is_bounded_and_preserves_limit_disclosure():
    calls = []
    def correction(context):
        calls.append(context.get("correction_round", 1))
        return StageResult(output={"needs_reanalysis": True})
    handlers = {stage: complete_handler for stage in MANDATORY_STAGES}
    handlers["correction_and_reanalysis"] = correction
    result = BSIExecutionOrchestrator(handlers, max_correction_rounds=2).run(
        {"text": "A sufficiently long target text."}
    )
    assert calls == [1, 2]
    record = next(x for x in result.trace.stages if x.stage == "correction_and_reanalysis")
    assert "maximum" in record.limitation
