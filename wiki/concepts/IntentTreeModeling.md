---
title: "IntentTreeModeling"
type: concept
tags: [intent-tree, dialogue-history, hierarchical, exploration-exploitation]
sources: [proutt]
last_updated: 2026-05-29
---

# IntentTreeModeling

意图树建模（Intent Tree Modeling）是将对话历史组织为层次化意图结构而非扁平序列的方法，捕捉意图的结构化演变和分支关系。

## 核心思想

传统对话历史以扁平 token 序列表示，无法捕捉意图的层次结构和分支演变。意图树将每个意图作为节点，其子分支代表意图的细分和演变，形成树状结构。

## ProUtt 双视角推理

- **Exploitation 视角** — 沿已知意图分支预测下一 utterance（沿树向下）
- **Exploration 视角** — 探索新意图分支预测下一 utterance（横向扩展）

## 偏好数据构造

通过扰动（perturbation）与修正（correction）自动构造偏好数据：
- 扰动：在推理轨迹中引入偏差
- 修正：生成正确的推理轨迹
- 两者构成偏好对（chosen vs rejected），无需人工标注

## 关联
- [[IntentRecommendation]] — 意图树建模服务于意图推荐
- [[RecursiveIntentMemory]] — 递归记忆 vs 层次化意图树的对比
- [[AgentMemory]] — 意图树作为记忆的结构化表示