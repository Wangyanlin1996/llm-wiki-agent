---
title: "Policy Conflict Detection"
type: concept
tags: [policy, conflict, notification, 5g]
sources: [28556-j00]
last_updated: 2026-05-22
---

## Summary

Policy Conflict Detection is the mechanism in 3GPP Policy MnS whereby the MnS Producer checks incoming new or updated policies against previously stored policies for conflicts. When a conflict is detected, the producer notifies the consumer via the notifyPolicyConflict notification.

## Notification: notifyPolicyConflict

| Parameter | Qualifier | Description |
|---|---|---|
| objectClass | M | ManagedEntity class name |
| objectInstance | M | DN of the ManagedElement instance |
| notificationId | M | Unique notification identifier |
| eventTime | M | Event occurrence time (ITU-T Generalised Time) |
| systemDN | C | DN of management service producer |
| notificationType | M | "notifyPolicyConflict" |
| conflictDescription | M | Details of the policy conflict (conflicting events, conditions, actions) |

## RESTful HTTP Mapping

The notification is delivered via HTTP POST to `/notificationSink` with parameters mapped to the request body as JSON attributes (href, notificationId, notificationType, eventTime, systemDN, conflictDescription, plus optional correlatedNotifications, additionalText, sourceIndicator, attributeList).

## Connections

- [[PolicyMnS]] — the service performing conflict detection
- [[PolicyIOC]] — the policy objects being checked for conflicts
- [[3GPP]] — defining standards body