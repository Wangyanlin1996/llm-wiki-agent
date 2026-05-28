---
title: "Agent Memory"
type: concept
tags: [agent-memory, LLM-agent, memory-system, episodic-memory]
sources: [evo-memory, agent-memory-survey, lightmem, emem]
last_updated: 2026-05-27
---

# Agent Memory

Agent Memory refers to the mechanisms by which LLM-based agents store, retrieve, and evolve information across interactions. It has evolved from passive trajectory storage to active experience abstraction.

## Evolutionary Framework

Per [[agent-memory-survey]], agent memory evolves through three stages:
- **Storage**: raw trajectory preservation — saving dialogue/action history
- **Reflection**: trajectory refinement — summarization, extraction, compression
- **Experience**: trajectory abstraction — cross-trajectory aggregation, proactive exploration

Three core drivers: long-range consistency, dynamic environments, continual learning.

## Key Approaches

- **[[EvoMemory]]** (Evo-Memory): streaming benchmark for self-evolving memory evaluation; proposes [[ReMem]] pipeline (action-think-memory refine)
- **[[LightMem]]**: SLM-driven lightweight memory with STM/MTM/LTM three-tier architecture; 83ms retrieval latency, F1 +2.5 over [[A-MEM]]
- **[[Emem]]**: Episodic Context Reconstruction shifting from preprocessing to context preservation; master+assistant multi-agent; 54% F1 surpassing [[GAM]] by 7.75%, >70% token reduction

## Common Benchmarks

- **[[LoCoMo]]**: Long-term Conversation Memory benchmark — standard evaluation for agent memory systems
- **Evo-Memory benchmark**: streaming evaluation across 10 datasets

## Cross-direction Relevance

Agent memory is foundational for both [[IntentUnderstanding]] (per-user intent history) and [[IntentRecommendation]] (proactive intent detection requires memory of past interactions and preferences). The [[PASK]] DD-MM-PAS paradigm explicitly links memory modeling to proactive recommendation.

## Key Challenge

Memory preprocessing causes destructive de-contextualization — compressing sequential dependencies into static structures (embeddings, graphs) severs contextual integrity essential for deep reasoning ([[emem]]).