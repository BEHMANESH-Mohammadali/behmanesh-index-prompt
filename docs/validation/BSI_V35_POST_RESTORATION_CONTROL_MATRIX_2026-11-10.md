# BSI v3.5 — Post-Restoration Control Matrix

**Review date:** 2026-11-10  
**Reviewed branch:** `work/bsi-v3.5-minimal-audit-fixes`  
**Reviewed tree after guarded-execution integration:** `c3879ee042837eff6f933421ecb8411cd02370f2`  
**Automated test commit:** `c3879ee042837eff6f933421ecb8411cd02370f2`  
**Scope:** Canonical BSI v3.5 prompt package, scoring/runtime, execution lifecycle, documentation consistency, package integrity, and repository test evidence.

This is a control review, not a claim that every file in the repository was read line by line, that the framework has independent empirical validation, or that a successful test suite proves the truth or quality of supplied assessments.

## Status legend

- **PASS** — inspected evidence and/or automated test supports the control.
- **PARTIAL** — some implementation exists, but coverage or end-to-end behavior is incomplete.
- **OPEN** — a real conflict or decision remains; it is not silently resolved by this review.
- **NOT CLAIMED** — the property requires external or empirical evidence not produced here.

## A. Identity, scope, and protected boundaries

| ID | Control requirement | Evidence checked | Status | Finding |
|---|---|---|---|---|
| C-01 | Keep BSI core separate from benchmark and benchmark-results repositories. | Root README related-repository section; repository scope and changed-file comparison. | PASS | This work changes only `behmanesh-index-prompt`. No benchmark or results repository was modified. |
| C-02 | Preserve the BSI Knowledge Core, seven official criteria, official names, ordering, and weights. | Master Prompt §§1–2; Architectural Invariants; `BSI_WEIGHTS`; scoring tests. | PASS | D1–D7 weights remain 0.22/0.18/0.18/0.17/0.12/0.08/0.05; sum = 1.00. No new criterion or official weight was introduced. |
| C-03 | Keep Execution Architecture from redefining analytical ontology or scoring authority. | Master Prompt, Execution Architecture, Architectural Invariants, Layer C contract. | PASS | Layer A/B/C/D responsibilities remain distinct. |
| C-04 | Keep v3.4.2 lineage artifacts distinct from the canonical v3.5 framework and runtime. | README, Master Prompt, prompt registry. | PASS | README identifies `core/bsi_pipeline.py` as a v3.4.2 lineage artifact, not the v3.5 scoring runtime. |
| C-05 | Preserve source/evidence distinctions and separate direct statements, historical reports, observations, inferences, and hypotheses. | Master Prompt output requirements; execution analysis output schema; Layer C uncertainty and limitation requirements. | PARTIAL | The distinctions are explicitly represented in the analysis contract and model output schema. The presence of fields does not independently validate their correct use in every generated analysis. |

## B. D2 and D2-SI controls

| ID | Control requirement | Evidence checked | Status | Finding |
|---|---|---|---|---|
| C-06 | Preserve official D2 identity and weight 0.18. | Master Prompt, canonical matrix, formula, `BSI_WEIGHTS`, scoring tests. | PASS | D2 remains LongitudinalCoherence at 0.18. |
| C-07 | Retain a numeric single-content D2-SI path when explicitly supplied and authorized, without inferring it from content scope. | `calculate_d2_si()`, `d2_si_to_normalized_score()`, `run_v35_scoring()`, guarded execution tests. | PASS | The model-assisted path forwards only an explicit `d2_si_scores` payload with dimension-specific evidence. The deterministic runtime normalizes it and checks equality with the supplied D2 input. Omission preserves the 31 October internal-coherence-only basis. |
| C-08 | Preserve the proposed D2-SI subdimension weights and scale. | Master Prompt, canonical matrix, hybrid formula, scoring tests. | PASS | I/D/C/R = 0.40/0.30/0.20/0.10; scores are 0–4; applicable dimensions are renormalized only for genuine N/A. |
| C-09 | Never convert N/A-only, insufficient-evidence, or not-assessed states into fabricated numeric zeroes. | `calculate_d2_si()`, normalization guard, tests for non-score states and all-N/A. | PASS | Non-calculated states return no numeric D2-SI and cannot be normalized. |
| C-10 | Prevent D2-SI from being mistaken for proof of longitudinal continuity, persistence, or historical development. | Master Prompt D2-SI scope language; formula and matrix provenance language; runtime scope check. | PASS | D2-SI is explicitly a constrained single-input operationalization, not BIO v1.0's canonical longitudinal D2 formula. It is rejected for `longitudinal_corpus`. |
| C-11 | Preserve the 31 October single-content D2 definition while recording the later D2-SI explanation without superseding it. | Canonical matrix single-content resolution (2026-10-31); owner clarification (2026-11-10); runtime basis validation and execution tests. | PASS | The 31 October rule remains governing: single-content D2 basis is `internal_coherence_only`. The later explanation is additive context about the purpose of retaining a defensible numeric D2 result; it does not change the 31 October assessment basis or authorize automatic activation/inference of D2-SI merely because an input is single-content. An explicitly supplied D2-SI payload remains subject to the deterministic runtime's evidence, scope, and normalized-score checks. No longitudinal claim is derived from one content item. |
| C-12 | Align guarded model-assisted execution with deterministic scoring for an explicitly supplied, evidence-backed D2-SI payload. | `core/bsi_v35_execution.py`, `core/bsi_v35_runtime.py`, D2-SI evidence gate, positive and negative execution tests. | PASS | `/bsi/execute` forwards the optional payload only for `single_content`, requires evidence for I/D/C/R, preserves `internal_coherence_only`, and delegates normalization and D2 equality validation to `run_v35_scoring()`. It does not infer D2-SI when the payload is absent. Missing D2-SI-specific evidence blocks scoring when a payload is supplied. |

