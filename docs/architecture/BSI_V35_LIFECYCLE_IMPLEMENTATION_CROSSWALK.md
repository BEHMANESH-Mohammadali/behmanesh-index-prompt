# BSI v3.5 — Lifecycle-to-Implementation Crosswalk

**Status:** Canonical maintenance map  
**Scope:** Execution lifecycle only; this document does not redefine analytical criteria, scoring, or the protected Knowledge Core.

The numbered 17-item lifecycle in the Master Prompt is a conceptual workflow. It is **not a one-to-one enumeration of the 17 code registry handlers**: the implementation makes Draft Analysis and bounded Correction/Reanalysis explicit handlers, while Completion Gate and Final Answer are executed outside the registry. This crosswalk records those differences rather than concealing them.

| Master lifecycle # | Master/architecture concept | Code implementation | Mapping |
|---:|---|---|---|
| 1 | Task Intake | `task_intake` | Direct handler |
| 2 | Epistemic Need Assessment | `epistemic_need_assessment` | Direct handler |
| 3 | Effort Calibration | `effort_calibration` | Direct handler |
| 4 | Evidence Sufficiency | `evidence_sufficiency` | Direct handler |
| 5 | Evidence Exhaustion / Retrieval Escalation | `evidence_retrieval_or_gap_record` | Combined retrieval-or-gap handler |
| 6 | Counterevidence Search | `counterevidence` | Direct handler |
| 7 | Competing Interpretation Check | `competing_interpretations` | Direct handler |
| 8 | Structural Analysis | `structural_analysis` | Direct handler |
| 9 | Verification | `verification` | Direct handler |
| 10 | Assumption Excavation | `assumption_excavation` | Direct handler |
| 11 | EIG | `eig` | Direct handler |
| 12 | ECC | `ecc` | Direct handler |
| 13 | REIG | `draft_analysis` → `reig_draft_audit` | Draft Analysis is an explicit prerequisite handler; REIG audits that draft |
| 14 | Final Re-read | `correction_and_reanalysis` → `final_reread` | Bounded correction/reanalysis is an explicit prerequisite handler; final re-read remains distinct |
| 15 | Execution Status | `execution_status` | Direct handler |
| 16 | Completion Gate | `core/execution_orchestrator.py::run` → `ExecutionTrace.completion_gate` | Post-registry authorization; not a handler |
| 17 | Final Answer | `execute_bsi_v35` response assembly | Output construction after authorized completion; not a handler |

## Registry and control rules

- `MANDATORY_STAGES` defines the exact ordered 17 code handlers.
- `build_bsi_v35_handlers()` must provide one handler for every registry entry, in registry order.
- The orchestrator executes registered handlers sequentially; no parallel stage execution is implied.
- Completion Gate runs after the complete registry loop and fails closed on missing or blocked mandatory handlers.
- Final Answer is response construction after authorization, not an additional registry handler.
- Correction/Reanalysis is a bounded loop inside its registered handler.
- REIG, Final Re-read, and Completion Gate remain functionally distinct.

Tests must assert exact stage/handler coverage, the two explicit implementation substeps, and that Completion Gate and Final Answer are outside `MANDATORY_STAGES`.
