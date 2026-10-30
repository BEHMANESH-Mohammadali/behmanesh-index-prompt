# Canonical Specification Matrix — BSI v3.5

**Status:** Working Canonicalization Specification  
**Purpose:** Resolve authoritative semantics before implementation changes  
**Scope:** BSI v3.5 analytical architecture only

---

## 1. EIG

### Authoritative source
`CORE-BEHMANESH/Shared_Components/EIG/Epistemic_Integrity_Gap_Analyzer_v1.0.md`

### Canonical semantics

EIG v1.0 defines four official epistemic gaps:

| Gap | Weight |
|---|---:|
| Method-Conclusion Gap (MCG) | 0.30 |
| Claim-Evidence Gap (CEG) | 0.35 |
| Framing-Content Gap (FCG) | 0.15 |
| Longitudinal Consistency Gap (LCG) | 0.20 |

EIG classification and interpretation remain exactly those defined in EIG v1.0.

Evolution, Rupture, and Unknown handling remain unchanged.

The EIG score is descriptive and must not be treated as an independent judgment of the person or target.

### Canonical rule

No architectural or execution change may redefine, reweight, replace, or silently reinterpret EIG v1.0.

The mapping from EIG gap values to the BSI penalty mechanism must remain explicit.

---

## 2. ECC

### Authoritative sources

- ECC v2.0
- `SOP_Intellectual_Content_Analysis_v3.4.2.md`
- `ARCHITECTURAL_INVARIANTS_BSI_v3.5.md`

### Canonical semantics

ECC v2.0 remains an invariant epistemic-calibration component.

Its four-layer structure remains:

- ECC-C
- ECC-E
- ECC-M
- ECC-L

Its relationship with Recursive EIG remains unchanged.

### Unresolved implementation detail

The exact computational aggregation semantics of ECC v2.0 have not yet been canonically resolved in this matrix.

Therefore:

- execution architecture may enforce ECC where required;
- execution architecture may not redefine ECC;
- execution architecture may not substitute another calibration mechanism;
- execution architecture may not invent aggregation or weighting rules.

---

## 3. REIG

### Authoritative source

`CORE-BEHMANESH/Shared_Components/EIG/Recursive_EIG_v1.0.md`

### Canonical semantics

REIG audits the Draft Analysis rather than the target text.

Official dimensions:

| Dimension | Meaning |
|---|---|
| ERG | Evidence Recursive Gap |
| MRG | Method Recursive Gap |
| CRG | Confidence Recursive Gap |
| ARG | Assumption Recursive Gap |
| FRG | Fairness Recursive Gap |

Scale:

- 0 = No gap
- 1 = Minor
- 2 = Moderate
- 3 = Severe
- 4 = Critical

Where defensibly calculable:

`REIG_Total = mean(ERG, MRG, CRG, ARG, FRG)`

The legacy four SOP audit dimensions may remain additional diagnostics, but must not replace the five official REIG dimensions.

REIG remains a correction mechanism:

`Draft Analysis → REIG → Correction → Re-analysis → Final Validation`

---

## 4. BSI SCORING

### Authoritative source

`SOP_Intellectual_Content_Analysis_v3.4.2.md`

### Official D1–D7 weights

| Dimension | Weight |
|---|---:|
| D1 Conditional Depth | 0.22 |
| D2 Longitudinal Coherence | 0.18 |
| D3 Authentic Ethical Layer | 0.18 |
| D4 Creative Value Add | 0.17 |
| D5 Strategic Depth | 0.12 |
| D6 Interdisciplinary Breadth | 0.08 |
| D7 Anti-Performative Drift | 0.05 |

Total:

`1.00`

### Linear formula

`BSI_linear = Σ(w_i × D_i) × (1 − EIG_penalty)`

with:

`EIG_penalty = EIG_avg / 10`

where `EIG_avg` is the applicable weighted average of EIG gaps on the 0–10 scale.

### Nonlinear formula

`BSI_nonlinear = 100 × Π((D_i / 100)^w_i) × (1 − EIG_penalty)`

### Unresolved implementation detail

The authoritative threshold that activates nonlinear calculation in cases of foundational weakness has not been canonically specified.

No threshold may be invented by the execution architecture.

If calculation mode cannot be established from the authoritative specification, the limitation must be disclosed rather than silently selecting a mode.

---

## 5. LONGITUDINAL HANDLING

### D2 canonical formula

`D2 = 0.40 × Trajectory_Stability
   + 0.30 × Contradiction_Resolution_Rate
   + 0.20 × Stable_Nodes_Consistency
   + 0.10 × Theme_Evolution`

D2 measures continuity and coherence of reasoning across time, texts, and contexts.

### Canonical rule

Longitudinal evidence must be distinguished from absence of longitudinal evidence.

A single input must not be used to fabricate longitudinal claims.

