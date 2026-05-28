---
title: "IntentRL"
type: paper
tags: [intent-recommendation, proactive-agent, deep-research, RL, intent-clarification]
authors: [Haohao Luo, Zexi Li, Yuexiang Xie]
year: 2026
venue: arXiv
citation_count: 4
arxiv_id: "2602.03468"
doi: null
pdf_url: "https://arxiv.org/pdf/2602.03468"
sub_area: intent-recommendation
---

## Abstract
Deep Research (DR) agents extend LLMs beyond parametric knowledge by autonomously retrieving and synthesizing evidence from large web corpora into long-form reports. However, DR is computationally expensive, creating an autonomy-interaction dilemma: high autonomy on ambiguous user queries often leads to prolonged execution with unsatisfactory outcomes. IntentRL trains proactive agents to clarify latent user intents before starting long-horizon research. It introduces a scalable pipeline that expands seed samples into high-quality dialogue turns via a shallow-to-deep intent refinement graph, and adopts a two-stage RL strategy (offline dialogues → online rollouts with user simulator). Experiments show IntentRL significantly improves both intent hit rate and downstream task performance, outperforming built-in clarify modules of closed-source DR agents.

## Key Contributions
- RL-trained proactive intent clarification
- Shallow-to-deep intent refinement graph
- Two-stage RL (offline+online with simulator)
- Autonomy-interaction dilemma resolution
- Outperforms closed-source DR clarify modules