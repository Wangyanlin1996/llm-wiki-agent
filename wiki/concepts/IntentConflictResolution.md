---
title: "Intent Conflict Resolution"
type: concept
tags: [intent, conflict, 5g]
sources: [28312-j50]
last_updated: 2026-05-22
---

## Summary

Intent conflict resolution in 3GPP TS 28.312 covers detection and handling of three types of conflicts: target conflict (within same expectation), expectation conflict (within same intent), and intent conflict (between different intents). Conflicts arise when actions for one target degrade another target.

## Three Conflict Types

| Conflict Type | Scope | Example |
|---|---|---|
| Target conflict | Two targets in same expectation | throughput↑ vs interference↓ |
| Expectation conflict | Two expectations in same intent | latency expectation vs throughput expectation |
| Intent conflict | Two different intents | Energy-saving intent vs coverage intent |

## Resolution Mechanisms

- **Suspension**: Producer suspends conflicting intent or whole intent containing conflicts
- **Recommendation**: Producer recommends new intent (modified expectations, targets, or reduced scope)
- **Preemption**: intentPriority and intentPreemptionCapability allow higher-priority intents to preempt lower ones
- **Consumer guidance**: Consumer can provide ordered expectation lists or explicit priorities
- **Reduced scope**: Consumer may narrow expected managed entities to resolve conflict

## Reporting

Conflict information is included in [[IntentReport]] via intentConflictReports attribute, containing conflict type and possible solutions.

## Comparison with Policy Conflict

[[PolicyConflictDetection]] in TS 28.556 detects when a new policy conflicts with a stored policy and notifies via notifyPolicyConflict. Intent conflict is richer — three conflict levels, with resolution recommendations and preemption mechanisms.

## Connections

- [[IntentDrivenMnS]] — the service performing conflict detection
- [[IntentIOC]] — intents that may conflict
- [[IntentExpectation]] — expectations/targets that may conflict
- [[IntentReport]] — where conflict info is reported
- [[PolicyConflictDetection]] — simpler policy-level conflict mechanism