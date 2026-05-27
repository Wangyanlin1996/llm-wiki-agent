---
title: "Evo-Memory"
type: paper
tags: [agent-memory, streaming-benchmark, self-evolving, continual-learning]
authors: [Tianxin Wei, Noveen Sachdeva, Benjamin Coleman]
year: 2025
venue: arXiv
citation_count: 71
arxiv_id: "2511.20857"
doi: "10.48550/arXiv.2511.20857"
pdf_url: "https://arxiv.org/pdf/2511.20857"
sub_area: agent-memory
---

## Abstract
Statefulness is essential for large language model (LLM) agents to perform long-term planning and problem-solving. This makes memory a critical component, yet its management and evolution remain largely underexplored. Existing evaluations mostly focus on static conversational settings, where memory is passively retrieved from dialogue to answer queries, overlooking the dynamic ability to accumulate and reuse experience across evolving task streams. In real-world environments such as interactive problem assistants or embodied agents, LLMs are required to handle continuous task streams, yet often fail to learn from accumulated interactions, losing valuable contextual insights, a limitation that calls for test-time evolution, where LLMs retrieve, integrate, and update memory continuously during deployment. To bridge this gap, we introduce Evo-Memory, a comprehensive streaming benchmark and framework for evaluating self-evolving memory in LLM agents. Evo-Memory structures datasets into sequential task streams, requiring LLMs to search, adapt, and evolve memory after each interaction. We unify and implement over ten representative memory modules and evaluate them across 10 diverse multi-turn goal-oriented and single-turn reasoning and QA datasets. To better benchmark experience reuse, we provide a baseline method, ExpRAG, for retrieving and utilizing prior experience, and further propose ReMem, an action-think-memory refine pipeline that tightly integrates reasoning, task actions, and memory updates to achieve continual improvement.

## Key Contributions
- Evo-Memory streaming benchmark
- 10+ memory module unified evaluation
- ExpRAG baseline
- ReMem pipeline (action-think-memory refine)
- Continual improvement analysis