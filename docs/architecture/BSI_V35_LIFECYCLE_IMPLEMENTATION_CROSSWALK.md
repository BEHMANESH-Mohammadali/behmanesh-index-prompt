# BSI v3.5 — Lifecycle-to-Implementation Crosswalk

**Status:** Canonical maintenance map  
**Scope:** Execution lifecycle only; this document does not redefine analytical criteria, scoring, or the protected Knowledge Core.

This crosswalk resolves the presentation-level lifecycle in the Master Prompt and Execution Architecture against the executable stage registry. The registry is the source of truth for the 17 ordered handlers. Completion Gate and Final Answer are deliberately outside that registry.

| # | Master/architecture lifecycle concept | Executable stage / location | Boundary |
|---:|---|---|---|
| 1 | task intake | `MANDATORY_STAGES[0]` / `core/bsi_v35_execution.py::task_intake` | Mandatory ordered handler |
| 2 | epistemic need assessment | `MANDATORY_STAGES[1]` / `core/bsi_v35_execution.py::epistemic_need_assessment` | Mandatory ordered handler |
| 3 | effort calibration | `MANDATORY_STAGES[2]` / `core/bsi_v35_execution.py::effort_calibration` | Mandatory ordered handler |
| 4 | evidence sufficiency | `MANDATORY_STAGES[3]` / `core/bsi_v35_execution.py::evidence_sufficiency` | Mandatory ordered handler |
| 5 | evidence retrieval or gap record | `MANDATORY_STAGES[4]` / `core/bsi_v35_execution.py::evidence_retrieval_or_gap_record` | Mandatory ordered handler |
| 6 | counterevidence | `MANDATORY_STAGES[5]` / `core/bsi_v35_execution.py::counterevidence` | Mandatory ordered handler |
| 7 | competing interpretations | `MANDATORY_STAGES[6]` / `core/bsi_v35_execution.py::competing_interpretations` | Mandatory ordered handler |
| 8 | structural analysis | `MANDATORY_STAGES[7]` / `core/bsi_v35_execution.py::structural_analysis` | Mandatory ordered handler |
| 9 | verification | `MANDATORY_STAGES[8]` / `core/bsi_v35_execution.py::verification` | Mandatory ordered handler |
| 10 | assumption excavation | `MANDATORY_STAGES[9]` / `core/bsi_v35_execution.py::assumption_excavation` | Mandatory ordered handler |
| 11 | eig | `MANDATORY_STAGES[10]` / `core/bsi_v35_execution.py::eig` | Mandatory ordered handler |
| 12 | ecc | `MANDATORY_STAGES[11]` / `core/bsi_v35_execution.py::ecc` | Mandatory ordered handler |
| 13 | draft analysis | `MANDATORY_STAGES[12]` / `core/bsi_v35_execution.py::draft_analysis` | Mandatory ordered handler |
| 14 | reig draft audit | `MANDATORY_STAGES[13]` / `core/bsi_v35_execution.py::reig_draft_audit` | Mandatory ordered handler |
| 15 | correction and reanalysis | `MANDATORY_STAGES[14]` / `core/bsi_v35_execution.py::correction_and_reanalysis` | Mandatory ordered handler |
| 16 | final reread | `MANDATORY_STAGES[15]` / `core/bsi_v35_execution.py::final_reread` | Mandatory ordered handler |
| 17 | execution status | `MANDATORY_STAGES[16]` / `core/bsi_v35_execution.py::execution_status` | Mandatory ordered handler |
| — | Completion Gate | `core/execution_orchestrator.py::run` → `ExecutionTrace.completion_gate` | Post-stage authorization; not a handler |
| — | Final Answer | `execute_bsi_v35` response assembly | Output construction after authorized completion; not a handler |

## Control rules

- `MANDATORY_STAGES` defines the exact ordered 17-stage registry.
- `build_bsi_v35_handlers()` must provide one handler for every registry entry.
- The orchestrator executes handlers sequentially; no parallel stage execution is implied.
- Completion Gate runs after the stage loop and fails closed on missing or blocked mandatory stages.
- Final Answer is response construction, not an additional execution stage.
- Correction/reanalysis is a bounded loop inside its registered stage; REIG remains a distinct audit input to that stage.
- Final Re-read remains distinct from REIG and Completion Gate.

Tests must assert exact stage/handler coverage and that Completion Gate is not included in `MANDATORY_STAGES`.
