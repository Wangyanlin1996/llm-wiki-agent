---
title: "IntentRL"
type: source
tags: [intent-recommendation, proactive-agent, reinforcement-learning]
date: 2026-02-03
source_file: raw/papers/intentrl.md
last_updated: 2026-05-27
---

## Summary
IntentRL trains proactive agents to clarify latent user intents before starting deep research, resolving the autonomy-interaction dilemma. It uses a shallow-to-deep intent refinement graph and two-stage RL (offline dialogues + online rollouts with user simulator), outperforming built-in clarify modules of closed-source DR agents.

## Key Claims
- Deep research agents face an autonomy-interaction dilemma on ambiguous queries
- Proactive intent clarification before research improves outcomes
- Shallow-to-deep intent refinement graph scales training data
- Two-stage RL (offline+online simulator) achieves strong intent clarification
- Outperforms closed-source DR agents' built-in clarify modules

## Key Quotes
> "high autonomy on ambiguous user queries often leads to prolonged execution with unsatisfactory outcomes" — dilemma

> "IntentRL trains proactive agents to clarify latent user intents before starting long-horizon research" — approach

## Connections
- [[IntentRecommendation]] — IntentRL implements proactive IntentRecommendation via RL
- [[IntentRL]] — the RL-trained proactive intent clarification concept formalized here
- [[IntentUnderstanding]] — intent clarification is a form of IntentUnderstanding
- [[PIRABench]] — PIRA-Bench evaluates proactive intent recommendation relevant to IntentRL
- [[PASK]] — proactive agent paradigm aligned with IntentRL's proactive clarification

## Contradictions
- Contradicts full-autonomy assumption: IntentRL demonstrates that proactively clarifying intent before deep research yields better outcomes