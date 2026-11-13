"""BSI v3.5 execution handlers that reuse existing repository components.

This is a guarded integration layer, not a new BSI ontology or scoring method.
LLM output remains draft analysis. External retrieval signals remain leads,
not proof. Scoring is allowed only from explicitly supplied assessments.
"""
from __future__ import annotations

import json
import os
import re
from typing import Any, Mapping

from core.execution_orchestrator import StageResult
from core.prompt_registry import load_bsi_v35_package
from core.model_contracts import ModelRequest, ModelAdapterError, ModelRouter
from core.model_adapters import OpenAICompatibleChatAdapter, StaticModelRouter
from core.local_model_adapters import OllamaChatAdapter
from core.bsi_v35_runtime import run_v35_scoring
from core.bsi_scoring_v35 import ScoringInputError
from core.rag.rag_engine import evaluate_claim_with_rag
from core.bsi_engine import (
    extract_core_claim,
    excavate_assumptions,
    detect_domain,
)


def _task(context: Mapping[str, Any]) -> Mapping[str, Any]:
    task = context.get("task", {})
    return task if isinstance(task, Mapping) else {}


def _text(context: Mapping[str, Any]) -> str:
    task = _task(context)
    value = task.get("text") or task.get("content") or ""
    return value if isinstance(value, str) else ""


def _public_task(task: Mapping[str, Any]) -> dict[str, Any]:
    """Exclude runtime objects/secrets from prompts and JSON responses."""
    return {key: value for key, value in task.items() if key != "model_router"}


def _json_object(text: str) -> dict[str, Any]:
    candidate = text.strip()
    if candidate.startswith("```"):
        candidate = re.sub(r"^\`\`\`(?:json)?\s*|\s*\`\`\`$", "", candidate, flags=re.I)
    try:
        value = json.loads(candidate)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", candidate, flags=re.S)
        if not match:
            raise ValueError("Model output is not a JSON object.")
        value = json.loads(match.group(0))
    if not isinstance(value, dict):
        raise ValueError("Model output must be a JSON object.")
    return value


def _call_model(context: Mapping[str, Any], role: str, instruction: str, payload: Mapping[str, Any]) -> StageResult:
    router = _task(context).get("model_router")
    if router is None:
        return StageResult(
            output={"blocked": True, "block_reason": f"No model router configured for role '{role}'."},
            limitation="External or local LLM adapter is required for this analytical stage.",
        )
    try:
        adapter = router.resolve(role)
        prompt = load_bsi_v35_package()
        response = adapter.generate(ModelRequest(
            task=role,
            system_instruction=instruction,
            input_text=json.dumps({
                "task": _public_task(_task(context)),
                "stage_context": dict(payload),
                "canonical_prompt_package": prompt,
            }, ensure_ascii=False, default=str),
            temperature=0.0,
            max_output_tokens=int(_task(context).get("max_output_tokens", 6000)),
        ))
        parsed = _json_object(response.content)
        parsed["_model"] = {"provider": response.provider, "model": response.model, "request_id": response.request_id}
        parsed["_unverified_model_output"] = True
        return StageResult(output=parsed, verification_state="NOT_EXTERNALLY_VERIFIABLE",
                           limitation="Model output is draft analysis; claims require source-backed verification.")
    except Exception as exc:
        return StageResult(
            output={"blocked": True, "block_reason": f"{type(exc).__name__}: {exc}"},
            limitation="Model call or structured-output parsing failed; this stage is not complete.",
        )


def task_intake(context: Mapping[str, Any]) -> StageResult:
    text = _text(context)
    if len(text.strip()) < 10:
        return StageResult(output={"blocked": True, "block_reason": "Target text is missing or shorter than 10 characters."})
    task = _task(context)
    # Compute lightweight legacy candidates once and reuse them downstream.
    candidates = {
        "core_claim": extract_core_claim(text),
        "assumptions": excavate_assumptions(text),
        "detected_domain": detect_domain(text),
    }
    return StageResult(output={
        "task_type": task.get("task_type", "structural_analysis"),
        "target_id": task.get("target_id"),
        "text_length": len(text),
        "domain": task.get("domain") or candidates["detected_domain"],
        "candidate_artifacts": candidates,
        "external_verification_requested": bool(task.get("external_verification", True)),
        "unresolved_t8": False,
    })


