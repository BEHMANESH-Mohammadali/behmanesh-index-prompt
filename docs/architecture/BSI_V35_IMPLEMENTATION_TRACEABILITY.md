# BSI v3.5 Implementation Traceability Review

**Review scope:** existing Master Prompt, Execution Architecture, v3.5 scoring runtime, existing v3.4.2 analysis/RAG pipeline, provider adapters, and execution orchestrator.
**Purpose:** map already-defined requirements to existing code and identify genuine connection gaps. This document does not create or redefine BSI analytical requirements.
**Review basis:** repository files inspected on `feat/model-agnostic-execution-adapters` at the review commit. CI was checked for the execution-trace commit `fd7cb8b6dbbcd7a37310a70bf87cccc822babba9`.

## Decision

Do not add a second set of analytical-stage implementations. The Master Prompt and Execution Architecture already specify the analytical obligations. The repository now has a guarded v3.5 execution integration layer in `core/bsi_v35_execution.py`, an API entry point at `POST /bsi/execute`, and provider-neutral local/hosted model adapters. This connects the named lifecycle stages to existing retrieval, claim extraction, assumption heuristics, model-assisted analysis/audit, and the explicit-input scoring runtime.

This is an operational guarded workflow, not a claim of independent validation or universal autonomous completion. It intentionally blocks when source text is absent, a model role is unconfigured, evidence is inadequate, or scoring inputs lack explicit evidence bases. Experimental RAG signals remain leads, not proof.

## Requirement-to-code matrix

| Requirement already specified in the canonical documents | Existing implementation | Status | Required action |
|---|---|---|---|
| Preserve BSI Knowledge Core, criteria, weights, and scoring authority | `MASTER_PROMPT_BSI_v3.5.md`; `core/bsi_scoring_v35.py` | Defined; explicit-input scoring implemented | Keep protected. No duplicate criteria or score inference from raw text. |
| Intake through execution status lifecycle | `BSI_3.5_Execution_Architecture.md`; `core/execution_contract.py`; `core/execution_orchestrator.py`; `core/bsi_v35_execution.py` | All mandatory stage names now have concrete guarded handlers and are wired through the orchestrator | Keep fail-closed behavior. Handler completion means that the specified step ran; it does not imply independent validation. |
| Core claim extraction and claim classification | `core/bsi_engine.py` | Legacy heuristic implementation exists | Review for suitability and known limitations before reuse. It is not evidence verification and must not silently become the v3.5 authority. |
| Manifest / Latent / Meta, assumptions and structural analysis | `core/bsi_engine.py`; `core/bsi_v35_execution.py` | Legacy extractors are reused as candidate inputs; full structural analysis and assumption excavation are model-assisted handlers | Keep legacy heuristics as candidates only; model output remains draft and unverified until source review. |
| Evidence retrieval and claim-level support/conflict signals | `core/rag/*`; `core/bsi_pipeline.py` | Experimental RAG components and legacy integration exist | Inspect retrieval backend, source metadata, failure behavior, and tests. RAG output is a lead/signal, not proof by itself. |
| Counterevidence and competing interpretations | `core/bsi_v35_execution.py` | Dedicated auditor/analyst handlers wired; require retrieval leads or supplied source materials | Treat their outputs as model-assisted analysis; retain unresolved gaps and source references. |
| EIG assessment | Legacy heuristics in `core/bsi_engine.py` / `core/bsi_pipeline.py`; formal v3.5 calculator in `core/bsi_scoring_v35.py` | Two distinct paths; v3.5 calculator requires explicit inputs | Do not route legacy heuristic outputs into v3.5 scoring without a documented equivalence review and explicit approval. |
| ECC v2.0 | `core/bsi_scoring_v35.py` | Formal calculation exists in v3.5 runtime; legacy `core/bsi_pipeline.py` uses a different simplified calculation | Use the v3.5 ECC implementation for v3.5 scoring. Keep legacy behavior clearly version-scoped; do not blend formulas. |
| REIG on Draft Analysis | `core/bsi_v35_execution.py`; `core/bsi_scoring_v35.py`; `core/bsi_v35_runtime.py` | REIG model-assisted audit is connected to Draft Analysis; correction now reruns REIG on the corrected draft | Preserve the Draft Analysis boundary and block scoring when any REIG dimension lacks an evidence basis. |
| Explicit-input scoring API and MCP contract | `api/routes/bsi.py`, `api/mcp.py`, `core/bsi_v35_runtime.py` | Connected to v3.5 calculator; raw-text-only scoring is rejected | Keep this safety boundary. API acceptance proves scoring integration, not autonomous analysis completion. |
| Model-provider neutrality | `core/model_contracts.py`, `core/model_adapters.py`, `core/local_model_adapters.py` | Adapter contracts and generic transports implemented | Keep adapters behind the contract; add capability conformance probes before trusting declared capabilities. |
| Completion Gate / fail-closed lifecycle | `core/execution_contract.py`, `core/execution_orchestrator.py`, `core/bsi_v35_execution.py` | Connected to concrete handlers; explicit stage blockers, unresolved T8, missing source verification, and unresolved correction block completion | Preserve fail-closed behavior; scoring has an additional evidence-basis gate. |
| Execution trace, provenance, verification state and persistence | `StageRecord` / `ExecutionTrace` hold trace fields in memory | Partial; no durable persistence established by this review | Do not claim persistence. Define/locate the existing persistence boundary before implementing one. |
| Final re-read and output firewall | Master Prompt / Architecture; `core/bsi_v35_execution.py` | Auditor final re-read is wired; completion requires a passing result | Do not describe model self-audit as independent validation. |
| Validation | `.github/workflows/bsi-v35-validation.yml` and repository tests | CI passed on reviewed commit | The workflow verifies compilation and test suite, not real external retrieval or a full autonomous run. |

