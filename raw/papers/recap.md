---
title: "RECAP: REwriting Conversations for Intent Understanding in Agentic Planning"
type: paper
tags: [intent-understanding, intent-rewriting, agentic-planning, conversational-assistant]
authors: [Kushan Mitra, Dan Zhang, Hannah Kim]
year: 2025
venue: arXiv
citation_count: null
arxiv_id: "2509.04472"
doi: null
pdf_url: "https://arxiv.org/pdf/2509.04472"
sub_area: intent-understanding
---

## Abstract
Understanding user intent is essential for effective planning in conversational assistants, particularly those powered by large language models coordinating multiple agents. Traditional classification-based approaches struggle to generalize in open-ended settings. We propose RECAP, a new benchmark designed to evaluate and advance intent rewriting, reframing user-agent dialogues into concise representations of user goals. RECAP captures diverse challenges such as ambiguity, intent drift, vagueness, and mixed-goal conversations. We introduce an LLM-based evaluator that assesses planning utility given the rewritten intent. Using RECAP, we develop a prompt-based rewriting approach that outperforms baselines in terms of plan preference. Fine-tuning two DPO-based rewriters yields additional utility gains.

## Key Contributions
- Introduces RECAP benchmark for evaluating intent rewriting in agentic planning
- Reframes user-agent dialogues into concise goal representations
- Captures challenges: ambiguity, intent drift, vagueness, mixed-goal conversations
- Proposes LLM-based evaluator assessing planning utility of rewritten intents
- Develops prompt-based rewriting approach outperforming baselines
- Fine-tunes DPO-based rewriters for additional utility gains