---
title: 'TokenDance: 集体 KV 缓存共享'
type: source
tags:
- cache-reuse
- kv-cache
- multi-agent
- collective-sharing
- diff-compression
sources:
- tokendance-collective-sharing
source_file: raw/papers/tokendance-collective-sharing.pdf
last_updated: 2026-07-09
arxiv_id: '2604.03143'
authors:
- et al.
year: 2026
venue: arXiv preprint
citation_count: 0
---
## 概要
多 agent LLM 应用以同步轮组织执行——中央调度器收集所有 agent 输出再重新分发合并上下文。这种 All-Gather 模式产生大量 KV cache 冗余：每个 agent 的 prompt 包含相同共享输出块。TokenDance 提出 KV Collector 集体复用和 Diff-Aware Storage。

## 关键贡献
- KV Collector 在整轮上一步集体复用 KV cache，共享块复用成本只付一次
- Diff-Aware Storage 将兄弟缓存编码为对单一主副本的块稀疏 diff
- 11-17x 压缩
- 支持 2.7x 更多并发 agent，per-agent KV 存储 17.5x 压缩，1.9x prefill 加速

## 方法细节
- **All-Gather 模式分析**：多 agent 同步轮中，调度器收集所有 agent 输出→合并→重新分发给所有 agent——每个 agent 的新 prompt 包含所有其他 agent 的输出，产生大量共享 KV block
- **KV Collector**：在整轮上一步集体复用 KV cache——共享块（如所有 agent 的输出）的 KV 计算只执行一次，然后复制到所有 agent 的缓存中
- **Diff-Aware Storage**：
  - 选择一个 agent 的完整缓存作为"主副本"
  - 其他 agent 的缓存编码为对主副本的块稀疏 diff——只存储与主副本不同的 KV block
  - 11-17x 压缩比——因为大部分 KV block 是共享的
- **集体复用**：共享块的复用成本与 agent 数量无关——不论 2 个还是 20 个 agent，共享块只计算一次

## 关键引用
> "KV Collector collectively reuses KV cache across the entire round — shared blocks cost only once regardless of agent count."

## 关联
- [[CacheReuse]] — 缓存复用方向
- [[SAECache]] — SAECache 做缓存淘汰，TokenDance 做多 agent 间共享
- [[StatefulInference]] — StatefulInference 做跨轮 KV 复用，TokenDance 做跨 agent KV 共享
- [[SAGA]] — SAGA 做工作流内 KV 复用，TokenDance 做多 agent 间 KV 共享

## 矛盾
- 与"每个 agent 独立 prefill"的矛盾：TokenDance 表明集体复用能 17.5x 压缩存储
