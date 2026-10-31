# BSI v3.5 Implementation Traceability Review

**Review scope:** existing Master Prompt, Execution Architecture, v3.5 scoring runtime, existing v3.4.2 analysis/RAG pipeline, provider adapters, and execution orchestrator.
**Purpose:** map already-defined requirements to existing code and identify genuine connection gaps. This document does not create or redefine BSI analytical requirements.
**Review basis:** repository files inspected on `feat/model-agnostic-execution-adapters` at the review commit. CI was checked for the execution-trace commit `fd7cb8b6dbbcd7a37310a70bf87cccc822babba9`.

## Decision

Do not add a second set of analytical-stage implementations. The Master Prompt and Execution Architecture already specify the analytical obligations. The current codebase contains some relevant legacy analysis/RAG functions and a separate v3.5 explicit-input scoring runtime, but these are not yet connected as one evidence-grounded v3.5 execution path.

The immediate work is traceability, safe reuse, tests, and integration planning. Do not connect legacy heuristic scores to the v3.5 scoring runtime or treat model output as evidence.

## Requirement-to-code matrix

| Requirement already specified in the canonical documents | Existing implementation | Status | Required action |
|---|---|---|---|
| Preserve BSI Knowledge Core, criteria, weights, and scoring authority | `MASTER_PROMPT_BSI_v3.5.md`; `core/bsi_scoring_v35.py` | Defined; explicit-input scoring implemented | Keep protected. No duplicate criteria or score inference from raw text. |
| Intake, effort calibration, evidence sufficiency, retrieval/gap recording, counterevidence, alternatives, verification, assumption excavation, EIG, ECC, draft, REIG, correction, final re-read, execution status | `BSI_3.5_Execution_Architecture.md`; `core/execution_contract.py`; `core/execution_orchestrator.py` | Requirements defined; lifecycle skeleton exists; actual analytical handlers not wired | Reuse the stage contract. Connect only existing verified functions where their semantics match; otherwise mark the stage blocked, not complete. |
| Core claim extraction and claim classification | `core/bsi_engine.py` | Legacy heuristic implementation exists | Review for suitability and known limitations before reuse. It is not evidence verification and must not silently become the v3.5 authority. |
| Manifest / Latent / Meta, assumptions and structural analysis | `core/bsi_engine.py` and consumers in `core/bsi_pipeline.py` | Legacy implementation exists; v3.5 orchestration connection unverified | Map output schemas and evidence provenance before adapter wiring. |
| Evidence retrieval and claim-level support/conflict signals | `core/rag/*`; `core/bsi_pipeline.py` | Experimental RAG components and legacy integration exist | Inspect retrieval backend, source metadata, failure behavior, and tests. RAG output is a lead/signal, not proof by itself. |
| Counterevidence and competing interpretations | Specified in Master Prompt / Architecture; some RAG conflict fields exist | No verified end-to-end handler found in the v3.5 orchestrator | Do not count a generic RAG conflict field as completion of the full requirement. Trace the existing implementation and its source-level coverage first. |
| EIG assessment | Legacy heuristics in `core/bsi_engine.py` / `core/bsi_pipeline.py`; formal v3.5 calculator in `core/bsi_scoring_v35.py` | Two distinct paths; v3.5 calculator requires explicit inputs | Do not route legacy heuristic outputs into v3.5 scoring without a documented equivalence review and explicit approval. |
| ECC v2.0 | `core/bsi_scoring_v35.py` | Formal calculation exists in v3.5 runtime; legacy `core/bsi_pipeline.py` uses a different simplified calculation | Use the v3.5 ECC implementation for v3.5 scoring. Keep legacy behavior clearly version-scoped; do not blend formulas. |
| REIG on Draft Analysis | `core/bsi_scoring_v35.py`; `core/bsi_v35_runtime.py` | Formal explicit-input calculation exists; automatic draft-audit population is not connected | Preserve the Draft Analysis object boundary. Require evidence-backed REIG inputs; no inferred default scores. |
| Explicit-input scoring API and MCP contract | `api/routes/bsi.py`, `api/mcp.py`, `core/bsi_v35_runtime.py` | Connected to v3.5 calculator; raw-text-only scoring is rejected | Keep this safety boundary. API acceptance proves scoring integration, not autonomous analysis completion. |
| Model-provider neutrality | `core/model_contracts.py`, `core/model_adapters.py`, `core/local_model_adapters.py` | Adapter contracts and generic transports implemented | Keep adapters behind the contract; add capability conformance probes before trusting declared capabilities. |
| Completion Gate / fail-closed lifecycle | `core/execution_contract.py`, `core/execution_orchestrator.py` | Skeleton implemented and tested; it only orchestrates supplied handlers | Missing handlers must remain blockers. A run with placeholder handlers is not evidence of a completed BSI analysis. |
| Execution trace, provenance, verification state and persistence | `StageRecord` / `ExecutionTrace` hold trace fields in memory | Partial; no durable persistence established by this review | Do not claim persistence. Define/locate the existing persistence boundary before implementing one. |
| Final re-read and output firewall | Master Prompt / Architecture; named stages in orchestrator | Requirement exists; concrete quality-control handler is not wired | Connect only after its input/output contract is explicit and tests prove the gate blocks unresolved defects. |
| Validation | `.github/workflows/bsi-v35-validation.yml` and repository tests | CI passed on reviewed commit | The workflow verifies compilation and test suite, not real external retrieval or a full autonomous run. |

## Confirmed corrections and validation

- The execution contract includes `execution_status` as a mandatory lifecycle stage.
- The correction/reanalysis stage is marked `BLOCKED` when the bounded correction loop ends with unresolved defects.
- T8 detection is accumulated from stage outputs rather than being restricted to task intake.
- Tests cover missing handlers, successful orchestration with test handlers, unresolved T8, bounded correction, and correction-limit blocking.
- GitHub Actions run `41227403595` for commit `fd7cb8b6dbbcd7a37310a70bf87cccc822babba9` completed successfully. The job steps reported success for Python compilation and the repository test suite.

## Integration sequence (reuse-first; no duplicate modules)

1. **Freeze the boundary:** keep Master Prompt and Knowledge Core unchanged during wiring.
2. **Inventory callable functions and schemas:** map actual inputs/outputs of the existing engine, pipeline, RAG components, v3.5 scoring runtime, and API. Record version and evidence provenance for each.
3. **Resolve version boundaries:** label legacy v3.4.1/v3.4.2 heuristic behavior separately from v3.5 explicit-input scoring. Never feed legacy scores into v3.5 by name alone.
4. **Connect existing functions only where semantically equivalent:** each handler must return a typed result, source/evidence references where applicable, a truthful verification state, and explicit limitations.
5. **Fail closed on absent coverage:** do not mark counterevidence, competing interpretations, source verification, assumption excavation, or REIG as completed merely because an adjacent function ran.
6. **Add integration tests using controlled fixtures:** assert evidence provenance, error propagation, unresolved-gap blocking, single-content D2 limits, and no score inference from raw text.
7. **Run CI and inspect the final diff:** report exact commit, changed files, tests, and unresolved gaps. Keep the PR draft and unmerged pending review.

## Non-goals for this pass

- No new BSI criteria, weights, scoring formulas, ontology, or parallel analytical framework.
- No new duplicate claim-extraction, RAG, EIG, ECC, or REIG implementation.
- No automatic score generation from model prose.
- No claim that a fully autonomous BSI pipeline exists until the actual handlers are connected and integration-tested.
