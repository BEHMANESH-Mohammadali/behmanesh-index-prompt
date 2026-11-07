# BSI 3.5 — Analytical Output Presentation Companion
# SOP Output Format & Presentation

**Version:** 1.2
**Compatibility note:** The repository filename retains the historical `v1.1` label; the document content is version 1.2.
**Status:** Mandatory companion guidance for BSI v3.5 analytical outputs
**Architectural role:** Presentation guidance subordinate to Layer C
**Canonical authority:** `docs/specification/ANALYTICAL_OUTPUT_CONTRACT_LAYERC_v3.5.md`
**Execution boundary:** `MASTER_PROMPT_BSI_v3.5.md` + `BSI_3.5_Execution_Architecture.md`

## 1. Governing Principle

The final BSI v3.5 response is a substantive analytical result, not a report of the process used to produce it. Layer C is authoritative for the mandatory sequence, required components, and boundaries. This SOP supplies presentation guidance only; if any wording here conflicts with Layer C, Layer C governs.

**Execution-to-Output Firewall:** Internal effort, retrieval, verification, counterevidence search, Assumption Excavation, EIG, ECC, REIG, and completion controls must improve analytical coverage, depth, synthesis, reliability, and uncertainty calibration. They must not be exposed as workflow narration, checklist dumps, machine traces, or artificial verbosity.

## 2. Canonical Output Sequence

Follow the exact Layer C sequence:
1. Analysis Title and Source Identification
2. Executive Summary
3. Seven Main BSI Criteria (D1–D7)
4. CreativeValueAdd
5. Deep Structural Analysis (Manifest / Latent / Meta)
6. Final Synthesis
7. D2 Temporal Evidence Presentation, where D2 is applicable
8. Final BSI Score

Uncertainty and material limitations are cross-cutting requirements; represent them wherever they materially affect interpretation, confidence, scoring, or reliability.

## 3. Source Identification and Core Claim

Identify the analyzed artifact with sufficient source information. State the Core Claim in one sentence in the Executive Summary. If no defensible central claim can be extracted, report that as a finding; do not invent one.

## 4. Executive Summary

Concisely communicate the central claim, principal structural findings, consequential strengths and weaknesses, material uncertainty or limitations, and overall BSI result only if defensibly calculated. Do not include unsupported praise or procedural completion narration.

## 5. Seven Main BSI Criteria

Report all seven official criteria in canonical names and order, preserving their weights:

| ID | Criterion | Weight |
|---|---|---:|
| D1 | ConditionalDepth | 0.22 |
| D2 | LongitudinalCoherence | 0.18 |
| D3 | AuthenticEthicalLayer | 0.18 |
| D4 | CreativeValueAdd | 0.17 |
| D5 | StrategicDepth | 0.12 |
| D6 | InterdisciplinaryBreadth | 0.08 |
| D7 | AntiPerformativeDrift | 0.05 |

For each criterion, provide a defensible score, evidence-based justification, structural findings, and material uncertainty. A score must not substitute for reasoning.

## 6. CreativeValueAdd

Preserve the official BIO v1.0 subcriteria and weights:
- **Epistemic Gap Targeting — 35%**
- **Combinatorial Synthesis — 40%**
- **Generative Capacity — 25%**

Explain what the work adds and whether that value-add is supported by identifiable evidence and defensible synthesis. Do not invent subcriteria or weights.

## 7. Deep Structural Analysis

Cover all three layers substantively.

### Manifest
Identify explicit claims, propositions, arguments, evidence, stated mechanisms, and relationships among them. Show how principal elements connect to the Core Claim.

### Latent
Examine material assumptions, hidden dependencies, mechanisms, feedback loops, blind spots, tensions, contradictions, and boundary conditions. Include Assumption Excavation findings only when supported by evidence.

### Meta
Examine higher-order epistemic and methodological patterns, the relation between claims, evidence, method, and conclusions, and relevant value or worldview commitments where evidence permits. Claims about broader intellectual structure or longitudinal development require suitable evidence across time and context.

Themes, mechanisms, dependencies, feedback loops, leverage points, and interactions among findings belong within the three-layer analysis and Final Synthesis. Do not impose arbitrary rankings or a fixed number of themes.

## 8. EIG, ECC, and REIG — Substantive Integration

EIG, ECC, and REIG are **not standalone items** in the canonical Layer C output sequence.

- **EIG:** Its substantive findings inform structural analysis and Final Synthesis. Keep the four gaps distinct; do not count one defect repeatedly without distinct evidence. Raw EIG values and audit traceability belong to Layer D where specified. The BSI penalty uses `EIG_penalty = EIG_avg / 20`; this SOP does not redefine EIG scales, gap weights, or scoring logic.
- **ECC:** Its substantive effect is reflected in calibrated confidence, claim strength, uncertainty, and conclusions. Do not expose a separate procedural report merely to show that ECC ran.
- **REIG:** Required corrections must be reflected in the corrected substantive analysis and conclusion. Draft Analysis and the REIG correction loop remain internal execution objects.

Do not add separate EIG, ECC, Draft Analysis, or REIG report sections as proof of execution.

## 9. Evidence and Epistemic Classification

Keep evidence distinct from interpretation. Use labels where they materially clarify claim status:
- **FACT:** directly supported by available evidence.
- **INFERENCE:** a reasoned conclusion drawn from identified evidence.
- **HYPOTHESIS:** a possible explanation requiring further evidence.
- **SPECULATION:** an insufficiently supported possibility; never present it as established.

Distinguish source claims, observed evidence, independent verification, and analytical inference. External verification should be reflected through evidence or a material limitation, not a search log.

## 10. D2 and Temporal Evidence

When D2 is applicable, present short-, mid-, and long-term evidence as overlapping analytical horizons, not mutually exclusive partitions or independent scoring weights.

For a single content item, assess internal coherence where possible; do not infer historical persistence, trajectory, or longitudinal development; do not treat absence of longitudinal evidence as inconsistency; state the limitation rather than inventing a longitudinal conclusion.

## 11. Final Synthesis and Score

Integrate principal structural findings, strengths, weaknesses, material EIG/ECC/REIG effects, and relevant limitations into one coherent assessment. Do not simply repeat earlier sections.

Calculate the final BSI score only through authoritative scoring logic and official BIO v1.0 weights. If the calculation mode or a required input cannot be established defensibly, disclose the limitation rather than silently substituting a formula or inventing a value.

## 12. Uncertainty and Material Limitations

Disclose limitations that materially affect interpretation, confidence, scoring, or reliability, including evidence gaps, verification limits, unavailable longitudinal evidence, ambiguous attribution, and credible competing interpretations. Missing data is not automatically evidence of weakness or inconsistency.

## 13. Internal-Only Execution Material

Execution lifecycle, effort calibration, tool logs, retrieval/escalation state, PASS/FAIL checklists, Draft Analysis, REIG workflow, Completion Gate, and machine/audit trace normally remain internal. If an execution limitation materially affects the result, report its substantive effect as uncertainty or a material limitation. Do not claim a process step occurred unless it actually did.

## 14. Style and Quality

- Use clear, professional Persian as the default; retain official BSI terminology where useful.
- Let analytical need determine length.
- Avoid false precision, unsupported certainty, repetitive criteria descriptions, and artificial verbosity.
- Ground important findings in identifiable evidence.
- Preserve the distinction between observation, inference, hypothesis, and speculation.
