---
title: "Intent Recommendation"
type: concept
tags: [intent-recommendation, proactive-agent, GUI-agent, intent-detection]
sources: [intentrl, pira-bench, pask, vitabench2]
last_updated: 2026-05-27
---

# Intent Recommendation

Intent Recommendation refers to AI agents proactively detecting and suggesting actions based on inferred user intent, transitioning from reactive (explicit instruction required) to proactive (agent anticipates needs) paradigm.

## Paradigm Transition

Current GUI and conversational agents operate reactively ([[PIRABench]] identifies this). The proactive paradigm requires:
- Detecting actionable events from continuous input (visual, conversational)
- Fitting recommendations to user preferences and profiles
- Managing multiple interleaved intent threads
- Handling noisy and ambiguous input segments

## Key Approaches

- **[[IntentRL]]**: RL-trained proactive agents for intent clarification before deep research; shallow-to-deep intent refinement graph; two-stage RL (offline dialogues + online simulator); outperforms closed-source DR clarify modules
- **[[PIRABench]]**: first benchmark for proactive intent recommendation on GUI; proposes [[PIRF]] memory-aware state-tracking framework; complex trajectories with interleaved intents
- **[[PASK]]**: DD-MM-PAS paradigm (Demand Detection → Memory Modeling → Proactive Agent System); [[IntentFlow]] demand detection; hybrid memory (workspace/user/global); [[LatentNeeds-Bench]] real-world evaluation

## DD-MM-PAS Paradigm

The [[PASK]] paper proposes a general paradigm for streaming proactive agents:
1. **DD** (Demand Detection): [[IntentFlow]] detects user needs from streaming interactions
2. **MM** (Memory Modeling): hybrid memory (workspace, user, global) for long-term context
3. **PAS** (Proactive Agent System): closed-loop detection-memory-action infrastructure

## Cross-direction Relevance

Intent recommendation depends on [[AgentMemory]] for storing past interactions and user preferences ([[PASK]] hybrid memory, [[PIRF]] state tracking). It also requires [[IntentUnderstanding]] to infer latent intent before recommending ([[IntentRL]] clarifies intent before research).

## Key Challenge

Real-world intent is fragmented and interleaved across multiple threads — agents must disambiguate noise from actionable events while maintaining preference-aware recommendations ([[PIRABench]]).