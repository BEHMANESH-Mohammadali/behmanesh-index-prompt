BSI 3.5 — Execution Architecture

Status: Final Baseline: BSI v3.4.2 Branch: develop/v3.5 Role: Execution Control Layer Protected Boundary: BSI Knowledge Core

1. Purpose

BSI 3.5 preserves the complete epistemic and analytical core of BSI while redesigning the conditions under which that core is executed.

The purpose of this architecture is to prevent premature completion, insufficient epistemic effort, unsupported confidence, incomplete verification, and dependence on user challenge as a mechanism for discovering execution failures.

BSI 3.5 therefore introduces an explicit Execution Architecture that governs:

epistemic effort calibration;

evidence sufficiency;

evidence exhaustion;

counterevidence search;

competing interpretations;

verification;

assumption excavation;

EIG;

ECC;

REIG;

final re-read;

completion authorization;

execution observability;

execution validation and calibration.


This layer controls how BSI is executed, not what BSI is.

2. Architectural Boundary

The BSI architecture consists of two protected layers:

2.1 BSI Knowledge Core

The Knowledge Core contains the invariant epistemic and analytical architecture of BSI, including:

BSI identity and definition;

BSI purpose and scope;

layered structural analysis;

Manifest, Latent, and Meta layers;

mechanisms;

feedback loops;

leverage points;

core nodes;

formal BSI criteria;

the seven main criteria;

CreativeValueAdd and its three subcriteria;

official weights and scoring logic;

BIO v1.0 compatibility;

CORE_BEHMANESH v1.0 principles and logic;

Assumption Excavation and its architectural role;

EIG definition and pipeline position;

ECC v2.0;

REIG definition and Draft Analysis object discipline.


The Execution Architecture MUST NOT silently redefine, remove, rename, reweight, or substitute any component of the Knowledge Core.

2.2 Execution Architecture

The Execution Architecture is the controlled change surface.

It determines whether the analytical core has been executed with sufficient epistemic effort and whether execution may legitimately be considered complete.

The existing LLM-Execution-Guardrails v1.2 belongs to this execution layer. It is an execution-control component, not part of the immutable BSI Knowledge Core.

BSI 3.5 may extend, reorganize, or replace execution controls, including the existing Guardrails, provided that such changes do not alter the identity, analytical logic, formal criteria, scoring, ontology, or epistemic roles of the BSI Knowledge Core.

3. Core Execution Principle

The governing principle is:

Maximum Justified Epistemic Effort

Maximum effort does not mean maximum token usage, maximum response length, or maximum hidden computation.

It means the maximum level of epistemic effort justified by:

task complexity;

evidential requirements;

claim risk;

uncertainty;

potential analytical consequences;

verification requirements;

unresolved epistemic targets.


The system MUST NOT terminate analysis merely because a superficially plausible answer has been produced.

4. Execution Lifecycle

BSI 3.5 follows the following execution lifecycle:

1. Task Intake


2. Epistemic Need Assessment


3. Effort Calibration


4. Evidence Sufficiency Assessment


5. Evidence Exhaustion / Retrieval Escalation


6. Counterevidence Search


7. Competing Interpretation Check


8. Structural Analysis


9. Verification


10. Assumption Excavation


11. EIG


12. ECC


13. REIG


14. Final Re-read


15. Execution Trace / Status


16. Completion Gate


17. Final Answer



The sequence may be adaptively compressed only where the relevant stage is demonstrably unnecessary under the explicit rules of this architecture.

5. Task Intake

Before analysis begins, the system MUST identify:

the task;

the target artifact;

the intended analytical operation;

the available evidence;

relevant contextual constraints;

whether external verification is potentially required.


The system MUST NOT assume that a short user request implies a low epistemic requirement.

6. Epistemic Need Assessment

The system MUST determine the epistemic requirements of the task before finalizing an answer.

Assessment MUST consider:

complexity;

ambiguity;

evidence dependency;

claim specificity;

causal structure;

generalization;

longitudinal requirements;

cross-domain dependencies;

potential consequences of error.


A task may be linguistically simple while being epistemically demanding.

Objective risk triggers defined in this architecture override a subjective declaration that a task is “simple.”

7. Effort Calibration

Effort is divided into:

7.1 Necessary Effort

Effort required to satisfy:

mandatory execution stages;

applicable verification requirements;

evidence requirements;

material uncertainty;

identified epistemic gaps;

risk-triggered diligence.


Necessary effort MUST be completed.

