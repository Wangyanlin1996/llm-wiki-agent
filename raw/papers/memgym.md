---
title: "MemGym: a Long-Horizon Memory Environment for LLM Agents"
type: paper
tags: [agent-memory, benchmark, long-horizon, agentic-memory]
authors: [Wujiang Xu, Yu Wang, Kai Mei, Kaiqu Liang, Zhenting Wang, Mingyu Jin, Han Zhang, Shi-Xiong Zhang, Wenyue Hua, Sambit Sahu, Dimitris N. Metaxas]
year: 2026
venue: arXiv
citation_count: null
arxiv_id: "2605.20833"
doi: "10.48550/arXiv.2605.20833"
pdf_url: "https://arxiv.org/pdf/2605.20833"
sub_area: agent-memory
---

## Abstract
Memory is a central capability for LLM agents operating across long-horizon tasks. Existing memory benchmarks predominantly evaluate retention of personalized information in multi-turn chat scenarios, overlooking the dynamic memory formation that occurs during extended agent execution. Consequently, the memory systems they produce transfer poorly to realistic agentic environments, such as coding and web navigation. We present MemGym, a benchmark for agentic memory that unifies existing agent gyms and in-house memory-grounded pipelines behind one memory-reasoning interface. MemGym spans five evaluation tracks grouped into four agentic regimes: tool-use dialogue (tau2-bench), multi-turn deep-research search (MEMGYM-DR), coding (SWE-Gym and MEMGYM-CODEQA), and computer use (WebArena-Infinity). MemGym reports memory-isolated scores that decouple memory performance from reasoning, retrieval, and tool-use ability, so memory strategies can be ranked without those confounders. Our synthetic pipelines for MEMGYM-CODEQA and MEMGYM-DR are length-controllable, ablation-verified at every stage, and tightly aligned with downstream scenarios. To make evaluation on coding environments academically tractable, we train MemRM, a lightweight reward model (Qwen3-1.7B fine-tuned with QLoRA) that scores compression quality as a fast scalar read in place of full Docker rollouts.

## Key Contributions
- Introduces MemGym, a unified benchmark for agentic memory evaluation across diverse environments
- Spans five evaluation tracks across four agentic regimes (tool-use, deep-research, coding, computer use)
- Proposes memory-isolated scoring to decouple memory from reasoning/retrieval/tool-use confounders
- Develops length-controllable synthetic pipelines for MEMGYM-CODEQA and MEMGYM-DR
- Trains MemRM, a lightweight reward model for fast compression quality evaluation