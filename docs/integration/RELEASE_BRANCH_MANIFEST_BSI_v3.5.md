# BSI v3.5 Release Branch — Integration Manifest

**Branch:** `release/bsi-v3.5`  
**Status:** Integrated release candidate; validation and independent portability review remain required.  
**Integration baseline:** `feat/d2-single-input-scoring` via `integration/bsi-v3.5-reconciled`.

## Included branch histories

- `feat/bsi-v3.5-scoring-engine` → `feat/model-agnostic-execution-adapters` → `feat/d2-single-input-scoring`: cumulative technical implementation lineage; the D2 branch is the integration baseline.
- `migration/bsi-v3.5-canonical`: merged as a history parent. Where its files conflicted with the newer D2 baseline, the integration tree was retained because it contains the more complete Prompt-First Master Prompt, updated formula, scoring/runtime routes, canonical ECC resolution, and single-input D2 safeguards.
- `conceptual-refactor-volume1`: merged as a history parent; new governance, publication, theory, and monograph documents absent from the technical baseline are included under their existing `docs/` namespaces. Existing runtime and Knowledge-Core files were not overwritten by this research branch.

## Canonical resolutions retained

- EIG penalty: `EIG_penalty = EIG_avg / 20`; EIG_avg remains on 0–10. The older `/10` mapping in the migration/develop line is superseded for v3.5 implementation. Provenance is preserved in branch history.
- ECC v2.0: `ECC_Total = mean(|EG|, |MG|, |LG|)`; signed component gaps and directions remain visible.
- Single-input D2: internal coherence only; no longitudinal trajectory, persistence, continuity, or historical development is inferred from one item.
- D2-SI: proposed constrained operationalization; not a replacement for canonical longitudinal D2 and not an empirically calibrated rubric.
- Nonlinear activation threshold: unresolved; no threshold is invented.
- Prompt-First execution remains standalone; runtime and provider adapters are optional automation.
- Self-audit, RAG leads, and model-generated text are not independent validation or source evidence.

## Deliberate conflict resolution

The migration branch's Master Prompt is substantially shorter and less complete than the D2 baseline's embedded Prompt-First package; its API entry points also predate the execution/scoring runtime integration. Its formula and canonical matrix retain the superseded EIG `/10` mapping and unresolved ECC status. Therefore those conflicting files were not copied over the D2 baseline. The more complete D2 versions are retained.

## Research/documentation boundary

The Interpretation Drift monograph and associated governance materials are documentation/research artifacts. Their presence in the release tree does not mean future-work proposals are implemented, that the monograph's empirical validation has been completed, or that those documents redefine BSI criteria, weights, or runtime behavior.

## Archive boundary

The branch `archive/main-as-bsi-v3.4.2` preserves the exact prior `main` head snapshot. That snapshot is frozen as requested by the project owner; it is not rewritten or sanitized. The snapshot contains a file named `MASTER_PROMPT_BSI_v3.5.md`, so its archival label denotes the owner's requested main-branch snapshot, not a claim that every file inside is a pure v3.4.2 artifact. The earlier `archive/bsi-v3.4.2-original` branch separately preserves the historical 2026-06-24 state.

## Validation status and limitations

- Repository tests and CI must be run against this release branch head before promotion.
- Independent-interface Prompt-Only portability test remains outstanding.
- Durable execution-trace persistence and independent human/third-party validation are not claimed.
- This branch is not yet promoted to `main`; no existing branch was deleted or force-updated.

## Main-branch test-import reconciliation (2026-11-05)

The `main` branch advanced by one commit after the release candidate was assembled. That commit added `tests/test_bsi_scoring_v35.py` with the earlier ECC expectation (`NOT_CALCULATED_SPECIFICATION_CONFLICT`). The release candidate already contains an expanded version of this test module covering ECC v2.0 absolute-gap aggregation with signed direction preservation, D2-SI arithmetic, and single-content D2 evidence constraints. The release version is therefore retained as the conflict resolution; the older test file is not copied over it. The merge commit records both branch histories while preserving the release tree, and the full test suite must be rerun on the resulting PR head before promotion.


## Final re-read readiness hardening (2026-11-05)

Maintenance PR #10 was merged after its pull-request CI passed. The `execution_status` handler now requires the final-reread result to contain literal boolean `passed=true` and literal boolean `ready_for_final=true`. Missing readiness, false readiness, and non-boolean pass values block completion. Regression tests cover these cases and the valid path.

Post-merge CI on release commit `cfc64fe5ed7875d1dcfc54731ade928ee6a853b6` passed (workflow runs #146 push and #147 pull_request), including Python compilation and the full pytest suite. This remains repository-level automated validation, not independent Prompt-Only portability acceptance or third-party review.


## Addendum — Assumption Excavation protocol integration (2026-11-10)

PR #15 proposes the complete Assumption Excavation Protocol v1.1 integration. The full normative source is embedded in `MASTER_PROMPT_BSI_v3.5.md`, separately loaded by `core/prompt_registry.py`, and pinned in `docs/integration/BSI_V35_PROMPT_PACKAGE_INTEGRITY.json`. The optional runtime now treats lexical candidates as leads and blocks completion when the four-step output schema is incomplete. PR CI run #166 passed Python compilation and the full test suite (78 passed, 0 failed; 3 non-blocking deprecation warnings). This evidence is limited to repository CI; independent Prompt-Only portability and inter-rater reliability are not claimed. PR #15 remains unmerged; release branch, tags, and release status are unchanged.


## Addendum — Final Compliance boundary clarification (2026-11-10)

- The Master Prompt retains the official SOP v3.4.2 + BIO v1.0 compliance statement.
- A new normative note clarifies that SOP v3.4.2 remains methodological lineage, while the v3.5 Layer C contract controls the final presentation sequence; legacy v3.4.2 JSON output structures are not automatically inherited.
- The note explicitly prohibits using the template to imply source verification, software execution, independent validation, or durable trace persistence unless actually performed.
- This is a prompt-text change on the readiness-audit branch only. It has not been merged into `release/bsi-v3.5`, and no tag/release has been created.
- CI, package-integrity hashes, and the independent Prompt-Only acceptance test must be rerun against the exact final candidate before release readiness can be claimed.
