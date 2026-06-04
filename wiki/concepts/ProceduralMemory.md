---
title: "程序性记忆（Procedural Memory）"
type: concept
tags: [agent-memory]
sources: [memp, peam]
last_updated: 2026-06-04
---

程序性记忆是Agent记忆的一种类型，指Agent通过经验内化获得的"如何做"的技能知识——不同于陈述性记忆的"知道什么"。Memp 将轨迹蒸馏为细粒度步骤指令+高层次脚本抽象两种形式，研究 Build/Retrieval/Update 三种策略的影响。PEAM 通过对比内化将失败-纠正轨迹对转换为参数驻留技能。程序性记忆的核心特征是可学习、可更新、终身化，且可以跨模型迁移（Memp 发现强模型记忆迁移到弱模型仍有增益）。

相关论文：[[memp]], [[peam]], [[mempi]], [[AgentKB]]