## C. Epistemic and scoring invariants

| ID | Control requirement | Evidence checked | Status | Finding |
|---|---|---|---|---|
| C-13 | Preserve EIG gap definitions, weights, and approved penalty denominator. | Formula, matrix, `calculate_eig()`, scoring tests. | PASS | EIG_avg remains on 0–10; penalty remains `EIG_avg / 20`, maximum 0.5. Test asserts the approved formula. |
| C-14 | Preserve ECC v2.0 absolute-gap aggregate while retaining signed directions. | ECC source, matrix, calculator, tests. | PASS | ECC_Total remains mean absolute gap; signed component gaps and OVERCLAIM/UNDERCLAIM/ALIGNED directions are retained. |
| C-15 | Keep REIG on Draft Analysis, not the target text; preserve five official dimensions. | Master Prompt, REIG source, execution handlers, scoring tests. | PASS | The model-assisted handler audits Draft Analysis; correction triggers re-audit. |
| C-16 | Do not invent missing scores, evidence, weights, or nonlinear activation thresholds. | Master Prompt, scoring runtime, execution evidence gate, tests. | PASS | Explicit inputs are required; missing dimensions are not imputed or renormalized; calculation mode must be explicit. |
| C-17 | Prevent double-penalty attribution without traceable distinct evidence and rationale. | D2-SI penalty attribution helper and tests; calibration protocol. | PASS | Code checks distinct evidence identifiers and rationale presence. The protocol correctly states that semantic distinctness still requires human review. |

## D. Execution architecture and efficiency

| ID | Control requirement | Evidence checked | Status | Finding |
|---|---|---|---|---|
| C-18 | Maintain exact mandatory handler coverage and keep Completion Gate / Final Answer outside the registry. | `MANDATORY_STAGES`, handler registry, orchestrator, lifecycle crosswalk, regression test. | PASS | The registry has 17 handlers; the test checks exact registry/handler coverage and confirms Completion Gate and Final Answer are not registry stages. |
| C-19 | Keep execution sequential unless a canonical dependency permits otherwise. | `core/execution_orchestrator.py` stage loop. | PASS | The orchestrator iterates over mandatory stages sequentially; no parallel stage execution was introduced. |
| C-20 | Remove only redundant helper recomputation; retain substantive analysis stages and counterfactual controls. | `core/bsi_v35_execution.py`; candidate reuse regression test. | PASS | Core-claim extraction, assumption extraction, and domain detection are computed once at intake and reused downstream. The structural-analysis and assumption-excavation stages remain. |
| C-21 | Preserve fail-closed completion and evidence-basis gates. | Execution contract, orchestrator, execution handlers, existing tests. | PASS | Missing readiness/evidence basis blocks scoring/completion; model self-audit is not described as independent validation. |
| C-22 | Preserve Layer C substantive output versus Layer D machine/audit trace boundary. | Canonical Layer C contract and architectural invariants. | PASS | EIG/ECC/REIG effects enter substantive findings; raw trace values remain audit data. |

## E. Documentation, integrity, and change control

