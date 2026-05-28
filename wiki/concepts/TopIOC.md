---
title: "Top IOC"
type: concept
tags: [information-model, nrm, foundation, 5g]
sources: [28622-k20]
last_updated: 2026-05-22
---

## 概要

Top IOC 是 3GPP 联合网络信息模型（FNIM）中 IOC 继承层次的根节点。所有符合 TS 32.102 规范的信息对象类都必须继承自 Top。它继承自 Top_（来自 TS 28.620 UIM）和 TopX（后者提供必需的 objectClass 和 objectInstance 属性）。

## 继承链

```
Top_ (TS 28.620 UIM) → Top (TS 28.622) → all domain-specific IOCs
                       ↑
                   TopX (objectClass, objectInstance)
```

## 作用

- 提供每个被管对象实例必须拥有的最小必需属性（objectClass, objectInstance）
- 名称包含关系：VsDataContainer 可以被 Top 名称包含（意味着任何 IOC 都可选地携带厂商特定数据）
- 所有符合规范的 IOC（包括 [[PolicyIOC]], [[IntentIOC]], [[IntentReport]]）均继承自 Top

## TopX 与 Top 的区别

- **TopX**：仅包含必需属性（objectClass, objectInstance）——所有符合规范的 IOC 继承自 TopX
- **Top**：继承自 Top_（UIM）和 TopX —— 增加通用通知支持和 VsDataContainer 包含关系

## 关联

- [[TS28622]] — 定义 Top IOC 的规范
- [[PolicyIOC]] — 继承自 Top
- [[IntentIOC]] — 继承自 Top
- [[NRM]] — Top 所锚定的模型框架