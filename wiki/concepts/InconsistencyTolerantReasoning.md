---
title: "不一致容忍推理（Inconsistency-Tolerant Reasoning）"
type: concept
tags: [ontology-reasoning, robustness]
sources: [falcon-inconsistent-alc, ontology-revision-plm, embedding-inconsistency-tolerant, inconsistency-kg-reasoning-survey, abox-abduction-repair-semantics]
last_updated: 2026-10-09
---

不一致容忍推理是一族在不一致/不完整本体上恢复有意义推理的技术，组织为检测-修复-容忍三方向（[[inconsistency-kg-reasoning-survey]]）。**容忍**路线在不修复的前提下继续推理，包括基于最大一致子集（MCS）的怀疑式/Brave/AR 语义推理（[[abox-abduction-repair-semantics]] 在其上定义溯因）、嵌入语义驱动的 MCS 选择（[[embedding-inconsistency-tolerant]] 用公理语义向量排序）、模糊多模型近似蕴含（[[falcon-inconsistent-alc]] 证明模型越多蕴含越忠实）、神经链接预测近似推理（[[neural-shqoi-instance-retrieval]] 在符号推理器失效处达 F1 1.00）。**修复**路线通过删除/重排公理恢复一致，如 [[ontology-revision-plm]] 用预训练语言模型编码公理语义做修订排序（最多省 90% 时间）。核心张力：保留有价值信息 vs 恢复形式一致性——容忍路线保留信息但失去经典蕴含保证，修复路线恢复一致性但可能删除信息。选择依据：不一致范围、信息价值、下游推理预算。相关论文：[[inconsistency-kg-reasoning-survey]]、[[falcon-inconsistent-alc]]、[[embedding-inconsistency-tolerant]]、[[ontology-revision-plm]]、[[abox-abduction-repair-semantics]]、[[neural-shqoi-instance-retrieval]]
