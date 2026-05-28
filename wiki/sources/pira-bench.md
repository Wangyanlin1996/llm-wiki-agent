---
title: "PIRA-Bench"
type: source
tags: [intent-recommendation, proactive-agent, GUI-agent, benchmark]
date: 2026-03-09
source_file: raw/papers/pira-bench.md
last_updated: 2026-05-27
---

## Summary
PIRA-Bench introduces the first benchmark for Proactive Intent Recommendation Agents on GUI, featuring complex trajectories with multiple interleaved intents, noisy segments, and user profile contexts. It proposes PIRF, a memory-aware state-tracking framework for multi-thread management, transitioning from reactive to proactive GUI agent paradigm.

## Key Claims
- Current GUI agents are purely reactive (require explicit instruction)
- Proactive intent recommendation requires detecting actionable events from continuous visual input
- Complex trajectories contain multiple interleaved intents and noise
- PIRF framework manages multiple task threads with memory-aware state tracking
- Proactive GUI agents need user profile context for preference-aware detection

## Key Quotes
> "Current GUI agents operate under a reactive paradigm requiring explicit user instruction" — problem

> "PIRA-Bench serves as an initial step toward robust proactive GUI-based personal assistants" — contribution

## Connections
- [[IntentRecommendation]] — PIRA-Bench evaluates proactive IntentRecommendation in GUI contexts
- [[PIRABench]] — the benchmark concept formalized here
- [[PIRF]] — memory-aware state-tracking framework proposed alongside PIRA-Bench
- [[IntentUnderstanding]] — detecting actionable events requires IntentUnderstanding
- [[VitaBench2]] — complementary benchmark evaluating personalized proactive agents
- [[AgentMemory]] — PIRF's memory-aware state tracking connects to AgentMemory mechanisms

## Contradictions
- Contradicts reactive GUI agent paradigm: PIRA-Bench demonstrates that proactive intent detection is necessary for effective GUI assistants