---
title: "PersonalAlign: Hierarchical Implicit Intent Alignment for Personalized GUI Agent"
type: paper
tags: [intent-understanding, implicit-intent, personalized-agent, GUI-agent, proactive]
authors: [Yibo Lyu, Gongwei Chen, Rui Shao]
year: 2026
venue: ACL 2026
citation_count: null
arxiv_id: "2601.09636"
doi: null
pdf_url: "https://arxiv.org/pdf/2601.09636"
sub_area: intent-understanding
---

## Abstract
While GUI agents have shown strong performance under explicit instructions, real-world deployment requires aligning with users' more complex implicit intents. We highlight Hierarchical Implicit Intent Alignment for Personalized GUI Agent (PersonalAlign), requiring agents to leverage long-term user records to resolve omitted preferences in vague instructions and anticipate latent routines by user state for proactive assistance. We introduce AndroidIntent, a benchmark for evaluating agents' ability in resolving vague instructions and providing proactive suggestions through reasoning over long-term user records. We annotated 775 user-specific preferences and 215 routines from 20k long-term records. We introduce Hierarchical Intent Memory Agent (HIM-Agent), which maintains continuously updating personal memory and hierarchically organizes user preferences and routines. HIM-Agent significantly improves both execution and proactive performance by 15.7% and 7.3%.

## Key Contributions
- Introduces PersonalAlign framework for hierarchical implicit intent alignment in GUI agents
- Proposes AndroidIntent benchmark for evaluating vague instruction resolution and proactive suggestions
- Annotates 775 user-specific preferences and 215 routines from 20k long-term records
- Develops HIM-Agent with continuously updating hierarchical personal memory
- Achieves 15.7% improvement in execution and 7.3% in proactive performance