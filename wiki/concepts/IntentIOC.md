---
title: "Intent IOC"
type: concept
tags: [information-model, intent, 5g]
sources: [28312-j50]
last_updated: 2026-05-22
---

## Summary

The Intent Information Object Class (IOC) is the core data structure in 3GPP TS 28.312 for representing an intent between MnS consumer and MnS producer. It inherits from Top IOC (TS 28.622) and encapsulates intent expectations, administrative state, report control, priority, and advanced features like utility functions and implicit intent discovery.

## Attributes

| Attribute | SQ | Readable | Writable | Invariant | Notifyable |
|---|---|---|---|---|---|
| intentExpectations | M | Yes | Yes | No | No |
| userLabel | M | Yes | Yes | No | No |
| intentMgmtPurpose | M | Yes | Yes | No | No |
| contextSelectivity | O | Yes | Yes | No | No |
| expectationSelectivity | O | Yes | Yes | No | No |
| intentContexts | O | Yes | Yes | No | No |
| intentReportControl | M | Yes | Yes | No | No |
| intentPriority | O | Yes | Yes | No | Yes |
| intentAdminState | CM | Yes | Yes | No | No |
| intentPreemptionCapability | CM | Yes | Yes | No | No |
| implicitIntentIndex | CM | Yes | Yes | No | No |
| consumerSatisfactionIndexThreshold | CO | Yes | Yes | No | No |
| intentReportReference | M | Yes | No | No | No |
| intentUtilityFormulaRef | CM | Yes | Yes | No | Yes |

## Key Attribute Definitions

- **intentExpectations**: List of [[IntentExpectation]] — the core content expressing desired outcomes
- **intentAdminState**: ACTIVATED/DEACTIVATED — supports intent suspension mechanism (CM: conditional mandatory)
- **intentPriority**: Integer — priority for conflict resolution among intents
- **intentPreemptionCapability**: Indicates whether this intent can preempt lower-priority intents (CM)
- **contextSelectivity**: ALL_OF / ONE_OF / ANY_OF — how to select among intent-level contexts
- **expectationSelectivity**: ALL_OF / ONE_OF / ANY_OF — how to select among alternative expectations (for feasibility validation). **Note**: This attribute's detailed semantics (ONE_OF = satisfy any one expectation, ANY_OF = satisfy as many as possible, ALL_OF = satisfy all) are defined only in the Stage 3 YAML (`TS28312_IntentNrm.yaml:246-250`), not explicitly described in the Stage 2 prose of the source document `[[28312-j50]]`
- **implicitIntentIndex**: Boolean — enables/disables discovery of implicit intent information
- **intentReportControl**: [[IntentReportControl]] dataType — specifies report types, conditions, and frequency
- **intentUtilityFormulaRef**: Reference to [[IntentUtilityFunction]] instance(s)

## Intent Handling State Lifecycle

| State | Transition Trigger |
|---|---|
| ACKNOWLEDGED | Intent instance created |
| COMPLIANT | Feasibility check result is 'feasible' |
| FULFILLMENT_FAILED | Feasibility check result is 'infeasible' or producer cannot fulfil |
| SUSPENDED | intentAdminState set to DEACTIVATED |
| FULFILLED | Producer considers intent satisfied |
| DEGRADED | Previously fulfilled intent no longer meets requirements |
| TERMINATED | Intent deleted |

## Connections

- [[IntentDrivenMnS]] — the management service managing Intent IOC instances
- [[IntentExpectation]] — the contained expectations
- [[IntentReport]] — the associated report instance
- [[IntentHandlingFunction]] — the function handling this intent
- [[IntentUtilityFunction]] — optional utility formula reference
- [[3GPP]] — standards body
- [[TS28622]] — Top IOC inheritance source