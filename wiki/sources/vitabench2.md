---
title: "VitaBench 2.0"
type: source
tags: [intent-understanding, intent-recommendation, benchmark, personalized-agent]
date: 2026-05-26
source_file: raw/papers/vitabench2.md
last_updated: 2026-05-27
---

## Summary
VitaBench 2.0 evaluates personalized and proactive agent behavior in long-term user interactions, requiring agents to extract, utilize, and update user preferences from fragmented interactions. It reveals a substantial gap between SOTA models and practical personalization requirements.

## Key Claims
- Existing benchmarks overlook preference inference from realistic interactions
- Personalization requires extracting preferences from fragmented heterogeneous data
- Proactiveness means recognizing missing info and actively acquiring it
- Even SOTA models fall far short of practical personalization needs

## Key Quotes
> "user intent is often reflected in fragmented daily interactions and requires both personalized modeling and proactive interaction" — challenge definition

> "real-world personalization remains highly challenging even for state-of-the-art models, revealing a substantial gap" — key finding

## Connections
- [[IntentUnderstanding]] — VitaBench 2.0 evaluates personalized IntentUnderstanding
- [[IntentRecommendation]] — proactiveness in VitaBench 2.0 connects to IntentRecommendation
- [[VitaBench2]] — the benchmark concept formalized here
- [[PIRABench]] — complementary benchmark for proactive intent in GUI settings
- [[PASK]] — proactive agent paradigm evaluated by VitaBench 2.0's requirements
- [[AgentMemory]] — long-term memory is essential for personalization in VitaBench 2.0
- [[IntPro]] — per-user adaptation aligns with VitaBench 2.0's personalization demands

## Contradictions
- Contradicts assumption that SOTA models are sufficient: VitaBench 2.0 reveals a substantial personalization gap