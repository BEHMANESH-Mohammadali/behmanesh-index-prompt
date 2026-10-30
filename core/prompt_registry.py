"""Version-pinned loader for the canonical BSI v3.5 prompt package.

This loader supplies the prompt and its authoritative references to an external
LLM generator. It does not itself execute an LLM or calculate BSI scores.
"""
from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
PROMPT_VERSION = "3.5"
PROMPT_PATH = "MASTER_PROMPT_BSI_v3.5.md"

AUTHORITATIVE_REFERENCES = {
    "architectural_invariants": "ARCHITECTURAL_INVARIANTS_BSI_v3.5.md",
    "execution_architecture": "BSI_3.5_Execution_Architecture.md",
    "output_contract": "docs/specification/ANALYTICAL_OUTPUT_CONTRACT_LAYERC_v3.5.md",
    "canonical_specification_matrix": "docs/specification/CANONICAL_SPECIFICATION_MATRIX_v3.5.md",
    "core_behmanesh": "CORE-BEHMANESH/v1.0/CORE_BEHMANESH_v1.0.md",
    "bio": "Ontology/BIO_v1.0.md",
    "sop": "SOP_Intellectual_Content_Analysis_v3.4.2.md",
    "eig": "CORE-BEHMANESH/Shared_Components/EIG/Epistemic_Integrity_Gap_Analyzer_v1.0.md",
    "ecc": "CORE-BEHMANESH/Shared_Components/EIG/Epistemic_Confidence_Calibration_v2.0.md",
    "reig": "CORE-BEHMANESH/Shared_Components/EIG/Recursive_EIG_v1.0.md",
    "calculation_formula": "BSI_Calculation_Formula_Hybrid_v3x.md",
}


class PromptPackageError(RuntimeError):
    """Raised when a required prompt or reference is missing or unreadable."""


def _read_verified(relative_path: str) -> dict[str, str]:
    path = (REPOSITORY_ROOT / relative_path).resolve()
    if REPOSITORY_ROOT not in path.parents:
        raise PromptPackageError(f"Reference escapes repository root: {relative_path}")
    if not path.is_file():
        raise PromptPackageError(f"Required BSI v3.5 file is missing: {relative_path}")
    try:
        content = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise PromptPackageError(f"Cannot read required file {relative_path}: {exc}") from exc
    digest = hashlib.sha256(content.encode("utf-8")).hexdigest()
    return {"path": relative_path, "sha256": digest, "content": content}


def load_bsi_v35_package() -> dict[str, Any]:
    """Return a complete, version-pinned prompt package for a downstream generator."""
    prompt = _read_verified(PROMPT_PATH)
    references = {
        key: _read_verified(path)
        for key, path in AUTHORITATIVE_REFERENCES.items()
    }
    return {
        "package_schema": "bsi-prompt-package/v1",
        "prompt_version": PROMPT_VERSION,
        "prompt_status": "canonical-prompt-runtime-integration-pending",
        "execution_mode": "external-llm-required",
        "does_not_compute_scores": True,
        "master_prompt": prompt,
        "authoritative_references": references,
    }
