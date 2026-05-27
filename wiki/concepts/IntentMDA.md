---
title: "Intent-driven MDA"
type: concept
tags: [intent, mda, analytics, 5g]
sources: [28912-j00]
last_updated: 2026-05-22
---

## Summary

Intent-driven MDA (Management Data Analytics) is a mechanism studied in 3GPP TR 28.912 where MDA functions are triggered by intent expectations. When the intent MnS producer receives an intent, it checks whether the ExpectationTargets are within the supportedMDACapabilities of correlated MDA functions, and if so, requests analysis via MDARequest.

## Procedure

1. Intent MnS producer receives intent with ExpectationTargets
2. Checks whether targets are within supportedMDACapabilities of correlated MDA function(s)
3. If not supported → informs consumer that intent cannot be fulfilled due to lack of MDA capability
4. If supported → creates MDARequest (createMOI) with analysis scope based on expectationObject, requestedMDAOutputs based on expectationTargets, and context information from the intent
5. MDA function performs analysis and returns report
6. Intent MnS producer uses MDA report to decide how to handle intent fulfilment

## Example

If an intent contains dLLatencyTarget or uLLatencyTarget (as in Service Support Expectation from TS 28.312), the correlated MDA function must have latency analysis capability. If it lacks this capability, the intent is reported as unfulfillable.

## Connections

- [[IntentDrivenMnS]] — the service integrating MDA for intent fulfilment
- [[IntentIOC]] — the intent triggering MDA analysis
- [[IntentExpectation]] — expectations whose targets drive MDA scope
- [[3GPP]] — standards body