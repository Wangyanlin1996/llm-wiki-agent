---
title: "IntentRL: Training Proactive User-intent Agents for Open-ended Deep Research via Reinforcement Learning"
type: paper
tags: [intent-recommendation, proactive-agent, reinforcement-learning, intent-clarification, LLM-agent]
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

1. IntentRL: RL-trained proactive agents for intent clarification before deep research
2. Shallow-to-deep intent refinement graph for expanding seed samples
3. Two-stage RL strategy: offline dialogues → online rollouts with user simulator
4. Autonomy-interaction dilemma resolution: clarify intent before committing to expensive research
5. Outperforming built-in clarify modules of closed-source DR agents

## Methodology

- Seed sample expansion via shallow-to-deep intent refinement graph
- Stage 1: offline dialogue training on curated intent clarification trajectories
- Stage 2: online RL rollouts with user simulator feedback
- Intent hit rate + downstream task performance evaluation