def epistemic_need_assessment(context: Mapping[str, Any]) -> StageResult:
    text = _text(context)
    cues = {
        "quantitative": bool(re.search(r"\b\d+(?:\.\d+)?%?\b", text)),
        "causal": bool(re.search(r"\b(cause|causes|caused|because|effect|result in|leads to|باعث|علت|سبب)\b", text, re.I)),
        "generalization": bool(re.search(r"\b(always|never|all|every|universal|همیشه|هرگز|همه)\b", text, re.I)),
        "longitudinal": bool(re.search(r"\b(over time|previously|changed|evolved|در طول زمان|قبلاً|تغییر کرد)\b", text, re.I)),
        "source_dependent": bool(re.search(r"\b(research|study|report|according to|منبع|گزارش|پژوهش|طبق)\b", text, re.I)),
    }
    return StageResult(output={"risk_triggers": cues, "external_retrieval": True,
                               "need": "evidence-aware structural analysis"})


def effort_calibration(context: Mapping[str, Any]) -> StageResult:
    task = _task(context)
    text = _text(context)
    effort = task.get("effort_profile", "standard")
    if effort not in {"light", "standard", "deep"}:
        return StageResult(output={"blocked": True, "block_reason": "effort_profile must be light, standard, or deep."})
    return StageResult(output={"effort_profile": effort, "target_chars": len(text),
                               "model_roles": task.get("model_roles", ["analyst", "auditor"])})


def evidence_sufficiency(context: Mapping[str, Any]) -> StageResult:
    text = _text(context)
    has_refs = bool(re.search(r"https?://|doi\s*:", text, re.I))
    supplied = _task(context).get("source_materials", [])
    usable = [item for item in supplied if isinstance(item, Mapping)
              and isinstance(item.get("text"), str) and item.get("text", "").strip()
              and item.get("source_ref")]
    return StageResult(output={
        "source_references_in_target": has_refs,
        "inspected_source_materials_supplied": len(usable),
        "evidence_sufficiency": "SOURCE_TEXT_SUPPLIED_PENDING_CLAIM_AUDIT" if usable else "NOT_YET_ESTABLISHED",
        "gaps": [] if usable else ["Claims have not yet been linked to independently inspected source material."],
    }, evidence_refs=tuple(str(item["source_ref"]) for item in usable),
       verification_state="SOURCE_TEXT_SUPPLIED" if usable else "NOT_EXTERNALLY_VERIFIABLE")


def evidence_retrieval_or_gap_record(context: Mapping[str, Any]) -> StageResult:
    text = _text(context)
    if not text.strip():
        return StageResult(output={"blocked": True, "block_reason": "No target text available."})
    try:
        intake = context.get("task_intake", {})
        candidates = intake.get("candidate_artifacts", {}) if isinstance(intake, Mapping) else {}
        claim = candidates.get("core_claim") or extract_core_claim(text)
        rag = evaluate_claim_with_rag(claim)
        enabled = bool(rag.get("enabled"))
        sources = int(rag.get("retrieved_sources", 0) or 0)
        return StageResult(
            output={"candidate_core_claim": claim, "retrieval_enabled": enabled,
                    "retrieval_signal": rag, "source_count": sources,
                    "evidence_sufficiency": "PARTIAL_LEADS_ONLY" if sources else "INSUFFICIENT",
                    "gaps": [] if sources else ["No retrievable evidence returned; claim remains unverified."]},
            evidence_refs=tuple(str(x) for x in rag.get("source_refs", []) if x),
            verification_state="NOT_EXTERNALLY_VERIFIABLE",
            limitation="Experimental heuristic RAG is a retrieval lead, not proof; source-level inspection is not implemented by this backend.",
        )
    except Exception as exc:
        return StageResult(output={"blocked": True, "block_reason": f"Retrieval failed: {type(exc).__name__}: {exc}"},
                           limitation="Retrieval failed; completion must remain blocked.")


