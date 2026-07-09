---
title: 'KV Policy: 学习淘汰的 RL 框架'
type: source
tags:
- cache-reuse
- kv-cache
- eviction-policy
- reinforcement-learning
sources:
- kv-policy-learning-evict
source_file: raw/papers/kv-policy-learning-evict.pdf
last_updated: 2026-07-09
arxiv_id: '2602.10238'
authors:
- et al.
year: 2026
venue: ICML 2026
citation_count: 0
---
## 概要
KV cache 的增长使推理挑战化。现有淘汰/压缩方法依赖启发式（recency 或过去注意力分数）——只是 token 未来效用的间接代理，且引入计算开销。KV Policy (KVP) 将 KV cache 淘汰重新表述为 RL 问题——学习按预测的未来解码效用来排序 token。

## 关键贡献
- 将 KV cache 淘汰重新表述为 RL 问题
- 轻量 per-head RL agent，仅用 key/value 向量训练
- 每个头学习专门化淘汰策略
- 奖励来自评估排序在所有缓存预算上质量的整体未来效用
- 无需修改底层 LLM 或额外推理
- RULER（128K token）和 OASST2-4k 上显著超越基线，在 BoolQ/LongBench/GovReport 上零样本泛化

## 方法细节
- **RL 问题表述**：状态 = 当前 KV cache 内容（key/value 向量）；动作 = 选择淘汰哪些 token；奖励 = 淘汰后生成质量的整体未来效用
- **Per-head Agent**：每个注意力头有独立的 RL agent——因为不同头关注不同信息（有的关注局部语法，有的关注全局语义），需要不同的淘汰策略
- **训练数据**：在预计算的生成轨迹上训练——不需要在线推理，训练时不影响服务
- **输入特征**：仅用 key/value 向量作为输入——不需要 token 文本或位置信息
- **奖励设计**：评估一个排序在所有缓存预算上的质量——即不论保留 10%、30%、50% 的 token，这个排序都能产生好的生成结果
- **零推理开销**：训练完成后，RL agent 的推理成本极低（轻量网络），不增加推理延迟

## 关键引用
> "KVP learns to rank tokens by predicted future decoding utility — per-head RL agents specialize eviction strategies without modifying the underlying LLM."

## 关联
- [[CacheReuse]] — 缓存复用方向
- [[SAECache]] — SAECache 用在线学习淘汰，KVP 用 RL 学习淘汰
- [[VeriCache]] — VeriCache 做无损压缩，KVP 做有损淘汰但学习最优策略

## 矛盾
- 与"启发式淘汰"的矛盾：KVP 表明 RL 学习的淘汰策略显著优于 recency/注意力启发式
