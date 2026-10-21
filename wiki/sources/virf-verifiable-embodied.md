---
title: "VIRF: 安全本体驱动的可验证具身AI神经符号架构"
type: source
tags: [llm-agent-ontology, neuro-symbolic]
sources: [virf-verifiable-embodied]
source_file: raw/papers/virf-verifiable-embodied.pdf
last_updated: 2026-07-25
arxiv_id: "2602.08373"
authors: ["Feiyu Wu", "Xu Zheng", "Yue Qu", "Zhuocheng Wang", "Zicheng Feng", "Hui Li"]
year: 2026
venue: "ICLR 2026"
citation_count: 0
---

## 概要
LLM 作为具身 AI 规划器有潜力，但其随机性缺乏形式推理，无法为物理部署提供严格安全保证。VIRF（Verifiable Iterative Refinement Framework）是神经符号架构，从被动安全门控转向主动协作。核心贡献是 tutor-apprentice 对话：确定性 Logic Tutor 基于形式安全本体提供因果和教学反馈给 LLM 规划器，实现智能计划修复而非仅避免。还引入从真实文档合成安全知识库的可扩展管线，修正现有基准的盲点。

## 关键贡献
- 神经符号架构：确定性 Logic Tutor + LLM 规划器 tutor-apprentice 对话
- 基于形式安全本体的因果和教学反馈驱动计划修复
- 家庭安全任务：HAR=0%，GCR=77.3%，平均仅需 1.1 次修正迭代
- 从真实文档合成安全知识库的可扩展管线
- ICLR 2026 发表

## 关键引用
> "Our core contribution is a tutor-apprentice dialogue where a deterministic Logic Tutor, grounded in a formal safety ontology, provides causal and pedagogical feedback to an LLM planner. This enables intelligent plan repairs rather than mere avoidance."

## 关联
- [[OntologyFirstAgentDesign]] — 本体优先Agent设计方法论
- [[NeuroSymbolicOntology]] — 神符号本体注入框架
- [[RuntimeGovernance]] — 运行时治理
- [[NeurosymbolicOrchestration]] — 神经符号编排
- [[ontobot-robotics-ontology]] — 服务机器人统一本体

## 矛盾
- 无
