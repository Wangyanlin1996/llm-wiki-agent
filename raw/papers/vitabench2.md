---
title: "VitaBench 2.0"
type: paper
tags: [intent-understanding, benchmark, personalized, proactive, user-preference]
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
- Personalized+proactive agent benchmark
- Temporally ordered task sequences
- Preference extraction from fragmented interactions
- Proactiveness evaluation (missing info recognition)
- Extensible memory interface
- Reveals SOTA vs. practical gap