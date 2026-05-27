---
title: "Intent Signal Theory: A Computational Framework for Intent-State Control in Human-AI Interaction"
type: paper
tags: [intent-understanding, intent-signal, computational-framework, human-AI, theory]
authors: [Gang Peng]
year: 2026
venue: arXiv
citation_count: null
arxiv_id: "2605.25058"
doi: null
pdf_url: "https://arxiv.org/pdf/2605.25058"
sub_area: intent-understanding
---

## Abstract

Current AI interaction models treat the prompt as the primary object of exchange, omitting a critical layer: the user's latent source intent, the goal state preceding and motivating the prompt. Here we introduce Intent Signal Theory (IST), a computational framework that formalises this missing intent layer. IST distinguishes four objects routinely conflated: latent source intent (I*), observable intent proxy (I-hat), encoded carrier (P), and model output (O). It formalises dimensional weights, encoding masks, structural and fidelity recovery scores, and public-private intent decomposition. The Theorem of Irreversible Intent Loss establishes that private intent absent from the carrier cannot be recovered beyond generic substitution. Evidence from four companion studies spanning six LLMs, three languages and three task domains shows structural-fidelity splits, human-validated metric dissociation, and weight-tolerance plateaus consistent with IST's predictions. IST reframes prompt engineering as intent-protocol design and identifies a computational layer that current AI systems lack.

## Key Contributions

1. Intent Signal Theory (IST): computational framework for the missing intent layer
2. Four-object distinction: I* (latent intent), I-hat (observable proxy), P (encoded carrier), O (model output)
3. Theorem of Irreversible Intent Loss: private intent absent from carrier cannot be recovered
4. Dimensional weights, encoding masks, structural/fidelity recovery scores
5. Public-private intent decomposition
6. Empirical validation across 6 LLMs, 3 languages, 3 task domains
7. Reframing prompt engineering as intent-protocol design

## Core Concepts

- **I*** (latent source intent): the user's true underlying goal
- **I-hat** (observable intent proxy): what can be observed from behavior
- **P** (encoded carrier): the prompt/input encoding
- **O** (model output): the system response
- Irreversible Intent Loss: information lost in encoding cannot be recovered