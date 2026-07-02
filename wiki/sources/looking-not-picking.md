---
title: "Looking Is Not Picking: An Attention-Segment Account of Tool-Selection Failures in LLM Agents（工具选择失败的注意力段解释）"
type: source
tags: [agent-explainability, tool-selection, attention-mechanism, contrastive-explanation]
sources: [looking-not-picking]
source_file: raw/papers/looking-not-picking.pdf
last_updated: 2026-07-02
arxiv_id: "2606.16364"
authors: ["Shiyang Chen"]
year: 2026
venue: "arXiv preprint"
citation_count: pending
---

## 概要

LLM agent 调错工具时，直觉猜测是模型在拥挤的工具脚手架中没"看到"正确工具。本文通过**注意力段透镜**证明相反：在真实 BFCL 失败中，按候选注意力 argmax 模型 80% 的时间注意到了正确工具（vs 21% 随机），黄金工具仅在 10% 的情况下是欠注意段——**它看对了却选错了**。这直接反驳"拥挤脚手架/中间丢失"解释：失败发生在决策读出（readout）而非脚手架。三种证据定位瓶颈：(1) 修复提示仅恢复 ≤23% 失败，而读出侧干预恢复 59-91%；(2) 注意力-logit 偏置与残差流转向向量恢复同一批失败（Jaccard 0.865）；(3) 免训练免黄金选择器在 BFCL +11.9 分、Seal-Tools +14.9 分。

## 关键贡献

- **"看 vs 选"诊断框架**：将工具选择失败定位到读出而非感知——为 AgentLoop 方向2（Skill 选择可解释性）提供精确归因
- **表示不变的干预验证**：两种不同表示（注意力偏置/残差流转向）恢复同一批失败，证明瓶颈局部化于读出
- **免训练选择器**：逐段注意力即可闭合大部分黄金无关 vs 预言机差距，可部署

## 关键引用

> "It looks at the right tool and still picks wrong. This directly refutes the intuitive 'crowded-harness / lost-in-the-middle' explanation: the failure is at the decision readout, not the harness."

## 关联

- [[AgentExplainability]] — 注意力段解释是工具选择可解释性的机制层
- [[ExplainablePlanning]] — "看 vs 选"诊断为对比解释提供注意力级证据
- [[ContrastiveSkillAssessment]] — 读出侧干预是对比解释的实现路径
- [[NeurosymbolicOrchestration]] — 工具选择的注意力诊断与神经符号编排互补

## 矛盾

与"拥挤脚手架导致工具调用失败"的直觉假设直接矛盾——本文证明失败在读出而非感知。
