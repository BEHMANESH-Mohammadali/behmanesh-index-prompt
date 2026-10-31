"""Provider-neutral execution trace and fail-closed completion contract."""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class StageStatus(str, Enum):
    NOT_STARTED = "NOT_STARTED"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    BLOCKED = "BLOCKED"
    NOT_APPLICABLE = "NOT_APPLICABLE"


MANDATORY_STAGES = (
    "task_intake",
    "epistemic_need_assessment",
    "effort_calibration",
    "evidence_sufficiency",
    "evidence_retrieval_or_gap_record",
    "counterevidence",
    "competing_interpretations",
    "structural_analysis",
    "verification",
    "assumption_excavation",
    "eig",
    "ecc",
    "draft_analysis",
    "reig_draft_audit",
    "correction_and_reanalysis",
    "final_reread",
)


@dataclass
class StageRecord:
    stage: str
    status: StageStatus = StageStatus.NOT_STARTED
    evidence_refs: list[str] = field(default_factory=list)
    verification_state: str | None = None
    limitation: str | None = None
    output: Any = None


@dataclass
class ExecutionTrace:
    execution_id: str
    stages: list[StageRecord]
    independent_evaluation: str = "BEST-EFFORT SELF-AUDIT — NOT INDEPENDENTLY VALIDATED"

    def completion_gate(self, *, unresolved_t8: bool = False) -> dict[str, Any]:
        incomplete = [
            item.stage for item in self.stages
            if item.stage in MANDATORY_STAGES
            and item.status not in {StageStatus.COMPLETED, StageStatus.NOT_APPLICABLE}
        ]
        blockers = list(incomplete)
        if unresolved_t8:
            blockers.append("unresolved_T8_claim_classification")
        return {
            "authorized": not blockers,
            "status": "AUTHORIZED" if not blockers else "BLOCKED",
            "blockers": blockers,
            "independent_evaluation": self.independent_evaluation,
        }