def counterevidence(context: Mapping[str, Any]) -> StageResult:
    text = _text(context)
    retrieval = context.get("evidence_retrieval_or_gap_record", {})
    if not isinstance(retrieval, Mapping):
        retrieval = {}
    signal = retrieval.get("retrieval_signal", {})
    if not isinstance(signal, Mapping):
        signal = {}
    supplied_sources = _task(context).get("source_materials", [])
    if not retrieval.get("source_count") and not supplied_sources:
        return StageResult(output={"blocked": True, "block_reason": "Counterevidence search has neither retrieval leads nor supplied source materials."},
                           limitation="Do not equate absence of retrieved evidence with support or absence of contradiction.")
    return _call_model(context, "auditor",
        "Find counterevidence and falsifiers for the target claims. Use only supplied source metadata as leads; do not invent sources. Return JSON with counterevidence, searched_sources, unresolved_gaps, and sufficient.",
        {"target_text": text, "retrieval_signal": signal,
         "source_materials": supplied_sources})


def competing_interpretations(context: Mapping[str, Any]) -> StageResult:
    prior = context.get("counterevidence", {})
    if not isinstance(prior, Mapping) or prior.get("blocked"):
        return StageResult(output={"blocked": True, "block_reason": "Counterevidence stage is blocked; competing-interpretation audit cannot be represented as complete."})
    return _call_model(context, "analyst",
        "Generate materially distinct interpretations and test each against the supplied content and evidence. Separate textual fact, inference, and hypothesis. Return JSON with interpretations, evidence_for_each, evidence_against_each, preferred_interpretation, uncertainty.",
        {"target_text": _text(context), "counterevidence": prior})


def structural_analysis(context: Mapping[str, Any]) -> StageResult:
    text = _text(context)
    prior = context.get("competing_interpretations", {})
    if not isinstance(prior, Mapping) or prior.get("blocked"):
        return StageResult(output={"blocked": True, "block_reason": "Competing-interpretation stage is blocked."})
    intake = context.get("task_intake", {})
    candidates = intake.get("candidate_artifacts", {}) if isinstance(intake, Mapping) else {}
    if not candidates:
        candidates = {
            "core_claim": extract_core_claim(text),
            "assumptions": excavate_assumptions(text),
            "detected_domain": detect_domain(text),
        }
    return _call_model(context, "analyst",
        "Perform BSI v3.5 structural analysis using the canonical prompt package. Return JSON with core_claim, manifest_layer, latent_layer, meta_layer, mechanisms, feedback_loops, leverage_points, claim_evidence_inference_graph, direct_statements, historical_reports, observations, inferences, hypotheses, counterevidence, uncertainty, limitations. Do not fabricate sources or scores.",
        {"target_text": text, "competing_interpretations": prior,
         "legacy_engine_extract": candidates})


def verification(context: Mapping[str, Any]) -> StageResult:
    analysis = context.get("structural_analysis", {})
    retrieval = context.get("evidence_retrieval_or_gap_record", {})
    if not isinstance(analysis, Mapping) or analysis.get("blocked"):
        return StageResult(output={"blocked": True, "block_reason": "No draft analysis to verify."})
    source_materials = _task(context).get("source_materials", [])
    usable_sources = [
        item for item in source_materials
        if isinstance(item, Mapping) and isinstance(item.get("text"), str)
        and item.get("text", "").strip() and item.get("source_ref")
    ]
    if not usable_sources:
        return StageResult(output={"blocked": True, "block_reason": "Source-level verification requires source_materials entries with source_ref and inspected text."},
                           verification_state="NOT_EXTERNALLY_VERIFIABLE",
                           limitation="RAG retrieval metadata/snippets do not establish source-level verification; provide inspected source text and a reference.")
    audited = _call_model(context, "auditor",
        "Audit each material claim against the supplied retrieval results. Do not claim to open or inspect sources unless source text/URL content is actually supplied. Return JSON with verified_claims, unverified_claims, contradictions, verification_state, unresolved_gaps. Any claim not directly supported by inspected source text must remain unverified.",
        {"draft_analysis": analysis, "retrieval_signal": retrieval.get("retrieval_signal"),
         "source_materials": usable_sources})
    if isinstance(audited.output, Mapping) and not audited.output.get("blocked"):
        return StageResult(
            output=audited.output,
            evidence_refs=tuple(str(item["source_ref"]) for item in usable_sources),
            verification_state="SOURCE_TEXT_REVIEWED_MODEL_ASSISTED",
            limitation="Source text was supplied and reviewed with model assistance; this is not independent validation.",
        )
    return audited


