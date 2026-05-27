---
title: "Intent Utility Function"
type: concept
tags: [intent, utility, negotiation, 5g]
sources: [28312-j50]
last_updated: 2026-05-22
---

## Summary

Intent Utility Function is a mechanism in 3GPP TS 28.312 that allows MnS consumers to express quantitative preference information as mathematical functions, enabling producers to select solutions that maximize overall satisfaction across multiple intents.

## Components

- **Variables**: Quantify specific aspects of fulfilment (e.g., expectation targets)
- **Weights**: Define relative importance of each variable (e.g., latency weight > throughput weight)
- **Function**: Mathematical expression applied to variables (linear, logarithmic, polynomial, scalar)
- **Result**: Output representing utility level / satisfaction achieved

## Use Cases

- When no solution fully satisfies all intents, utility functions help producers balance trade-offs
- Can be defined per-intent or across multiple intents
- Aggregation possible when an intent has multiple expectations with different utility functions
- Normalization needed when variables have different scales (ms, Mbps, Joules)

## Examples

- U1 = f(throughput, latency, packetLoss) — single function for an intent
- U2 = f(latency) and U3 = f(throughput) — multiple functions for different expectations

## Model

Defined via IntentUtilityFormula IOC (referenced by [[IntentIOC]]'s intentUtilityFormulaRef attribute), containing UtilityDefinition and UtilityParameter dataTypes.

## Connections

- [[IntentIOC]] — references utility formulas via intentUtilityFormulaRef
- [[IntentDrivenMnS]] — the service supporting utility functions
- [[IntentNegotiation]] — utility functions used during negotiation
- [[IntentReport]] — utility results reported via intentUtilityReports