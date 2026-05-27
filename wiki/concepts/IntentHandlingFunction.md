---
title: "Intent Handling Function"
type: concept
tags: [intent, capability, 5g]
sources: [28312-j50]
last_updated: 2026-05-22
---

## Summary

IntentHandlingFunction is an IOC in 3GPP TS 28.312 representing the intent handling capabilities of a specific function within the MnS producer. It exposes what expectation objects and targets the producer can support, enabling MnS consumers to discover capabilities before expressing intents.

## Key Points

- Instances are created/modified/deleted by MnS producer only — consumers cannot manage them
- MnS consumers query IntentHandlingFunction to discover supported expectation objects, targets, and value ranges
- Multiple IntentHandlingFunction instances may exist, each supporting different domains (e.g., one for RAN, one for 5GC)
- The DN of an IntentHandlingFunction instance can be used to query all Intent instances it handles

## Capability Exposure

IntentHandlingCapability dataType includes:
- Supported expectation object types and corresponding targets
- Supported value ranges for targets
- Description of alternative expectations that can be evaluated

## Connections

- [[IntentDrivenMnS]] — the service providing these functions
- [[IntentIOC]] — intents handled by this function
- [[IntentExpectation]] — expectations supported by this function
- [[3GPP]] — standards body