---
title: "E-mem"
type: paper
tags: [agent-memory, episodic-context, multi-agent, hierarchical, token-efficiency]
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
- Episodic Context Reconstruction paradigm
- Master+assistant multi-agent hierarchy
- Uncompressed memory preservation
- Local reasoning before aggregation
- 54% F1 surpassing GAM by 7.75%
- >70% token cost reduction