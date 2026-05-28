---
title: "IntPro"
type: source
tags: [intent-understanding, proxy-agent, retrieval-conditioned, GRPO]
date: 2026-03-03
source_file: raw/papers/intpro.md
last_updated: 2026-05-27
---

## Summary
IntPro is a proxy agent for context-aware intent understanding that adapts to individual users via retrieval-conditioned inference. It stores intent explanations in a per-user history library and trains via SFT + GRPO with tool-aware rewards, balancing historical pattern retrieval and direct inference across three diverse scenarios.

## Key Claims
- Intent understanding should be dynamic (not static recognition)
- Individual intent history improves accuracy and generalizability
- Retrieval-conditioned inference adapts per-user
- SFT+GRPO training enables learning when to retrieve vs. infer directly

## Key Quotes
> "existing approaches often treat intent understanding as a static recognition task, overlooking users' accumulated intent patterns" — gap identification

> "IntPro achieves strong intent understanding performance with effective context-aware reasoning capabilities across different scenarios and model types" — result

## Connections
- [[IntentUnderstanding]] — IntPro is a concrete approach for context-aware IntentUnderstanding
- [[IntPro]] — the proxy agent concept formalized here
- [[IntentSignalTheory]] — IST's intent objects align with IntPro's per-user intent history
- [[VitaBench2]] — VitaBench 2.0 evaluates personalized intent understanding relevant to IntPro
- [[AgentMemory]] — per-user history library connects to AgentMemory mechanisms
- [[PIRABench]] — PIRA-Bench evaluates proactive intent that IntPro could inform

## Contradictions
- Contradicts static intent recognition: IntPro demonstrates that intent understanding must be dynamic and user-adaptive