---
title: "VitaBench 2.0: Evaluating Personalized and Proactive Agents in Long-Term User Interactions"
type: paper
tags: [intent-understanding, intent-recommendation, benchmark, personalized-agent, proactive-agent]
authors: [Yuxin Chen, Yi Zhang, Zhengzhou Cai]
year: 2026
venue: arXiv
citation_count: 0
arxiv_id: "2605.27141"
doi: null
pdf_url: "https://arxiv.org/pdf/2605.27141"
sub_area: intent-understanding
---

## Abstract

Large language models (LLMs) have evolved into interactive agents that collaborate with users in real-world tasks. Effective collaboration in such settings increasingly depends on understanding the user beyond what is explicitly stated, as user intent is often reflected in fragmented daily interactions and requires both personalized modeling and proactive interaction. However, existing agent benchmarks primarily evaluate reasoning and tool use, largely overlooking the challenges of inferring and leveraging user preferences in realistic scenarios. To address this gap, we introduce VitaBench 2.0, a benchmark for evaluating personalized and proactive agent behavior in long-term user interactions. In VitaBench 2.0, tasks are organized as temporally ordered sequences for individual users, where preferences are embedded in fragmented and heterogeneous interactions. Successful completion of tasks requires the agent to continuously extract, utilize, and update user preferences from these interactions. We further evaluate proactiveness through tasks that require agents to recognize missing information and actively acquire it from users or environments before making decisions. Results show that real-world personalization remains highly challenging even for state-of-the-art models, revealing a substantial gap between current capabilities and practical requirements.

## Key Contributions

1. VitaBench 2.0: benchmark for personalized and proactive agent evaluation
2. Temporally ordered task sequences for individual users
3. Preference extraction from fragmented and heterogeneous interactions
4. Proactiveness evaluation: recognizing missing information, actively acquiring it
5. Extensible memory interface design
6. Revealing substantial gap between SOTA and practical personalization requirements

## Evaluation Dimensions

- Personalization: extracting, utilizing, updating user preferences from fragmented interactions
- Proactiveness: recognizing missing info, actively acquiring before decision-making
- Long-term interaction: temporally ordered sequences per user