ASSUMPTION_CATEGORIES = (
    "methodological", "modeling", "generalizability", "value",
)


def _assumption_excavation_schema_errors(output: Mapping[str, Any]) -> list[str]:
    """Require observable coverage of the canonical four-step protocol."""
    errors: list[str] = []
    if not isinstance(output.get("conditional_formulations"), list) or not output["conditional_formulations"]:
        errors.append("conditional_formulations must be a non-empty list.")
    categories = output.get("category_review")
    if not isinstance(categories, Mapping):
        errors.append("category_review must cover all four canonical categories.")
    else:
        for category in ASSUMPTION_CATEGORIES:
            item = categories.get(category)
            if not isinstance(item, Mapping):
                errors.append(f"category_review.{category} is missing.")
                continue
            if item.get("status") not in {"FINDINGS", "NONE_IDENTIFIED", "NOT_APPLICABLE"}:
                errors.append(f"category_review.{category}.status is invalid.")
            if item.get("status") == "NONE_IDENTIFIED" and not str(item.get("rationale", "")).strip():
                errors.append(f"category_review.{category} requires a no-finding rationale.")
    assumptions = output.get("assumptions")
    if not isinstance(assumptions, list):
        errors.append("assumptions must be a list.")
    else:
        for index, item in enumerate(assumptions):
            if not isinstance(item, Mapping):
                errors.append(f"assumptions[{index}] must be an object.")
                continue
            for field in ("category", "assumption", "rank", "evidence_label", "counterfactual_effect", "core_claim_link"):
                if not str(item.get(field, "")).strip():
                    errors.append(f"assumptions[{index}].{field} is required.")
            if item.get("category") not in ASSUMPTION_CATEGORIES:
                errors.append(f"assumptions[{index}].category is invalid.")
            if item.get("rank") not in {"foundational", "supporting", "secondary"}:
                errors.append(f"assumptions[{index}].rank is invalid.")
            if item.get("evidence_label") not in {"FACT", "INFERENCE"}:
                errors.append(f"assumptions[{index}].evidence_label must be FACT or INFERENCE.")
            if item.get("rank") == "foundational" and not str(item.get("author_awareness", "")).strip():
                errors.append(f"assumptions[{index}] foundational item requires author_awareness.")
    tests = output.get("counterfactual_tests")
    if not isinstance(tests, list) or any(
        not isinstance(item, Mapping) or not str(item.get("assumption", "")).strip()
        or not str(item.get("effect_if_false", "")).strip() for item in tests
    ):
        errors.append("counterfactual_tests must be a list of complete tests (or an explicit empty list).")
    if not str(output.get("synthesis", "")).strip():
        errors.append("synthesis is required.")
    if not isinstance(output.get("limitations"), list):
        errors.append("limitations must be a list.")
    return errors


def assumption_excavation(context: Mapping[str, Any]) -> StageResult:
    text = _text(context)
    analysis = context.get("structural_analysis", {})
    intake = context.get("task_intake", {})
    candidates = intake.get("candidate_artifacts", {}) if isinstance(intake, Mapping) else {}
    assumptions = candidates.get("assumptions")
    if assumptions is None:
        assumptions = excavate_assumptions(text)
    protocol = load_bsi_v35_package()["authoritative_references"]["assumption_excavation_protocol"]["content"]
    result = _call_model(
        context, "analyst",
        "Execute the complete canonical Assumption Excavation Protocol v1.1 in canonical_protocol. "
        "Legacy heuristic candidates are leads only, never findings or completion. Step 1: formulate each key claim "
        "as If X, then Y, or state why it cannot be conditionally formulated. Step 2: explicitly review all four "
        "categories: methodological, modeling, generalizability, value; include NONE_IDENTIFIED with rationale "
        "where applicable. Step 3: counterfactually test every identified assumption, classify impact as foundational, "
        "supporting, or secondary, and assess author awareness only from textual evidence; absence of explanation is "
        "not proof of unawareness. Step 4: synthesize the pattern and connect every foundational assumption to Core Claim. "
        "Label direct textual support FACT and analyst inference INFERENCE; do not infer intent or invent numeric weights. "
        "Return conditional_formulations, category_review, assumptions, counterfactual_tests, synthesis, limitations. "
        "Each assumption requires category, assumption, rank, evidence_label, counterfactual_effect, core_claim_link; "
        "foundational items also require author_awareness.",
        {"target_text": text, "draft_analysis": analysis, "canonical_protocol": protocol,
         "legacy_heuristic_candidates": assumptions},
    )
    if not isinstance(result.output, Mapping) or result.output.get("blocked"):
        return result
    errors = _assumption_excavation_schema_errors(result.output)
    if errors:
        return StageResult(
            output={"blocked": True, "block_reason": "Assumption Excavation four-step protocol output is incomplete.",
                    "schema_errors": errors, "partial_output": dict(result.output)},
            limitation="The output did not demonstrate all four steps and category coverage; completion is blocked.",
        )
    return result


