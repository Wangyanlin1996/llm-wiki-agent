---
title: "Intent Driven MnS"
type: concept
tags: [intent, management-service, 5g]
sources: [28312-j50]
last_updated: 2026-05-22
---

## Summary

Intent Driven Management Service (IDMS) is a 3GPP-defined management service that allows consumers to express desired network/service outcomes as intents (declarative "what" statements), while the producer determines "how" to achieve them. It replaces traditional rule/policy-based management with a higher abstraction level.

## Key Capabilities

- **Intent lifecycle**: Create, Delete, Modify, Query, Activate, Deactivate — all via generic provisioning MnS operations from [[TS28532]]
- **Intent translation**: Producer translates intents to executable actions (policies, closed loops, AI/ML mechanisms)
- **Intent reporting**: Producer reports fulfilment status, conflicts, feasibility, exploration results, negotiation outcomes, and utility results
- **Intent negotiation**: Pre-evaluation (feasibility check, exploration) and fulfilment (negotiation on outcomes)
- **Intent closed-loop**: Intents can be translated to policies driving closed-loop automation (implementation not standardized)

## Intent Fulfilment Categories

- **Intent deployment**: Steps to satisfy a newly received intent (initial setup)
- **Intent assurance**: Recurring actions to maintain ongoing quality requirements (continuous monitoring)

## Role-Based Intent Types

| Role | Intent Type | Example |
|---|---|---|
| CSC (Communication Service Customer) | Intent-CSC | "Enable V2X service for vehicles" |
| CSP (Communication Service Provider) | Intent-CSP | "Provide network supporting 500 vehicles on highway" |
| NOP (Network Operator) | Intent-NOP | "Provide radio network satisfying coverage in area" |

Intent translation chains: CSC→CSP→NOP→NEP, each level translates to lower-level intents.

## Connections

- [[IntentIOC]] — the information object class for intents
- [[IntentExpectation]] — how expectations are structured
- [[IntentReport]] — how results are reported
- [[IntentHandlingFunction]] — capability exposure
- [[IntentConflictResolution]] — conflict handling
- [[IntentNegotiation]] — negotiation mechanisms
- [[IntentUtilityFunction]] — preference quantification
- [[RulePolicyIntentRelation]] — relationship to policy/rule
- [[PolicyMnS]] — complementary policy-based management
- [[3GPP]] — standards body
- [[TS28532]] — generic provisioning MnS foundation