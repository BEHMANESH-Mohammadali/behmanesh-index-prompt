from fastapi import APIRouter
from core.bsi_v35_runtime import run_v35_scoring
from core.bsi_scoring_v35 import ScoringInputError
from datetime import datetime

router = APIRouter()

FRAMEWORK_VERSION = "3.5"
ENGINE_STATUS = "V3_5_SCORING_CONNECTED"


@router.get("/version")
def version():
    return {
        "framework_version": FRAMEWORK_VERSION,
        "canonical_prompt_version": FRAMEWORK_VERSION,
        "engine_version": "3.5.0-explicit-input",
        "engine_status": ENGINE_STATUS,
        "v3_5_prompt_package": "/bsi/prompt",
        "scoring_endpoints_are_v3_5": True,
        "scoring_contract": "Explicit evidence-backed assessments required; no heuristic score generation from raw text.",
        "scoring_components": ["BSI_D1_D7", "EIG", "ECC_COMPONENT_GAPS", "REIG_DRAFT_AUDIT_INPUT"],
        "execution_scope": "EXPLICIT_INPUT_SCORING_ONLY",
        "autonomous_evidence_analysis": False,
        "draft_correction_loop": False,
        "api_version": "1.3.0",
        "endpoints": ["/bsi/score", "/bsi/analyze", "/bsi/compare", "/bsi/version", "/bsi/prompt"]
    }


@router.post("/score")
def score(payload: dict):
    text = payload.get("text", "")
    detail = payload.get("detail", False)
    assessment = payload.get("assessment")

    if len(text) < 10:
        return {"error": {"code": "TEXT_TOO_SHORT", "message": "Minimum length is 10"}}
    if not isinstance(assessment, dict):
        from fastapi import HTTPException
        raise HTTPException(
            status_code=422,
            detail={
                "code": "MISSING_V35_ASSESSMENT",
                "message": (
                    "BSI v3.5 scoring requires explicit evidence-backed D1-D7, EIG, "
                    "ECC component, and Draft Analysis REIG assessments. Raw text "
                    "alone is not converted into heuristic scores."
                ),
            },
        )
    try:
        result = run_v35_scoring(assessment)
    except ScoringInputError as exc:
        from fastapi import HTTPException
        raise HTTPException(
            status_code=422,
            detail={"code": "INVALID_V35_ASSESSMENT", "message": str(exc)},
        ) from exc

    result["timestamp"] = datetime.utcnow().isoformat()
    result["input_text_length"] = len(text)
    if not detail:
        result.pop("limitations", None)
    return result


@router.post("/analyze")
def analyze(payload: dict):
    text = payload.get("text", "")
    assessment = payload.get("assessment")
    if len(text) < 10:
        return {"error": {"code": "TEXT_TOO_SHORT", "message": "Minimum length is 10"}}
    if not isinstance(assessment, dict):
        from fastapi import HTTPException
        raise HTTPException(status_code=422, detail={
            "code": "MISSING_V35_ASSESSMENT",
            "message": "Provide explicit evidence-backed assessments; raw text is not heuristically scored.",
        })
    try:
        result = run_v35_scoring(assessment)
    except ScoringInputError as exc:
        from fastapi import HTTPException
        raise HTTPException(status_code=422, detail={
            "code": "INVALID_V35_ASSESSMENT", "message": str(exc)
        }) from exc
    result["timestamp"] = datetime.utcnow().isoformat()
    result["input_text_length"] = len(text)
    return result


@router.post("/compare")
def compare(payload: dict):
    text_a = payload.get("text_a", "")
    text_b = payload.get("text_b", "")
    assessment_a = payload.get("assessment_a")
    assessment_b = payload.get("assessment_b")
    if len(text_a) < 10 or len(text_b) < 10:
        return {"error": {"code": "TEXT_TOO_SHORT", "message": "Both texts must be at least 10 chars"}}
    if not isinstance(assessment_a, dict) or not isinstance(assessment_b, dict):
        from fastapi import HTTPException
        raise HTTPException(status_code=422, detail={
            "code": "MISSING_V35_ASSESSMENTS",
            "message": "Provide evidence-backed assessment_a and assessment_b; raw texts are not heuristically scored.",
        })
    try:
        result_a = run_v35_scoring(assessment_a)
        result_b = run_v35_scoring(assessment_b)
    except ScoringInputError as exc:
        from fastapi import HTTPException
        raise HTTPException(status_code=422, detail={
            "code": "INVALID_V35_ASSESSMENT", "message": str(exc)
        }) from exc
    a = result_a["BSI"]["BSI_score"]
    b = result_b["BSI"]["BSI_score"]
    return {
        "framework_version": FRAMEWORK_VERSION,
        "engine_version": "3.5.0-explicit-input",
        "engine_status": ENGINE_STATUS,
        "comparison_mode": "DESCRIPTIVE_SIDE_BY_SIDE",
        "text_a": result_a,
        "text_b": result_b,
        "difference": round(a - b, 4),
        "warning": "Scores are comparable only if assessment methods and evidence standards are equivalent. This endpoint does not rank authors or infer truth from score differences.",
        "timestamp": datetime.utcnow().isoformat(),
    }
