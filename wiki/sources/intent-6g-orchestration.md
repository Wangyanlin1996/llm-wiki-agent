---
title: "Intent-Driven 6G编排: 语义服务目录+TMF意图本体+SHACL验证"
type: source
tags: [semantic-layer, ontology-reasoning]
sources: [intent-6g-orchestration]
source_file: raw/papers/intent-6g-orchestration.pdf
last_updated: 2026-07-25
arxiv_id: "2606.28348"
authors: ["Jean Martins", "Leonid Mokrushin", "Marin Orlic", "Amardeep Kumar A"]
year: 2026
venue: "AI4NextG @ ICML'26 Workshop"
citation_count: 0
---

## 概要
6G 的意图驱动自动化设想网络由高层目标而非低层配置驱动。现有 LLM 方法将自然语言翻译为看似合理的意图表示，但通常省略生产部署所需：实际服务目录接地、形式验证和跨层分解。本文提出 agentic 工作流，包含三层耦合推理：(1) 在暴露 TMF 合规服务规格的语义服务目录中接地翻译；(2) 通过 SHACL 结构检查对 TMF 意图本体验证 RDF 意图；(3) 通过 QoS 能力包络上的约束满足选择 CFSS profile，再通过加权集合覆盖覆盖基础设施需求。

## 关键贡献
- 三层耦合推理：语义服务目录接地 → SHACL 本体验证 → 约束满足分解
- TMF 意图本体 + SHACL 结构检查形式化验证
- 930 次基准运行：结构化模式 97% 成功，自然语言场景平均 90%
- 100% 正确拒绝不可行请求
- 服务目录能力元数据接地减少对抗性幻觉 26 个百分点

## 关键引用
> "Grounding LLM context in catalog capability metadata reduces adversarial hallucinations by 26 percentage points; larger gains than scaling model size alone."

## 关联
- [[OntologySemanticLayer]] — 本体语义层
- [[IntentDrivenMnS]] — 3GPP意图驱动管理服务
- [[semantic-training-gap]] — 本体嵌入工具层消除语义鸿沟
- [[security-ontology-autonomous-networks]] — TM Forum安全本体
- [[RulePolicyIntentRelation]] — 规则-策略-意图关系

## 矛盾
- 无
