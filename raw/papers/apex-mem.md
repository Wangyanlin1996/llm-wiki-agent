---
title: "APEX-MEM: Agentic Semi-Structured Memory with Temporal Reasoning for Long-Term Conversational Agents"
type: paper
tags: [agent-memory, temporal-reasoning, property-graph, conversational-ai]
authors: [Pratyay Banerjee, Masud Moshtaghi, Shivashankar Subramanian, Amita Misra, Ankit Chadha]
year: 2026
venue: ACL 2026
citation_count: null
arxiv_id: "2604.14362"
doi: "10.48550/arXiv.2604.14362"
pdf_url: "https://arxiv.org/pdf/2604.14362"
sub_area: agent-memory
---

## Abstract
Large language models still struggle with reliable long-term conversational memory: simply enlarging context windows or applying naive retrieval often introduces noise and destabilizes responses. We present APEX-MEM, a conversational memory system that combines three key innovations: (1) a property graph which uses domain-agnostic ontology to structure conversations as temporally grounded events in an entity-centric framework, (2) append-only storage that preserves the full temporal evolution of information, and (3) a multi-tool retrieval agent that understands and resolves conflicting or evolving information at query time, producing a compact and contextually relevant memory summary. This retrieval-time resolution preserves the full interaction history while suppressing irrelevant details. APEX-MEM achieves 88.88% accuracy on LOCOMO's Question Answering task and 86.2% on LongMemEval, outperforming state-of-the-art session-aware approaches and demonstrating that structured property graphs enable more temporally coherent long-term conversational reasoning.

## Key Contributions
- Introduces property graph with domain-agnostic ontology for temporally grounded, entity-centric memory structuring
- Implements append-only storage preserving full temporal evolution of information
- Develops multi-tool retrieval agent that resolves conflicting/evolving information at query time
- Achieves 88.88% on LOCOMO QA and 86.2% on LongMemEval, outperforming SOTA session-aware approaches
- Demonstrates structured property graphs enable more temporally coherent long-term conversational reasoning