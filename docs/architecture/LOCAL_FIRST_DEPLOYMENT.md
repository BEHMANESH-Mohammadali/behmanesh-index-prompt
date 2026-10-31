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
5. Instantiate OllamaChatAdapter and pass it to StaticModelRouter under the
   semantic task roles required by the run.

No credentials or hosted API subscription are needed for this local adapter.

## Important limits

- A local model's answer is candidate analysis, not evidence.
- External/source-dependent claims still require source retrieval and direct
  inspection. Local inference cannot replace that capability.
- No source retrieval adapter is bundled in this change.
- BSI D1-D7, EIG, ECC, and REIG retain their existing definitions. This
  orchestrator does not derive numerical scores from raw text.
- The explicit-input scoring runtime remains the only scoring authority.
- The execution orchestrator requires a handler for every mandatory stage.
  Missing or failed handlers block completion; it never marks a partial run
  complete.
- This is an execution framework, not a claim that all stage handlers or
  independent evaluation are already operational.

## Deployment profiles

- Local-only: local model plus manually supplied/source-inspected evidence.
  No paid model API; external retrieval must be performed through an available
  local or separately configured retrieval tool.
- Hybrid: local model for extraction/drafting, external retrieval for
  source-dependent verification. Any paid service is optional.
- Hosted: one or more hosted model endpoints. API usage and cost depend on
  provider, model, token volume, and retrieval services.
