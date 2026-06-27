---
title: STALE：记忆过期检测与隐式冲突
type: source
tags:
- agent-memory
sources:
- stale
source_file: raw/papers/stale.pdf
last_updated: 2026-06-08
arxiv_id: '2605.06527'
authors:
- Hanxiang Chao
- Yihan Bai
- Rui Sheng
- Tianle Li
- Yushi Sun
year: 2026
---
## 概要
STALE 首次系统研究 LLM Agent 记忆过期问题。提出隐式冲突（Implicit Conflict）概念：后续观察使早期记忆失效但无显式否定，需上下文推理和常识判断来检测。400 专家验证冲突场景（1200 评测查询），3 维探测框架：状态解析、前提抵抗、隐式策略适应。最佳模型仅 55.2% 整体准确率。提出 CUPMem 原型：结构化状态裁决+传播感知搜索。

## 关键贡献
- 隐式冲突概念：区分显式否定 vs 上下文隐式失效
- 3 维探测框架：State Resolution + Premise Resistance + Implicit Policy Adaptation
- CUPMem 原型：write-time 修订 + 传播感知搜索，显式状态裁决方向

## 关键引用
> "Models often accept outdated assumptions embedded in a user's query, and struggle to recognize when a change in one aspect should invalidate related memories" — 核心发现

## 关联
- [[AgentMemory]] — STALE 补充了 Storage→Reflection→Experience 的"过期"维度：经验不仅需要抽象，还需要检测何时失效
- [[MemCog]] — MemCog 强调主动认知，STALE 强调主动检测过期——都是"主动性"但面向不同问题
- [[H-Mem]] — H-Mem 的 facts+summaries+profiles 混合表示面临过期问题：何时更新 profile？

## 矛盾
- STALE 发现"检索到更新信息 ≠ 基于更新信息行动"——模型能检索但不能自动应用更新，这与 [[Mem-π]] 的"按需生成而非检索"范式呼应