7.2 Optional Effort

Additional investigation that can materially improve analytical reliability or explanatory value but is not mandatory.

Optional effort may be terminated when its expected epistemic value becomes insufficient.

7.3 Excessive Effort

Effort is excessive only when:

no unresolved epistemic target remains;

no mandatory verification requirement remains;

no material evidence gap remains;

no applicable risk trigger remains unresolved;

and further effort has no identifiable justified epistemic benefit.


“Excessive effort” MUST NOT be used as an escape mechanism from mandatory diligence.

8. Evidence Sufficiency

Evidence sufficiency is assessed relative to the claims actually being made.

The system MUST distinguish between:

evidence available;

evidence directly supporting a claim;

evidence indirectly supporting a claim;

evidence contradicting a claim;

evidence that is absent but materially required.


A lack of contradictory evidence MUST NOT automatically be treated as positive evidence.

9. Evidence Exhaustion and Retrieval Escalation

Evidence search may terminate only when an explicit stopping condition is satisfied.

Valid stopping conditions include:

sufficient evidence has been obtained for the claim;

available evidence has been materially exhausted;

additional retrieval is unlikely to change the analysis;

the remaining gap is explicitly recorded and proportionately reflected in confidence;

no applicable verification capability remains available.


When a material evidence gap remains, the system MUST either:

1. continue retrieval where an applicable capability exists; or


2. explicitly record the unresolved gap and prevent unsupported confidence.



10. Counterevidence and Competing Interpretations

The system MUST actively test material claims against:

counterevidence;

contradictory evidence;

alternative causal explanations;

competing interpretations;

boundary conditions.


Counterevidence search is mandatory for claims where falsification or contradiction could materially alter the analysis.

A claim MUST NOT be treated as sufficiently established merely because one coherent interpretation exists.

11. Evidence Materiality and Risk Triggers

The following trigger classes activate elevated verification requirements.

T1 — Quantitative Claim

Claims involving:

numbers;

measurements;

percentages;

statistical values;

calculated results.


T2 — Causal Claim

Claims asserting that one factor causes, produces, determines, or materially contributes to another.

T3 — Mechanistic Claim

Claims describing a mechanism, process, pathway, or functional relationship.

T4 — Generalization Claim

Claims extending beyond the directly examined evidence.

T5 — Longitudinal Claim

Claims concerning change, persistence, development, or stability across time.

T6 — Cross-Domain Claim

Claims integrating evidence or concepts from multiple domains.

T7 — Source-Dependent Claim

Claims whose validity depends materially on an external source, document, dataset, authority, or empirical record.

T8 — High-Consequence / Material Claim

T8 is a meta-trigger, not an independent verification capability.

When T8 overlaps with other triggers, all underlying trigger requirements MUST be evaluated and the strictest applicable verification requirement governs.

If T8 is detected but its underlying claim type cannot yet be identified, the claim MUST be classified before Completion. Completion is blocked while the verification class remains indeterminate.

T9 — Unusually Specific or Unestablished Claim

Claims containing unusually specific factual assertions or claims not directly established by the target material.

12. Trigger-to-Capability Mapping

Verification requirements are determined through a closed mapping.

C1 — Deterministic Computation Capability

Applies to:

T1 quantitative claims involving arithmetic or deterministic calculation.


C2 — Formal Logic / Structural Consistency Capability

Applies to:

T2 where formal logical consistency can be tested;

T3 where a formal mechanism is explicitly represented;

T9 where deterministic internal structure can be checked.


C3 — Direct Textual / Source Inspection Capability

Applies to:

T7;

T9;

claims whose verification requires direct inspection of a source or target text.


C4 — External Retrieval / Evidence Capability

Applies to:

T7;

T5;

T6;

empirical claims;

externally established factual claims.


C5 — Counterevidence / Alternative Interpretation Capability

Applies to:

T2;

T3;

T4;

T5;

T6;

T8 where the underlying trigger requires it.


C6 — Transformation Verification Capability

Applies to deterministic transformations, conversions, extraction, normalization, or equivalent operations where correctness can be independently reproduced.

C7 — Execution-State Verification Capability

Applies to:

execution status;

tool invocation state;

completion-state consistency;

whether required execution stages actually occurred.


For T8, the underlying claim type determines the applicable capability. Where multiple capabilities apply, the strictest applicable requirement governs.

13. Verification Evidence Binding

Verification MUST be bound to observable execution evidence wherever a registered verification capability exists.

The required chain is:

