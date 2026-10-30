from fastapi import APIRouter
from core.bsi_engine import compute_bsi
from core.bsi_pipeline import run_pipeline
from datetime import datetime

router = APIRouter()

# The prompt framework is canonical v3.5, but these score routes still invoke
# the legacy v3.4.1 deterministic engine. Keep the distinction explicit.
FRAMEWORK_VERSION = "3.5"
LEGACY_ENGINE_VERSION = "3.4.1"
ENGINE_STATUS = "LEGACY_NOT_V3_5"


@router.get("/version")
def version():
    return {
        "framework_version": FRAMEWORK_VERSION,
        "canonical_prompt_version": FRAMEWORK_VERSION,
        "engine_version": LEGACY_ENGINE_VERSION,
        "engine_status": ENGINE_STATUS,
        "v3_5_prompt_package": "/bsi/prompt",
        "scoring_endpoints_are_v3_5": False,
        "pipeline_stages": ["BSI", "EIG", "ECC", "DRAFT", "REIG", "FINAL"],
        "api_version": "1.3.0",
        "endpoints": ["/bsi/score", "/bsi/analyze", "/bsi/compare", "/bsi/version", "/bsi/prompt"]
    }


@router.post("/score")
def score(payload: dict):
    text = payload.get("text", "")
    detail = payload.get("detail", False)
    full_pipeline = payload.get("pipeline", False)

    if len(text) < 10:
        return {"error": {"code": "TEXT_TOO_SHORT", "message": "Minimum length is 10"}}

    result = compute_bsi(text)
    details = result.get("details", {})

    if full_pipeline:
        pipeline_result = run_pipeline(text, details)
        pipeline_result["framework_version"] = FRAMEWORK_VERSION
        pipeline_result["engine_version"] = LEGACY_ENGINE_VERSION
        pipeline_result["engine_status"] = ENGINE_STATUS
        pipeline_result["version_warning"] = (
            "This pipeline uses the legacy v3.4.1 engine and is not a BSI v3.5 execution."
        )
        return pipeline_result

    metrics = details.get("metrics", {})
    layers = details.get("bsi_layers", {})

    response = {
        "framework_version": FRAMEWORK_VERSION,
        "engine_version": LEGACY_ENGINE_VERSION,
        "engine_status": ENGINE_STATUS,
        "timestamp": datetime.utcnow().isoformat(),
        "bsi_score": result["bsi"],
        "eig_score": result["eig"],
        "interpretation": result["label"],
        "version_warning": "Scores are produced by the legacy v3.4.1 engine, not a validated BSI v3.5 runtime."
    }

    if detail:
        response["components"] = metrics.get("BSI_criteria", {})
        response["eig_gaps"] = layers.get("meta", {}).get("EIG", {}).get("gaps", {})
        response["failure_modes"] = details.get("failure_modes", [])
        response["assumptions"] = layers.get("latent", {}).get("assumptions_excavated", [])
        response["themes"] = layers.get("latent", {}).get("themes", [])
        response["core_claim"] = layers.get("manifest", {}).get("core_claim", "")
        response["domain"] = details.get("domain", "")
        response["recommendations"] = [
            f for f in details.get("failure_modes", [])
            if f != "هیچ failure mode بحرانی شناسایی نشد"
        ]

    return response


@router.post("/analyze")
def analyze(payload: dict):
    text = payload.get("text", "")
    if len(text) < 10:
        return {"error": {"code": "TEXT_TOO_SHORT", "message": "Minimum length is 10"}}
    result = compute_bsi(text)
    details = result.get("details", {})
    response = run_pipeline(text, details)
    response["framework_version"] = FRAMEWORK_VERSION
    response["engine_version"] = LEGACY_ENGINE_VERSION
    response["engine_status"] = ENGINE_STATUS
    response["version_warning"] = "This analysis uses the legacy v3.4.1 engine and is not a BSI v3.5 execution."
    return response


@router.post("/compare")
def compare(payload: dict):
    text_a = payload.get("text_a", "")
    text_b = payload.get("text_b", "")

    if len(text_a) < 10 or len(text_b) < 10:
        return {"error": {"code": "TEXT_TOO_SHORT", "message": "Both texts must be at least 10 chars"}}

    result_a = compute_bsi(text_a)
    result_b = compute_bsi(text_b)

    bsi_a = result_a["bsi"]
    bsi_b = result_b["bsi"]
    eig_a = result_a["eig"]
    eig_b = result_b["eig"]

    if bsi_a > bsi_b:
        winner = "text_a"
        margin = round(bsi_a - bsi_b, 3)
    elif bsi_b > bsi_a:
        winner = "text_b"
        margin = round(bsi_b - bsi_a, 3)
    else:
        winner = "tie"
        margin = 0.0

    return {
        "framework_version": FRAMEWORK_VERSION,
        "engine_version": LEGACY_ENGINE_VERSION,
        "engine_status": ENGINE_STATUS,
        "version_warning": "Comparison uses the legacy v3.4.1 engine, not a validated BSI v3.5 runtime.",
        "timestamp": datetime.utcnow().isoformat(),
        "text_a": {
            "bsi_score": bsi_a,
            "eig_score": eig_a,
            "interpretation": result_a["label"]
        },
        "text_b": {
            "bsi_score": bsi_b,
            "eig_score": eig_b,
            "interpretation": result_b["label"]
        },
        "comparison": {
            "winner": winner,
            "bsi_margin": margin,
            "eig_delta": round(abs(eig_a - eig_b), 3),
            "verdict": (
                f"text_a از نظر BSI قوی‌تر است (+{margin})"
                if winner == "text_a" else
                f"text_b از نظر BSI قوی‌تر است (+{margin})"
                if winner == "text_b" else
                "هر دو متن امتیاز یکسانی دارند"
            )
        }
    }
