---
title: "Top IOC"
type: concept
tags: [information-model, nrm, foundation, 5g]
sources: [28622-k20]
last_updated: 2026-05-22
---

## Summary

The Top IOC is the root of the IOC inheritance hierarchy in 3GPP's Federated Network Information Model (FNIM). All information object classes defined in specifications conformant to TS 32.102 must inherit from Top. It inherits from Top_ (from TS 28.620 UIM) and TopX (which provides mandatory objectClass and objectInstance attributes).

## Inheritance Chain

```
Top_ (TS 28.620 UIM) → Top (TS 28.622) → all domain-specific IOCs
                       ↑
                   TopX (objectClass, objectInstance)
```

## Role

- Provides the minimum mandatory attributes (objectClass, objectInstance) that every managed object instance must have
- Name-containment: VsDataContainer can be name-contained by Top (meaning any IOC can optionally carry vendor-specific data)
- All conformant IOCs (including [[PolicyIOC]], [[IntentIOC]], [[IntentReport]]) inherit from Top

## TopX vs Top

- **TopX**: Mandatory attributes only (objectClass, objectInstance) — all conformant IOCs inherit from TopX
- **Top**: Inherits from both Top_ (UIM) and TopX — adds common notification support and VsDataContainer containment

## Connections

- [[TS28622]] — the specification defining Top IOC
- [[PolicyIOC]] — inherits from Top
- [[IntentIOC]] — inherits from Top
- [[NRM]] — the model framework Top anchors