---
title: "Prompt 优化（Prompt Optimization）"
type: concept
tags: ['prompt-engineering', 'automatic-optimization', 'multi-objective', 'reliability']
sources: ["apex-dynamic-data-selection", "prompt-codebooks-pco", "spear-code-augmented-prompt", "mo-capo-multi-objective", "maspo-joint-mas-prompt", "prism-prompt-reliability"]
last_updated: 2026-07-09
---

Prompt 优化自动化搜索最优自然语言指令，从手动试错转向系统化搜索。核心挑战：搜索空间巨大、评估成本高、泛化性差。

**六大方向**：
1. **动态数据选择** — [[APEX]] 根据优化历史将数据分层为 Easy/Hard/Mixed，优先使用 Mixed 层的 addressable frontier 和 rank-sensitive frontier，5000 次评估预算下 +11.2%。
2. **离散 codebook 学习** — [[PromptCodebooks]] 将 prompt 优化重表述为有限"本能"词汇表上的离散学习，per-instance 路由使不同输入获得不同本能组合，比零样本 +30.36pp。
3. **Agent 式优化器** — [[SPEAR]] 将 CodeAct 范式引入 APE，优化器自主编写 Python 做结构化错误分析（混淆矩阵、错误聚类），13 个任务全胜。
4. **多目标成本感知** — [[MO-CAPO]] 联合优化性能和推理成本，提出部署导向成本目标捕捉完整计算特征，发现单目标优化器遗漏的 trade-off 解集。
5. **多 Agent 联合优化** — [[MASPO]] 联合评估机制不只看 prompt 局部有效性，而看其促进下游 agent 成功的能力，无需 ground-truth 标签，平均 +2.9。
6. **持续可靠性工程** — [[PRISM-PromptReliability]] 将 prompt 工程从一次性问题转为持续可靠性问题，自动生成测试用例+模拟多轮对话+诊断根因+外科手术式修复，99% 生产可靠性。

**演进趋势**：从"优化一个全局 prompt 字符串"→"per-instance 路由+多目标+持续监控"。优化器本身从固定管线→agent 式自主决策。
