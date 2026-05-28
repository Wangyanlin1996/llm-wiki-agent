---
title: "E-mem"
type: source
tags: [agent-memory, episodic-memory, multi-agent]
date: 2026-01-17
source_file: raw/papers/emem.md
last_updated: 2026-05-27
---

## Summary
E-mem shifts from Memory Preprocessing to Episodic Context Reconstruction, using a heterogeneous multi-agent hierarchy where assistant agents maintain uncompressed memory and locally reason before aggregation. It achieves 54% F1 on LoCoMo (surpassing GAM by 7.75%) with >70% token cost reduction.

## Key Claims
- Memory preprocessing causes destructive de-contextualization
- Episodic context reconstruction preserves contextual integrity for deep reasoning
- Multi-agent hierarchy enables local reasoning before aggregation
- 54% F1 surpassing GAM by 7.75% with >70% token reduction

## Key Quotes
> "prevalent memory preprocessing paradigms suffer from destructive de-contextualization" — problem diagnosis

> "shifting from Memory Preprocessing to Episodic Context Reconstruction" — paradigm shift

## Connections
- [[AgentMemory]] — E-mem proposes a paradigm shift within AgentMemory research
- [[Emem]] — the episodic context reconstruction concept formalized here
- [[LoCoMo]] — primary evaluation benchmark where E-mem achieves 54% F1
- [[GAM]] — baseline method that E-mem surpasses by 7.75%
- [[EvoMemory]] — E-mem's approach could be evaluated under Evo-Memory's streaming paradigm
- [[LightMem]] — alternative lightweight approach with different memory architecture

## Contradictions
- Contradicts preprocessing-based memory: E-mem argues preprocessing causes destructive de-contextualization, advocating instead for episodic context reconstruction