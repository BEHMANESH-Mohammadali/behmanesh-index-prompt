# BSI v3.5 — Analytical Output Contract
## Layer C Specification — v3.5

**Status:** Canonical  
**Layer:** C — Analytical Output Contract  
**Version:** 3.5  
**Scope:** BSI analytical output only

---

## 1. Purpose

Layer C defines the contract for the substantive analytical output produced by BSI v3.5.

It specifies:

- the required organization of substantive findings;
- the required analytical components;
- the communication of uncertainty;
- the representation of material limitations affecting result reliability;
- the substantive effects of execution that materially affect the analytical result;
- the required presentation sequence of the completed analysis.

Layer C does not redefine the BSI Knowledge Core, its ontology, criteria, weights, scoring logic, EIG, ECC, or REIG.

Layer C does not define machine-observable execution state. Machine-observable execution state belongs to Layer D.

---

## 2. Canonical Output Sequence

The final BSI analysis MUST contain the following substantive sequence:

1. Analysis Title and Source Identification
2. Executive Summary
3. Seven Main BSI Criteria (D1–D7)
4. CreativeValueAdd
5. Deep Structural Analysis (Manifest / Latent / Meta)
6. Final Synthesis
7. D2 Temporal Evidence Presentation (where D2 is applicable)
8. Final BSI Score

The sequence above is the authoritative presentation order specified by BSI v3.5.

Uncertainty (§15) and Material Limitations (§16) are not a fixed step in this sequence; they are cross-cutting requirements that MUST be represented wherever, within the sequence above, they materially affect interpretation, confidence, or reliability.

EIG, ECC, and REIG are not independent items in this sequence either. Per the Execution-to-Output Firewall (DHR-0007), their substantive effects are integrated into the items above — primarily into Deep Structural Analysis and Final Synthesis — rather than presented as standalone procedural reports. §8–§11 below specify what each mechanism contributes to those items and what remains Layer-D-only.

Draft Analysis is an internal Layer B working object, not a Layer C output component, and never appears as a numbered item in this sequence (see §10).

---

## 3. Analysis Title and Source Identification

The analysis MUST identify the analyzed article, document, or intellectual artifact and provide sufficient bibliographic or source information.

---

## 4. Executive Summary

The Executive Summary MUST contain:

- Executive Summary;
- Core Claim;
- overall BSI score.

---

## 5. Seven Main BSI Criteria

The analysis MUST provide all seven official BSI criteria.

For each criterion, report:

- official criterion name;
- score;
- evidence-based justification;
- relevant structural findings;
- uncertainty or limitation where applicable.

The official criteria MUST NOT be:

- renamed;
- merged;
- reordered;
- reweighted;
- replaced.

Official BSI weighting and scoring logic MUST be preserved.

---

## 6. CreativeValueAdd

CreativeValueAdd MUST be evaluated according to the official BIO v1.0 definition and all three official internal subcriteria:

- Epistemic Gap Targeting — 35%;
- Combinatorial Synthesis — 40%;
- Generative Capacity — 25%.

The official BIO ordering is authoritative for presentation.

The operational calculation order must not be treated as a redefinition of the ontology.

---

## 7. Deep Structural Analysis

The substantive structural analysis MUST contain all three analytical layers:

### 7.1 Manifest Layer

Identify:

- explicit claims;
- structures;
- arguments;
- stated mechanisms;
- evidence;
- assumptions;
- observable patterns.

### 7.2 Latent Layer

Identify, where supported:

- underlying structures;
- hidden mechanisms;
- recurring patterns;
- implicit assumptions;
- dependencies;
- feedback relationships;
- tensions;
- structural constraints.

The Latent Layer MUST receive substantial analytical attention.

### 7.3 Meta Layer

Analyze higher-order:

- epistemic patterns;
- methodological patterns;
- structural patterns;
- interpretive patterns.

Where justified, also identify:

- mechanisms;
- feedback loops;
- leverage points;
- structural dependencies;
- contradictions or tensions.

Hypotheses and interpretations MUST NOT be presented as established facts.

---

## 8. EIG — Substantive Integration

EIG MUST be performed according to the formal EIG architecture (Layer A/B).

Its substantive output enters Layer C only as integrated findings, not as a standalone "EIG Analysis" report:

