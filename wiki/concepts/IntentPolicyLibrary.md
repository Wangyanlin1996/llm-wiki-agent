---
title: "Intent Policy Library"
type: concept
tags: [3gpp, intent, policy, telecom, governance]
sources: [28312-j50, 28914-j00]
last_updated: 2026-05-29
---

# 意图策略库（Intent Policy Library）

意图策略库是 3GPP Intent 管理体系中的一个概念层，将电信意图模板映射到可治理的策略候选集。它位于 [[IntentDrivenMnS]] 和 [[PolicyMnS]] 之间，作为意图翻译链的中间桥梁——当 [[IntentIOC]] 的声明式目标需要被转化为 [[PolicyIOC]] 的条件-动作模型时，策略库提供可选的策略模板以供选择和治理。

## 与 [[RulePolicyIntentRelation]] 的关系

[[RulePolicyIntentRelation]] 定义了 Rule→Policy→Intent 的抽象层级。Intent Policy Library 位于 Policy 层级，但服务于 Intent 向 Policy 的下行翻译：它不是简单的策略集合，而是**意图感知的策略选择机制**——根据意图目标筛选合适的策略候选。

## 与 [[IntentNegotiation]] 的协同

在意图协商过程中，当 [[IntentNegotiation]] 判断某意图不可完全满足时，策略库可提供替代策略方案供协商使用，结合 [[IntentUtilityFunction]] 进行定量偏好评估。