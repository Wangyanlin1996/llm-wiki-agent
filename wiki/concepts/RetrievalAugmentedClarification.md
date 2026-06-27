---
title: "检索增强澄清（Retrieval-Augmented Clarification）"
type: concept
tags: [memory-intent-clarification, RAG]
sources: [rac, corpus-rag-clarifying, sensitivity-aware-clarification]
last_updated: 2026-06-27
---

检索增强澄清（RAC）是指用检索增强生成（RAG）技术增强对话式搜索/Agent 中的模糊意图澄清能力。核心思想是将检索语料库作为"外部记忆"，从中检索相关文档为澄清问题生成提供证据支撑，使澄清问题锚定在可用信息中而非"幻觉"。

三条互补路径：[[rac]] 追求语料锚定最大化（对比偏好优化）；[[corpus-rag-clarifying]] 联合建模 query+corpus 端到端定位不确定性；[[sensitivity-aware-clarification]] 在敏感域中限制检索范围。与 [[IntentSimUncertainty]]（意图空间判断何时澄清）和 [[StructuredUncertaintyClarification]]（参数域量化消歧价值）代表两种互补方向：前者用外部记忆增强问题质量，后者用内部不确定度判断问题时机。
