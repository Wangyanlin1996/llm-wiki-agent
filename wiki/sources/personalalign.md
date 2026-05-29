---
title: "PersonalAlign"
type: source
tags: [intent-understanding, implicit-intent, GUI-agent, personalized, ACL]
date: 2026-01-09
source_file: raw/papers/personalalign.md
last_updated: 2026-05-28
---

## 概要
PersonalAlign（ACL 2026）为个性化 GUI agents 引入 Hierarchical Implicit Intent Alignment（层级式隐意图对齐），要求 agents 利用长期用户记录来解决模糊指令和预判潜在例行操作。HIM-Agent 维持持续更新的个人 memory（记忆），以层级式偏好/例行组织，实现执行 +15.7% 和主动式表现 +7.3% 的提升。

## 核心论点
- 真实 GUI 指令往往模糊（implicit intent，隐意图）
- 长期用户记录解决被省略的偏好
- Hierarchical memory（层级式记忆）组织偏好和例行操作
- HIM-Agent 实现执行 +15.7% 和主动式表现 +7.3% 提升

## 关键引述
> "Real-world GUI instructions are often vague (implicit intent)" — 动机：真实 GUI 指令往往模糊

## 关联
- [[IntentUnderstanding]] — PersonalAlign 解决隐意图理解
- [[PersonalAlign]] — 引入的框架
- [[VitaBench2]] — 相关的个性化 agent 评测基准
- [[PIRABench]] — 主动式意图推荐评测基准关联
- [[AgentMemory]] — 层级式记忆作为 agent memory 变体
- [[PIRF]] — 主动式检索与隐意图解决相关