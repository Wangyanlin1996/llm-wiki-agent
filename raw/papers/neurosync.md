---
title: "NeuroSync: Intent-Aware Code-Based Problem Solving via Direct LLM Understanding Modification"
type: paper
tags: [intent-understanding, intent-task-matching, code-generation, interaction-paradigm]
authors: [Wenshuo Zhang, Leixian Shen, Shuchang Xu]
year: 2025
venue: UIST 2025
citation_count: null
arxiv_id: "2508.02823"
doi: "10.1145/3746059.3747668"
pdf_url: "https://arxiv.org/pdf/2508.02823"
sub_area: intent-understanding
---

## Abstract
Conversational LLMs face misalignment between user intent and generated code due to bidirectional ambiguity: both user intents and coding tasks are inherently nonlinear, yet must be expressed through linear prompts and code sequences. We propose direct intent-task matching, a new human-LLM interaction paradigm that externalizes and enables direct manipulation of the LLM understanding prior to code generation. Implemented in NeuroSync, which employs knowledge distillation to extract LLM understanding, user intents, and their mappings, and allows users to inspect and edit them via visualizations. User study (N=12) shows enhanced intent-task alignment, lower cognitive effort, and improved coding efficiency.

## Key Contributions
- Proposes direct intent-task matching as a new human-LLM interaction paradigm
- Implements NeuroSync with knowledge distillation to extract LLM understanding and intent mappings
- Enables user inspection and editing of LLM understanding via visualizations prior to code generation
- User study (N=12) demonstrates enhanced intent-task alignment, lower cognitive effort, improved efficiency