---
title: 'CoACT: 动作保持的观测压缩'
type: source
tags:
- context-optimization
- kv-cache
- agent-compression
sources:
- coact-action-preserving-compression
source_file: raw/papers/coact-action-preserving-compression.pdf
last_updated: 2026-07-09
arxiv_id: '2607.02911'
authors:
- Zhiyao Wu
- et al.
year: 2026
venue: arXiv preprint
citation_count: 0
---
## 概要
LLM coding agent 迭代交互中，工具输出、文件内容、测试结果等 observation 不断累积进上下文，成为推理成本的主要来源。现有压缩方法只缩短文本，不显式建模压缩对 agent 后续行为的影响——压缩后 agent 可能做出不同的下一步动作。CoACT 提出 Next-Action Preservation (NAP) 原则：压缩后的 observation 必须诱导与原始 observation 相同的下一步动作。

## 关键贡献
- 提出 NAP 原则——以"下一步动作一致性"作为压缩质量的核心约束
- Teacher model 生成多个压缩候选，用 NAP 动作保持奖励过滤，再用长度缩减奖励选择紧凑候选
- 训练轻量压缩器，在 SWE-bench Verified 上三种 agentic model 验证
- Token 消耗降低 33%，任务解决效果接近未压缩

## 方法细节
- **候选生成**：teacher model 对同一 observation 生成多个不同压缩程度的候选
- **NAP 过滤**：对每个候选，执行一步推理得到预测的下一步动作，与原始 observation 的下一步动作比对，过滤掉动作不一致的候选
- **长度选择**：在通过 NAP 过滤的候选中，选择最紧凑的作为训练标签
- **压缩器训练**：轻量模型学习从原始 observation 到 NAP-compliant 压缩的映射

## 关键引用
> "Compression must preserve not just information, but the agent's next action."

## 关联
- [[ContextOptimization]] — 上下文优化方向的代表工作
- [[SmoothAgent]] — 同为上下文优化，但 SmoothAgent 关注 KV cache 复用而非压缩质量
- [[LatentContextCompilation]] — 同为上下文压缩，但用 LoRA 编译而非动作保持

## 矛盾
- 与传统摘要式压缩的假设冲突：传统方法假设信息保留即可，CoACT 认为动作保持才是正确目标
