"""API endpoint for guarded end-to-end BSI v3.5 execution."""
from fastapi import APIRouter, HTTPException

from core.bsi_v35_execution import execute_bsi_v35, configured_model_router
from core.model_contracts import ModelAdapterError

execution_router = APIRouter()


@execution_router.post("/execute")
def execute(payload: dict):
    """Run the canonical execution lifecycle; incomplete stages fail closed."""
    text = payload.get("text") or payload.get("content") or ""
    if not isinstance(text, str) or len(text.strip()) < 10:
        raise HTTPException(status_code=422, detail={
            "code": "TEXT_TOO_SHORT",
            "message": "Provide target text of at least 10 characters.",
        })
    try:
        router = configured_model_router()
    except ModelAdapterError as exc:
        raise HTTPException(status_code=503, detail={
            "code": "MODEL_ROUTER_NOT_CONFIGURED",
            "message": str(exc),
        }) from exc

    task = dict(payload)
    task.pop("model_router", None)
    task["model_router"] = router
    return execute_bsi_v35(task)