### Unresolved implementation detail

The complete canonical handling of D2 when only a single input is available requires explicit specification.

Until resolved, the execution architecture must not invent longitudinal evidence, trajectories, contradictions, or stability claims.

EIG's Longitudinal Consistency Gap remains an interpretive lens and must not be converted into causal claims.

---

## 6. PENALTY LOGIC

### Canonical relation

The BSI penalty mechanism uses:

`EIG_penalty = EIG_avg / 10`

where `EIG_avg` is a weighted average of applicable EIG gaps on the 0–10 scale.

### Important distinction

The following are not interchangeable:

1. Raw EIG gap values: 0–10
2. `EIG_avg`: weighted average of applicable gaps, 0–10
3. `EIG_Score`: EIG descriptive score, 0–100
4. `EIG_penalty`: value applied to the BSI formula

The execution architecture must not silently substitute:

`EIG_Score / 100`

for:

`EIG_avg / 10`

unless an authoritative future specification explicitly establishes that equivalence.

---

## 7. IMPLEMENTATION SEMANTICS

### Four-layer architecture

#### Layer A — BSI Knowledge Core

Defines:

- what BSI is;
- what it analyzes;
- epistemic structure;
- analytical layers;
- formal criteria;
- scoring semantics.

Layer A is immutable during the v3.5 execution-architecture work.

#### Layer B — Execution Architecture

Defines execution conditions required to obtain a sufficiently rigorous analysis, including:

- sufficient analytical effort;
- evidence control;
- retrieval escalation;
- counterevidence checking;
- verification;
- premature-completion prevention;
- completion control;
- correction and re-analysis.

Layer B must not redefine Layer A.

#### Layer C — Analytical Output Contract

Defines the organization and presentation of substantive analytical findings, including:

- substantive findings;
- uncertainty;
- material limitations;
- substantive effects of execution;
- output organization.

Changes to Layer C must be independently versioned and documented.

#### Layer D — Audit / Machine Trace

Defines machine-observable execution information and audit state.

It must preserve the distinction:

`Claimed ≠ Observed ≠ Independently Validated`

Layer D is an audit/trace layer and must not become a second analytical report.

---

## 8. EXECUTION-TO-OUTPUT BOUNDARY

Execution controls exist to improve analytical quality.

Execution effort must convert into analytical value through:

- broader justified evidence coverage;
- deeper analysis;
- stronger verification;
- counterevidence consideration;
- improved synthesis;
- calibrated inference;
- explicit uncertainty.

Execution effort must not be converted into:

- procedural narration;
- redundant prose;
- artificial verbosity;
- unsupported certainty;
- fabricated evidence.

---

## 9. AUDIT SEMANTICS

The architecture must distinguish:

`Claimed`

from:

`Observed`

and:

`Independently Validated`

Self-report or internal execution claims do not constitute independent validation.

Where no independent evaluator exists, the analysis must not imply independent validation.

---

## 10. REIG CORRECTION LOOP

REIG must operate on the produced Draft Analysis.

Canonical sequence:

`Draft Analysis`
→ `REIG`
→ `Correction`
→ `Re-analysis`
→ `Final Validation`

REIG must not replace BSI, EIG, ECC, or the Knowledge Core.

---

## 11. NULL / NEGATIVE FINDINGS

Null, absent, negative, or inconclusive findings are substantive analytical outcomes where the evidence supports them.

The architecture must preserve the ability to report:

- no evidence found;
- insufficient evidence;
- contradiction not established;
- relationship not established;
- longitudinal inference unavailable.

Absence of evidence must not automatically be transformed into evidence of absence.

---

## 12. EXPLICITLY UNRESOLVED ITEMS

The following items remain unresolved and must be explicitly specified before implementation silently depends on them:

### U1 — Nonlinear BSI activation threshold

The exact authoritative condition for selecting nonlinear BSI calculation remains unresolved.

### D2 — Legacy 60% Longitudinal Rule — Deprecated

The former minimum-60% longitudinal weighting rule found in pre-BIO v1.0 execution documents is deprecated and is not part of the current canonical BSI scoring architecture.

It MUST NOT modify, override, or supplement the canonical D2 weight of 0.18, nor introduce an additional longitudinal weighting layer.

Longitudinal evidence remains intrinsic to D2, but its analytical role is expressed through the canonical D2 construct and its defined subcriteria, not through a separate 60% numerical weighting rule.

The legacy references in active execution documents must be marked deprecated or removed.

D2 subcriterion provenance: the 40/30/20/10 decomposition is specified by `BSI_Calculation_Formula_Hybrid_v3x.md` as the operationalization of BIO v1.0. BIO v1.0 itself establishes D2 and its 0.18 weight, but does not directly specify this internal decomposition.

---

### D2 — Canonical Temporal Horizon Mapping

**Status: RESOLVED**

