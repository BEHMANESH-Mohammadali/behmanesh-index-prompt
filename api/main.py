from fastapi import FastAPI
from api.routes.bsi import router as bsi_router
from api.routes.prompt import prompt_router
from api.mcp import mcp_router

app = FastAPI(
    title="Behmanesh Structural Index",
    version="3.5",
    description="BSI v3.5 canonical prompt package API; legacy scoring engine is explicitly identified.",
)
app.include_router(bsi_router, prefix="/bsi")
app.include_router(prompt_router, prefix="/bsi")
app.include_router(mcp_router)


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "framework_version": "3.5",
        "prompt_version": "3.5",
        "prompt_package_endpoint": "/bsi/prompt",
        "scoring_runtime": "legacy-v3.4.1",
        "scoring_runtime_is_v3_5": False,
    }
