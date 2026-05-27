---
title: "PolicyContent"
type: concept
tags: [data-type, policy, 5g]
sources: [28556-j00]
last_updated: 2026-05-22
---

## Summary

PolicyContent is a dataType defined in 3GPP TS 28.556 that represents the core logic of a network policy through a condition-action pair. When a condition is met, the corresponding action is triggered.

## Attributes

| Attribute | Support Qualifier | Readable | Writable | Invariant | Notifyable |
|---|---|---|---|---|---|
| condition | M (Mandatory) | Yes | Yes | No | Yes |
| action | M (Mandatory) | Yes | Yes | No | Yes |

## Attribute Definitions

- **condition**: Identifies the trigger condition for the policy. The type depends on the concrete policy implementation (not specified in the standard).
- **action**: Identifies the action to execute when the condition is met. The type also depends on the concrete policy.

## Connections

- [[PolicyIOC]] — contains PolicyContent as its policyContent attribute
- [[PolicyMnS]] — the management service managing policies with this structure
- [[5GNetworkManagement]] — broader management domain