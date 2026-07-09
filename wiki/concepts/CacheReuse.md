---
title: "缓存复用（Cache Reuse）"
type: concept
tags: ['kv-cache', 'prefix-caching', 'eviction-policy', 'compression', 'multi-agent']
sources: ["saecache-semantic-eviction", "leyline-kv-directives", "tokendance-collective-sharing", "prism-scheduling-memory", "stateful-inference-multi-agent", "kv-policy-learning-evict", "vericache-lossless-compression"]
last_updated: 2026-07-09
---

缓存复用解决 KV cache 的内存稀缺与重复计算问题。核心洞察：agent 工作负载中 85-95% 的 prompt 与上一轮相同，但现有框架从头重新处理。

**七大方向**：
1. **语义感知淘汰** — [[SAECache]] 发现不同 token 类型复用率差异达 756x，多队列架构+在线学习 token 权重，TTFT 提升 1.4-2.7x。
2. **缓存编辑指令** — [[Leyline]] 用声明式 4-tuple 分离"编辑什么"与"如何保持位置正确"，闭式 RoPE 旋转校正恢复注意力数学，solve rate +14.3pp。
3. **集体 KV 共享** — [[TokenDance]] KV Collector 集体复用共享块（成本只付一次），Diff-Aware Storage 将兄弟缓存编码为块稀疏 diff，17.5x 压缩。
4. **调度-内存协同** — [[PRISM-SchedulingMemory]] 联合设计查询感知调度器 (QAS) 和需求感知 radix tree (DART)，对齐请求接入与 KV 保留，P99 TTFT 降 37.1%。
5. **有状态推理** — [[StatefulInference]] 从 O(n_t) per-turn 转为 O(Δ_t) delta-only，持久 KV cache 跨轮存活，35 轮中位数 4.2x 加速。
6. **RL 淘汰策略** — [[KVPolicy]] 将淘汰重表述为 RL 问题，per-head agent 学习专门化策略，仅用 key/value 向量训练，零推理开销。
7. **无损压缩** — [[VeriCache]] 用压缩 KV 草拟+全 KV 验证，并行执行+长草拟范围摊销换入成本，4x 吞吐提升，输出完全相同。

**关键趋势**：从"LRU 均匀淘汰"→"语义感知+学习驱动淘汰"；从"缓存仅追加"→"主动编辑+集体共享"；从"有损压缩"→"无损草拟-验证"。
