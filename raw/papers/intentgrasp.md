---
title: "IntentGrasp: A Comprehensive Benchmark for Intent Understanding"
type: paper
tags: [intent-understanding, benchmark, intention, fine-tuning, cross-domain]
authors: [Yuwei Yin, Chuyuan Li, Giuseppe Carenini]
year: 2026
venue: arXiv
citation_count: null
arxiv_id: "2605.06832"
doi: null
pdf_url: "https://arxiv.org/pdf/2605.06832"
sub_area: intent-understanding
---

## Abstract
Accurately understanding the intent behind speech, conversation, and writing is crucial to the development of helpful Large Language Model (LLM) assistants. This paper introduces IntentGrasp, a comprehensive benchmark for evaluating the intent understanding capability of LLMs. Derived from 49 high-quality, open-licensed corpora spanning 12 diverse domains, IntentGrasp is constructed through source datasets curation, intent label contextualization, and task format unification. IntentGrasp contains a large-scale training set of 262,759 instances and two evaluation sets: an All Set of 12,909 test cases and a more balanced and challenging Gem Set of 470 cases. Extensive evaluations on 20 LLMs across 7 families demonstrate unsatisfactory performance, with scores below 60% on All Set and below 25% on Gem set. Notably, 17 out of 20 tested models perform worse than a random-guess baseline on Gem Set, while the estimated human performance is ~81.1%. To enhance such ability, this paper proposes Intentional Fine-Tuning (IFT), which fine-tunes models on the training set in IntentGrasp, yielding significant gains of 30+ F1 points on All Set and 20+ points on Gem Set. The leave-one-domain-out experiments demonstrate the strong cross-domain generalizability of IFT.

## Key Contributions
- Introduces IntentGrasp, a comprehensive benchmark for intent understanding from 49 corpora across 12 domains
- Provides large-scale training set (262,759 instances) and two evaluation sets (All Set: 12,909; Gem Set: 470)
- Demonstrates poor LLM performance: below 60% on All Set, below 25% on Gem Set; 17/20 worse than random baseline
- Proposes Intentional Fine-Tuning (IFT) yielding 30+ F1 points on All Set and 20+ on Gem Set
- Shows strong cross-domain generalizability through leave-one-domain-out experiments