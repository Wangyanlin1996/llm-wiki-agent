---
title: "Intent Report"
type: concept
tags: [intent, report, 5g]
sources: [28312-j50]
last_updated: 2026-05-22
---

## Summary

IntentReport is an IOC in 3GPP TS 28.312 that represents intent report information from MnS producer to MnS consumer. It is created by the MnS producer based on the IntentReportControl specified in the [[IntentIOC]]. When an intent is deleted, its corresponding IntentReport instance is automatically deleted.

## Report Types

| Report Type | Attribute | Content |
|---|---|---|
| Fulfilment report | intentFulfilmentReport | Fulfilment status and achieved values for targets |
| Conflict report | intentConflictReports | Conflict type (intent/expectation/target) + solutions |
| Feasibility check report | intentFeasibilityCheckReport | Feasible or infeasible, with reasons |
| Exploration report | intentExplorationReport | Best values for targets/contexts during pre-evaluation |
| Negotiation report | intentFulfilmentNegotiationReport | Alternatives and outcomes during fulfilment phase |
| Utility report | intentUtilityReports | Utility function calculation results |

## Attributes

All report attributes are CM (conditional mandatory) — present only if the corresponding capability is supported by the intent handling function. Key attributes:

- intentFulfilmentReport, intentConflictReports, intentFeasibilityCheckReport, intentExplorationReport, intentFulfilmentNegotiationReport, intentUtilityReports (all CM, Read-only, Notifyable)
- lastUpdatedTime (M)
- intentReference (M, Read-only) — DN reference to the associated Intent instance

## Management Operations

| Operation | IS Operation |
|---|---|
| Query intent report | getMOIAttributes |
| Subscribe intent report | createMOI (on NtfSubscriptionControl) |
| Notify intent report | notifyMOIAttributeValueChanges |
| Unsubscribe intent report | deleteMOI |

## Connections

- [[IntentIOC]] — the intent this report belongs to
- [[IntentDrivenMnS]] — the service producing reports
- [[IntentConflictResolution]] — conflict information in reports
- [[IntentNegotiation]] — negotiation information in reports
- [[IntentUtilityFunction]] — utility results in reports