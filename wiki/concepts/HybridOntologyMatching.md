---
title: "混合本体匹配 (Hybrid Ontology Matching)"
type: concept
tags: [ontology-graph-retrieval]
sources: [agentmap-ontology-matching, ontoextend-ontology-extension]
last_updated: 2026-08-31
---

混合本体匹配（HOM）是统一 equivalence 和 subsumption 发现为单一任务的本体匹配新范式。传统 OM 系统仅能发现单一类型的语义对应关系（LogMap/AML/BERTMap/GenOM 仅 equivalence；BERTSub 仅 subsumption 候选排序），而实际知识集成场景中源概念是否在目标本体中有精确匹配或仅有更宽泛的匹配事先未知。HOM 的核心方法是分阶段多智能体推理：AgentES（初始等价筛选）→ AgentEV（等价验证，利用本体层次结构）→ AgentSD（迭代 subsumption 发现，逐层向上遍历本体层次），采用等价优先策略。关键发现：移除层次搜索使 subsumption 准确率下降 58.2%，而移除词法匹配冲突解决仅使 equivalence 准确率下降 1.7%——表明"分阶段语义决策+迭代结构感知推理"是 LLM agent 处理层次结构的一般原则。相关论文：[[agentmap-ontology-matching]]、[[ontoextend-ontology-extension]]。与 [[OntologyMatching]]（Round 14）的稳定匹配对齐概念互补——后者关注 1:1 匹配的对齐质量，HOM 关注同时发现多类型映射。
