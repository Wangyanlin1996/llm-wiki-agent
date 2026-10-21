---
title: "本体优先Agent设计（Ontology-First Agent Design）"
type: concept
tags: [llm-agent-ontology]
sources: [agentic-redux, deontic-policies-agenticrei, semantic-training-gap, auto-ontology-construction-llm, virf-verifiable-embodied, cybercane-neuro-symbolic-rag, neuron-clinical-explainability, bdi-ontology, daoql-explicit-world-model]
last_updated: 2026-07-25
---

本体优先Agent设计是一种方法论：在构建 LLM agent 系统时，首先由人类专家用形式本体（如 BFO）对问题域进行本体化，然后以本体为基础设施定义 agent 角色、工具接口、治理规则和验证约束。其核心理念是将本体从"事后附加的知识源"提升为"agent 架构的基础层"——本体不仅提供知识，更提供类型约束、语义验证、审计凭证和治理边界。Agentic Redux 用类型 lambda 演算证明本体优先设计的语义正确性；Deontic Policies 用 OWL 道义策略语言在 LLM 外部实现义务/豁免/冲突解决治理；Semantic Training Gap 将本体嵌入工具层实现 0% 幻觉率；VIRF 用形式安全本体驱动 tutor-apprentice 计划修复。该方法论与 [[RuntimeGovernance]] 的"从信任到验证"转变直接呼应——本体提供机器可验证的治理基础。相关论文：[[agentic-redux]]、[[deontic-policies-agenticrei]]、[[semantic-training-gap]]、[[auto-ontology-construction-llm]]、[[virf-verifiable-embodied]]、[[cybercane-neuro-symbolic-rag]]、[[neuron-clinical-explainability]]、[[bdi-ontology]]、[[daoql-explicit-world-model]]
