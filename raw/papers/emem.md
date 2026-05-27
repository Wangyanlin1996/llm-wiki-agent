---
title: "E-mem: Multi-agent based Episodic Context Reconstruction for LLM Agent Memory"
type: paper
tags: [agent-memory, episodic-memory, multi-agent, LLM-agent, context-reconstruction]
authors: [Kaixiang Wang, Yidan Lin, Jiong Lou]
year: 2026
venue: arXiv
citation_count: 3
arxiv_id: "2601.21714"
doi: "10.48550/arXiv.2601.21714"
pdf_url: "https://arxiv.org/pdf/2601.21714"
sub_area: agent-memory
---

## Abstract

The evolution of Large Language Model (LLM) agents towards System 2 reasoning, characterized by deliberative, high-precision problem-solving, requires maintaining rigorous logical integrity over extended horizons. However, prevalent memory preprocessing paradigms suffer from destructive de-contextualization. By compressing complex sequential dependencies into pre-defined structures (e.g., embeddings or graphs), these methods sever the contextual integrity essential for deep reasoning. To address this, we propose E-mem, a framework shifting from Memory Preprocessing to Episodic Context Reconstruction. Inspired by biological engrams, E-mem employs a heterogeneous hierarchical architecture where multiple assistant agents maintain uncompressed memory contexts, while a central master agent orchestrates global planning. Unlike passive retrieval, our mechanism empowers assistants to locally reason within activated segments, extracting context-aware evidence before aggregation. Evaluations on the LoCoMo benchmark demonstrate that E-mem achieves over 54% F1, surpassing the state-of-the-art GAM by 7.75%, while reducing token cost by over 70%.

## Key Contributions

1. E-mem framework: Episodic Context Reconstruction vs. Memory Preprocessing
2. Heterogeneous hierarchical multi-agent architecture (master + assistants)
3. Uncompressed memory context preservation (no destructive de-contextualization)
4. Local reasoning within activated segments before aggregation
5. 54% F1 on LoCoMo, surpassing GAM by 7.75%, token cost reduction >70%
6. Biological engram-inspired design

## Architecture

- Master agent: global planning and orchestration
- Assistant agents: maintain uncompressed memory contexts, locally reason within activated segments
- Shift from "preprocess then retrieve" to "activate then reason"