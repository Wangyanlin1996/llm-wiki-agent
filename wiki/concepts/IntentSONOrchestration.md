---
title: "Intent-driven SON Orchestration"
type: concept
tags: [intent, son, orchestration, 5g]
sources: [28912-j00]
last_updated: 2026-05-22
---

## Summary

Intent-driven SON (Self-Organizing Network) Orchestration is a mechanism studied in 3GPP TR 28.912 where SON functions are driven by intent expectations. The SON orchestrator categorizes received intents into three types based on whether parameters and contexts reference network control parameters or KPIs, and detects contradictions within SON execution.

## Intent Types for SON

| Type | Parameters | Context | Example |
|---|---|---|---|
| Type 1 | Network control parameters | None or control parameters | Increase cell TXP; make cell TXP constant |
| Type 2 | KPIs | None or KPIs | Reduce cell interference; increase cell throughput |
| Type 3 | Mixed (control params + KPIs) | Mixed | Make cell TXP constant AND reduce interference |

If an intent does not fit any of these three categories, SON orchestration informs the consumer that the intent cannot be executed via SON.

## Contradiction Detection

SON orchestration may detect contradictions between targets on different expectations. These are reported to the intent MnS consumer via attributes in FulfilmentInfo or intent report, indicating contradictions detected in SON orchestration (distinct from intent-level conflicts).

## Connections

- [[IntentDrivenMnS]] — the service that can leverage SON orchestration for intent fulfilment
- [[IntentIOC]] — the intent being orchestrated
- [[IntentExpectation]] — expectations categorized for SON
- [[IntentConflictResolution]] — related but distinct (SON contradictions vs intent conflicts)
- [[3GPP]] — standards body