## Confirmed corrections and validation

- The execution contract includes `execution_status` as a mandatory lifecycle stage.
- The correction/reanalysis stage is marked `BLOCKED` when the bounded correction loop ends with unresolved defects.
- T8 detection is accumulated from stage outputs rather than being restricted to task intake.
- Tests cover missing handlers, successful orchestration with test handlers, unresolved T8, bounded correction, and correction-limit blocking.
- Integration is exercised by `tests/test_bsi_v35_execution.py` using controlled model fixtures; this does not validate live provider quality or real-world source coverage.
- Source-level verification requires caller-supplied `source_materials` entries with both `source_ref` and inspected `text`; retrieval snippets alone do not qualify.
- The v3.5 scoring gate now requires explicit D1-D7 evidence mappings, per-component EIG evidence, ECC basis, and per-dimension REIG evidence. Missing basis blocks scoring.
- Correction now re-runs REIG on the corrected draft rather than reusing the pre-correction audit.
- The local Ollama adapter honors the requested output-token limit.

## Remaining integration and deployment constraints

1. Configure analyst and auditor roles using either local Ollama (`BSI_OLLAMA_MODEL`, or role-specific model names) or an explicitly configured OpenAI-compatible endpoint.
2. Supply inspected source materials as `source_materials: [{ "source_ref": "...", "text": "..." }]`; the API does not fetch/open arbitrary URLs as source verification.
3. Supply explicit D1-D7 values and their evidence mapping as `dimension_scores` and `dimension_score_evidence`; the pipeline never invents these values.
4. Treat the RAG backend as experimental keyword retrieval. It does not establish source-level verification and can return no source references.
5. Durable execution-trace persistence, independent human/third-party validation, live-provider conformance probes, and broad retrieval coverage are not implemented by this integration.
6. Keep legacy v3.4.1/v3.4.2 heuristic scoring separate from v3.5 explicit-input scoring.
7. Keep PR Draft and unmerged pending review; do not merge without explicit authorization.

## Non-goals for this pass

- No new BSI criteria, weights, scoring formulas, ontology, or parallel analytical framework.
- No new duplicate claim-extraction, RAG, EIG, ECC, or REIG implementation.
- No automatic score generation from model prose.
- No claim of independent validation, durable persistence, or unrestricted autonomous operation. The guarded execution endpoint is model-assisted and requires explicit source materials and evidence-backed scoring inputs.


## Prompt-First Portability Review (2026-10-31)

| Requirement | Previous state | Corrected target | Status |
|---|---|---|---|
| Direct execution from one prompt | Master Prompt referenced external repository documents and a separate Execution Architecture file | Embedded normative snapshots (including Execution Architecture, architectural invariants, output contract, specification matrix, CORE_BEHMANESH, BIO, EIG, ECC, REIG, SOP v3.4.2, and hybrid calculation formula) and a self-contained Prompt-Only Execution Contract in `MASTER_PROMPT_BSI_v3.5.md` | Implemented in prompt artifact; independent-interface portability test remains pending |
| Runtime dependency | `core/prompt_registry.py` labelled execution as `external-llm-required`; API request required configured model roles | Runtime/API/adapters are optional automation paths; direct prompt execution does not invoke them | Registry metadata corrected; runtime remains optional |
| External verification | Runtime requires inspected source materials for source-level verification | Prompt-only mode distinguishes supplied-text analysis from external verification; absent tools do not fabricate verification or invalidate bounded analysis | Explicitly specified |
| Numerical scoring | Explicit evidence-backed inputs required by runtime | Prompt-only and runtime both prohibit invented scores; if score inputs/bases cannot be established, numerical total is not calculable | Preserved |
| Execution trace/persistence | Runtime trace is in-memory; durable persistence not established | No prompt-only claim of machine trace persistence; substantive limitations only in final output | Preserved |

### Scope and validation boundary

This change restores the v3.4.2-style portability property: the complete prompt can be copied into a capable LLM chat and executed without a BSI service or API. It does not promise identical output across models, external source access without tools, independent validation, or durable trace persistence. Existing API/Ollama/provider adapters remain optional and are not removed. No BSI criteria, weights, ontology, EIG/ECC/REIG definitions, or scoring authority are changed.

### Required validation

- Check the canonical `/20` EIG penalty lock in the prompt.
- Check that prompt-only execution contract explicitly says API/runtime are not prerequisites.
- Check that all required normative reference documents are embedded in the prompt, including SOP v3.4.2 and the hybrid calculation formula.
- Run the existing repository test suite and prompt-package tests.
- Perform a manual portability test by pasting only the Master Prompt plus a target text into at least one independent LLM interface without repository/API access; record the model/interface and limitations before claiming this test passed.
