---
title: "From Storage to Experience"
type: source
tags: [agent-memory, survey, LLM-agent, memory-evolution]
date: 2026-05-09
source_file: raw/papers/agent-memory-survey.md
last_updated: 2026-05-27
---

## Summary
This survey proposes a novel evolutionary framework for LLM agent memory, formalizing three stages: Storage (trajectory preservation), Reflection (trajectory refinement), and Experience (trajectory abstraction). It bridges the fragmented OS engineering and cognitive science perspectives, identifying proactive exploration and cross-trajectory abstraction as frontier mechanisms in the Experience stage.

## Key Claims
- Agent memory research is fragmented between OS engineering and cognitive science
- Memory evolution follows Storage→Reflection→Experience trajectory
- Three core drivers: long-range consistency, dynamic environments, continual learning
- Frontier Experience stage features proactive exploration and cross-trajectory abstraction

## Key Quotes
> "current research remains fragmented, oscillating between operating system engineering and cognitive science" — fragmentation diagnosis

> "formalizing the development process into three stages: Storage, Reflection, and Experience" — evolutionary framework

## Connections
- [[AgentMemory]] — the survey provides the evolutionary framework for AgentMemory mechanisms
- [[EvoMemory]] — test-time evolution aligns with the Experience stage in the framework
- [[LightMem]] — SLM-driven lightweight memory fits within the Storage→Reflection progression
- [[Emem]] — episodic context reconstruction represents a shift toward the Experience stage
- [[IntentUnderstanding]] — proactive exploration in Experience stage connects to intent understanding
- [[IntentRecommendation]] — cross-trajectory abstraction enables proactive intent recommendation

## Contradictions
- Contradicts OS-engineering-only view of memory: the survey argues memory must evolve beyond storage toward experiential abstraction