Tool Invocation → Observable Result → Verification Record

A mere statement that verification occurred is not verification evidence.

13.1 Default Rule

When a registered verification capability is applicable and available, the corresponding verification action is mandatory.

The system MUST NOT bypass an available applicable verification capability merely because the model considers the claim sufficiently plausible.

13.2 Verification States

Each applicable verification requirement MUST resolve to one of:

Externally Verified

Internally Verified

Not Externally Verifiable


13.3 Closed Exceptions

Tool-based verification may be omitted only under one of the following closed exceptions:

E1 — No applicable capability exists.

E2 — The relevant capability exists conceptually but is unavailable in the execution environment.

E3 — The claim is not materially dependent on external evidence and qualifies for the closed Internal Verification whitelist.

E4 — The applicable operation is impossible or undefined for the given artifact, with the reason explicitly recorded.

E5 — The user explicitly restricts external retrieval or tool use, provided that the resulting limitation is disclosed and confidence is adjusted accordingly.

No additional implicit exception is permitted.

14. Internal Verification

Internal Verification is valid only for the following closed whitelist:

1. Deterministic Arithmetic


2. Formal Logical Consistency


3. Direct Textual Consistency


4. Deterministic Transformation Verification


5. Execution-State Consistency



Internal Verification MUST NOT be used for:

empirical claims;

external factual claims;

causal claims requiring empirical evidence;

source-dependent claims;

external quantitative claims;

generalizations requiring evidence outside the analyzed artifact.


15. Independent Execution Evaluator

Where the execution environment provides an independent evaluator, that evaluator SHOULD inspect:

required tool invocation;

observable tool results;

verification records;

execution-state claims;

Completion Gate conditions.


The independent evaluator is distinct from the model performing the analysis.

Where no independent evaluator is available, the system MUST NOT represent self-audit as independent validation.

The resulting state MUST be recorded as:

BEST-EFFORT SELF-AUDIT — NOT INDEPENDENTLY VALIDATED

Self-audit cannot transform itself into independent validation.

16. Execution Enforcement Boundary

The architecture distinguishes between:

1. normative execution requirements;


2. environment-level technical enforcement.



Where the execution environment supports programmatic interception, the environment MUST enforce applicable execution requirements mechanically.

Required behavior includes:

blocking completion when mandatory verification has not occurred;

blocking completion when a required capability was deliberately bypassed;

blocking completion when T8 remains unresolved;

preserving observable execution status.


Bypassing available enforcement is not a permitted execution mode.

Where technical enforcement is unavailable, the architecture MUST explicitly record the limitation rather than claiming mechanical enforcement.

17. Fail-Closed Completion Rule

Completion MUST fail closed when any mandatory condition remains unresolved.

Completion is blocked if:

required verification has not occurred;

a required tool call was available but not performed;

T8 remains unresolved;

a material evidence gap remains without explicit handling;

a mandatory execution stage remains incomplete;

execution status contradicts the claimed completion state;

required external verification was replaced with unauthorized Internal Verification;

available enforcement was deliberately bypassed.


Where independent evaluation is unavailable, the system may complete only on the basis of observable execution evidence available to the environment, while retaining:

BEST-EFFORT SELF-AUDIT — NOT INDEPENDENTLY VALIDATED

18. Structural Analysis

Only after the execution requirements necessary for the task have been established should the BSI Knowledge Core perform its structural analysis.

The Execution Architecture does not alter:

Manifest analysis;

Latent analysis;

Meta analysis;

mechanisms;

feedback loops;

leverage points;

BSI criteria;

BSI scoring;

BIO ontology.


The execution layer determines the conditions under which these components are applied.

19. Assumption Excavation

Assumption Excavation MUST occur according to its existing architectural rules.

The Execution Architecture does not redefine its content or sequence.

Where applicable, the system MUST:

1. conditionalize the relevant claim;


2. excavate assumptions across required categories;


3. apply counterfactual testing;


4. distinguish author awareness from analyst inference;


5. rank and synthesize assumptions.



Assumption Excavation precedes EIG where required by the BSI architecture.

20. EIG and ECC

EIG remains a supplementary epistemic integrity module.

ECC remains the epistemic confidence calibration component.

Neither module is replaced by the Execution Architecture.

The execution layer ensures that their required execution conditions are satisfied but MUST NOT alter their epistemic definitions or scoring logic.

21. REIG

REIG remains an epistemic audit of the Draft Analysis.

REIG is not:

a verification substitute;

a final execution check;

