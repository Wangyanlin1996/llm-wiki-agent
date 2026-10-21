---
title: "校验反馈闭环（Validation Feedback Loop）"
type: concept
tags: [owl2-reasoning]
sources: [qraken-graph-distillation, kg-repair-shacl-llm, xpshacl-explainable-validation, shacr-smart-home-conflict, g-spec-5g-policy, aml-shacl-validation-llm]
last_updated: 2026-10-21
---

校验反馈闭环指"LLM 生成 → 确定性校验 → 结构化诊断 → 定向修复/解释"的完整循环，是 Round 19 论文的公共骨架。校验端有三层递进：语法（可解析）→ 词法/词汇（不造词）→ 数据模型/语义（不违反本体约束），[[qraken-graph-distillation]] 的三级管线与 [[g-spec-5g-policy]] 的原子化 SHACL 预执行校验（违规整体拒绝）是两个代表；[[shacr-smart-home-conflict]] 把修复动作空间做成白名单并用 validate_repair 复检，防止 LLM 自治改图。

反馈端有三种去向：定向修复 prompt（QRAKEN 自愈循环、[[kg-repair-shacl-llm]] 的 S+F+ 上下文裁剪策略）、自然语言解释（[[xpshacl-explainable-validation]] 的论证树+RAG+LLM、[[aml-shacl-validation-llm]] 的报告人话化）、拒绝重规划（G-SPEC 的结构化 RejectionReason）。评测方法论同样成型：VIO 机制自造"已知答案"违规做回归测试（KG-Repair），四级阶梯指标（语法→语义→relaxed iso→exact iso）区分"修好"与"修对"。

设计红线：校验上下文并非越多越好——整个 manifest 会"过载并分散注意力"，精选源 shape + 依赖 + 一个正例最优（KG-Repair 消融）；修复提示词可能反噬（[[ReasonerGuidedRepair]] 的 −14.4pp 反例）。

Related: [[OntologyConstrainedGeneration]] · [[RuntimeGovernance]] · [[VerificationCoEvolution]]
