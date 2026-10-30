# Behmanesh Structural Index (BSI)

**شاخص ساختاری بهمنش**

**Canonical framework and master prompt: BSI v3.5**

Developed by Mohammadali Behmanesh (محمدعلی بهمنش).

BSI is a layered, interdisciplinary framework for structural analysis of intellectual content. It examines the organization and development of ideas, conceptual relationships, mechanisms, assumptions, explicit and latent structures, analytical coherence, and structural depth.

## Canonical version

The canonical framework prompt is **[MASTER_PROMPT_BSI_v3.5.md](MASTER_PROMPT_BSI_v3.5.md)**.

The v3.5 definition is governed by its authoritative references, including:

- [Architectural Invariants](ARCHITECTURAL_INVARIANTS_BSI_v3.5.md)
- [Execution Architecture](BSI_3.5_Execution_Architecture.md)
- [Canonical Specification Matrix](docs/specification/CANONICAL_SPECIFICATION_MATRIX_v3.5.md)
- [Analytical Output Contract — Layer C](docs/specification/ANALYTICAL_OUTPUT_CONTRACT_LAYERC_v3.5.md)
- [BIO v1.0](Ontology/BIO_v1.0.md)
- [CORE-BEHMANESH v1.0](CORE-BEHMANESH/v1.0/CORE_BEHMANESH_v1.0.md)

The framework workflow remains:

`CORE_BEHMANESH → BSI → EIG → ECC → REIG → Final Assessment`

## Prompt package endpoint

The API exposes the canonical, version-pinned prompt package at:

`GET /bsi/prompt`

The package includes the complete master prompt, required authoritative reference documents, and SHA-256 digests. It is intended for a downstream LLM generator to consume as its system/developer instruction package.

The loader fails closed if a required reference is missing. It does not itself call an LLM or calculate BSI scores.

## Runtime status — important

**The canonical prompt package is v3.5. The existing deterministic scoring engine and legacy pipeline are not yet a faithful implementation of BSI v3.5.**

Existing scoring endpoints continue to use legacy v3.4.x logic. They must not be represented as v3.5 scoring. The API health/version metadata explicitly identifies this limitation. Full v3.5 execution requires a downstream LLM generator integration and a separately validated implementation of any computational scoring components whose semantics are fully specified.

In particular, unresolved semantics documented in the Canonical Specification Matrix must not be filled with invented weights, formulas, or substitute algorithms.

## Versioning and archives

Older prompt/framework artifacts are retained under [Archive](Archive/) for provenance. They are not the current canonical prompt.

The SOP v3.4.2 remains a referenced baseline document where explicitly cited by the v3.5 specification; its presence does not make v3.4.2 the current framework version.

## Reproducibility

For every generated analysis, record:

- framework and master prompt version;
- prompt-package SHA-256;
- source text and source provenance;
- model/provider and generation settings;
- date of execution;
- any runtime or reference limitations.

Do not mix outputs from different framework versions without explicit version identification.

## Related repositories

- Benchmark: [bsi-benchmark](https://github.com/BEHMANESH-Mohammadali/bsi-benchmark)
- Benchmark results: [bsi-benchmark-results-bsi](https://github.com/BEHMANESH-Mohammadali/bsi-benchmark-results-bsi)

## Author

Mohammadali Behmanesh / محمدعلی بهمنش

- GitHub: [@BEHMANESH-Mohammadali](https://github.com/BEHMANESH-Mohammadali)
- X: [@behmanesham](https://x.com/behmanesham)

## License

MIT
