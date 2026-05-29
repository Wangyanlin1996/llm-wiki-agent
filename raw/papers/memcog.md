---
title: "MemCog: From Memory-as-Tool to Memory-as-Cognition in Conversational Agents"
type: paper
tags: [agent-memory, conversational-agent, proactive-memory, memory-as-cognition]
authors: [Zihan Li, Xingyu Fan, Feifei Li, Wenhui Que]
year: 2026
venue: arXiv
citation_count: null
arxiv_id: "2605.28046"
doi: "10.48550/arXiv.2605.28046"
pdf_url: "https://arxiv.org/pdf/2605.28046"
sub_area: agent-memory
---

## Abstract
Existing agent memory systems universally follow what we term a Memory-as-Tool paradigm where a single query triggers one-shot retrieval of flat passage lists, suffering from passive invocation, reasoning-retrieval decoupling, and structural mismatch between retrieved fragments and the agent's navigational needs. We propose MemCog, a Memory-as-Cognition system that makes memory access an integral part of the reasoning process. MemCog organizes user knowledge as Navigable Memory Store with associative link graphs, exposes Cross-Dimensional Navigation Interface for multi-step reasoning-driven traversal, and employs Proactive Reasoning Protocol that drives agents to spontaneously initiate memory exploration from conversational context. We additionally construct ProactiveMemBench, the first benchmark for evaluating proactive memory triggering. Experiments show that MemCog achieves state-of-the-art on passive QA benchmarks (92.98 on LoCoMo, 95.8 on LongMemEval) while substantially outperforming baselines on ProactiveMemBench, demonstrating the advantage of Memory-as-Cognition.

## Key Contributions
- Proposes Memory-as-Cognition paradigm shifting from passive one-shot retrieval to integrated reasoning-driven memory access
- Introduces Navigable Memory Store with associative link graphs for structured user knowledge
- Designs Cross-Dimensional Navigation Interface for multi-step reasoning-driven traversal
- Develops Proactive Reasoning Protocol for spontaneous memory exploration
- Constructs ProactiveMemBench, the first benchmark for proactive memory triggering evaluation
- Achieves SOTA on LoCoMo (92.98) and LongMemEval (95.8) passive QA benchmarks