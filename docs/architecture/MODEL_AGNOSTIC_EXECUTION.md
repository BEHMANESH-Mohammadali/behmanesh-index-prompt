# Model-Agnostic BSI Execution Architecture

Status: implementation contract / adapter foundation  
Scope: Execution Architecture only. The BSI Knowledge Core is unchanged.

## 1. Invariant

BSI orchestration MUST depend on provider-neutral interfaces, not vendor SDKs,
model names, proprietary prompt formats, or a single provider's feature set.
A model is selected by execution role (for example, extraction, evidence
synthesis, or independent review), and any role may be assigned to a different
compatible model.

"Model-agnostic" means any model with an accessible interface can be integrated
through a conforming adapter. It does not mean every model has every capability.

## 2. Layers

1. **BSI core:** canonical criteria, weights, EIG, ECC, REIG, and scoring logic.
2. **Execution orchestrator:** lifecycle, stage dependencies, trace, bounded
   correction cycle, and fail-closed Completion Gate.
3. **Model contract:** task/request/response/capability types in
   `core/model_contracts.py`.
4. **Provider adapters:** transport and provider-specific normalization only.
5. **Evidence adapters:** separate retrieval interfaces; a language model is
   not itself a source or evidence-verification capability.

## 3. Adapter contract

Every model adapter implements:
- `capabilities`: declared, probeable capabilities;
- `generate(ModelRequest) -> ModelResponse`;
- normalized failures via `ModelAdapterError`.

A model's advertised JSON mode, tool use, context size, or multimodal support
MUST NOT be assumed. Capability declarations are configuration until verified
by adapter-level conformance tests. If a required capability is absent, the
stage is blocked or an explicitly validated fallback is used.

The included `OpenAICompatibleChatAdapter` implements one common wire protocol
as an optional adapter, not as the architecture's dependency. Other adapters
can implement the same Python Protocol without inheriting from it or using the
same API shape. No provider SDK is required by the core.

## 4. Configuration

Environment variables for the optional chat-completions adapter:
- `BSI_MODEL_BASE_URL`: endpoint base URL, including any provider API prefix;
- `BSI_MODEL_API_KEY`: secret; never commit it;
- `BSI_MODEL_NAME`: model identifier understood by that endpoint.

The adapter sends to `{base_url}/chat/completions`. Use a provider-specific
adapter if the service does not implement that wire contract. Keep provider
credentials and model routing outside source control.

## 5. Role routing and mixed-model execution

The router maps semantic roles to adapters. The role names are BSI task roles,
not fixed vendor/model identities. A run may use different adapters for
different stages. Model substitution MUST NOT modify BSI criteria, weights,
scoring formulas, or evidence records.

## 6. Structured output

The internal contract may carry an output schema. An adapter may request native
structured output only when that capability is declared and tested. The
orchestrator remains responsible for validating the returned payload against
the task schema. Invalid output is an execution failure, not a low-confidence
assessment and not permission to invent missing fields.

## 7. Evidence and verification separation

Model-generated statements are candidate analysis, not source evidence.
Evidence retrieval, source inspection, counterevidence, deterministic
calculation, and execution-state verification remain distinct capabilities.
A model cannot self-certify external verification by returning a claim that it
has verified something.

## 8. Completion

The execution trace records lifecycle stages and observable verification state.
The Completion Gate fails closed when mandatory stages are incomplete or T8
classification remains unresolved. The trace explicitly labels self-audit as
not independently validated when no independent evaluator is available.

## 9. Current implementation boundary

This change adds provider-neutral contracts, a generic optional transport
adapter, role routing, and a fail-closed trace contract. It does NOT yet provide:
- a complete autonomous BSI analysis orchestrator;
- a source retrieval provider;
- verified capability probes for arbitrary providers;
- operational D1-D7 scoring anchors beyond authoritative source rubrics;
- durable execution persistence;
- an independent evaluator.

These are separate implementation steps. The current explicit-input scoring
runtime remains authoritative and unchanged. No autonomous analysis or full
cycle is claimed by this adapter foundation.
