---
title: "Workflow-to-Skill: 通过路由-工作流-语义-附件分解创建技能（Skill Creation via WSA Decomposition）"
type: source
tags: [ontology-skill-routing]
sources: [workflow-to-skill]
source_file: raw/papers/workflow-to-skill.pdf
last_updated: 2026-09-08
arxiv_id: "2606.06893"
authors: ["Yuyang Zhang", "Xinyuan Han", "Xudong Jiang", "Run Wang"]
year: 2026
venue: "arXiv preprint"
citation_count: 0
---

## 概要
本文将 LLM agent 的自动化 Skill 生成重新定义为结构化归纳任务而非轨迹摘要问题，提出中间表示 Skill-IR，将 Skill 分解为路由头（Routing Header）和三部分运行时规范：Workflow Backbone (W)、Operational Semantics (S)、Runtime Attachments (A)。基于 Skill-IR，提出 W2S 框架，从异构交互证据中重建可执行 Skill：分段轨迹→诱导路径级草稿→对齐合并共享结构→协调条件分支→压缩冗余同时保留验证/审批/回滚行为。在 70 个 Skill 的 WSASkill 数据集上，W2S 在 replay-based behavioral fidelity 上较 Anthropic Skill Creator 平均提升 10.5%。

## 解决的问题
Skill 主要靠手工编写，无法跨域/跨工具/跨环境扩展。现有 trace-grounded skill induction 方法（Agent Workflow Memory、AutoSkill、Trace2Skill）将轨迹压缩为自由文本摘要或松散组织的 lessons，丢失了运行时结构——激活条件、工作流阶段、分支 criteria、retry/fallback 规则、工具绑定、验证检查、终止条件。摘要方法失败的根本原因：summarization 按 semantic salience 压缩，而 skill creation 需要重建可支持未来执行的过程知识。

## 方法与技术
1. **Skill-IR 的 WSA 分解**：Skill = (R, W+S+A)。R（路由头）= front matter + description，决定 Skill 何时被选择；W（工作流骨架）= (N, E)，节点集+有向边集；S（操作语义）= 节点索引的解释函数；A（运行时附件）= 工具、脚本、资源、配置约束、输出 schema。分解出 8 种 Skill 类型（T0-T7）。
2. **证据驱动的 WSA 重建**：将轨迹视为多信号对象——用户请求揭示激活条件、agent 动作揭示工作流顺序、justification 揭示决策 criteria、失败路径揭示节点约束、最终响应揭示输出契约。证据分为 E={E_W, E_S, E_A} 并记录 provenance。
3. **WSA 约束的 Skill 生成**：三条规则——(1) 每条主要指令必须可追溯到 W/S/A 证据；(2) 分支替代和稀有路径保持显式；(3) 不确定性必须表示为不确定性。
4. **类型化反馈精修循环**：三个检查——coverage check、consistency check、executability check。失败时返回 WSA-localized 反馈：W 级修复、S 级修复、A 级修复。
5. **W-path 枚举与场景对齐**：对工作流型 Skill，解析骨架图并枚举所有 W-path，每条 path 收集 10 条轨迹作为重建输入证据。

## 创新点
- **Skill = Runtime Specification（而非文本摘要）**（vs Agent Workflow Memory 自由文本 lessons、Agent Skill Induction 可执行程序但不分离运行时组件）——首次将 Skill 明确定义为结构化运行时规范并分离 W/S/A 三个正交维度。
- **WSA 三部分分解**——将"何时应用"(R)、"如何执行"(W)、"如何决策"(S)、"运行时约束"(A) 显式分离，使重建错误可归因。
- **Evidence Provenance 纪律**——区分"直接观测"、"推断"、"未观测"三种证据来源，低频但安全关键的操作被显式保留。
- **直接对标 Anthropic Skill Creator (ASC)**——在 WSASkill 数据集上以相同输入证据对比 ASC。

## 效果
- Dataset: WSASkill (70 skills) | Metric: Replay Fidelity (avg) | W2S: 0.503 | ASC: 0.455 | Δ: [+10.5%]
- Dataset: WSASkill T2 (Semantic Guideline) | Metric: Fidelity | W2S: 0.760 | ASC: 0.638 | Δ: +0.122
- Dataset: WSASkill T7 (Full Runtime) | Metric: Fidelity | W2S: 0.652 | ASC: 0.613 | Δ: +0.039
- **Ablation**: T5 (W+A, no semantics) is the only type where ASC wins: 0.550 vs 0.480 (−0.070) — attachment-heavy workflow 是当前最具挑战性的类别

## 关键引用
> "A skill is not merely a prompt fragment; it is a runtime specification intended to guide agent behavior across future tasks." — Section 1, p.1

> "Skill creation differs from ordinary summarization in its objective. Summarization typically compresses historical content according to semantic salience, whereas skill creation aims to reconstruct procedural knowledge that can support future execution." — Section 1, p.2

> "The proper unit of skill induction should not be a textual instruction, but a structured runtime specification, especially for automated skill generation." — Section 1, p.2

## 关联
- [[OntologyGuidedQueryGeneration]] — 本体引导查询构造
- [[AgentMemory]] — Agent 记忆概念
- [[skillnet-ai-skills]] — 本轮技能网络
- [[trove-trace-route-validation]] — 本轮 TROVE 轨迹路由验证
- [[ProceduralMemory]] — 程序性记忆概念