def eig(context: Mapping[str, Any]) -> StageResult:
    analysis = context.get("structural_analysis", {})
    verification_result = context.get("verification", {})
    if not isinstance(analysis, Mapping) or not isinstance(verification_result, Mapping):
        return StageResult(output={"blocked": True, "block_reason": "Analysis or verification data is missing."})
    return _call_model(context, "analyst",
        "Assess EIG components MCG, CEG, FCG, LCG according to canonical EIG reference. Values must be evidence-justified; do not guess. Return JSON with raw_gaps (MCG, CEG, FCG, LCG each 0..10), lcg_interpretation (Evolution/Rupture/Unknown), evidence_for_each_gap, missing_evidence, and ready_for_scoring boolean. If any value cannot be justified, set ready_for_scoring=false.",
        {"draft_analysis": analysis, "verification": verification_result,
         "retrieval": context.get("evidence_retrieval_or_gap_record")})


def ecc(context: Mapping[str, Any]) -> StageResult:
    analysis = context.get("structural_analysis", {})
    verification_result = context.get("verification", {})
    return _call_model(context, "analyst",
        "Calibrate the confidence of the draft claims using the canonical ECC v2.0 reference. Return JSON with claimed_confidence, supported_evidence, supported_method, supported_conclusion (0..100), evidence_basis, uncertainty, ready_for_scoring. Do not infer confidence from rhetoric.",
        {"draft_analysis": analysis, "verification": verification_result})


def draft_analysis(context: Mapping[str, Any]) -> StageResult:
    analysis = context.get("structural_analysis", {})
    assumptions = context.get("assumption_excavation", {})
    verification_result = context.get("verification", {})
    eig_result = context.get("eig", {})
    ecc_result = context.get("ecc", {})
    if any(not isinstance(x, Mapping) or x.get("blocked") for x in (analysis, assumptions, verification_result, eig_result, ecc_result)):
        return StageResult(output={"blocked": True, "block_reason": "Required analysis, assumption excavation, verification, EIG, or ECC is blocked."})
    return StageResult(output={
        "draft": {"structural_analysis": analysis, "assumption_excavation": assumptions,
                  "verification": verification_result, "eig": context.get("eig"), "ecc": context.get("ecc")},
        "status": "DRAFT_NOT_FINAL",
    }, verification_state="NOT_EXTERNALLY_VERIFIABLE",
       limitation="Draft contains model-generated analysis and source leads; source inspection is not independently established.")


def reig_draft_audit(context: Mapping[str, Any]) -> StageResult:
    draft = context.get("draft_analysis", {})
    if not isinstance(draft, Mapping) or draft.get("blocked"):
        return StageResult(output={"blocked": True, "block_reason": "Draft Analysis unavailable for REIG."})
    return _call_model(context, "auditor",
        "Apply official REIG dimensions ERG, MRG, CRG, ARG, FRG (0..4) to the Draft Analysis itself, not the target text. Return JSON with scores, evidence_for_each_dimension, defects, needs_reanalysis, ready_for_scoring. Do not treat model self-audit as independent evaluation.",
        {"draft_analysis": draft})


