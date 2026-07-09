---
title: 'SAECache: 语义感知 KV 缓存淘汰'
type: source
tags:
- cache-reuse
- kv-cache
- eviction-policy
- prefix-caching
sources:
- saecache-semantic-eviction
source_file: raw/papers/saecache-semantic-eviction.pdf
last_updated: 2026-07-09
arxiv_id: '2605.18825'
authors:
- et al.
year: 2026
venue: arXiv preprint
citation_count: 0
---
## 概要
Prefix caching 是 LLM 服务的关键优化，但 GPU 内存稀缺，淘汰策略决定收益。现有策略（如 LRU）大致均匀对待缓存块——忽略了 LLM prompt 的基本属性：不同 token 类型（系统 prompt、用户查询、工具输出、模型响应、CoT 推理）的复用率差异达 756x。

## 关键贡献
- 多队列架构将 KV block 路由到任务特定队列
- 语义感知 token 权重机制，通过淘汰反馈在线学习不同 token 类型的复用价值
- 全自适应在线学习 schema，所有参数自动更新
- 1.4x-2.7x TTFT 提升，固定参数替代方案在负载不匹配时退化 2.7x

## 方法细节
- **多队列架构**：将 KV block 按 token 类型路由到不同队列（如 system-prompt 队列、user-query 队列、tool-output 队列、CoT 队列），每个队列有独立的优先级指标
- **语义感知 token 权重**：为每种 token 类型分配权重，反映其复用价值——通过淘汰反馈在线学习：
  - 被淘汰后很快被重新请求的 token 类型→提高权重
  - 被淘汰后很少再被请求的 token 类型→降低权重
- **全自适应在线学习**：
  - 对数正态时序参数——建模 token 复用的时间衰减
  - 位置衰减——越靠后的 token 在 prefix 中越容易被复用
  - 队列权重——各队列的相对重要性
  - 元参数——控制学习率等
  - 全部自动更新，消除手动调参

## 关键引用
> "Different token types exhibit up to 756x difference in reuse rates — LRU treats them uniformly."

## 关联
- [[CacheReuse]] — 缓存复用方向
- [[Leyline]] — Leyline 做缓存编辑指令，SAECache 做缓存淘汰策略
- [[KVPolicy]] — KVPolicy 用 RL 学习淘汰策略，SAECache 用在线学习
- [[SmoothAgent]] — SmoothAgent 优化变换导致的缓存失效，SAECache 优化缓存淘汰

## 矛盾
- 与"LRU 均匀淘汰"的矛盾：SAECache 表明语义感知淘汰能 2.7x 提升
