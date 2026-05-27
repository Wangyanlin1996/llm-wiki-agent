---
title: "PASK: Toward Intent-Aware Proactive Agents with Long-Term Memory"
type: paper
tags: [intent-recommendation, proactive-agent, long-term-memory, intent-detection, LLM-agent]
authors: [Zhifei Xie, Zongzheng Hu, Fangda Ye]
year: 2026
venue: arXiv
citation_count: 2
arxiv_id: "2604.08000"
doi: null
pdf_url: "https://arxiv.org/pdf/2604.08000"
sub_area: intent-recommendation
---

## Abstract

Proposes DD-MM-PAS (Demand Detection, Memory Modeling, Proactive Agent System) as a general paradigm for streaming proactive AI agents. Pask instantiates this with IntentFlow model for demand detection, hybrid memory (workspace, user, global) for long-term memory modeling, and PAS infra framework forming a closed loop. Also introduces LatentNeeds-Bench, a real-world benchmark built from user-consented data. Experiments show IntentFlow matches leading Gemini3-Flash models under latency constraints while identifying deeper user intent.

## Key Contributions

1. DD-MM-PAS paradigm: Demand Detection → Memory Modeling → Proactive Agent System
2. IntentFlow: intent/demand detection model matching Gemini3-Flash under latency constraints
3. Hybrid memory architecture: workspace memory, user memory, global memory
4. PAS infra framework: closed-loop proactive agent system
5. LatentNeeds-Bench: real-world benchmark from user-consented data
6. Identifying deeper user intent beyond surface-level queries

## DD-MM-PAS Paradigm

- **DD (Demand Detection)**: IntentFlow model detecting user needs from streaming interactions
- **MM (Memory Modeling)**: Hybrid memory (workspace/user/global) for long-term context
- **PAS (Proactive Agent System)**: Infrastructure framework forming detection-memory-action closed loop