def correction_and_reanalysis(context: Mapping[str, Any]) -> StageResult:
    audit = context.get("reig_draft_audit", {})
    draft = context.get("draft_analysis", {})
    if not isinstance(audit, Mapping) or audit.get("blocked") or not isinstance(draft, Mapping) or draft.get("blocked"):
        return StageResult(output={"blocked": True, "block_reason": "Correction cannot run without a draft and REIG audit."})
    previous = context.get("previous_correction")
    if isinstance(previous, Mapping):
        current_draft = previous.get("corrected_draft", draft)
        current_audit = previous.get("reig_audit", audit)
        if not previous.get("needs_reanalysis") and not previous.get("defects_remaining"):
            return StageResult(output={**dict(previous), "needs_reanalysis": False,
                                       "corrected_draft": current_draft,
                                       "reig_audit": current_audit,
                                       "ready_for_scoring": bool(previous.get("ready_for_scoring") and current_audit.get("ready_for_scoring"))})
        draft, audit = current_draft, current_audit
    elif not audit.get("needs_reanalysis"):
        return StageResult(output={"needs_reanalysis": False, "corrected_draft": draft,
                                   "reig_audit": audit, "ready_for_scoring": bool(audit.get("ready_for_scoring"))})
    corrected = _call_model(context, "analyst",
        "Correct only defects identified by the REIG audit. Preserve source/evidence distinctions and all explicit uncertainties. Return JSON with corrected_draft, defects_remaining, needs_reanalysis, ready_for_scoring.",
        {"draft_analysis": draft, "reig_audit": audit})
    if isinstance(corrected.output, Mapping) and not corrected.output.get("blocked"):
        corrected_draft = corrected.output.get("corrected_draft")
        if not isinstance(corrected_draft, Mapping):
            return StageResult(output={"blocked": True, "block_reason": "Correction model did not return a corrected_draft object."})
        refreshed_audit = reig_draft_audit({**context, "draft_analysis": corrected_draft})
        if not isinstance(refreshed_audit.output, Mapping) or refreshed_audit.output.get("blocked"):
            return StageResult(output={"blocked": True, "block_reason": "REIG could not be rerun against the corrected draft."},
                               limitation=refreshed_audit.limitation)
        refreshed = refreshed_audit.output
        defects_remaining = bool(corrected.output.get("defects_remaining"))
        needs_reanalysis = bool(corrected.output.get("needs_reanalysis") or refreshed.get("needs_reanalysis") or defects_remaining)
        return StageResult(
            output={**dict(corrected.output), "corrected_draft": corrected_draft,
                    "reig_audit": refreshed, "needs_reanalysis": needs_reanalysis,
                    "ready_for_scoring": bool(corrected.output.get("ready_for_scoring")
                                              and refreshed.get("ready_for_scoring")
                                              and not needs_reanalysis)},
            evidence_refs=corrected.evidence_refs,
            verification_state=corrected.verification_state,
            limitation=corrected.limitation or "REIG was rerun after correction; model-assisted self-audit is not independent validation.",
        )
    return corrected


def final_reread(context: Mapping[str, Any]) -> StageResult:
    correction = context.get("correction_and_reanalysis", {})
    if not isinstance(correction, Mapping) or correction.get("blocked"):
        return StageResult(output={"blocked": True, "block_reason": "No corrected draft available."})
    if correction.get("needs_reanalysis") or correction.get("defects_remaining"):
        return StageResult(output={"blocked": True, "block_reason": "Unresolved defects remain after correction."})
    return _call_model(context, "auditor",
        "Final re-read for omissions, contradictions, unsupported claims, false verification, missing limitations, and scope violations. Return JSON with passed, defects, unresolved_gaps, ready_for_final. Set passed=false if any material issue remains.",
        {"corrected_draft": correction.get("corrected_draft", correction.get("draft"))})


def execution_status(context: Mapping[str, Any]) -> StageResult:
    reread = context.get("final_reread", {})
    if (
        not isinstance(reread, Mapping)
        or reread.get("blocked")
        or reread.get("passed") is not True
        or reread.get("ready_for_final") is not True
    ):
        return StageResult(output={
            "blocked": True,
            "block_reason": "Final re-read must explicitly pass and set ready_for_final=true.",
        })
    unresolved_t8 = any(
        isinstance(context.get(name), Mapping)
        and bool(context[name].get("unresolved_t8"))
        for name in ("structural_analysis", "verification", "counterevidence",
                     "competing_interpretations", "assumption_excavation")
    )
    return StageResult(output={"status": "SELF_AUDIT_ONLY", "independently_validated": False,
                               "unresolved_t8": unresolved_t8,
                               "ready_for_completion": not unresolved_t8})


