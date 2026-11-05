RAG_FOR_EIG_v0.1

Purpose

External Evidence Retrieval Layer for Epistemic Integrity Gap (EIG)

Goal

Assess claim consistency against external knowledge sources without altering:

- CORE-BEHMANESH
- BSI Formula
- Ontology/BIO
- Existing Scoring Methodology

---

Architectural Principle

RAG is not a replacement for BSI.

RAG acts as an evidence-enrichment layer for EIG.

Architecture:

Input
→ CORE
→ Claim Extraction
→ External Retrieval
→ EIG
→ BSI Score

---

Proposed Repository Structure

core/
├── bsi_engine.py
├── bsi_pipeline.py
├── eig_engine.py
└── rag/
├── claim_retriever.py
├── evidence_summarizer.py
├── retrieval_models.py
└── rag_config.py

docs/
└── RAG_FOR_EIG_v0.1.md

---

Execution Flow

Input Document
↓
CORE Analysis
↓
Claim Extraction
↓
Selective Retrieval
↓
External Evidence Summary
↓
EIG Computation
↓
BSI Scoring
↓
Explainable Report

---

claim_retriever.py

Purpose:

Retrieve external evidence relevant to a claim.

Interface:

retrieve_external_evidence(claim)

Output:

{
"claim": "...",
"supporting": [],
"contradicting": [],
"neutral": []
}

No scoring occurs at this stage.

Retrieval only.

---

evidence_summarizer.py

Purpose:

Compress retrieved evidence into EIG-consumable form.

Output:

{
"support_score": 0.72,
"conflict_score": 0.11,
"evidence_count": 14,
"summary": "..."
}

---

retrieval_models.py

Purpose:

Abstract retrieval providers.

Future providers may include:

- Local Knowledge Base
- Semantic Search
- Vector Store
- GraphRAG
- Scientific Databases

Interface:

retrieve(query)

Output should remain provider-independent.

---

rag_config.py

TOP_K = 5

MAX_EVIDENCE_TOKENS = 500

MIN_CLAIM_CONFIDENCE = 0.60

ENABLE_RAG = True

---

EIG Extension

Current Model

Claim
↔
Internal Evidence

Proposed Model

Claim
↔
Internal Evidence
↔
External Evidence

---

New EIG Variable

external_conflict_factor

Range:

0.0 → 1.0

Interpretation:

0.0 = No conflict detected

1.0 = Strong conflict detected

---

Example

Claim:

"X causes Y"

Internal Evidence:

Strong

External Retrieval:

80% of retrieved evidence contradicts claim

Result:

external_conflict_factor = High

This value is reported to EIG.

---

Suggested Output Extension

{
"eig": 0.31,
"external_conflict": 0.82,
"external_support": 0.12,
"retrieved_sources": 5
}

---

Phase-1 Constraints

Do NOT modify:

- CORE-BEHMANESH
- Hybrid Formula
- BIO Ontology

Operate strictly as an optional enhancement layer.

Enable direct comparison with baseline EIG.

---

Success Metrics

1. Better claim verification

2. Reduced unsupported conclusions

3. Lower hallucination acceptance

4. Improved EIG explainability

5. Minimal token overhead

---

Recommended Phase-1 Scope

Only retrieve evidence for claims that satisfy at least one condition:

- Low confidence
- Weak supporting evidence
- High preliminary EIG
- High uncertainty

This selective retrieval strategy minimizes token consumption while maximizing epistemic value.

---

Long-Term Evolution

Phase 1:
Selective Claim-Level RAG

Phase 2:
Domain-Aware Retrieval

Phase 3:
Scientific Evidence Retrieval

Phase 4:
GraphRAG Integration

Phase 5:
Ontology-Aware Retrieval Based on BIO

At all stages, RAG remains subordinate to CORE and EIG and does not replace the primary epistemic evaluation methodology.
