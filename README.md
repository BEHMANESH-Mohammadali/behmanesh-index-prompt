Behmanesh Structural Index (BSI)

شاخص ساختاری بهمنش

Version: 3.4.2

Developed by Mohammadali Behmanesh (محمدعلی بهمنش).

"Version" (https://img.shields.io/badge/version-3.4.2-blue.svg)
"License" (https://img.shields.io/badge/license-MIT-green.svg)

What is BSI?

BSI — Behmanesh Structural Index / شاخص ساختاری بهمنش is a layered, interdisciplinary framework for structural analysis of intellectual content.

Its purpose is to move beyond surface-level description and examine the organization and development of ideas, including:

- patterns and themes
- conceptual relationships
- intellectual development
- worldview
- underlying mechanisms
- explicit and latent structures
- analytical coherence
- structural depth

BSI is designed as an analytical framework rather than as a simple textual scoring system.

Core orientation

BSI approaches intellectual content through layered analysis.

The framework is concerned not only with what a text says, but also with how its concepts, mechanisms, assumptions, relationships, and development form an underlying intellectual structure.

Its broader conceptual environment includes ideas such as:

- Mechanistic Realism
- Graph of Thoughts
- layered analysis
- temporal triangulation
- interdisciplinary structural reasoning

These concepts are part of the broader intellectual context of the project and should not be treated as interchangeable names for BSI itself.

Current framework architecture

The current BSI workflow is organized around:

CORE_BEHMANESH
      ↓
BSI
      ↓
EIG
      ↓
ECC
      ↓
REIG
      ↓
Final Assessment

The framework is implemented through versioned prompt and specification files.

The repository should be treated as the authoritative location for the corresponding BSI prompt definitions and framework documents.

Current version

BSI v3.4.2

The current master prompt is:

MASTER_PROMPT_BSI_v3.4.2.md

Versioned files are retained so that benchmark runs can identify exactly which framework definition was used.

Benchmark integration

BSI is currently integrated end-to-end with the separate benchmark project:

"BEHMANESH-Mohammadali/bsi-benchmark"

The corresponding registered benchmark evidence is maintained in:

"BEHMANESH-Mohammadali/bsi-benchmark-results-bsi"

The benchmark compares BSI-guided analysis with RAW/default analysis on the same source material.

The benchmark is intended to evaluate analytical realization and value added rather than simply measuring the amount of generated text.

Reproducibility

For reproducible use, record:

- BSI version
- master prompt version
- source text
- model
- relevant generation settings
- date of execution
- benchmark configuration, when applicable

Changing the framework definition should be treated as a versioned change rather than silently mixing results across versions.

Repository contents

The repository contains the BSI framework definitions, prompts, supporting specifications, and versioned research material.

The benchmark source code and benchmark results are intentionally maintained in separate repositories.

Related repositories

Benchmark

"BEHMANESH-Mohammadali/bsi-benchmark"

Reproducible infrastructure for comparing RAW and BSI-guided analytical outputs.

Benchmark results

"BEHMANESH-Mohammadali/bsi-benchmark-results-bsi"

Registered benchmark evidence, case studies, aggregate reports, and provenance.

Canonical author profile

"BEHMANESH-Mohammadali/BEHMANESH-Mohammadali"

Canonical GitHub identity point for the project.

Author

Mohammadali Behmanesh / محمدعلی بهمنش

GitHub: @BEHMANESH-Mohammadali

X: @behmanesham

Primary work:

Behmanesh Structural Index (BSI)
شاخص ساختاری بهمنش

License

MIT
