---
title: "Evo-Memory"
type: source
tags: [agent-memory, benchmark, LLM-agent, test-time-learning]
date: 2025-11-20
source_file: raw/papers/evo-memory.md
last_updated: 2026-05-27
---

## Summary
Evo-Memory introduces the first streaming benchmark for evaluating self-evolving memory in LLM agents, requiring agents to search, adapt, and evolve memory after each interaction across 10 diverse datasets. It unifies 10+ memory modules and proposes ExpRAG (experience retrieval) and ReMem (action-think-memory refine pipeline) baselines, demonstrating that test-time memory evolution is critical for long-horizon agent performance.

## Key Claims
- Memory management and evolution are underexplored in LLM agents
- Static conversational evaluation overlooks dynamic memory accumulation
- Test-time evolution (continuous memory update during deployment) is essential
- ReMem pipeline integrates reasoning-actions-memory for continual improvement

## Key Quotes
> "Statefulness is essential for large language model (LLM) agents to perform long-term planning and problem-solving" — core motivation

> "Evo-Memory structures datasets into sequential task streams, requiring LLMs to search, adapt, and evolve memory after each interaction" — benchmark design

## Connections
- [[AgentMemory]] — Evo-Memory evaluates the memory mechanisms described in AgentMemory
- [[EvoMemory]] — the benchmark itself is the concept formalized here
- [[LoCoMo]] — commonly used evaluation baseline in the Evo-Memory benchmark
- [[A-MEM]] — existing memory baseline method evaluated in Evo-Memory
- [[LightMem]] — lightweight memory approach that could benefit from Evo-Memory evaluation
- [[Emem]] — episodic memory paradigm that addresses de-contextualization identified in Evo-Memory

## Contradictions
- Contradicts static-memory assumptions: Evo-Memory demonstrates that static conversational evaluation overlooks dynamic memory accumulation