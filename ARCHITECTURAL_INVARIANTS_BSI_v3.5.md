# BSI 3.5 — Architectural Invariants

**Status:** Development Architecture
**Baseline:** BSI v3.4.2
**Branch:** `develop/v3.5`

---

## 1. Foundational Principle

> **The BSI epistemic and analytical core is invariant; only its execution architecture may evolve.**

BSI v3.5 does not redesign the Behmanesh Structural Index itself.

It redesigns the conditions under which the existing BSI framework is executed, verified, and considered complete.

The distinction is fundamental:

- **BSI Knowledge Core** defines what BSI is and how it analyzes.
- **Execution Architecture** defines how an LLM must execute BSI reliably.
- **Output Layer** defines how the completed analysis is presented.

No execution-control mechanism may silently alter the epistemic identity, analytical structure, criteria, ontology, or scoring logic of BSI.

---

## 2. Immutable BSI Knowledge Core

The following components are invariant unless explicitly versioned as a change to BSI itself.

### 2.1 BSI Identity

- Behmanesh Structural Index
- شاخص ساختاری بهمنش
- BSI definition, purpose, scope, and conceptual identity

### 2.2 Epistemic and Analytical Structure

The following remain unchanged:

- layered structural analysis
- Manifest Layer
- Latent Layer
- Meta Layer
- mechanisms
- feedback loops
- leverage points
- core nodes
- structural relationships
- intellectual development
- worldview and underlying mechanisms

### 2.3 Formal BSI Criteria

The seven formal BSI criteria are immutable. Their official names, titles, descriptions, definitions, weights, layer assignments, and internal subcriteria must remain exactly as defined by the authoritative BSI/BIO documents. No self-derived translation, renaming, paraphrasing, reordering, substitution, or reinterpretation is permitted.

| ID | Official Name | Weight | Layer |
|---|---|---:|---|
| D1 | ConditionalDepth | 0.22 | Manifest + Latent |
| D2 | LongitudinalCoherence | 0.18 | Meta + Temporal |
| D3 | AuthenticEthicalLayer | 0.18 | Latent + Meta |
| D4 | CreativeValueAdd | 0.17 | Latent + Meta |
| D5 | StrategicDepth | 0.12 | Manifest + Latent |
| D6 | InterdisciplinaryBreadth | 0.08 | Manifest |
| D7 | AntiPerformativeDrift | 0.05 | Meta |

#### D1 — ConditionalDepth

**تعریف BIO:** عمق استدلال شرطی و پیش‌بینی‌کننده — آیا محتوا روابط «اگر...آنگاه» مکانیسمی می‌سازد؟

#### D2 — LongitudinalCoherence

**تعریف BIO:** تداوم و انسجام استدلال در طول زمان، متن‌ها و زمینه‌ها

#### D3 — AuthenticEthicalLayer

**تعریف BIO:** اصالت لایه اخلاقی — نه performative، بلکه قابل راستی‌آزمایی

#### D4 — CreativeValueAdd

**تعریف BIO:** آیا محتوا یا سازنده آن یک شکاف معرفتی واقعی را شناسایی کرده و با ترکیب حوزه‌ای هدفمند، خروجی‌ای تولید کرده که ظرفیت تولید فکر جدید و ابزارهای فکری در دیگران را ایجاد می‌کند؟

#### D5 — StrategicDepth

**تعریف BIO:** کیفیت عمق تحلیل نسبت به حجم — کمتر اما عمیق‌تر

#### D6 — InterdisciplinaryBreadth

**تعریف BIO:** گستردگی چندحوزه‌ای بدون از دست دادن دقت

#### D7 — AntiPerformativeDrift

**تعریف BIO:** اجتناب از تولید محتوای نمایشی، engagement-driven یا attention-optimized

For `CreativeValueAdd`, the official BIO v1.0 internal subcriteria are:

| Subcriterion | Weight | Layer |
|---|---:|---|
| Epistemic Gap Targeting | 35% | Latent |
| Combinatorial Synthesis | 40% | Latent |
| Generative Capacity | 25% | Meta |

The names, titles, definitions, descriptions, weights, and ordering above are baseline-controlled against BIO v1.0 and the authoritative BSI calculation specification. Execution Architecture must not rename, translate, redefine, reweight, or otherwise alter them.

### 2.4 CORE_BEHMANESH

