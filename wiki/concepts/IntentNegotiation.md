---
title: "Intent Negotiation"
type: concept
tags: [intent, negotiation, 5g]
sources: [28312-j50]
last_updated: 2026-05-22
---

## Summary

Intent negotiation in 3GPP TS 28.312 enables collaborative interactions between MnS consumer and MnS producer to find the best way to fulfil intents. Negotiation occurs in two phases: pre-evaluation (before intent submission) and fulfilment (after submission).

## Pre-Evaluation Phase

| Capability | Description |
|---|---|
| Intent feasibility check | Check if proposed intent can be supported by producer |
| Intent exploration | Find best values for targets/contexts aligned with producer capabilities |

Two exploration scenarios:
1. Explore best value for a single target/context
2. Explore best combination of values for multiple targets/contexts (e.g., balancing energy saving vs throughput)

## Fulfilment Phase

| Capability | Description |
|---|---|
| Check fulfillable outcomes | Obtain list of possible outcomes the producer can deliver |
| Check best possible outcome | Find best outcome for specific or all targets while keeping others unchanged |
| Recommend fulfillable outcomes | Producer provides recommended targets/contexts |
| Advise on preferred outcome | Consumer advises preference among alternatives, possibly with utility function or satisfaction index |

## IS Operations

| Operation | IS Mapping |
|---|---|
| Intent feasibility check | createMOI |
| Intent exploration | createMOI |
| Intent fulfilment negotiation | createMOI / modifyMOIAttributes |

## Connections

- [[IntentDrivenMnS]] — the service providing negotiation
- [[IntentIOC]] — the intent being negotiated
- [[IntentReport]] — negotiation reports
- [[IntentUtilityFunction]] — used for preference quantification in negotiation
- [[IntentConflictResolution]] — conflicts may trigger negotiation