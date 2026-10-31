"""MCP-compatible interface for the explicit-input BSI v3.5 scoring runtime."""
from datetime import datetime

from fastapi import APIRouter
from core.bsi_scoring_v35 import ScoringInputError
from core.bsi_v35_runtime import run_v35_scoring

mcp_router = APIRouter()


@mcp_router.get("/mcp")
def mcp_manifest():
    return {
        "schema_version": "v1",
        "name": "BSI Analyzer",
        "description": "Behmanesh Structural Index v3.5 explicit-input scoring interface.",
        "tools": [{
            "name": "analyze_with_bsi",
            "description": "Calculate BSI v3.5 from explicit evidence-backed assessments. Raw text alone is not heuristically scored.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "text": {"type": "string", "description": "The source content being assessed"},
                    "assessment": {"type": "object", "description": "Evidence-backed D1-D7, EIG, ECC, REIG, calculation mode, and explicit D2 evidence scope."},
                },
                "required": ["text", "assessment"],
            },
        }],
    }


@mcp_router.post("/mcp/call")
def mcp_call(payload: dict):
    tool = payload.get("tool")
    params = payload.get("params", {})
    if tool != "analyze_with_bsi":
        return {"error": {"code": "UNKNOWN_TOOL", "message": "Unknown MCP tool"}}

    text = params.get("text", "")
    assessment = params.get("assessment")
    if not isinstance(text, str) or len(text) < 10:
        return {"error": {"code": "TEXT_TOO_SHORT", "message": "Minimum length is 10"}}
    if not isinstance(assessment, dict):
        return {"error": {"code": "MISSING_V35_ASSESSMENT", "message": "Provide explicit evidence-backed assessments; raw text is not heuristically scored."}}

    try:
        result = run_v35_scoring(assessment)
    except ScoringInputError as exc:
        return {"error": {"code": "INVALID_V35_ASSESSMENT", "message": str(exc)}}

    result["timestamp"] = datetime.utcnow().isoformat()
    result["input_text_length"] = len(text)
    return {"result": result}
