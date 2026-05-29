---
title: "MINTEval: Evaluating Memory under Multi-Target Interference in Long-Horizon Agent Systems"
type: paper
tags: [agent-memory, benchmark, interference, long-horizon, multi-target]
authors: [Hyunji Lee, Justin Chih-Yao Chen, Joykirat Singh, Zaid Khan, Elias Stengel-Eskin, Mohit Bansal]
year: 2026
venue: arXiv
citation_count: null
arxiv_id: "2605.18565"
doi: "10.48550/arXiv.2605.18565"
pdf_url: "https://arxiv.org/pdf/2605.18565"
sub_area: agent-memory
---

## Abstract
Real-world agents operate over long and evolving horizons, where information is repeatedly updated and may interfere across memories, requiring accurate recall and aggregated reasoning over multiple pieces of information. However, existing benchmarks focus on static, independent recall and fail to capture these dynamic interactions between evolving memories. In this paper, we study how current memory-augmented agents perform in realistic, interference-heavy, long-horizon settings across diverse domains and question types. We introduce MINTEval (Long-Horizon Memory under INTerference Evaluation), a benchmark featuring (1) long, highly interconnected contexts with frequently updated information that induces substantial interference, (2) diverse domains (state tracking, multi-turn dialogue, Wikipedia revisions, and GitHub commits), enabling evaluation of domain generalization, and (3) diverse question types that assess robustness to interference, including (i) single-target recall tasks requiring retrieval of a specific target from long contexts, and (ii) multi-target aggregation tasks requiring reasoning over multiple relevant pieces of information. Overall, MINTEval has 15.6k question-answering pairs over long-horizon contexts averaging 138.8k tokens and extending up to 1.8M tokens per instance. We evaluate 7 representative systems, including vanilla long-context LLMs, RAG, and memory-augmented agent frameworks. Across all systems, we observe consistently low performance (avg. 27.9% accuracy), especially on questions requiring aggregated reasoning over multiple pieces of evidence. Our analysis shows that performance is primarily limited by retrieval and memory construction. Furthermore, current memory systems struggle to recall and reason over earlier facts that are revised or interfered with by subsequent context, with accuracy degrading as the number of intervening updates increases.

## Key Contributions
- Introduces MINTEval benchmark for evaluating memory under multi-target interference
- Features long interconnected contexts with frequently updated information inducing substantial interference
- Covers diverse domains: state tracking, multi-turn dialogue, Wikipedia revisions, GitHub commits
- Includes 15.6k QA pairs over contexts averaging 138.8k tokens (up to 1.8M tokens)
- Evaluates 7 systems showing consistently low performance (avg. 27.9% accuracy)
- Identifies retrieval and memory construction as primary performance bottlenecks