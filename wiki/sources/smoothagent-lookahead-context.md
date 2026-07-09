---
title: 'SmoothAgent: 前瞻上下文工程'
type: source
tags:
- context-optimization
- kv-cache
- ttft-optimization
sources:
- smoothagent-lookahead-context
source_file: raw/papers/smoothagent-lookahead-context.pdf
last_updated: 2026-07-09
arxiv_id: '2607.00151'
authors:
- et al.
year: 2026
venue: arXiv preprint
citation_count: 0
---
## 概要
Agent 框架用 context engineering 策略（offloading、reduction、isolation）控制上下文长度，但这些变换会使已有 KV cache 失效，触发重新 prefill，导致 TTFT 暴涨。SmoothAgent 发现 context 变换是"段可分解的"（segment-decomposable）——前缀的变换独立于未来 token，可提前执行。

## 关键贡献
- 发现 context 变换的段可分解性——前缀变换独立于未来 token
- 提出 lookahead 编程模型：agent 框架将 context 变换表达为异步操作
- Runtime 提前执行变换并准备好变换后的 KV cache，实现直接上下文替换无需阻塞
- Lookahead-aware 调度器支持异步请求与延迟敏感工作负载共存
- TTFT 降低 11.9x

## 方法细节
- **段可分解性**：context 变换（如删除旧轮次、合并摘要）作用于前缀 token，与未来生成 token 无依赖
- **lookahead 编程模型**：agent 框架在当前轮次执行时，异步提交下一轮的 context 变换请求
- **Runtime 预计算**：推理引擎提前执行变换并生成变换后 KV cache，存入备用
- **直接替换**：下一轮请求到达时，直接使用预计算的 KV cache，跳过 prefill

## 关键引用
> "Context transforms are segment-decomposable — prefix transforms are independent of future tokens, enabling precomputation."

## 关联
- [[ContextOptimization]] — 上下文优化方向
- [[CoACT]] — CoACT 压缩 observation 内容，SmoothAgent 优化变换时机的 KV 复用
- [[SAECache]] — SAECache 优化缓存淘汰策略，SmoothAgent 优化变换导致的缓存失效

## 矛盾
- 隐含与"压缩即优化"的矛盾：SmoothAgent 表明变换时机比压缩内容更重要
