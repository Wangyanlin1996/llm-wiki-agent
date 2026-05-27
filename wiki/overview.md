---
title: "Overview"
type: synthesis
tags: []
sources: [28556-j00, 28312-j50, 28622-k20, 28912-j00, 28914-j00]
last_updated: 2026-05-22
---

# Overview

## 5G Network Management: Policy and Intent

The wiki covers two complementary 3GPP management specifications for 5G networks:

- **TS 28.556** ([[PolicyMnS]]) — Policy-based management: "what action to take when condition occurs"
- **TS 28.312** ([[IntentDrivenMnS]]) — Intent-based management: "what outcome to achieve, without specifying how"

### Abstraction Hierarchy

The [[RulePolicyIntentRelation]] describes a progressive shift in management paradigm:

```
Rule (explicit logic) → Policy (condition+action) → Intent (declarative goal)
        "how"                          "how+what"                "what"
```

Policy ([[PolicyIOC]]) uses a simple **condition-action** model ([[PolicyContent]]). Intent ([[IntentIOC]]) uses a richer **expectationObject + expectationTarget + context** model ([[IntentExpectation]]). Intent can be translated to policies for closed-loop automation, but the reverse is not true — policies cannot express abstract goals.

### Policy Management (TS 28.556)

A [[PolicyIOC]] instance has four mandatory attributes: policyPriority (LOW/Medium/High), policyStatus (ACTIVATED/DEACTIVATED), policyType, and policyContent. Lifecycle managed via generic provisioning MnS from [[TS28532]]. [[PolicyConflictDetection]] provides single-level conflict notification (notifyPolicyConflict).

### Intent Management (TS 28.312)

An [[IntentIOC]] instance carries intentExpectations, intentAdminState, intentPriority, intentReportControl, and advanced features (intentPreemptionCapability, implicitIntentIndex, intentUtilityFormulaRef). Intent lifecycle has six states: ACKNOWLEDGED → COMPLIANT → FULFILLED → DEGRADED (with SUSPENDED and FULFILLMENT_FAILED as alternate paths).

Intent expectations are categorized by user role:
- **Intent-CSC** — Communication Service Customer expresses service expectations
- **Intent-CSP** — Communication Service Provider expresses network expectations
- **Intent-NOP** — Network Operator expresses subnetwork expectations

Intent translation chains across roles: CSC→CSP→NOP→NEP.

### Conflict Handling Comparison

| Feature | Policy (TS 28.556) | Intent (TS 28.312) |
|---|---|---|
| Conflict levels | Single (policy vs policy) | Three (target, expectation, intent) |
| Resolution | Notification only | Preemption, recommendations, negotiation |
| Notification | notifyPolicyConflict | IntentReport with conflictReports |

### Intent Advanced Features

- **[[IntentNegotiation]]** — Pre-evaluation (feasibility check, exploration) and fulfilment phase (alternative outcomes, best possible outcome)
- **[[IntentUtilityFunction]]** — Mathematical preference expression (variables, weights, function, result) for quantitative solution selection
- **[[IntentReport]]** — Six report types: fulfilment, conflict, feasibility, exploration, negotiation, utility
- **[[IntentHandlingFunction]]** — Producer capability exposure (supported objects, targets, value ranges)

### Standards Context

Both specifications are part of the [[5GNetworkManagement]] family (TS 28.x series), produced by [[3GPP]] TSG SA5. They reuse generic provisioning MnS from [[TS28532]] and inherit from [[TopIOC]] defined in [[TS28622]].

### Foundation: Generic NRM (TS 28.622)

TS 28.622 provides the foundational [[NRM]] information model. The [[TopIOC]] is the root of the IOC inheritance hierarchy — all domain-specific IOCs (Policy, Intent, IntentReport, IntentHandlingFunction) inherit from it via TopX (mandatory objectClass + objectInstance attributes). Key foundation IOCs include SubNetwork (managed entity sets), ManagedElement (NE representation), ManagedFunction (functional sub-classing), NtfSubscriptionControl (notification subscriptions), and common data types (GeoArea, TimeWindow, SchedulingTime).

### Study Reports: TR 28.912 (Rel-18) and TR 28.914 (Rel-19)

The normative TS 28.312 features were informed by two study TRs:

- **TR 28.912** (Rel-18): Studied intent-driven RAN energy saving, three-level conflict classification, 5GC expectations, [[IntentReport]] IOC, closed-loop composition, [[IntentHandlingFunction]], [[IntentSONOrchestration]], [[IntentMDA]], AI/ML capability mapping, and TM Forum collaboration
- **TR 28.914** (Rel-19): Studied enhanced radio service/network expectations, implicit intent report, intent degradation (PreferenceWeight), [[IntentUtilityFunction]] with satisfaction index, [[IntentNegotiation]] during fulfilment, intent exploration, feasibility check (intentMgmtPurpose), network maintenance intent, and vendor extension guidelines