`CORE_BEHMANESH v1.0` remains the authoritative analytical core.

Its principles and logic are preserved.

In particular:

> **Evaluate robustness of knowledge architecture, not correctness of conclusions.**

### 2.5 BIO Compatibility

BIO v1.0 compatibility remains unchanged.

Execution Architecture may enforce compliance with BIO, but may not redefine BIO or substitute another ontology.

### 2.6 Assumption Excavation

The Assumption Excavation Protocol remains an analytical component of the BSI execution pipeline.

Its:

- purpose
- four-category structure
- four-step sequence
- claim classification
- counterfactual testing
- ranking logic
- connection to EIG

remain unchanged.

Execution Architecture may ensure that the protocol is executed when required; it may not rewrite its analytical logic.

### 2.7 EIG

EIG remains an epistemic analysis component of the existing BSI architecture.

Its definition, role, logic, and position in the pipeline remain unchanged.

### 2.8 ECC — Epistemic Confidence Calibration

`ECC v2.0` remains an invariant epistemic calibration component of the BSI architecture.

Its definition, four-layer structure (`ECC-C`, `ECC-E`, `ECC-M`, `ECC-L`), confidence-calibration logic, and relationship to Recursive EIG remain unchanged.

Execution Architecture may ensure that ECC is executed when required, but may not redefine, remove, replace, reweight, or convert ECC into a different heuristic.

### 2.9 REIG

REIG remains an audit of the **Draft Analysis**, not the target text.

Execution Architecture may ensure that this object discipline is respected, but may not redefine REIG.

---

## 3. Execution Architecture — The Change Surface

BSI 3.5 introduces a distinct execution-control layer.

The existing `LLM-Execution-Guardrails v1.2` belongs to this execution layer.
It is an execution-control component, not part of the immutable BSI Knowledge Core.

BSI 3.5 may extend, reorganize, or replace execution controls, including the existing Guardrails, provided that such changes do not alter the identity, analytical logic, formal criteria, scoring, ontology, or epistemic roles of the BSI Knowledge Core.

Its purpose is not to change the analysis itself, but to control whether the model has performed sufficient justified epistemic work before producing a final answer.

The execution layer may include:

1. Effort Calibration
2. Evidence Sufficiency Assessment
3. Evidence Exhaustion Check
4. Counterevidence Search
5. Competing Interpretation Check
6. Verification
7. Retrieval Escalation
8. Final Re-read
9. Premature Completion Prevention
10. Completion Gate
11. User-Challenge Independence
12. Evidence-Proportional Confidence

These mechanisms govern execution quality, not BSI meaning.

---

## 4. Maximum Justified Epistemic Effort

BSI 3.5 requires:

> **Maximum Justified Epistemic Effort before the first answer.**

This does **not** mean:

- maximum token usage
- maximum response length
- unnecessary computation
- exhaustive investigation regardless of task complexity

It means that the model must allocate sufficient analytical effort for the epistemic demands of the task.

Effort should scale with factors such as:

- complexity of the source
- number of relevant claims
- uncertainty
- contradiction intensity
- evidence density
- domain difficulty
- longitudinal requirements
- consequences of premature conclusions
- need for verification

Efficiency is permitted only after the minimum justified epistemic work has been completed.

---

## 5. Premature Completion Prevention

A model must not terminate analysis merely because a plausible interpretation has been found.

Before finalization, the execution layer must determine whether important unresolved questions remain.

At minimum, the model must consider:

- Have relevant evidence sources been sufficiently examined?
- Are important claims still unsupported?
- Is there meaningful counterevidence?
- Is a competing interpretation plausible?
- Are important uncertainties unresolved?
- Has the analysis reached the required structural depth?
- Have required verification steps been completed?

If the answer to any material completion condition is negative, analysis must continue or the limitation must be explicitly reported.

---

## 6. Evidence Sufficiency and Exhaustion

Evidence collection must distinguish between:

**Evidence Sufficiency**

Whether the available evidence is sufficient for the intended claim.

and

**Evidence Exhaustion**

Whether reasonable available evidence-search paths have been sufficiently explored before concluding that evidence is unavailable or limited.

Absence of immediately available evidence must not automatically be treated as evidence of absence.

Where further retrieval could materially change the conclusion, the execution architecture should escalate retrieval before finalization.

---

