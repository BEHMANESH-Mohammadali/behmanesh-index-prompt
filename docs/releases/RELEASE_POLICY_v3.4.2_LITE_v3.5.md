# BSI Release Policy — v3.4.2 Lite and v3.5

## Release line

- **BSI v3.4.2 Lite** is the retained legacy/lightweight line. Its source is frozen as the exact historical `main` snapshot at commit `abce8fbf624880fcfd3be47c8191e589bde4e3bb`, preserved on `archive/main-as-bsi-v3.4.2`. It is not rewritten to resemble the v3.5 architecture.
- **BSI v3.5** is the current full release line, based on `release/bsi-v3.5`. It contains the integrated scoring engine, model-agnostic execution path, canonicalization decisions, and research/governance documentation in their proper boundaries.

## Compatibility and maintenance

The Lite line is retained for users who need the earlier, simpler v3.4.2 baseline. It is not the development base for v3.5 and does not receive v3.5 runtime or scoring features by backport.

The v3.5 line is the active development and release target. Changes to core criteria, weights, rubrics, or Knowledge Core require their normal source-of-authority review; a release does not itself authorize changes to those invariants.

## Provenance note

The frozen main snapshot contains a file named `MASTER_PROMPT_BSI_v3.5.md`. The Lite designation is the owner's product-line decision for preserving the main snapshot, not a claim that every file in that snapshot is a clean, independently packaged v3.4.2 artifact. The archived tree remains byte-for-byte as the selected source commit.

## Release verification

The v3.5 release candidate passed the repository CI workflow on commit `5d4d5e0b3e2f5471db2c3193cf404391f28d24ec`, including Python compilation and the pytest suite. This does not substitute for independent Prompt-Only portability testing, third-party validation, or claims of empirical calibration that remain outstanding.