- material epistemic gaps enter the relevant D-criterion justification (§5) and/or the Deep Structural Analysis (§7);
- gaps materially affecting confidence enter Uncertainty and Material Limitations;
- gaps materially affecting the final score enter Final BSI Score (§14) as a disclosed input, not as an invented narrative.

Wherever EIG's findings are reflected, the analysis MUST distinguish:

- what is supported;
- what is inferred;
- what remains uncertain;
- what is insufficiently evidenced;
- what assumptions materially affect the analysis.

EIG values or conclusions MUST NOT be invented merely to complete an output template.

Raw EIG gap values, the applicable gap weights, and the resulting EIG_avg / EIG_penalty are score-traceability inputs. They belong to Layer D (Audit / Machine Trace), not to a Layer C narrative section. Layer C may state that an EIG-driven adjustment occurred and its substantive consequence, without reproducing the full gap-by-gap computation as reader-facing content.

---

## 9. ECC — Substantive Integration

ECC v2.0 MUST be performed according to the official ECC architecture. ECC is a calibration subsystem of EIG and does not replace EIG.

Its substantive output enters Layer C through claim-level calibration, not as a standalone "ECC Analysis" report. The analysis MUST distinguish:

- FACT;
- INFERENCE;
- HYPOTHESIS;
- SPECULATION.

Where these distinctions cannot be adequately established, the required state is:

**LOW CONFIDENCE ASSESSMENT**

ECC's effect on specific claims MUST be reflected through this labeling and through Uncertainty, wherever it materially changes how a finding should be read.

The numeric calibration layers (ECC-C, ECC-E, ECC-M, ECC-L) and ECC_Total are Layer D audit values, used for score traceability. They are not required Layer C reader-facing content and MUST NOT be invented when required evidence is unavailable.

---

## 10. Draft Analysis — Internal Working Object

The Draft Analysis is a Layer B execution artifact: the working representation that REIG audits before Final Synthesis is produced.

The Draft Analysis is NOT the source article or target text, and it is NOT a Layer C output component. It MUST NOT appear as a numbered section, header, or reader-facing block in the final analysis.

Where auditability requires recording that a draft stage occurred, that record (e.g. a state marker) belongs to Layer D, not Layer C.

---

## 11. REIG — Correction Integration

REIG MUST be applied to the Draft Analysis as a repair mechanism:

`Draft Analysis → REIG → Correction → Re-analysis → Final Validation`

REIG's substantive output enters Layer C only as corrected analytical content:

- where REIG identifies a material weakness, the correction MUST be reflected directly in the relevant D-criterion justification (§5), the Deep Structural Analysis (§7), or Final Synthesis (§12) — not reported as a separate audit finding;
- where REIG finds no material issue, no "REIG Report" section is produced.

The five official REIG dimensions remain:

1. Evidence Consistency Check — ERG
2. Method Consistency Check — MRG
3. Confidence Consistency Check — CRG
4. Assumption Consistency Check — ARG
5. Fairness Consistency Check — FRG

Per-dimension REIG scores and findings, and the four legacy audit dimensions where used as additional diagnostics, are Layer D audit-trace content. They MUST NOT replace the five official dimensions at the Layer D level, and they MUST NOT be surfaced as a standalone Layer C report.

If REIG required correction, Final Synthesis (§12) MUST disclose the material consequence in substantive terms (e.g. "an inference regarding X was narrowed because the supporting evidence did not establish generalization") without narrating the audit procedure itself.

---

## 12. Final Synthesis

After REIG, the analysis MUST produce the final integrated assessment.

It MUST include:

- overall structural synthesis;
- strengths;
- weaknesses;
- improvement recommendations;
- material uncertainty;
- evidence limitations;
- analytical limitations;
- where REIG required correction (§11), the corrected conclusion and its substantive basis.

Recommendations MUST remain evidence-proportional and MUST NOT be presented as established facts when they are inferential.

---

## 13. D2 Temporal Evidence Presentation

When D2 is applicable, the analytical output MUST make the temporal evidence mapping inspectable.

Where sufficient evidence exists, report the D2 evidence through the three overlapping horizons:

1. Short-term
2. Mid-term
3. Long-term

