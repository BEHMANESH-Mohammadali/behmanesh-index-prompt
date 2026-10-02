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
5. Deep Structural Analysis
6. EIG Analysis
7. ECC Analysis
8. Draft Analysis
9. REIG — Recursive EIG
10. Final Synthesis
11. Final BSI Score

The sequence above is the authoritative presentation order specified by BSI v3.5.

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

## 8. EIG Analysis

The analysis MUST perform EIG according to the formal EIG architecture.

The output MUST distinguish between:

- what is supported;
- what is inferred;
- what remains uncertain;
- what is insufficiently evidenced;
- what assumptions materially affect the analysis.

EIG values or conclusions MUST NOT be invented merely to complete an output template.

---

## 9. ECC Analysis

The analysis MUST perform ECC v2.0 according to the official ECC architecture.

ECC is a calibration subsystem of EIG and does not replace EIG.

The analysis MUST distinguish:

- FACT;
- INFERENCE;
- HYPOTHESIS;
- SPECULATION.

Where these distinctions cannot be adequately established, the required state is:

**LOW CONFIDENCE ASSESSMENT**

Where applicable, report:

- CC-C;
- SC-E;
- SC-M;
- SC-L;
- EG;
- MG;
- LG;
- ECC_Total.

ECC values MUST NOT be invented when required evidence is unavailable.

---

## 10. Draft Analysis

Before REIG, the analysis MUST construct the Draft Analysis containing the substantive analytical output produced so far.

The Draft Analysis is the object audited by REIG.

The Draft Analysis is NOT the source article or target text.

---

## 11. REIG

REIG MUST be applied to the Draft Analysis.

The output MUST report, for each applicable official REIG dimension:

- dimension;
- score;
- finding;
- supporting evidence or reasoning;
- required correction where a material violation exists.

The five official REIG dimensions are:

1. Evidence Consistency Check — ERG
2. Method Consistency Check — MRG
3. Confidence Consistency Check — CRG
4. Assumption Consistency Check — ARG
5. FAIRNESS Consistency Check — FRG

The four legacy audit dimensions may be used as additional diagnostics but MUST NOT replace the five official dimensions.

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
- analytical limitations.

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

## 13. Final BSI Score

The final BSI score MUST be calculated using the official BSI scoring logic and official BIO v1.0 weights.

Layer C does not redefine or alter the scoring specification.

If the applicable calculation mode cannot be established from authoritative BSI materials, the limitation MUST be disclosed rather than an alternative being silently selected.

If a required scoring input cannot be defensibly established, the limitation MUST be disclosed rather than a value being invented.

---

## 14. Uncertainty

Uncertainty MUST be explicitly represented wherever it materially affects interpretation, confidence, scoring, or conclusion.

The analysis MUST distinguish evidence from interpretation and MUST calibrate confidence to available support.

Unsupported certainty MUST NOT be introduced merely to complete the output structure.

---

## 15. Material Limitations

The completed analysis MUST disclose material:

- evidence limitations;
- analytical limitations;
- uncertainty affecting interpretation or reliability;
- unresolved material execution requirements that affect the analytical result.

Absence of a limitation MUST NOT be inferred merely because a corresponding field is not populated.

---

## 16. Substantive Effects of Execution

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

## 17. Boundary with Layer D

Layer C MUST NOT become a machine-execution trace.

The following distinction is preserved:

**Claimed ≠ Observed ≠ Independently Validated**

Execution status, machine-observable state, retrieval/escalation state, verification state, and other audit-trace information belong to Layer D.

A rich execution-status report MUST NOT substitute for the mandatory BSI analytical output.

---

## 18. Analytical Output Completeness

Completion of the analytical output requires the presence and internal coherence of all mandatory substantive components required by BSI v3.5, including:

- all seven BSI criteria;
- CreativeValueAdd and all three official subcriteria;
- Manifest / Latent / Meta analysis;
- EIG;
- ECC;
- Draft Analysis;
- REIG audit of the Draft Analysis;
- Final Synthesis;
- uncertainty and limitations.

Execution completeness alone does not authorize analytical completion.

If a mandatory analytical component is missing, the analysis MUST NOT be declared complete.

---

## 19. Non-Modification Rule

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

## 20. Canonical Source Basis

This specification is derived from the existing BSI v3.5 authoritative materials, including:

- `MASTER_PROMPT_BSI_v3.5.md`
- `ARCHITECTURAL_INVARIANTS_BSI_v3.5.md`
- the canonical BSI/EIG/ECC/REIG specifications referenced by those materials.

Legacy v3.4.2 output structures are not automatically inherited as Layer C v3.5 schema elements.

