---
title: "Intent Understanding"
type: concept
tags: [intent-understanding, human-AI-interaction, context-aware, intent-recognition]
sources: [intpro, intent-signal-theory, vitabench2, intent-communication-design]
last_updated: 2026-05-27
---

# Intent Understanding

Intent Understanding in AI agents refers to inferring user intentions from situational contexts, moving beyond static recognition toward dynamic, context-aware, and personalized reasoning.

## Theoretical Frameworks

- **[[IntentSignalTheory]]** (IST): formalizes four distinct objects — I* (latent source intent), I-hat (observable proxy), P (encoded carrier), O (model output). Proves the **Irreversible Intent Loss** theorem: private intent absent from carrier cannot be recovered. Reframes prompt engineering as intent-protocol design.
- **Intent Communication Design Space** ([[intent-communication-design]]): Transparency (what) × Abstraction (when) × Modality (how) — multidimensional framework for agent-human intent communication across bystander, cooperative, and shared control scenarios.

## Key Approaches

- **[[IntPro]]**: proxy agent with retrieval-conditioned intent inference; per-user intent history library; SFT + GRPO training with tool-aware rewards; evaluates when to retrieve past patterns vs. infer directly
- **[[VitaBench2]]**: benchmark for personalized+proactive agent evaluation; reveals substantial gap between SOTA and practical personalization

## From Static to Dynamic

Traditional intent understanding treats it as static recognition ([[IntPro]] identifies this gap). Current approaches emphasize:
- Context-aware reasoning over immediate context + underlying motivations
- Individual adaptation via per-user intent patterns
- Proactive recognition of missing information

## Cross-direction Relevance

Intent understanding enables [[IntentRecommendation]] — understanding latent intent is prerequisite for proactively recommending actions. [[VitaBench2]] bridges both understanding and recommendation. [[IntentRL]] trains agents to clarify intent before acting.

## Key Challenge

Users' latent source intent (I*) is often absent from the observable prompt (P), creating an information gap that cannot be fully recovered ([[IntentSignalTheory]] Irreversible Intent Loss).