The presentation MUST NOT imply that these horizons are mutually exclusive data partitions.

Where relevant, explicitly identify:
- evidence present in multiple horizons;
- continuity across horizons;
- revisions or developmental changes;
- evidence limitations for any horizon;
- whether a conclusion concerns internal coherence, referential continuity, developmental continuity, or broader longitudinal persistence.

A single present-time datum may appear in more than one horizon when it falls within the corresponding temporal windows.

This presentation requirement does not introduce a new D2 score, weight, criterion, or scoring layer.

---

## 14. Final BSI Score

The final BSI score MUST be calculated using the official BSI scoring logic and official BIO v1.0 weights.

Layer C does not redefine or alter the scoring specification.

If the applicable calculation mode cannot be established from authoritative BSI materials, the limitation MUST be disclosed rather than an alternative being silently selected.

If a required scoring input cannot be defensibly established, the limitation MUST be disclosed rather than a value being invented.

---

## 15. Uncertainty

Uncertainty MUST be explicitly represented wherever it materially affects interpretation, confidence, scoring, or conclusion.

The analysis MUST distinguish evidence from interpretation and MUST calibrate confidence to available support.

Unsupported certainty MUST NOT be introduced merely to complete the output structure.

---

## 16. Material Limitations

The completed analysis MUST disclose material:

- evidence limitations;
- analytical limitations;
- uncertainty affecting interpretation or reliability;
- unresolved material execution requirements that affect the analytical result.

Absence of a limitation MUST NOT be inferred merely because a corresponding field is not populated.

---

## 17. Substantive Effects of Execution

Execution requirements belong primarily to Layer B.

However, when execution produces a substantive effect on the analytical result—such as a material limitation in evidence, verification, retrieval, uncertainty, or completion—that effect MUST enter the Layer C analytical result in the appropriate substantive section.

Procedural execution narration MUST NOT be inserted into the analytical result merely to demonstrate that execution occurred.

Execution effort MUST contribute to analytical value through:

- coverage;
- depth;
- verification;
- synthesis;
- inferential reliability;
- uncertainty calibration.

It MUST NOT be converted into procedural verbosity, redundant narration, or unsupported claims.

---

## 18. Boundary with Layer D

Layer C MUST NOT become a machine-execution trace.

The following distinction is preserved:

**Claimed ≠ Observed ≠ Independently Validated**

Execution status, machine-observable state, retrieval/escalation state, verification state, and other audit-trace information belong to Layer D.

A rich execution-status report MUST NOT substitute for the mandatory BSI analytical output.

---

## 19. Analytical Output Completeness

Completion of the analytical output requires the presence and internal coherence of all mandatory substantive components required by BSI v3.5, including:

- all seven BSI criteria;
- CreativeValueAdd and all three official subcriteria;
- Manifest / Latent / Meta analysis;
- the substantive integration of EIG findings (§8);
- the substantive integration of ECC calibration (§9);
- the substantive integration of REIG corrections, where applicable (§11);
- Final Synthesis;
- D2 temporal evidence presentation, where D2 is applicable;
- uncertainty and limitations.

Completion does NOT require, and MUST NOT be demonstrated by, standalone EIG, ECC, Draft, or REIG report sections.

Execution completeness alone does not authorize analytical completion. The converse also holds: the presence of separate procedural report sections does not substitute for substantive analytical completeness.

If a mandatory analytical component is missing, the analysis MUST NOT be declared complete.

---

## 20. Non-Modification Rule

This Layer C specification MUST NOT:

- introduce a new BSI criterion;
- introduce an independent scoring dimension;
- alter an official weight;
- redefine an official BSI construct;
- redefine EIG;
- redefine ECC;
- redefine REIG;
- convert execution controls into analytical criteria;
- convert audit trace into substantive analysis.

Any future change to Layer C MUST be explicitly versioned and documented.

---

## 21. Canonical Source Basis

This specification is derived from the existing BSI v3.5 authoritative materials, including:

- `MASTER_PROMPT_BSI_v3.5.md`
- `ARCHITECTURAL_INVARIANTS_BSI_v3.5.md`
- the canonical BSI/EIG/ECC/REIG specifications referenced by those materials.

Legacy v3.4.2 output structures are not automatically inherited as Layer C v3.5 schema elements.

