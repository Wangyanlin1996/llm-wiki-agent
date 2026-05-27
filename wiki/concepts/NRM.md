---
title: "NRM"
type: concept
tags: [nrm, information-model, network-resource, 5g]
sources: [28622-k20]
last_updated: 2026-05-22
---

## Summary

Network Resource Model (NRM) is a 3GPP concept defined in TS 28.622 as "a collection of IOCs, inclusive of their associations, attributes and operations, representing a set of network resources under management." The Generic NRM (TS 28.622) provides the foundational IOCs and data types that domain-specific NRMs (TS 28.541 for 5G, etc.) extend.

## Structure

An NRM defines:
- **IOCs** (Information Object Classes) — management aspects of network resources
- **Associations** — relationships between IOCs (reference attributes, containment)
- **Attributes** — properties of IOCs
- **Operations** — management services invocable on IOC instances
- **Notifications** — event reporting for IOC instances

An NRM instance (MIB - Management Information Base) consists of:
1. Name space (DN containment hierarchy)
2. Managed Objects with attributes
3. Associations between MOs

## Generic vs Domain-Specific

- **Generic NRM** (TS 28.622): [[TopIOC]], SubNetwork, ManagedElement, ManagedFunction, etc.
- **5G NRM** (TS 28.541): Extends Generic with 5G-specific IOCs (gNB, NRCellDU, AMF, etc.)
- **Policy NRM** (TS 28.556): Extends Generic with [[PolicyIOC]]
- **Intent NRM** (TS 28.312): Extends Generic with [[IntentIOC]], [[IntentReport]], [[IntentHandlingFunction]]

## Key Definition

> "A network resource: discrete entity represented by an Information Object Class (IOC) for the purpose of network and service management." — TS 28.622 Section 3.1

> "Network Resource Model (NRM): A collection of IOCs, inclusive of their associations, attributes and operations, representing a set of network resources under management." — TS 28.622 Section 3.1

## Connections

- [[TopIOC]] — the root IOC anchoring the NRM hierarchy
- [[TS28622]] — the Generic NRM specification
- [[5GNetworkManagement]] — the broader domain using NRM
- [[PolicyIOC]] — policy-specific NRM extension
- [[IntentIOC]] — intent-specific NRM extension