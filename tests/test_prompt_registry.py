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
    assert package["master_prompt"]["git_blob_sha1"]
    assert set(package["authoritative_references"]) == set(AUTHORITATIVE_REFERENCES)
    assert all(item["sha256"] and item["content"] for item in package["authoritative_references"].values())


def test_package_does_not_claim_to_execute_the_llm_or_compute_scores():
    package = load_bsi_v35_package()
    assert package["execution_mode"] == "prompt-only-supported; optional-runtime-integration"
    assert package["does_not_compute_scores"] is True



def test_master_prompt_is_standalone_and_prompt_first():
    package = load_bsi_v35_package()
    prompt = package["master_prompt"]["content"]
    assert "No BSI API, Ollama" in prompt
    assert "COMPLETE — BOUNDED TO SUPPLIED MATERIAL" in prompt
    assert "Embedded source: EXECUTION ARCHITECTURE" in prompt
    assert "Embedded source: BIO v1.0" in prompt
    assert "EIG_penalty = EIG_avg / 20" in prompt
    assert "EIG_penalty = EIG_avg / 10" not in prompt



def test_prompt_package_is_pinned_to_expected_git_blob_hashes():
    package = load_bsi_v35_package()
    assert package["master_prompt"]["git_blob_sha1"]
    for item in package["authoritative_references"].values():
        assert item["git_blob_sha1"]


def test_assumption_excavation_protocol_is_embedded_and_version_pinned():
    package = load_bsi_v35_package()
    prompt = package["master_prompt"]["content"]
    protocol = package["authoritative_references"]["assumption_excavation_protocol"]["content"]
    assert "Embedded normative source: Assumption Excavation Protocol v1.1" in prompt
    assert "گام ۱ — تبدیل ادعا به فرمت شرطی" in prompt
    assert "گام ۲ — کاوش سیستماتیک پیش‌فرض‌ها" in prompt
    assert "گام ۳ — تست نقض (Counterfactual Test)" in prompt
    assert "گام ۴ — رتبه‌بندی و سنتز" in prompt
    assert "Manifest Bias" in protocol
    assert "غیاب توضیح لزوماً غیاب آگاهی نیست" in protocol