## 7. Counterevidence and Competing Interpretations

A completed analysis must not rely solely on evidence supporting its initial interpretation.

Where materially relevant, the model should actively test:

- counterevidence
- contradictory passages
- alternative explanations
- competing structural interpretations
- boundary conditions

This is an execution safeguard.

It does not authorize the model to introduce unrelated analytical criteria into BSI.

---

## 8. Verification

Verification must be proportional to epistemic risk.

Higher-risk claims require stronger verification.

Verification may include:

- textual cross-checking
- internal consistency checks
- source comparison
- claim-to-evidence alignment
- contradiction checks
- numerical or methodological verification where applicable
- re-reading relevant source sections

Verification must not be represented as completed when it was not performed.

---

## 9. Evidence-Proportional Confidence

Confidence must not exceed the strength of the available evidence.

The execution architecture therefore requires explicit separation between:

- what is directly supported
- what is inferred
- what is hypothesized
- what remains speculative

Existing BSI / CORE / BIO claim-classification rules remain authoritative.

This architecture controls their execution; it does not redefine them.

---

## 10. User-Challenge Independence

A fundamental requirement of BSI 3.5 is:

> **The user should not need to challenge, remind, or repeatedly instruct the model in order to obtain ordinary justified diligence.**

Therefore, prompts such as:

- "read it again"
- "did you read the whole text?"
- "look more carefully"
- "check the evidence"
- "you missed something"

must not be treated as necessary activation signals for ordinary analytical diligence.

The execution architecture must attempt to perform such justified diligence before the first answer.

User feedback may still identify genuine omissions or errors, but it must not be the mechanism that activates the baseline level of appropriate effort.

---

## 11. Four-Layer Separation of Concerns

BSI 3.5 maintains four distinct architectural layers.

### Layer A — BSI Knowledge Core

Defines:

- what BSI is
- what BSI analyzes
- its epistemic structure
- its analytical layers
- its formal criteria
- its scoring logic

### Layer B — Execution Architecture

Defines:

- how sufficient analytical effort is determined
- how evidence is controlled
- when retrieval should escalate
- when counterevidence should be checked
- when verification is required
- when completion is justified
- how detected weaknesses are corrected

### Layer C — Analytical Output Contract

Defines:

- how substantive findings are organized
- how uncertainty is communicated
- which substantive effects of execution must enter the analytical result
- how material limitations affecting result reliability are represented
- how the completed analysis is presented

Layer C is part of the BSI delivery architecture, but changes to Layer C must be explicitly versioned and documented.

### Layer D — Audit / Machine Trace

Defines:

- machine-observable execution state
- deterministic audit information
- the distinction between claimed, observed, and independently validated execution state

Layer D is not a second analytical report.

No layer may silently substitute for another.

---

## 12. Baseline Protection

BSI 3.5 must preserve compatibility with the BSI v3.4.2 baseline.

Any proposed architectural change must first answer:

> **Does this change alter what BSI is, or only how BSI is executed?**

If it alters what BSI is, it is not an execution-architecture change and must be treated as a separate BSI framework change.

If it changes only execution conditions, it may belong in the BSI 3.5 Execution Architecture.

---

## 13. Acceptance Conditions

A BSI 3.5 execution architecture is acceptable only if:

1. The BSI knowledge core remains unchanged.
2. Existing BSI criteria remain unchanged.
3. Existing scoring and weighting remain unchanged.
4. BIO compatibility remains intact.
5. CORE_BEHMANESH remains authoritative.
6. Assumption Excavation, EIG, and REIG retain their defined analytical roles.
7. Execution controls operate independently from BSI scoring.
8. Ordinary justified diligence occurs before the first answer.
9. Premature completion is actively controlled.
10. Evidence and confidence remain proportionate.
11. User challenge is not required to activate baseline diligence.
12. The architecture does not reward verbosity for its own sake.
13. Efficiency remains possible after justified epistemic work has been completed.

---

## 14. Change-Control Rule

For every proposed BSI 3.5 modification, apply this question first:

> **Does this change alter what BSI is, or only how BSI is executed?**

Only changes belonging to the second category may be incorporated into the execution architecture without changing the BSI knowledge core.

---

## 15. Final Invariant

> **BSI 3.5 must not redesign BSI; it must redesign the conditions under which BSI is executed and considered complete.**
