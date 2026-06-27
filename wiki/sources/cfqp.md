---
title: CFQP：协同过滤下一问题预测
type: source
tags:
- intent-recommendation
sources:
- cfqp
source_file: raw/papers/cfqp.pdf
last_updated: 2026-06-08
arxiv_id: '2511.12949'
authors:
- Bokang Fu
- Jiahao Wang
- Xiaojing Liu
- Yuli Liu
year: 2025
---
## 概要
CFQP（Collaborative Filtering-enhanced Question Prediction）提出个性化记忆模块+图偏好传播的双机制框架，动态建模演化中的用户-问题交互。记忆模块自适应学习用户特定历史，图偏好传播通过相似用户的协同信号精化预测。实验证明该方法有效生成模拟真实用户提问模式的 Agent。

## 关键贡献
- 个性化记忆模块：用户特定历史自适应学习
- 图偏好传播：相似用户协同信号精化预测
- 序列意图建模：用户历史问题序列揭示演化兴趣模式

## 关键引用
> "The sequence of a user's historical questions provides a rich, implicit signal of evolving interests and cognitive patterns" — 序列即意图

## 关联
- [[IntentRecommendation]] — CFQP 的下一问题预测是 IR 在搜索场景的体现
- [[OnePred]] — OnePred 的递归意图记忆预测下一查询，CFQP 用协同过滤——不同方法同一目标
- [[AgentMemory]] — CFQP 的个性化记忆模块与 [[LightMem]] 的 SLM 记忆机制概念相似

## 矛盾
- CFQP 依赖相似用户协同信号，但 [[KnowU-Bench]] 发现用户偏好高度个体化——协同过滤可能在长尾用户上效果有限