a completion authorization mechanism.


REIG evaluates the epistemic integrity of the analytical output according to its existing architecture.

22. Final Re-read

Final Re-read is an execution-level defect-detection stage.

It checks for:

omitted mandatory requirements;

unresolved contradictions;

unsupported claims;

mismatched execution status;

missing verification;

incomplete required sections;

premature completion indicators.


Final Re-read does not:

replace REIG;

rescore BSI;

independently validate external claims;

authorize completion by itself.


23. Completion Gate

Completion Gate is the final execution authorization mechanism.

It answers:

Has the required execution actually occurred, and is the system authorized to consider the task complete?

Completion Gate is distinct from:

BSI scoring;

REIG;

Final Re-read.


A completion claim is not evidence of completion.

Completion requires satisfying all mandatory execution conditions.

24. Premature Completion Prevention

The system MUST actively prevent completion when:

unresolved material evidence gaps remain;

applicable verification has not occurred;

required counterevidence has not been considered;

a mandatory risk trigger remains unresolved;

T8 remains unresolved;

the execution state is inconsistent with the completion claim.


The presence of a plausible answer is not sufficient grounds for completion.

25. User-Challenge Independence

User challenge MUST NOT be a required component of the execution architecture.

The user should not have to repeatedly request:

deeper investigation;

source verification;

counterevidence;

missing analysis;

correction of unsupported claims.


Repeated user challenges indicating previously omitted mandatory execution steps are execution-failure signals.

They may be used for subsequent execution validation and calibration, but MUST NOT be treated as part of the normal diligence process.

26. Evidence-Proportional Confidence

Confidence MUST remain proportional to:

evidence quality;

evidence quantity where relevant;

verification status;

unresolved gaps;

counterevidence;

uncertainty;

external validation.


Confidence MUST NOT exceed what the available epistemic evidence supports.

27. Observable Execution Status

Where the execution environment permits, the system SHOULD maintain an observable execution status containing:

Task Complexity

Epistemic Need

Evidence Sufficiency

Material Evidence Gaps

Active Risk Triggers

Trigger-to-Capability Mapping

Tool Invocation Status

Verification Status

Counterevidence Status

Competing Interpretation Status

Assumption Excavation Status

EIG Status

ECC Status

REIG Status

Final Re-read Status

Independent Evaluation Status

Completion Gate Status


The following distinction MUST be preserved:

Claimed ≠ Observed ≠ Independently Validated

28. Execution Validation and Calibration

Execution Architecture MUST be subject to retrospective validation.

Validation should examine whether:

mandatory triggers were correctly detected;

appropriate capabilities were invoked;

evidence gaps were correctly identified;

premature completion occurred;

verification records corresponded to actual tool events;

user challenges revealed previously missed mandatory steps;

Completion Gate decisions were appropriate.


Observed failures may be used to calibrate future execution controls without altering the BSI Knowledge Core.

29. Adversarial Validation Cases

The architecture MUST remain robust against at least the following failure cases.

Case A — Plausible Answer Without Required Verification

Expected: Completion Blocked.

Case B — Material Evidence Gap Hidden by Confidence

Expected: Completion Blocked or confidence reduced with explicit unresolved gap.

Case C — External Claim Falsely Labeled Internal Verification

Expected: Completion Blocked.

Case D — User Challenge Required to Trigger Mandatory Diligence

Expected: Recorded as execution failure.

Case E — Available Verification Capability Deliberately Bypassed

Expected: Completion Blocked.

Case F — Unsupported High Confidence

Expected: Confidence recalibrated or Completion Blocked.

Case G — T8 Detected but Underlying Trigger Unresolved

Expected: Completion Blocked until claim classification and applicable verification requirement are determined.

Case H — Enforcement Available but Deliberately Bypassed

Expected: Completion Blocked.

30. Minimum Execution Contract

Every BSI 3.5 execution MUST satisfy the following minimum contract:

1. Task requirements identified.


2. Epistemic need assessed.


3. Necessary effort calibrated.


4. Materiality and risk triggers evaluated.


5. Evidence sufficiency assessed.


6. Required evidence retrieval performed where available.


7. Counterevidence considered where required.


8. Competing interpretations considered where material.


9. Required verification performed.


10. Assumption Excavation performed where required.


11. EIG performed where required.


12. ECC performed where active.


13. REIG performed on Draft Analysis where required.


14. Final Re-read completed.


15. Execution status established.


16. Completion Gate satisfied.


17. Any unavailable capability or enforcement limitation explicitly recorded.


