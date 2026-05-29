---
title: "H-Mem: A Novel Memory Mechanism for Evolving and Retrieving Agent Memory via a Hybrid Structure"
type: paper
tags: [agent-memory, hybrid-structure, knowledge-graph, temporal-tree]
authors: [Jiawei Yu, Yixiang Fang, Xilin Liu, Yuchi Ma]
year: 2026
venue: arXiv
citation_count: null
arxiv_id: "2605.15701"
doi: "10.48550/arXiv.2605.15701"
pdf_url: "https://arxiv.org/pdf/2605.15701"
sub_area: agent-memory
---

## Abstract
Memory data are ubiquitous in Large Language Model (LLM)-based agents (e.g., OpenClaw and Manus). A few recent works have attempted to exploit agents' memory for improving their performance on the question-answering (QA) task, but they lack a principled mechanism for effectively modeling how memory data evolves over time and retrieving memory data effectively, leading to poor performance in memory utilization. To fill this gap, we present H-Mem, a novel memory mechanism via a hybrid structure that can not only effectively model the evolution of agent memory over a long period of time, but also provide an efficient memory retrieval approach. Particularly, H-Mem builds a temporal and semantic tree structure that allows the short-term memory data to evolve progressively into long-term memory data, where the latter provides summarized information about the former, while simultaneously constructing a knowledge graph to capture the relationships between entities in memory. Moreover, it offers an effective memory retrieval approach by exploiting the hybrid structure of the tree and graph structures. Extensive experiments on three agent memory benchmarks show that H-Mem achieves state-of-the-art performance on the QA task.

## Key Contributions
- Proposes H-Mem, a hybrid memory mechanism combining temporal-semantic tree and knowledge graph
- Builds temporal and semantic tree structure for progressive short-term to long-term memory evolution
- Constructs knowledge graph to capture entity relationships in memory
- Provides efficient retrieval exploiting the hybrid tree-graph structure
- Achieves SOTA on three agent memory benchmarks for QA tasks