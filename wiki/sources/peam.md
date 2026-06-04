---
title: "PEAM: 参数化具身Agent记忆——Minecraft中的对比经验内化"
type: source
tags: [agent-memory]
sources: [peam]
source_file: raw/papers/2605.27762.pdf
last_updated: 2026-06-04
---

## 概要
PEAM 在Minecraft中将Agent记忆从推理时检索转变为参数驻留技能。双系统设计：慢推理LLM+快参数化MoE-LoRA模块；per-category物理隔离适配器防止灾难遗忘；失败作为一等训练信号，联合行为克隆+对比目标内化失败-纠正轨迹对；parameterization-worthiness score决定哪些经验内化；scale-free自触发整合机制无需手工阈值。

## 关键贡献
- 参数驻留技能 vs 推理时检索——记忆内化到模型参数
- 双系统：慢推理LLM + 快参数化MoE-LoRA执行模块
- per-category物理隔离适配器防止灾难遗忘
- 失败-纠正轨迹对的对比学习——学习什么成功+如何纠正
- parameterization-worthiness score + scale-free自触发整合

## 关键引用
> "transforms agent memory from inference-time retrieval into parameter-resident skills internalized through experience" — 核心转换

## 关联
- [[AgentMemory]] — 参数化记忆作为新的记忆形式
- [[MemCog]] — 记忆即认知——参数化记忆是最彻底的认知内化
- [[Memp]] — 同为经验内化到参数，但PEAM用MoE-LoRA而Memp用脚本蒸馏
- [[Mem-π]] — 同为生成式而非检索式，但PEAM内化到参数而Mem-π用独立模型生成

## 矛盾
- 与所有外部记忆库方法的根本矛盾——记忆应内化到参数而非外部存储