| ID | Control requirement | Evidence checked | Status | Finding |
|---|---|---|---|---|
| C-23 | Keep README runtime claims consistent with actual scoring/runtime behavior. | README and runtime inspection. | PASS | README now describes the optional single-content D2-SI scoring path and explicitly states that `/bsi/execute` does not derive D2-SI automatically. |
| C-24 | Detect canonical prompt-package drift using pinned hashes. | Integrity manifest, `core/prompt_registry.py`, package loading tests. | PASS | All 15 files listed in the manifest matched their expected Git blob SHA at review time; the registry checks manifest version and SHA-256 content hashes. |
| C-25 | Preserve the historical reconciliation record rather than rewriting history. | 2026-11-04 reconciliation, owner clarification (2026-11-10), and this control-matrix addendum. | PASS | Historical documents were left intact. The 31 October rule remains authoritative; the 10 November clarification is recorded additively in this matrix. No historical record was silently overwritten. |
| C-26 | Keep changes confined to the BSI core repository and do not promote without authorization. | GitHub branch refs and compare results. | PASS | Release branch remains at `77dd0834625025929380cdb28671c26bab9ff02b`; pre-audit backup remains at the same SHA. No PR, merge, tag, or benchmark/results change was made. |
| C-27 | Avoid leaving temporary CI configuration changes. | Workflow file comparison after run. | PASS | The temporary `work/**` push trigger was removed after the run; workflow file is back to its original contents. |

## F. Actual automated validation

**GitHub Actions run:** [Run #158 — BSI v3.5 validation](https://github.com/BEHMANESH-Mohammadali/behmanesh-index-prompt/actions/runs/42711754847)  
**Tested commit:** `c3879ee042837eff6f933421ecb8411cd02370f2`  
**Python:** 3.12.16

| Validation step | Actual result |
|---|---|
| Dependency installation | Passed |
| `python -m compileall -q api core` | Passed |
| `python -m pytest -q` | **75 passed, 0 failed** |
| Pytest warnings | 3 deprecation warnings |

Warnings recorded:
1. Starlette deprecation notice concerning use of `httpx` with `starlette.testclient`.
2. `datetime.utcnow()` deprecation in `api/routes/bsi.py`.
3. `datetime.utcnow()` deprecation in `api/mcp.py`.

These warnings did not fail the run. They are maintenance notices, not evidence of a BSI scoring failure, and no unrelated changes were made to address them.

The tested commit includes the guarded D2-SI forwarding implementation and two new execution-path regression tests: one confirms successful forwarding and deterministic normalization; the other confirms that missing dimension-specific D2-SI evidence blocks scoring. After that run, only this control-matrix document and restoration of the workflow's original branch filters were changed; no Python source or test file changed.

## G. Validation not established by this run

| Item | Status | Boundary |
|---|---|---|
| Independent Prompt-Only portability acceptance on another LLM interface | NOT CLAIMED | Not performed by GitHub Actions. |
| Empirical D2-SI inter-rater reliability | NOT CLAIMED | Calibration protocol exists; no independent evaluator dataset or coefficient exists. |
| Live provider/model conformance and real-world source coverage | NOT CLAIMED | Test fixtures and unit/integration tests do not establish live-provider quality. |
| Durable execution-trace persistence | NOT CLAIMED | In-memory trace is not durable persistence. |
| Independent human/third-party validation | NOT CLAIMED | Repository CI is not independent validation. |
| End-to-end D2-SI scoring through `/bsi/execute` | PASS (explicit payload path) | The guarded path forwards explicitly supplied evidence-backed D2-SI and uses the deterministic normalizer/equality check. Automatic inference from raw text remains intentionally unsupported. |

## Overall disposition

- **Automated repository validation:** PASS (73/73 tests; Python compilation passed).
- **Canonical package integrity:** PASS (15/15 pinned files matched).
- **Release branch protection by separation:** PASS (release head unchanged).
- **D2-SI numerical calculation in deterministic runtime:** PASS.
- **D2-SI single-content governance wording:** PASS; 31 October definition remains authoritative, later explanation is additive.
- **D2-SI through guarded `/bsi/execute`:** PASS for explicitly supplied, evidence-backed payloads (C-12).

**No release promotion is authorized by this report.** The guarded execution path is validated for explicitly supplied, evidence-backed D2-SI payloads. Before merging, retain the release/backup separation and review the 42-commit branch diff as a whole; this report does not authorize merge, tag, or release. Do not alter official weights or the BIO v1.0 definition.