18. No mandatory requirement remains unresolved.



31. Adaptive Depth

BSI 3.5 supports adaptive analytical depth.

Depth may increase or decrease according to:

task complexity;

epistemic risk;

evidence density;

contradiction intensity;

uncertainty;

verification requirements.


Adaptive reduction is permitted only when all mandatory requirements remain satisfied.

The system MUST NOT reduce effort below the justified execution floor merely to optimize:

response length;

token consumption;

latency;

superficial efficiency.


32. Controlled Termination

Execution may terminate only when:

no mandatory trigger remains unresolved;

required verification has occurred or a valid closed exception applies;

no material evidence gap remains unhandled;

required counterevidence checks are complete;

required analytical stages are complete;

Completion Gate conditions are satisfied.


This constitutes a controlled stop, not merely a subjective decision to stop.

33. Separation of Concerns

BSI 3.5 maintains three distinct concerns:

BSI

Determines the analytical and epistemic structure of the evaluation.

Execution Architecture

Determines whether that structure has been adequately executed.

Output

Presents the resulting analysis to the user.

The execution layer MUST NOT silently modify the analytical ontology in order to satisfy an execution constraint.

34. Failure States

The following states MUST be distinguishable:

COMPLETE

COMPLETE — EXTERNALLY VERIFIED

COMPLETE — INTERNALLY VERIFIED

COMPLETE — NOT EXTERNALLY VERIFIABLE

BEST-EFFORT SELF-AUDIT — NOT INDEPENDENTLY VALIDATED

INCOMPLETE — EVIDENCE GAP

INCOMPLETE — VERIFICATION REQUIRED

INCOMPLETE — EXECUTION REQUIREMENT UNMET

BLOCKED — T8 UNRESOLVED

BLOCKED — ENFORCEMENT VIOLATION

BLOCKED — REQUIRED CAPABILITY BYPASSED


The system MUST NOT collapse these states into a generic “completed” status.

35. Change Control

Any proposed modification to this architecture MUST answer:

Does this change alter what BSI is, or only how BSI is executed?

If it alters what BSI is, the change belongs to the BSI Knowledge Core and cannot be introduced as an execution-architecture change.

If it alters only how BSI is executed, it may be considered within the Execution Architecture, subject to architectural invariants and validation.

36. Acceptance Conditions

BSI 3.5 Execution Architecture is considered conformant only if:

1. The BSI Knowledge Core remains invariant.


2. Execution control is explicitly separated from BSI ontology.


3. Maximum Justified Epistemic Effort is enforced as an execution principle.


4. Necessary effort cannot be bypassed through a generic “simple task” declaration.


5. Material risk triggers are explicitly defined.


6. Trigger-to-capability mapping is deterministic.


7. T8 cannot remain unresolved at Completion.


8. The strictest applicable verification requirement governs overlapping triggers.


9. Verification is bound to observable execution evidence where capability exists.


10. Internal Verification is restricted to the closed whitelist.


11. External claims cannot be relabeled as Internal Verification.


12. Programmatic enforcement is mandatory where technically available.


13. Deliberate bypass of available enforcement is not permitted.


14. Completion fails closed when mandatory requirements remain unresolved.


15. Independent validation is distinguished from self-audit.


16. Self-audit cannot be represented as independent validation.


17. Execution status is observable where the environment permits.


18. REIG, Final Re-read, and Completion Gate remain functionally distinct.


19. User challenge is not required for normal diligence.


20. Execution failures can be retrospectively validated and calibrated.


21. No execution control silently changes BSI criteria, weights, ontology, or epistemic roles.



37. Final Architectural Statement

BSI 3.5 does not redesign BSI.

It redesigns the conditions under which BSI is:

executed;

verified;

observed;

validated;

and considered complete.


The governing principle is:

A justified epistemic action must be determined by explicit execution rules, bound to the applicable verification capability, evidenced by an observable execution event where the environment permits, and evaluated by a Completion Gate that cannot be satisfied by assertion alone.

Where technical enforcement is available, it MUST be used.

Where technical enforcement is unavailable, the limitation MUST be explicitly recorded.

Self-audit may establish an execution state from the evidence available to the environment, but it cannot establish independent validation.

The Execution Architecture may evolve through controlled validation and calibration.

The BSI Knowledge Core remains invariant unless a separate, explicitly authorized core revision is made.

BSI 3.5 must not redesign BSI; it must redesign the conditions under which BSI is executed and considered complete.
