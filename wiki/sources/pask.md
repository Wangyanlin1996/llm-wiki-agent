---
title: "PASK"
type: source
tags: [intent-recommendation, proactive-agent, long-term-memory]
date: 2026-04-09
source_file: raw/papers/pask.md
last_updated: 2026-05-27
---

## Summary
PASK proposes the DD-MM-PAS paradigm (Demand Detection→Memory Modeling→Proactive Agent System) for streaming proactive AI agents, instantiated with IntentFlow for demand detection, hybrid memory (workspace/user/global), and PAS infra. It introduces LatentNeeds-Bench and shows IntentFlow matches Gemini3-Flash under latency constraints while identifying deeper intent.

## Key Claims
- Streaming proactive agents need a systematic paradigm (DD-MM-PAS)
- IntentFlow detects demands matching Gemini3-Flash under latency
- Hybrid memory (workspace/user/global) supports long-term context
- LatentNeeds-Bench provides real-world evaluation from user-consented data
- Proactive agents identify deeper intent beyond surface queries

## Key Quotes
> "DD-MM-PAS as a general paradigm for streaming proactive AI agents" — paradigm

> "IntentFlow matches leading Gemini3-Flash models under latency constraints while identifying deeper user intent" — result

## Connections
- [[IntentRecommendation]] — PASK implements proactive IntentRecommendation via DD-MM-PAS
- [[PASK]] — the intent-aware proactive agent concept formalized here
- [[DDMM-PAS]] — the systematic paradigm proposed by PASK
- [[AgentMemory]] — hybrid memory architecture connects to AgentMemory mechanisms
- [[LightMem]] — PASK's memory modeling aligns with LightMem's lightweight approach
- [[PIRABench]] — PIRA-Bench evaluates proactive intent recommendation relevant to PASK
- [[VitaBench2]] — VitaBench 2.0's personalization demands align with PASK's proactive paradigm

## Contradictions
- Contradicts surface-query satisfaction: PASK demonstrates that identifying deeper intent beyond surface queries is essential for proactive agents