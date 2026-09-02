---
title: "OntoLogX: 本体引导网络安全日志知识图谱提取（Ontology-Guided KG Extraction from Cybersecurity Logs）"
type: source
tags: [ontology-graph-retrieval]
sources: [ontologx-cybersecurity-kg]
source_file: raw/papers/ontologx-cybersecurity-kg.pdf
last_updated: 2026-08-31
arxiv_id: "2510.01409"
authors: ["Luca Cotti", "Idilio Drago", "Anisa Rula", "Devis Bianchini", "Federico Cerutti"]
year: 2025
venue: "arXiv preprint"
citation_count: 0
doi: ""
---

## 概要
OntoLogX 是一个自主 AI agent，利用 LLM 将原始网络安全日志转换为 ontology-grounded Knowledge Graph（KG）。系统集成了轻量级日志 ontology、RAG 检索机制和迭代 SHACL 校验步骤，确保生成的 KG 在语法和语义上均有效。系统进一步将事件级 KG 聚合为 session，使用 LLM 预测 MITRE ATT&CK tactics。在公开 AIT-LDS 数据集和真实 Cowrie honeypot 数据上的实验表明，OntoLogX 能跨多个 LLM 后端稳健生成符合 ontology 的 KG。

## 解决的问题
网络安全日志（尤其 honeypot 日志）虽富含 Cyber Threat Intelligence（CTI），但具有非结构化、语法异构、语义模糊且跨设备碎片化等特点。传统 rule-based 解析方法（如 SLOGERT 的 log parsing + 自定义 ontology、KRYSTAL 的 SPARQL 后向-前向链推理）依赖预定义规则，无法适应不断演变的威胁行为和日志格式变体。现有 LLM 方法中，LogPrécis 需 fine-tune 且依赖预处理日志 session、缺乏语义 grounding；CyKG-RAG 仍需 rule-based 步骤构建 KG。核心缺口：在单一 LLM 框架内同时集成 retrieval、ontology 指导和 SHACL 校验。

## 方法与技术
1. **轻量级日志 ontology + SHACL schema**：以 `Event` 为核心类（映射至 `prov:Entity`），链接 `Source`（映射至 `prov:Agent`）、`Parameter` 子类（`NetworkAddress`、`File`、`Application`、`UserCredential` 等，`TimeStamp` 对齐 W3C time ontology）；配套 SHACL 规则约束属性基数、类型一致性、必填字段。
2. **混合检索（hybrid retrieval）**：对输入日志同时执行 vector search（基于 `gte-multilingual-base` embedding 的语义相似度）和 full-text search（基于词项的精确匹配），各分数归一化后合并排序。
3. **Maximal Marginal Relevance（MMR）重排序**：在归一化检索结果上应用 MMR，`MMR(d) = λ·Sim(d,q) − (1−λ)·max_{s∈S} Sim(d,s)`，惩罚冗余候选，确保 few-shot examples 覆盖更广模式。
4. **结构化输出 + 迭代 SHACL 三阶段校验**：通过 function-calling 接口约束 LLM 输出为预定义 JSON graph schema；校验分三阶段——(i) 语法有效性、(ii) ontology 合规性（SHACL）、(iii) 语义一致性（缺失/重复 Event 节点、悬空引用）；违规时构造针对性 correction prompt 迭代修正，最多 3 轮。
5. **Session 聚合 + MITRE ATT&CK tactics 预测**：将验证后的单事件 KG 按时序关系或共性属性聚合为 session，LLM 分析聚合 KG 并标注一个或多个 MITRE ATT&CK enterprise tactics。

## 创新点
- **vs. SLOGERT/KRYSTAL**：用 LLM 直接从原始日志生成 KG，无需预解析，通过 RAG + ontology 约束保证语义一致性，而非依赖 rule-based log parsing。
- **vs. LogPrécis**：无需领域特定训练，利用预训练 LLM 泛化能力 + RAG few-shot 适配异构日志源。
- **vs. CyKG-RAG**：首次在单一框架内整合 retrieval + ontology 指导 + SHACL 校验，实现端到端自主处理。
- **vs. UCO/SEPSES ontology**：UCO 过于复杂（增加 LLM 错误概率），提出折中的轻量级 ontology，平衡表达力与自动化生成可行性。

## 效果
- Dataset: AIT-LDS | Metric: F1 Score | Result: 0.832 (Claude Sonnet 4, Populated DB) | Baseline: 0.283 (Baseline) | Δ: [+194%]
- Dataset: AIT-LDS | Metric: Precision | Result: 0.845 (Claude Sonnet 4) | Baseline: 0.330 | Δ: [+156%]
- Dataset: AIT-LDS | Metric: Entity Linking Accuracy | Result: 0.762 | Baseline: 0.278 | Δ: [+174%]
- Dataset: AIT-LDS | Metric: Relationship Linking Accuracy | Result: 0.822 | Baseline: 0.410 | Δ: [+100%]
- Dataset: AIT-LDS | Metric: F1 Score (open-weights) | Result: 0.762 (Qwen3 Coder 32B) | Baseline: 0.429 | Δ: [+78%]
- **Ablation**: Retrieval 贡献最大——Baseline F1=0.283 → Retrieval-only F1=0.758 → Full retrieval F1=0.786
- **Ablation**: G-Eval vs F1 trade-off——高 G-Eval 伴随低 F1 意味着语义丰富但有噪声（spurious triples），推荐 G-Eval 目标区间 0.7–0.8

## 关键引用
> "We argue that existing cybersecurity ontologies are not well-suited for LLM-based log processing. Minimal models capture too few concepts to be useful for CTI analysis. In contrast, large frameworks like UCO are overly complex for automated generation." — Section 3.2, p.5-6

> "a balanced approach, targeting G-Eval scores in the range of 0.7–0.8, is preferable for practical applications of OntoLogX, as it ensures both semantic fidelity and ontological integrity." — Section 4.1.4, p.11

> "Prior works addressed individual aspects such as ontology alignment or retrieval grounding, OntoLogX instead integrates retrieval, ontology guidance, and validation, within a single LLM-based framework." — Section 2.4, p.4

## 关联
- [[OntologyGraphRetrieval]] — 本体图检索核心概念
- [[OntologyGroundedRAG]] — 本体 grounding RAG
- [[titan-graph-reasoning-cti]] — Round 10 TITAN 本体(MITRE)威胁情报图推理
- [[ontologyrag-biomedical-code-mapping]] — Round 15 本体 KG 动态检索替代微调
- [[AuditableStructuredRetrieval]] — 可审计结构化检索
