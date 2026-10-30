from core.prompt_registry import (
    AUTHORITATIVE_REFERENCES,
    PROMPT_VERSION,
    load_bsi_v35_package,
)


def test_canonical_prompt_package_is_complete_and_version_pinned():
    package = load_bsi_v35_package()
    assert package["prompt_version"] == "3.5"
    assert package["master_prompt"]["path"] == "MASTER_PROMPT_BSI_v3.5.md"
    assert package["master_prompt"]["sha256"]
    assert set(package["authoritative_references"]) == set(AUTHORITATIVE_REFERENCES)
    assert all(item["sha256"] and item["content"] for item in package["authoritative_references"].values())


def test_package_does_not_claim_to_execute_the_llm_or_compute_scores():
    package = load_bsi_v35_package()
    assert package["execution_mode"] == "external-llm-required"
    assert package["does_not_compute_scores"] is True
