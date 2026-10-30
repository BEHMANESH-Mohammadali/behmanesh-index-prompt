from fastapi import APIRouter, HTTPException

from core.prompt_registry import PromptPackageError, load_bsi_v35_package

prompt_router = APIRouter()


@prompt_router.get("/prompt")
def get_canonical_prompt_package():
    """Return the pinned BSI v3.5 prompt and all required authoritative references."""
    try:
        return load_bsi_v35_package()
    except PromptPackageError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
