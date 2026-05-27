---
title: "Policy IOC"
type: concept
tags: [information-model, policy, 5g]
sources: [28556-j00]
last_updated: 2026-05-22
---

## Summary

The Policy Information Object Class (IOC) is the core data structure defined in 3GPP TS 28.556 for representing a network policy. It inherits from the Top IOC (defined in TS 28.622) and encapsulates priority, status, type, and content of a policy.

## Attributes

| Attribute | Support Qualifier | Readable | Writable | Invariant | Notifyable |
|---|---|---|---|---|---|
| policyPriority | M (Mandatory) | Yes | Yes | No | Yes |
| policyStatus | M | Yes | Yes | No | Yes |
| policyType | M | Yes | Yes | No | Yes |
| policyContent | M | Yes | Yes | No | Yes |

## Attribute Definitions

- **policyPriority**: ENUM (LOW, Medium, High) — specifies the priority level of the policy
- **policyStatus**: ENUM (ACTIVATED, DEACTIVATED), default DEACTIVATED — indicates whether the policy is active
- **policyType**: string, multiplicity 0..N — specifies the type of policy (value not defined in this spec)
- **policyContent**: [[PolicyContent]] dataType, multiplicity 1 — identifies the condition-action content

## Notifications

Inherits generic provisioning MnS notifications (notifyMOICreation, notifyMOIDeletion, etc.) and adds the notifyPolicyConflict notification (see [[PolicyConflictDetection]]).

## Connections

- [[PolicyMnS]] — the management service using this IOC
- [[PolicyContent]] — the contained dataType
- [[3GPP]] — defining standards body
- [[TS28622]] — Top IOC inheritance source