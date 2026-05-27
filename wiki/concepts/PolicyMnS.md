---
title: "Policy MnS"
type: concept
tags: [policy, management-service, 5g]
sources: [28556-j00]
last_updated: 2026-05-22
---

## Summary

Policy Management Service (Policy MnS) is a 3GPP-defined management service for creating, managing, and governing network policies in 5G mobile networks. It provides lifecycle management (creation, deletion, update, query, activation, deactivation) and conflict detection/notification capabilities through a MnS Producer–MnS Consumer interaction model.

## Lifecycle Procedures

| Procedure | MnS Consumer Action | MnS Producer Action |
|---|---|---|
| Creation | Sends createMOI request | Creates and configures Policy MOI |
| Deletion | Sends deleteMOI request | Deletes Policy MOI |
| Update | Sends modifyMOIAttributes request | Updates Policy MOI |
| Query | Sends getMOIAttributes request | Queries Policy MOI |
| Activation | Sends activation request | Activates Policy MOI |
| Deactivation | Sends deactivation request | Deactivates Policy MOI |

## Conflict Detection

When the MnS Producer receives a new or updated policy, it checks for conflicts with existing stored policies. If detected, it sends a notifyPolicyConflict notification (see [[PolicyConflictDetection]]) to the MnS Consumer.

## Information Model

The [[PolicyIOC]] inherits from Top IOC and carries four mandatory attributes: policyPriority, policyStatus, policyType, and [[PolicyContent]].

## Solution Sets

- **RESTful HTTP**: PUT (create), GET (query), PUT/PATCH (modify), DELETE (delete) operations mapped to HTTP methods on PoliMnS resource URIs
- **YANG/NETCONF**: Uses generic provisioning MnS solution set from [[TS28532]]

## Connections

- [[3GPP]] — standards body defining Policy MnS
- [[PolicyIOC]] — the information object class for policies
- [[PolicyContent]] — condition-action data type
- [[PolicyConflictDetection]] — conflict notification mechanism
- [[5GNetworkManagement]] — broader management context
- [[TS28532]] — referenced generic management services