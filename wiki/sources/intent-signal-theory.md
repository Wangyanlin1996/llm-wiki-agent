---
title: "Intent Signal Theory"
type: source
tags: [intent-understanding, intent-signal, computational-framework, theory]
date: 2026-05-20
source_file: raw/papers/intent-signal-theory.md
last_updated: 2026-05-27
---

## Summary
Intent Signal Theory (IST) formalizes the missing intent layer in AI interaction, distinguishing four objects: latent source intent (I*), observable intent proxy (I-hat), encoded carrier (P), and model output (O). It proves the Irreversible Intent Loss theorem and reframes prompt engineering as intent-protocol design, validated across 6 LLMs, 3 languages, and 3 task domains.

## Key Claims
- Current AI models conflate four distinct intent objects
- Private intent absent from carrier cannot be recovered (Irreversible Intent Loss theorem)
- Prompt engineering should be reframed as intent-protocol design
- Structural-fidelity splits validated across multiple LLMs and languages

## Key Quotes
> "Current AI interaction models treat the prompt as the primary object of exchange, omitting a critical layer: the user's latent source intent" — core critique

> "The Theorem of Irreversible Intent Loss establishes that private intent absent from the carrier cannot be recovered beyond generic substitution" — key theorem

## Connections
- [[IntentUnderstanding]] — IST provides the theoretical foundation for IntentUnderstanding
- [[IntentSignalTheory]] — the computational framework formalized here
- [[IntPro]] — IntPro's per-user history addresses the intent loss IST identifies
- [[IntentRL]] — IntentRL's proactive clarification mitigates the Irreversible Intent Loss
- [[IntentRecommendation]] — proactive recommendation compensates for absent intent signals

## Contradictions
- Contradicts prompt-as-primary-object view: IST argues prompts are merely carriers, not the intent itself