# BSI v3.5 Local-First Deployment

## Cost and API requirements

The BSI scoring core, execution contracts, orchestrator, and a local model
adapter do not require a paid API or an internet connection at runtime.
A local model server such as Ollama can run on the user's own computer.
The Ollama adapter uses its local HTTP endpoint and requires no API key.

The local software is free; hardware is not. Runtime speed and usable context
depend on available RAM/VRAM, model size, quantization, and context settings.
Downloading a model requires internet access once and consumes disk space.

## Setup

1. Install Ollama from its official distribution for the operating system.
2. Download a model supported by the local machine using the Ollama CLI.
3. Start Ollama and confirm its local service is reachable.
4. Configure environment variables:
   - BSI_OLLAMA_HOST=http://127.0.0.1:11434
   - BSI_OLLAMA_MODEL=<installed-model-name>
5. For the API execution path, set `BSI_OLLAMA_MODEL` to an installed model
   name, or set `BSI_OLLAMA_MODEL_ANALYST` and `BSI_OLLAMA_MODEL_AUDITOR`
   to separate local models.
6. Start the API and call `POST /bsi/execute` with a JSON body containing
   `text`, `source_materials`, and (when numerical scoring is requested)
   explicit evidence-backed `dimension_scores` and `calculation_mode`.

Example request shape (use real inspected source text and a stable reference):

```json
{
  "text": "Target content to analyze...",
  "source_materials": [
    {"source_ref": "https://example.org/inspected-source", "text": "Inspected source text..."}
  ],
  "dimension_scores": {
    "D1": 70, "D2": 70, "D3": 70, "D4": 70,
    "D5": 70, "D6": 70, "D7": 70
  },
  "calculation_mode": "linear",
  "content_scope": "single_content"
}
```

The example scores are placeholders only; callers must not copy them as
assessments without a real evidence-backed evaluation. For a single item,
D2 is restricted to internal coherence. Do not provide a longitudinal basis
unless a linked longitudinal corpus is actually available.

No credentials or hosted API subscription are needed for this local adapter.

## Important limits

- A local model's answer is candidate analysis, not evidence.
- External/source-dependent claims still require source retrieval and direct
  inspection. Local inference cannot replace that capability.
- The API execution route is connected to the mandatory lifecycle handlers,
  the existing experimental RAG signal generator, and the explicit-input
  v3.5 scoring runtime. The RAG backend is still heuristic/experimental and
  does not provide complete canonical source URLs and inspected source text.
- Therefore `source_materials` with `source_ref` and actual `text` are
  required for the verification stage. Retrieval snippets alone cannot pass it.
- BSI D1-D7, EIG, ECC, and REIG retain their existing definitions. The runtime
  never silently converts legacy heuristic scores or raw text into v3.5 scores.
- If a required model, evidence item, stage output, correction, final re-read,
  or explicit scoring input is missing/invalid, the execution remains blocked.
- A passing run is model-assisted and self-audited, not independently validated.
  Durable trace persistence is not included.

## Deployment profiles

- Local-only: local model plus manually supplied/source-inspected evidence.
  No paid model API; external retrieval must be performed through an available
  local or separately configured retrieval tool.
- Hybrid: local model for extraction/drafting, external retrieval for
  source-dependent verification. Any paid service is optional.
- Hosted: one or more hosted model endpoints. API usage and cost depend on
  provider, model, token volume, and retrieval services.
