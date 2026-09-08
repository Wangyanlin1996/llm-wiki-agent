---
title: "SkillNet: 创建、评估与连接 AI 技能（Create, Evaluate, and Connect AI Skills）"
type: source
tags: [ontology-skill-routing]
sources: [skillnet-ai-skills]
source_file: raw/papers/skillnet-ai-skills.pdf
last_updated: 2026-09-08
arxiv_id: "2603.04448"
authors: ["Yuan Liang", "Ruobin Zhong", "Haoming Xu", "Chen Jiang", "Yi Zhong"]
year: 2026
venue: "arXiv preprint"
citation_count: 0
---

## 概要
SkillNet 是一个用于大规模创建、评估与组织 AI agent skills 的开放基础设施，把 skills 建模为连接非结构化语言理解与结构化可执行逻辑的统一知识表示。它构建了三层 Skill Ontology（taxonomy 分类层 + relation graph 关系层 + package library 部署层），并提出跨 Safety/Completeness/Executability/Maintainability/Cost-awareness 五维的评估框架。在 ALFWorld/WebShop/ScienceWorld 三个文本模拟环境上，集成 SkillNet 使平均 reward 提升 40%、执行步数减少 30%。

## 解决的问题
AI agent 能灵活调用工具执行复杂任务，但长期进步受制于缺乏系统化的 skill 积累与迁移——没有统一机制时 agent 反复"reinvent the wheel"，在孤立上下文中重新发现方案。现有方法主要靠人工工程或瞬态 in-context learning，且 skill 获取是手动、片段式的而非自主累积的；同时没有原则性框架在大规模上验证和维护 skill 质量。

## 方法与技术
1. **多源自动 skill 创建管线**：从四类来源（执行轨迹/对话日志、GitHub 仓库、半结构化文档、直接 NL prompt）经 LLM 抽取可执行模式并结构化为标准化 skill（含 SKILL.md 元数据+指令+可选脚本/模板/资源）。
2. **数据驱动过滤与固化**：多阶段 curation——dedup、filtering、categorization/tagging（10 大功能类）、五维评估、选择性固化，使仓库自演化。
3. **三层 Skill Ontology**：taxonomy 层用 category/tag 做功能层级；relation graph 层用 similar_to/compose_with/belong_to/depend_on 四类关系边建模 skill 间依赖与组合；package library 层用 packaged_in 关系封装为可部署包。
4. **五维 LLM 评估 + 经验校验**：Safety（危险操作/抗 prompt injection）、Completeness（关键步骤与前置依赖）、Executability（沙箱实测）、Maintainability（模块化/可组合）、Cost-awareness（延迟/算力/成本）。
5. **SkillNet-Gym（动态基准）+ SkillNet-Fabric（路由层）**：Gym 从真实 skill 生态自动构造评测 skill 构建/检索/组合；Fabric 在全局生态与最终集合间放置任务特定 Wiki 做路由。

## 创新点
- **全生命周期基础设施 vs 单点仓库**（vs ClawHub 仅版本管理、SkillsMP 仅目录聚合、SkillHub 人工评级）——唯一支持自动创建+多维评估+关系图分析的 full-lifecycle 基础设施。
- **场景介导的有向 skill 图构建**——用 pre-scenario/post-scenario 抽象 skill 状态转换，FAISS + Louvain 社区检测 + LLM judge 验证后聚合为 compose_with 边，使组合关系可验证。
- **五维评估框架 + 人机一致性验证**——自动评估器 MAE<0.03、QWK≈1.000，证明评估可扩展且人机对齐。
- **Skills 作为可演化可组合资产的形式化**——把 skill 定义为连接声明式知识与可执行程序的中间能力单元，使 agent 能力"累积式"增长。

## 效果
- Dataset: ALFWorld Seen (Gemini 2.5 Pro) | Metric: Reward R↑ | Result: 91.43 | Baseline: 60.00 (React) | Δ: [+52.4%]
- Dataset: ALFWorld Seen (DeepSeek V3.2) | Metric: Reward | Result: 80.60 | Baseline: 66.43 | Δ: [+21.3%]; Steps↓: 19.51→14.54
- Dataset: WebShop Seen (Gemini 2.5 Pro) | Metric: Reward | Result: 53.02 | Baseline: 31.66 | Δ: [+67.5%]
- **Overall**: Avg reward +40%, execution steps −30% (vs React, across 3 backbones)
- **Evaluator reliability**: MAE < 0.03, QWK ≈ 1.000 (200 skills, 3 PhD annotators)
- **Task synthesis consistency**: Fleiss's κ = 0.834

## 关键引用
> "Without a unified mechanism for skill consolidation and sharing, agents repeatedly 'reinvent the wheel' in isolated contexts." — Section 1, p.2

> "skill acquisition remains a manual and episodic process rather than an autonomous, cumulative one." — Section 1, p.2

> "By formalizing skills as independent, systematically accumulated, knowledge-grounded capability units, agent competence can be enhanced cumulatively rather than episodically." — Section 4.2

## 关联
- [[OntologyGuidedQueryGeneration]] — 本体引导查询构造
- [[AgentMemory]] — Agent 记忆概念
- [[dynamic-ontology-llm-agents]] — Round 16 动态本体内核
- [[ontology-project-memory-coding]] — Round 16 编码 Agent 本体记忆
- [[trove-trace-route-validation]] — 本轮 TROVE 轨迹路由验证
