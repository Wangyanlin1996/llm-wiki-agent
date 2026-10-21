---
title: "本体约束 LLM 生成（Ontology-Constrained Generation）"
type: concept
tags: [owl2-reasoning]
sources: [structured-decomposition-swrl, cause-effect-spec-kg-llm, llm-capability-ontologies, transparent-cti-ontology-shacl, aml-shacl-validation-llm, qraken-graph-distillation]
last_updated: 2026-10-21
---

本体约束 LLM 生成指用 OWL 本体、SHACL shapes 或规则模板作为"生成契约"，把 LLM 输出限制在本体词汇与约束空间内的模式。Round 19 实证了它的四种形态：**约束生成对象是本体自身**（[[llm-capability-ontologies]] 用 CaSk TBox 作 prompt 上下文生成能力本体，few-shot 错误分低至 0.03）；**约束生成规则**（[[cause-effect-spec-kg-llm]] 禁止 LLM 发明本体外的阈值/位号，SWRL 语义接地率 100%）；**约束输出结构**（[[transparent-cti-ontology-shacl]] 用本体+SHACL 引导结构化输出，F1 最高 +0.802）；**约束查询**（[[qraken-graph-distillation]] 用经验词表防造词）。

两条互补的经验教训：其一，结构模板注入（one-shot 示例）是最大增益来源，few-shot 边际递减（[[llm-capability-ontologies]] 消融）；其二，**描述性经验内容优于规范性 schema 约束**——TTQL（数据实际长什么样）比 SHACL 形状（数据应当长什么样）F1 高 64%（[[qraken-graph-distillation]]）。

约束收益存在模型相关性反例（Mistral Large 在 [[transparent-cti-ontology-shacl]] 中退化），且结构化输出工具的表达力弱于 SHACL 约束语言，需外层校验兜底。与 [[OntologyFirstAgentDesign]] 的区别：本概念约束单次生成物，后者以本体为整个 agent 架构基础层。

Related: [[ReasonerGuidedRepair]] · [[ValidationFeedbackLoop]] · [[OntologyIntentAlignment]]
