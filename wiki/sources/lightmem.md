---
title: "LightMem"
type: source
tags: [agent-memory, lightweight, SLM, memory-system]
date: 2026-04-09
source_file: raw/papers/lightmem.md
last_updated: 2026-05-27
---

## Summary
LightMem proposes a lightweight agent memory system driven by Small Language Models (SLMs), separating online retrieval from offline consolidation. It uses a three-tier architecture (STM/MTM/LTM) with two-stage retrieval (vector coarse + semantic re-ranking), achieving F1 improvement of ~2.5 over A-MEM on LoCoMo with 83ms median retrieval latency.

## Key Claims
- SLM-driven memory achieves comparable accuracy with far lower latency
- Online/offline separation enables bounded-compute efficient memory invocation
- STM/MTM/LTM three-tier memory covers immediate context to consolidated knowledge
- Multi-user support via user identifiers
- F1 +2.5 over A-MEM on LoCoMo with 83ms retrieval

## Key Quotes
> "retrieval-based external memory systems incur low online overhead but suffer from unstable accuracy" — problem statement

> "LightMem modularizes memory retrieval, writing, and long-term consolidation, and separates online processing from offline consolidation" — architecture principle

## Connections
- [[AgentMemory]] — LightMem is a concrete instantiation of lightweight AgentMemory
- [[LightMem]] — the concept and system formalized in this source
- [[LoCoMo]] — primary evaluation benchmark for LightMem
- [[A-MEM]] — baseline method that LightMem surpasses by 2.5 F1
- [[Emem]] — alternative episodic memory approach with different architecture philosophy
- [[PASK]] — proactive agent that could leverage LightMem's low-latency memory

## Contradictions
- Contradicts heavy-LLM memory approaches: LightMem shows SLM-driven memory is sufficient with proper architecture