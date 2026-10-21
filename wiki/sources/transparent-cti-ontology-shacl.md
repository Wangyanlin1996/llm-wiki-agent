---
title: "Enabling Transparent CTI（本体+SHACL 约束 LLM 网络威胁情报抽取）"
type: source
tags: [owl2-reasoning]
sources: [transparent-cti-ontology-shacl]
source_file: raw/papers/transparent-cti-ontology-shacl.pdf
last_updated: 2026-10-21
arxiv_id: "2509.00081"
authors: ["Luca Cotti", "Anisa Rula", "Devis Bianchini", "Federico Cerutti"]
year: 2025
venue: "XAI-KRKG @ ECAI 2025 Workshop"
citation_count: 0
doi: ""
---

## 概要
蜜罐/系统日志非结构化、语法不一致、语义歧义，是 CTI 的核心数据源。本文提出本体驱动的结构化输出方法：自建轻量平面日志本体 + 配套 SHACL 规范（基数、类型一致性、必备属性存在性）同时引导 LLM 输出结构与校验生成 KG 的语义有效性，配合 MMR few-shot 示例检索与最多 3 轮迭代修正回路。5 个 LLM 上几乎全指标胜过 prompt-only 基线：Qwen 2.5 Coder 14B F1 0.009→0.811、Claude 3.5 Sonnet 0.611→0.859（Mistral Large 是唯一退化的反例 0.539→0.423）。与同组 OntoLogX（agent 式日志→KG 管线）是配套方法论论文。

## 解决的问题
传统固定规则/模板解析器适应性差；纯 prompt 的 LLM 抽取在领域内容上精度不足；UCO/STIX/SEPSES 等安全本体假设输入是已解析的结构化 observables（SEPSES 明确"不旨在引导自由文本信息抽取"）。缺口：一个既能引导 LLM 输出结构、又能做 SHACL 合规验证的轻量中间本体层。

## 方法与技术
1. **自建轻量平面日志本体**：核心类 Event + User Identity/Application/Process/File/Network Address/Source/URL，时间维度用 W3C Time 本体；自底向上从代表性日志数据集（含 honeynet 流）设计，参照澳大利亚网络安全中心日志指南；定位为与 STIX/SEPSES 对齐前的预处理层。
2. **配套 SHACL 规范**：对关键类/属性施加基数、类型一致性、必备属性存在性约束——明确其作用是"在 LLM 抽取管线中强制 schema 合规、缓解缺字段/错误关系"。
3. **MMR few-shot 示例检索**：向量库索引人工标注示例 KG，Maximal Marginal Relevance 平衡相关性与多样性选示例（λ 权衡），避免近重复。
4. **结构化输出生成**：model-agnostic prompt（角色+本体指令+常见失败模式约束：恰好一个 Event 节点、图必须连通、禁止新类型）+ Pydantic 结构化输出工具（function calling）；LangChain 实现，Neo4j 图数据库 + 向量索引，嵌入模型 gte-multilingual-base。
5. **迭代修正回路**：自动检查语法有效性+本体合规性，检出问题构造针对性修正 prompt 回喂 LLM，最多 3 轮；仍不合规则输出空图（主动惩罚指标，防脏数据入库）。

## 创新点
- **vs prompt-only 基线（同 LLM 同 JSON 格式说明，无结构化输出工具/MMR/修正回路）**：几乎所有模型几乎所有指标胜出——直接对照实验。
- **vs UCO/STIX/SEPSES 安全本体**：那些需预解析字段、复杂 modular schema、不支持 SHACL 引导生成；本方案是专为"自由文本输入+SHACL 合规生成"设计的最小扁平 schema（Table 1 逐维度对比）。
- **透明性主张**：抽取逻辑可通过 prompt 检查与修改，中间产物（KG、验证结果）可审计，支持人工监督。

## 效果
- Dataset: AIT-LDS v2.0（70 条多样化日志：10 few-shot/10 验证/50 测试），5 LLM，每实验重复 10 次 | Metric: F1 | Result: Qwen 2.5 Coder 14B **0.009→0.811**（+0.802）；Llama 3.3 70B 0.637→**0.856**（+0.219）；Claude 3.5 Sonnet 0.611→**0.859**（+0.248，最优）
- Dataset: 同上 | Metric: Precision / Recall | Result: Qwen P 0.420→0.870、R 0.005→0.759；Claude Sonnet R 0.514→0.858
- Dataset: 同上 | Metric: G-Eval（LLM-as-judge 语义保真度）| Result: 全模型提升（Qwen 0.008→0.723；Sonnet 0.728→0.767）
- **反例**：Mistral Large 123B 退化 0.539→0.423——唯一基线更好的模型
- SHACL 违规图比例大幅下降但不保证完全合规——归因于结构化输出工具表达力弱于 SHACL 约束语言；执行时延 1.4s/事件（Llama 3.3）至 9.8s（Mistral Large）

## 关键引用
> "SHACL enables automated quality control over knowledge, verifying whether generated KGs respect required types, property cardinalities, and relationship patterns." — Section 2.2

> "By enforcing constraints on cardinality, type consistency, and presence of essential properties, we ensure that generated KGs not only follow the OntoLogX vocabulary but are also semantically valid and queryable." — Section 3.1

> "Interestingly, the results are not guaranteed to be fully SHACL-compliant: this can be attributed to the limited expressiveness offered by the adopted structured output approach compared to the SHACL constraints language." — Section 4.1.3

## 关联
- [[OntologyConstrainedGeneration]] — 本体+SHACL 双重约束 LLM 输出结构的最直接同类工作
- [[ValidationFeedbackLoop]] — 迭代修正回路 + 空图惩罚策略防脏入库
- [[ontologx-cybersecurity-kg]] — 同组配套：本篇是方法论（约束引导结构化输出），OntoLogX 是 agent 管线（RAG+MITRE 预测）；共同点是 SHACL 三阶段校验
- [[llm-capability-ontologies]] — 同为"SHACL 校验 LLM 生成物"谱系，领域不同（工业能力本体 vs CTI 日志）
- [[titan-graph-reasoning-cti]] — 同为 CTI 结构化场景（TITAN MITRE 本体图推理）

## 矛盾
- Mistral Large 退化为反例：本体约束并非对所有模型都有益，可能干扰强模型的既有抽取模式——约束收益存在模型相关性
