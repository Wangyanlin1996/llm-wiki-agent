---
title: "IntentExpectation"
type: concept
tags: [data-type, intent, 5g]
sources: [28312-j50]
last_updated: 2026-05-22
---

## Summary

IntentExpectation is the core dataType in 3GPP TS 28.312 representing a combination of requirements, goals, and contexts for a set of expectation objects with the same properties. Each intent may contain one or multiple IntentExpectations, allowing the consumer to express different requirements for different object types.

## Structure

An IntentExpectation contains:

- **expectationObject**: The object(s) for which the expectation is addressed (e.g., network slice, radio network, service)
- **expectationTarget(s)**: Desired characteristics as tuples of [targetName, condition, value range]
- **context(s)**: Conditions under which the targets should be achieved, also as [attribute, condition, value range] tuples

## Expectation Object

The object can be identified by:
- Direct identifier (objectInstance)
- Object context (objectContext) — attribute/condition/value tuples filtering desired objects, e.g., "all network slices in city_ABC" = [(location, =, city_ABC), (objectType, =, network slice)]

## Expectation Target

Each target is a triple: **[targetName, condition, value range]**

Examples:
| targetName | Condition | Value range |
|---|---|---|
| Coverage area | Is greater than | 40 km radius |
| User throughput | Is greater than | 2 Mbps |
| RAN energy consumption | Is less than | X Joules |

## Context

Contexts constrain when targets should be achieved. Same tuple structure as targets but different semantics — conditions trigger management tasks rather than outcomes.

Example: "handoverFailureRate < 2% **if** Load > 80%" → target=(handoverFailureRate, <, 2%), context=(load, >, 80%)

Context selection mechanism: ALL_OF / ONE_OF / ANY_OF — defines how to select among multiple overlapping contexts.

## Scenario-Specific Expectations

TS 28.312 defines scenario-specific IntentExpectation definitions for:
- Radio Network Expectation
- Radio Service Expectation
- Edge Service Support Expectation
- 5GC Network Expectation
- End-to-end Network Optimization Expectation
- Network Maintenance Expectation

## Connections

- [[IntentIOC]] — contains IntentExpectation(s)
- [[IntentDrivenMnS]] — the service managing intents with these expectations
- [[RulePolicyIntentRelation]] — intent expresses "what", policy expresses "how"
- [[PolicyContent]] — contrast: PolicyContent = condition+action, IntentExpectation = object+target+context