---
title: "动作本体Agent (Action Ontology Agent)"
type: concept
tags: [task-execution, action-ontology, ontology-modeling, task-completion]
sources: [husky-language-agent, ontobot-robotics-ontology, hear-hypergraph-enterprise, kml-procedural-video-qa]
last_updated: 2026-07-07
---

动作本体Agent（Action Ontology Agent）是指利用本体定义的动作/任务空间来结构化语言 agent 的行为规划和执行。本体定义了 agent 可执行的动作类型、动作间的依赖关系、动作到能力的映射，以及动作执行的环境约束。Agent 在本体动作空间上进行推理——分解任务为动作序列、选择合适的动作、委托给专家模型或执行器。关键实例包括：统一动作本体+专家模型执行（[[husky-language-agent]]）、任务/动作/环境/能力统一本体+能力推理（[[ontobot-robotics-ontology]]）、分层超图本体的程序协议编码（[[hear-hypergraph-enterprise]]）、以及程序化知识图谱的神经知识模块（[[kml-procedural-video-qa]]）。动作本体Agent 的核心价值是将 agent 的行为空间结构化——使规划可分解、执行可委托、结果可验证。

## 关联论文
- [[husky-language-agent]] — 统一动作本体+专家模型
- [[ontobot-robotics-ontology]] — 任务/动作/环境/能力本体
- [[hear-hypergraph-enterprise]] — 超图本体程序协议
- [[kml-procedural-video-qa]] — 程序化知识模块

## 关联概念
- [[NeuroSymbolicKGModule]]
- [[DialogueStateTrackingOntology]]
- [[OntologyAwareTOD]]