D2 LongitudinalCoherence uses three **overlapping temporal horizons**. These horizons are analytical views over the same evidence universe, not mutually exclusive partitions of the dataset.

The canonical horizons are:

- **Short-term:** evidence within the defined short-term temporal window up to the present.
- **Mid-term:** evidence within the defined mid-term temporal window up to the present.
- **Long-term:** evidence extending from the earliest available relevant evidence up to the present.

The horizons are cumulative/overlapping:

`Short-term ⊆ Mid-term ⊆ Long-term`

Therefore, evidence occurring at the present time may legitimately contribute to all three horizons simultaneously.

A temporal horizon MUST NOT be implemented by assigning each datum to exactly one of the three horizons.

The three horizons are analytical mappings within D2 and MUST NOT become:
- additional BSI criteria;
- independent scoring dimensions;
- additional weights;
- replacements for the canonical D2 construct;
- a second longitudinal scoring layer.

Where evidence availability differs across horizons, the analysis MUST distinguish:
- observed evidence;
- unavailable evidence;
- insufficient evidence;
- unsupported longitudinal inference.

Absence of evidence in a horizon MUST NOT be silently converted into evidence of incoherence.

The temporal horizon model is used to examine the development and persistence of relevant structural patterns across time while preserving the distinction between:
- present-input internal coherence;
- referential continuity;
- developmental/revision continuity;
- longitudinal pattern persistence.

The canonical D2 weight remains `0.18`.

---

### U3 — Single-input longitudinal semantics — RESOLVED

A single input is sufficient to execute the canonical **Single-Input Coherence Path** for structural/internal coherence analysis, but it is not sufficient to establish longitudinal continuity, trajectory, development, persistence, or change across time.

Accordingly:

- Internal coherence of the available input MUST be evaluated through the canonical Single-Input Coherence Path.
- Longitudinal claims MUST NOT be fabricated, inferred solely from the existence of one input, or presented as established continuity.
- D2 remains a canonical scoring criterion with weight `0.18`; the absence of longitudinal evidence does not create an alternative D2 weight and does not trigger any additional weighting rule.
- The three D2 temporal horizons remain analytical views over the evidence universe. With only one input, the input may belong to every horizon whose temporal window contains it, but this does not constitute longitudinal evidence.
- Short-term, mid-term, and long-term availability MUST be distinguished from actual longitudinal evidence. Temporal inclusion alone is not evidence of trajectory or continuity.
- Where longitudinal evidence is unavailable, the analysis MUST explicitly state the limitation and MUST NOT convert missing evidence into evidence of incoherence.
- Longitudinal EIG claims requiring comparison across multiple temporally distinct inputs MUST be marked unavailable/not established when only one input exists.
- This resolution does not create a new criterion, weight, score, or substitute longitudinal score.

Thus, **single-input D2 handling is a constrained-availability state, not a redefinition of D2**.

### U5 — Layer C output contract

**Status: RESOLVED**

Layer C is canonically specified in:

`docs/specification/ANALYTICAL_OUTPUT_CONTRACT_LAYERC_v3.5.md`

The v3.5 Layer C contract is derived from the mandatory analytical-output requirements specified by `MASTER_PROMPT_BSI_v3.5.md` and the Layer C architectural requirements in `ARCHITECTURAL_INVARIANTS_BSI_v3.5.md`.

The canonical Layer C contract defines:

- the required substantive output sequence;
- the mandatory analytical components;
- uncertainty communication;
- material limitations;
- substantive effects of execution that affect the analytical result;
- the boundary between analytical output and Layer D audit trace;
- analytical-output completeness requirements.

The legacy v3.4.2 JSON output structures are not automatically inherited as the v3.5 Layer C schema.

Layer C does not modify the BSI Knowledge Core, ontology, criteria, weights, scoring logic, EIG, ECC, or REIG.

---

## 13. CANONICALIZATION RULE

No unresolved semantic issue may be silently resolved in implementation.

Any future resolution must:

1. identify the authoritative source;
2. state the exact semantic decision;
3. record the affected component;
4. identify whether the decision changes Layer A, B, C, or D;
5. document compatibility implications;
6. update this matrix before implementation relies on the decision.

The execution architecture must not become an implicit substitute for missing specification.

---

## 14. DECISION RECORD

This document is the working canonicalization matrix for BSI v3.5 architectural implementation.

It does not supersede:

- BSI Knowledge Core;
- BIO v1.0;
- CORE-BEHMANESH;
- EIG v1.0;
- ECC v2.0;
- Recursive EIG v1.0;
- SOP_Intellectual_Content_Analysis_v3.4.2.

Its purpose is to expose and resolve semantic dependencies before implementation changes.

No benchmark, comparison, ranking, winner determination, external judge, or competitive evaluation is part of this repository's analytical architecture.

The repository remains dedicated exclusively to BSI analysis.
