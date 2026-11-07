# D2-SI Inter-Rater Calibration Protocol v0.1

**Status:** Protocol prepared; empirical inter-rater study not yet conducted.  
**Scope:** Proposed D2-SI single-content operationalization only. This protocol does not redefine canonical longitudinal D2 or BIO v1.0.

## 1. Objective

Evaluate whether independent evaluators can apply the 0–4 behavioral anchors consistently to Internal Structural Coherence (I), Developmental Consistency (D), Cross-Context Transfer (C), and Reflective Integration (R), including the distinction between numeric scores and N/A / INSUFFICIENT_EVIDENCE / NOT_ASSESSED.

## 2. Calibration corpus

Use a deliberately varied set of standalone intellectual artifacts. Include:
- clear positive and negative examples for each dimension;
- boundary cases around 1/2 and 2/3;
- examples where one dimension is strong and another weak;
- cases with no genuine transfer opportunity (C=N/A);
- cases with an attempted but invalid transfer (C remains applicable and receives a numeric score);
- cases with acknowledged limitations that are not integrated downstream;
- cases with genuine reflective revision;
- cases where evidence is insufficient despite the dimension being applicable.

Do not construct the corpus only from idealized examples. Include naturalistic content and domain diversity. Record provenance, content scope, and any editing or synthetic construction. Synthetic vignettes may test anchor interpretation but must not be represented as empirical validation.

## 3. Independent rating procedure

1. Select at least two evaluators who understand the rubric.
2. Provide the same source artifacts and the same version of the rubric.
3. Hide reference labels and other evaluators' scores during the independent pass.
4. Require each evaluator to record, for every dimension: score/state, exact evidence location, anchor rationale, counterevidence/defect, and confidence.
5. Do not discuss cases or reconcile scores before independent ratings are locked.
6. Preserve original ratings; adjudication must be a separate record and must never overwrite the independent observations.

## 4. Agreement analysis

Report results separately for I, D, C, and R. For ordinal 0–4 scores:
- report exact agreement and adjacent-score agreement;
- provide the full confusion matrix;
- calculate a weighted Cohen's kappa for two raters, or an appropriate multi-rater ordinal agreement statistic when more than two raters participate;
- report confidence intervals where the sample size supports them.

For the numeric D2-SI aggregate, report an absolute-agreement intraclass correlation only when the study design and number of raters support the selected ICC model. State the exact model and unit (single-rater or average-rater). Do not substitute aggregate agreement for dimension-level agreement.

Report N/A, INSUFFICIENT_EVIDENCE, and NOT_ASSESSED separately. Do not force non-score states into numeric bins to inflate agreement. Examine disagreements around 1/2 and 2/3 qualitatively and identify whether they arise from ambiguous anchors, insufficient evidence, or evaluator error.

No pass threshold is prescribed in this protocol. Establish any acceptance threshold before examining the results and justify it for the intended use.

## 5. Adjudication and revision control

After independent agreement is measured:
- review disagreements against the source evidence and exact anchor wording;
- identify recurring ambiguity or dimension overlap;
- revise anchors only when the evidence shows a systematic interpretation problem;
- version every rubric revision;
- rerun the calibration set after material changes;
- preserve prior scores and explain any re-adjudication.

Do not silently tune anchors to one evaluator's preferred scoring pattern.

## 6. Double-penalty audit

For any underlying defect attributed to multiple dimensions, require distinct evidence references and a separate rationale for each alleged failure. The code-level traceability guard checks distinct evidence identifiers; human review must still determine whether the evidence establishes genuinely distinct failures rather than relabeling one defect.

## 7. Reporting template

For each study, report:
- rubric version and corpus version;
- number and background of evaluators;
- number and provenance of artifacts;
- independent ratings and missing/non-score states;
- per-dimension exact/adjacent agreement and ordinal statistic;
- aggregate reliability statistic, if appropriate;
- disagreement analysis;
- adjudicated outcomes in a separate layer;
- limitations, confidence intervals, and unresolved ambiguities.

**Current state:** The protocol is ready for use. No independent evaluator data, inter-rater coefficient, or empirical reliability claim is available yet.
