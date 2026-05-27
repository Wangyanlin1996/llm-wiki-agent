---
title: "Rule-Policy-Intent Relation"
type: concept
tags: [intent, policy, rule, abstraction, 5g]
sources: [28312-j50]
last_updated: 2026-05-22
---

## Summary

The Rule→Policy→Intent relation described in 3GPP TS 28.312 Section 4.4 represents a progressive shift in management abstraction from "how" to "what":

- **Rule**: Explicit or formula logic to be executed — fully specifies "how" (e.g., if X > threshold, execute command Y)
- **Policy**: Conditional action specification — specifies what action to take when a condition occurs, but leaves some flexibility (e.g., when throughput < 5Mbps, take optimization actions)
- **Intent**: Declarative goal specification — specifies "what" outcome is desired without specifying "how" (e.g., average throughput > 5Mbps in this area)

## Abstraction Spectrum

```
Rule ←— "how" focus —→ Policy ←— shifting to "what" —→ Intent
  (explicit logic)       (condition-action)          (declarative goal)
```

Current telecom systems are mainly at the rule/policy level ("how" focus). The increasing complexity of 5G networks drives the shift toward intent ("what" focus).

## Practical Relationship

- Intent can be **translated** to policies for closed-loop automation (see [[IntentDrivenMnS]] Section 4.3)
- Policy can be **translated** to rules for execution
- Intent → Policy → Rule is a decomposition chain from abstract to concrete
- [[PolicyMnS]] and [[IntentDrivenMnS]] are complementary: intent expresses the goal, policy defines the conditional actions to achieve it

## Model Comparison

| Aspect | Rule | Policy ([[PolicyIOC]]) | Intent ([[IntentIOC]]) |
|---|---|---|---|
| Focus | How | How+What | What |
| Model | Explicit logic | condition + action | expectationObject + target + context |
| Flexibility | None | Conditional | Declarative |
| Implementation | Fully specified | Partially specified | Not specified |

## Connections

- [[PolicyMnS]] — policy management at middle abstraction level
- [[IntentDrivenMnS]] — intent management at highest abstraction level
- [[PolicyIOC]] — the policy data structure
- [[IntentIOC]] — the intent data structure
- [[PolicyContent]] — policy's condition-action model
- [[IntentExpectation]] — intent's object-target-context model
- [[5GNetworkManagement]] — broader management domain