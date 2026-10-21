---
title: "Real-Time Health Analytics（BFO+SWRL+CEP+LLM 实时结核病检测）"
type: source
tags: [owl2-reasoning]
sources: [ontology-cep-health-analytics]
source_file: raw/papers/ontology-cep-health-analytics.pdf
last_updated: 2026-10-21
arxiv_id: "2510.09646"
authors: ["Ritesh Chandra", "Sonali Agarwal", "Navjot Singh"]
year: 2025
venue: "arXiv preprint"
citation_count: 0
doi: ""
---

## 概要
该论文构建了"本体 + 复杂事件处理（CEP）+ LLM"三合一的实时疾病检测平台，以印度 RNTCP 结核病防控协议为案例：Kafka/Spark 流式摄入患者数据，Siddhi CEP 引擎按 SWRL 诊断规则检测临床事件模式，LLM 负责事件解释、风险评估与**本体半自动演化**。核心架构特征是分工明确——实时路径走轻量 SWRL 规则，高复杂度任务卸载给 LLM，且 LLM 输出被本体系统"双重校验"（double check）后才被采纳。

## 解决的问题
公共卫生大数据场景中，本体建模、CEP、AI 诊断长期是三条平行线：同组前作 OCEP 框架做本体+CEP（85% 事件检测准确率）但无 LLM 推理；模糊规则 CEP 只做心血管预测、无语义层；OntoTB/O4TBSS 等静态 TB 本体无实时处理能力。缺口是缺乏统一平台，且静态本体无法随医学知识演化——本文补上 LLM 驱动的半自动本体演化回路。

## 方法与技术
1. **五组件大数据管线**：Kafka pub-sub（3 broker 副本容错）→ Spark Streaming 微批（5 秒窗口）→ Siddhi CEP 引擎按 RNTCP 临床协议做规则式事件检测（漏服药、异常化验、症状恶化）→ 告警分流给 LLM 与医务人员。
2. **BFO 顶层本体的 TB 本体**：Protégé 5.5 构建，continuant/occurrent 二分；RNTCP 行政体系（STC/STDC/DMC/PHI/DOTS）建模为 site/role/object-aggregate/process；对象属性（treats, appoints）+ 数据属性（hasCoughDuration, hasWeightLoss）。
3. **SWRL 规则库**：疾病分期 5 条（咳嗽≥14天+发热→Suspected_TB 等）+ 疑似筛查 13 条 + 确诊管理 13 条 + 重症 TB 10 条，编码 RNTCP 决策流程图；RDFLib 转 RDF 存入 GraphDB。
4. **选择性触发策略**：只在 SWRL 事件模式命中时才跑 SPARQL 查询，降低推理开销——实时性由规则层保证，语义深度由本体层提供。
5. **LLM 三重角色**：(a) all-MiniLM-L6-v2 嵌入临床指南 + FAISS 索引 + dynamic_tinybert QA 生成临床解释；(b) 对 CEP 告警做语义解释与风险评估；(c) LLM 辅助本体演化（Algorithm 1：抽取新概念/属性/规则 → 与现有本体比对找 gap → 专家审核 → Pellet 一致性校验 → 部署）。

## 创新点
- **vs OCEP（同组前作，85% 准确率）**：新增 LLM 推理层做事件解释、风险评估和本体半自动演化，而非只做规则检测。
- **vs 模糊规则 CEP（Kafka+Spark+Siddhi+fuzzy）**：用本体对齐的 SWRL 语义规则替代纯模糊逻辑规则，获得语义可解释性。
- **vs 静态 TB 本体（OntoTB/O4TBSS/OntoTBC）**：接入实时流处理，首次给 TB 本体加了"LLM 建议 + 专家在环 + 推理器校验"的半自动演化回路。
- **LLM 输出双重校验**：本体系统用诊断标准/治疗规范/患者历史核对 LLM 建议的医疗正确性后才采纳。

## 效果
- Dataset: Kaggle Tuberculosis Symptoms Dataset（1,000 患者）| Metric: 本体结构指标 | Result: Attribute Richness **0.496**、Class Richness 0.017、Relationship Richness 0.749
- Dataset: GraphDB 依赖分析 | Metric: SWRL 规模 | Result: **240 条 swrl:Imp 规则**、644 DatavaluedPropertyAtom、302 ClassAtom、75 BuiltinAtom
- Dataset: SPARQL 时延 | Metric: 查询延迟 | Result: 简单 **0.20–0.25s**、中等 0.30–0.40s、复杂时序 0.90s
- Dataset: 5 个临床问题 QA | Metric: F1（对照专家参考答案）| Result: **0.702–0.778**（Precision 0.690–0.815）；FAISS 相似度 0.7633–0.9879
- Dataset: 端到端（5 患者）| Metric: 时延 | Result: CEP 0.75–0.95s + LLM 推理 2.3–2.7s + 本体查询 1.0–1.3s = **4.2–4.7s/患者**
- ⚠️ TB 检测任务本身无与 baseline 的分类准确率对比表（对比表均为定性能力对比；OCEP 85% 是引用的先前工作数字）——具体数值待补充

## 关键引用
> "Previous research has largely concentrated on ontology-driven modeling, complex event processing, or AI-based diagnostics as separate efforts... the proposed work combines ontology, CEP, and LLMs into a unified framework for real-time tuberculosis detection within a single platform." — Section 2.4, p.5

> "The ontology system checks the results that the LLM gives it using a structured knowledge base with diagnostic criteria, treatment standards, patient history, and clinical protocols. This double check makes sure that the LLM's suggestions are correct from a medical point of view." — Section 3.10, p.11

> "Although LLMs can suggest these extensions, domain experts must review and implement final updates manually." — Section 5, p.14

## 关联
- [[OntologyConstrainedGeneration]] — LLM 辅助本体演化是"约束生成"的元级应用（生成对象是本体自身）
- [[ReasonerGuidedRepair]] — Pellet 一致性校验把关 LLM 本体演化建议，防止不一致公理入库
- [[OntologyReasoning]] — BFO+SWRL+Pellet 是经典 OWL 本体推理栈在实时场景的工程化
- [[agentic-redux]] — 同用 BFO 顶层本体做领域建模
- [[hear-hypergraph-enterprise]] — 同为医疗诊断场景的本体推理，HEAR 用超图、本文用 SWRL+CEP
