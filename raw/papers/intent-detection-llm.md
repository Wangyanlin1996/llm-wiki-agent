---
title: "Intent Detection in the Age of LLMs"
type: paper
tags: [intent-understanding, intent-detection, task-oriented-dialogue, OOS-detection, hybrid-system]
authors: [Gaurav Arora, Shreya Jain, S. Merugu]
year: 2024
venue: EMNLP 2024
citation_count: 41
arxiv_id: "2410.01627"
doi: "10.48550/arXiv.2410.01627"
pdf_url: "https://arxiv.org/pdf/2410.01627"
sub_area: intent-understanding
---

## Abstract
Intent detection is a critical component of task-oriented dialogue systems. Traditional approaches relied on computationally efficient supervised sentence transformer encoder models, which require substantial training data and struggle with out-of-scope detection. We adapt SOTA LLMs using adaptive in-context learning and chain-of-thought prompting for intent detection, and compare with SetFit models. We propose a hybrid system using uncertainty-based routing combining both approaches (within 2% of native LLM accuracy with 50% less latency). Controlled experiments reveal that OOS detection capability is significantly influenced by the scope of intent labels and the size of the label space. We introduce a two-step approach utilizing internal LLM representations, demonstrating empirical gains in OOS detection accuracy and F1-score by >5%.

## Key Contributions
- Adapts SOTA LLMs with adaptive in-context learning and CoT prompting for intent detection
- Proposes hybrid system with uncertainty-based routing (within 2% LLM accuracy, 50% less latency)
- Reveals OOS detection is significantly influenced by intent label scope and label space size
- Introduces two-step approach using internal LLM representations for OOS detection gains >5%