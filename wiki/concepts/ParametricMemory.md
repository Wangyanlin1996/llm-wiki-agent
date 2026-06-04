---
title: "参数化记忆（Parametric Memory）"
type: concept
tags: [agent-memory]
sources: [peam, mempi]
last_updated: 2026-06-04
---

参数化记忆是将Agent经验内化到模型参数中而非存储在外部记忆库中的记忆形式。PEAM 通过 MoE-LoRA 物理隔离适配器将技能驻留到参数，防止灾难遗忘。Mem-π 用独立参数的专用模型按需生成上下文特定指导而非检索静态条目。参数化记忆的核心优势是检索效率（无需外部存储访问）和执行速度（快模块的反射式执行），但挑战在于何时内化、如何防止遗忘、如何决定哪些经验值得参数化。

相关论文：[[peam]], [[mempi]], [[memp]]