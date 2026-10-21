---
title: "推理器引导修复（Reasoner-Guided Repair）"
type: concept
tags: [owl2-reasoning]
sources: [reasoner-guided-repair-owl2dl, structured-decomposition-swrl, entailllm-vulnerability-verification, llm-understand-dllite]
last_updated: 2026-10-21
---

推理器引导修复指用形式推理器（HermiT/Pellet/PyReason 等）对 LLM 输出做确定性裁决，并以裁决结果反馈修复 LLM 错误的模式。Round 19 的核心实证来自 [[reasoner-guided-repair-owl2dl]]：GPT-5.4 在 OWL 2 DL 蕴含查询上直答仅 43.9%，verdict-only 修复（仅注入推理器裁决、不加提示词）达 97.8%，而裁决+OWA 提示反而降到 67.2%——**提示框架比纠正内容更重要**。其成立前提是 [[llm-understand-dllite]] 测绘的 LLM 系统性失败面：TBox NI 传递规则与大规模 ABox 上 LLM 不可靠。

三种形态构成光谱：事前分工（[[structured-decomposition-swrl]] 让 LLM 只填 ABox、推理器判类）、事中校验（[[entailllm-vulnerability-verification]] 用时序标注逻辑蕴含过滤 LLM 路径，非蕴含可定位首个错误步）、事后修复（verdict-only 循环）。与 [[LLMReasonerHybrid]] 的区别在于本概念聚焦"校验→反馈→修复"闭环，而非推理分工本身。

关键警示：修复提示词设计可能反噬（Corrective Hints Hurt 的 −14.4pp 反例）；修复目标应区分"修好"（语义有效 86.17%）与"还原最优"（isomorphism 49.94%，[[kg-repair-shacl-llm]]）。

Related: [[OntologyReasoning]] · [[VerificationCoEvolution]] · [[NeurosymbolicOrchestration]]