def ecc_assessment(context: Mapping[str, Any]) -> StageResult:
    return ecc(context)


def build_bsi_v35_handlers() -> dict[str, Any]:
    """Return the canonical stage-name -> handler map used by the orchestrator."""
    return {
        "task_intake": task_intake,
        "epistemic_need_assessment": epistemic_need_assessment,
        "effort_calibration": effort_calibration,
        "evidence_sufficiency": evidence_sufficiency,
        "evidence_retrieval_or_gap_record": evidence_retrieval_or_gap_record,
        "counterevidence": counterevidence,
        "competing_interpretations": competing_interpretations,
        "structural_analysis": structural_analysis,
        "verification": verification,
        "assumption_excavation": assumption_excavation,
        "eig": eig,
        "ecc": ecc_assessment,
        "draft_analysis": draft_analysis,
        "reig_draft_audit": reig_draft_audit,
        "correction_and_reanalysis": correction_and_reanalysis,
        "final_reread": final_reread,
        "execution_status": execution_status,
    }


def execute_bsi_v35(task: Mapping[str, Any]) -> dict[str, Any]:
    """Execute analysis lifecycle and calculate scores only when every assessment is explicit."""
    from core.execution_orchestrator import BSIExecutionOrchestrator

    result = BSIExecutionOrchestrator(build_bsi_v35_handlers()).run(task)
    response: dict[str, Any] = {
        "execution_id": result.execution_id,
        "completion": result.completion,
        "trace": [
            {"stage": r.stage, "status": r.status.value, "evidence_refs": r.evidence_refs,
             "verification_state": r.verification_state, "limitation": r.limitation}
            for r in result.trace.stages
        ],
        "outputs": {**result.outputs, "task": _public_task(_task({"task": task}))},
        "scoring": None,
    }
    if not result.completion["authorized"]:
        response["status"] = "BLOCKED"
        return response

    correction = result.outputs.get("correction_and_reanalysis", {})
    audit = correction.get("reig_audit", {}) if isinstance(correction, Mapping) else {}
    analysis = correction.get("corrected_draft", {}) if isinstance(correction, Mapping) else {}
    eig_result = result.outputs.get("eig", {})
    ecc_result = result.outputs.get("ecc", {})
    task_scope = _task({"task": task}).get("content_scope", "single_content")
    dimension_scores = task.get("dimension_scores")
    dimension_evidence = task.get("dimension_score_evidence")
    # D2-SI is an optional, explicitly supplied scoring payload. Do not infer it
    # merely from single_content scope: the governing single-content D2 basis
    # remains internal_coherence_only unless a separately authorized payload
    # and its evidence basis are supplied.
    d2_si_scores = task.get("d2_si_scores")
    d2_si_evidence = task.get("d2_si_score_evidence")
    eig_basis = eig_result.get("evidence_for_each_gap") if isinstance(eig_result, Mapping) else None
    ecc_basis = ecc_result.get("evidence_basis") if isinstance(ecc_result, Mapping) else None
    reig_basis = audit.get("evidence_for_each_dimension") if isinstance(audit, Mapping) else None
    def _has_basis(value: Any, keys: tuple[str, ...] | None = None) -> bool:
        if not isinstance(value, Mapping):
            return False
        if keys is not None and not set(keys).issubset(value):
            return False
        return all(bool(value.get(key)) for key in (keys or tuple(value.keys())))
    required_eig = ("MCG", "CEG", "FCG", "LCG")
    required_reig = ("ERG", "MRG", "CRG", "ARG", "FRG")
    required_dimensions = tuple(f"D{i}" for i in range(1, 8))
    if (not isinstance(dimension_scores, Mapping)
            or not set(required_dimensions).issubset(dimension_scores)
            or not _has_basis(dimension_evidence, required_dimensions)
            or (d2_si_scores is not None and (
                task_scope != "single_content"
                or not isinstance(d2_si_scores, Mapping)
                or set(d2_si_scores) != {"I", "D", "C", "R"}
                or not _has_basis(d2_si_evidence, ("I", "D", "C", "R"))
            ))
            or not isinstance(eig_result, Mapping) or not eig_result.get("ready_for_scoring")
            or not _has_basis(eig_basis, required_eig)
            or not isinstance(ecc_result, Mapping) or not ecc_result.get("ready_for_scoring")
            or not ecc_basis
            or not isinstance(audit, Mapping) or not audit.get("ready_for_scoring")
            or not _has_basis(reig_basis, required_reig)):
        response["status"] = "ANALYSIS_COMPLETE_SCORING_BLOCKED"
        response["completion"] = {"authorized": False, "status": "BLOCKED",
                                  "blockers": ["Evidence basis is missing for one or more explicit D1-D7, EIG, ECC, or Draft Analysis REIG inputs."]}
        return response
    try:
        assessment = {
            "dimension_scores": dimension_scores,
            "eig_gaps": eig_result["raw_gaps"],
            "lcg_interpretation": eig_result["lcg_interpretation"],
            "calculation_mode": task.get("calculation_mode"),
            "content_scope": task_scope,
            "d2_assessment_basis": "internal_coherence_only" if task_scope == "single_content" else "longitudinal_evidence",
            "ecc": {k: ecc_result[k] for k in ("claimed_confidence", "supported_evidence", "supported_method", "supported_conclusion")},
            "reig": audit.get("scores"),
        }
        if d2_si_scores is not None:
            assessment["d2_si_scores"] = d2_si_scores
        response["scoring"] = run_v35_scoring(assessment)
        response["status"] = "COMPLETED_WITH_EXPLICIT_ASSESSMENTS"
    except (ScoringInputError, KeyError, TypeError) as exc:
        response["status"] = "ANALYSIS_COMPLETE_SCORING_BLOCKED"
        response["completion"] = {"authorized": False, "status": "BLOCKED", "blockers": [f"Scoring inputs invalid or incomplete: {exc}"]}
    return response



