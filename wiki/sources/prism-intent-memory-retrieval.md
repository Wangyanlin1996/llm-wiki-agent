---
title: 'PRISM: 意图感知记忆上的帕累托高效检索'
type: source
tags:
- context-optimization
- memory-retrieval
- long-term-memory
sources:
- prism-intent-memory-retrieval
source_file: raw/papers/prism-intent-memory-retrieval.pdf
last_updated: 2026-07-09
arxiv_id: '2605.12260'
authors:
- et al.
year: 2026
venue: arXiv preprint
citation_count: 0
---
## 概要
长时程 agent 对话历史累积速度远超固定上下文窗口。现有方法要么扩展窗口不解决检索什么，要么做重摄入时事实提取（token 成本高），要么用启发式图遍历（精度效率都不够）。PRISM 是训练免的检索侧框架，将长时程记忆视为图结构记忆上的联合检索-压缩问题。

## 关键贡献
- 训练免的检索侧框架——无需模型训练，纯推理时操作
- 四个正交推理时组件联合优化检索-压缩
- 在 LoCoMo 上以一个数量级更小的上下文预算取得更高 LLM-judge 准确率

## 方法细节
- **层次 Bundle Search**：在类型化关系路径上搜索，构建记忆的图结构表示，沿关系路径搜索候选 bundle
- **Query-Sensitive Edge Costing**：根据检测到的查询意图对齐遍历——不同查询类型（事实回忆、推理、情感）偏好不同关系路径
- **Evidence Compression**：将候选 bundle 压缩为紧凑的答案侧上下文——去除冗余，保留与查询最相关的证据
- **Adaptive Intent Routing**：将多数查询路由到零 LLM 层——简单查询直接从图结构检索答案，复杂查询才调用 LLM

## 关键引用
> "PRISM frames long-term memory as a joint retrieval-compression problem over graph-structured memory, achieving higher accuracy with an order of magnitude smaller context budget."

## 关联
- [[ContextOptimization]] — 上下文优化方向
- [[MemoryOS]] — 同为长时程记忆管理，MemoryOS 用 OS 式存储，PRISM 用图检索
- [[LightMem]] — LightMem 用 SLM 驱动压缩，PRISM 用训练免的图遍历

## 矛盾
- 与"重摄入时事实提取"的矛盾：PRISM 不预先提取事实，在检索时动态压缩
