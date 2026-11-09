"""Version-pinned loader for the canonical BSI v3.5 prompt package.

This loader supplies the prompt and its authoritative references to an external
LLM generator. It does not itself execute an LLM or calculate BSI scores.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
PROMPT_VERSION = "3.5"
PROMPT_PATH = "MASTER_PROMPT_BSI_v3.5.md"
INTEGRITY_MANIFEST_PATH = "docs/integration/BSI_V35_PROMPT_PACKAGE_INTEGRITY.json"

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


def _load_integrity_manifest() -> dict[str, str]:
    path = (REPOSITORY_ROOT / INTEGRITY_MANIFEST_PATH).resolve()
    if REPOSITORY_ROOT not in path.parents or not path.is_file():
        raise PromptPackageError("Canonical prompt integrity manifest is missing.")
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
        if manifest.get("schema") != "bsi-v35-content-integrity/v1":
            raise ValueError("Unsupported integrity manifest schema.")
        files = manifest.get("files")
        if not isinstance(files, dict) or not files:
            raise ValueError("Integrity manifest has no file hashes.")
        return files
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        raise PromptPackageError(f"Cannot load canonical integrity manifest: {exc}") from exc


def _read_verified(relative_path: str, expected_hashes: dict[str, str]) -> dict[str, str]:
    path = (REPOSITORY_ROOT / relative_path).resolve()
    if REPOSITORY_ROOT not in path.parents:
        raise PromptPackageError(f"Reference escapes repository root: {relative_path}")
    if not path.is_file():
        raise PromptPackageError(f"Required BSI v3.5 file is missing: {relative_path}")
    try:
        content = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise PromptPackageError(f"Cannot read required file {relative_path}: {exc}") from exc
    encoded = content.encode("utf-8")
    digest = hashlib.sha256(encoded).hexdigest()
    expected_git_blob = expected_hashes.get(relative_path)
    actual_git_blob = hashlib.sha1(
        f"blob {len(encoded)}\\0".encode("ascii") + encoded
    ).hexdigest()
    if expected_git_blob is None:
        raise PromptPackageError(f"No pinned integrity hash for required file: {relative_path}")
    if actual_git_blob != expected_git_blob:
        raise PromptPackageError(
            f"Canonical prompt integrity mismatch for {relative_path}: "
            f"expected {expected_git_blob}, got {actual_git_blob}"
        )
    return {"path": relative_path, "sha256": digest, "git_blob_sha1": actual_git_blob, "content": content}


def load_bsi_v35_package() -> dict[str, Any]:
    """Return a complete, version-pinned prompt package for a downstream generator."""
    expected_hashes = _load_integrity_manifest()
    prompt = _read_verified(PROMPT_PATH, expected_hashes)
    references = {
        key: _read_verified(path, expected_hashes)
        for key, path in AUTHORITATIVE_REFERENCES.items()
    }
    return {
        "package_schema": "bsi-prompt-package/v1",
        "prompt_version": PROMPT_VERSION,
        "prompt_status": "canonical-prompt-first-portable-candidate",
        "execution_mode": "prompt-only-supported; optional-runtime-integration",
        "does_not_compute_scores": True,
        "master_prompt": prompt,
        "authoritative_references": references,
    }