def configured_model_router() -> StaticModelRouter:
    """Build analyst/auditor roles from explicit environment configuration.

    Local Ollama is preferred when role-specific or shared local model names are
    supplied. Otherwise an OpenAI-compatible endpoint must be explicitly set.
    No network call occurs until a stage invokes generate().
    """
    shared_local = os.getenv("BSI_OLLAMA_MODEL", "").strip()
    analyst_local = os.getenv("BSI_OLLAMA_MODEL_ANALYST", shared_local).strip()
    auditor_local = os.getenv("BSI_OLLAMA_MODEL_AUDITOR", shared_local).strip()
    if analyst_local and auditor_local:
        return StaticModelRouter({
            "analyst": OllamaChatAdapter(model=analyst_local),
            "auditor": OllamaChatAdapter(model=auditor_local),
        })

    base_url = os.getenv("BSI_MODEL_BASE_URL", "").strip()
    shared_model = os.getenv("BSI_MODEL_NAME", "").strip()
    analyst_model = os.getenv("BSI_MODEL_NAME_ANALYST", shared_model).strip()
    auditor_model = os.getenv("BSI_MODEL_NAME_AUDITOR", shared_model).strip()
    if base_url and analyst_model and auditor_model:
        return StaticModelRouter({
            "analyst": OpenAICompatibleChatAdapter(
                base_url=base_url, model=analyst_model,
                api_key=os.getenv("BSI_MODEL_API_KEY", ""),
                provider_label=os.getenv("BSI_MODEL_PROVIDER", "openai-compatible"),
            ),
            "auditor": OpenAICompatibleChatAdapter(
                base_url=base_url, model=auditor_model,
                api_key=os.getenv("BSI_MODEL_API_KEY", ""),
                provider_label=os.getenv("BSI_MODEL_PROVIDER", "openai-compatible"),
            ),
        })
    raise ModelAdapterError(
        "Configure BSI_OLLAMA_MODEL (or role-specific Ollama model names), "
        "or BSI_MODEL_BASE_URL plus BSI_MODEL_NAME (or role-specific names)."
    )
