---
title: "SatIR: 约束满足驱动的临床试验可扩展高召回检索（Constraint-Satisfaction-Based IR for Clinical Trials）"
type: source
tags: [ontology-precise-retrieval]
sources: [satir-constraint-ir-clinical]
source_file: raw/papers/satir-constraint-ir-clinical.pdf
last_updated: 2026-09-08
arxiv_id: "2604.08849"
authors: ["Zikai Zhou", "Yufei Jin", "Yilin Xu", "Yu-Chiang Wang", "Chieh-Ju Chao"]
year: 2026
venue: "COLM 2026"
citation_count: 0
---

## 概要
SATIR 是一种基于形式化约束满足的可扩展临床试验检索方法。核心思路是将约束理解与约束满足分离：用 LLM 将非正式临床文本（试验入排标准、患者记录）转换为形式化 Satisfiability Modulo Theories (SMT) 约束，再将 SMT 匹配问题投影到关系代数实现高效数据库检索。系统引入 TRIALREPR 表示（支持布尔逻辑、数值阈值、时间窗、例外），基于 SNOMED 医学 ontology 做概念同一性和蕴含。在 SIGIR 2016 和 TREC 2022 基准上，SATIR 相比 TrialGPT 每患者多检索 32%–72% 的 relevant-and-eligible 试验，检索仅耗时 146 ms/患者。

## 解决的问题
相似性检索将资格约束视为软信号而非硬性要求。临床试验匹配是高 stakes 的 per-profile 匹配问题——每个试验定义自己的约束集，需对照同一患者记录逐一检查。现有系统（TrialGPT 等）将患者和试验表示为关键词/文本/embeddings，按 similarity 检索候选，但资格取决于必须联合满足的尖锐约束——否定、时间性、数值阈值、偏侧性——而非独立评分。

## 方法与技术
1. **TRIALREPR 形式化表示**：基于 SMT 的临床试验/患者表示，支持布尔逻辑、数值阈值、时间窗、例外；在 SNOMED 模型中融入 ontology-aware 的概念同一性和蕴含（ISA、finding–observable-entity 展开）。
2. **LLM-based 语义解析器**：将 under-specified 临床试验文本翻译为 TRIALREPR。包含 entity canonicalization（SNOMED 接地）、incremental SMT programming orchestration、LLM-orchestrated repair。
3. **SMT-to-Relational Algebra 投影**：将 SMT 匹配问题投影到关系代数，把 TRIALREPR 作为 first-class data 存入数据库。检索时用 SQL 查询联合评估 trial-side 和 patient-side 约束。
4. **Salience-Based Missingness Handling**：患者记录不完整时，salience 层为选定变量赋默认值，使约束求解器能拒绝入排标准要求缺失证据的试验。LLM 评估缺失信息的 salience。
5. **三档检索目标设计**：treat-chief（仅治疗主诉）、treat-any（治疗任何现有疾病）、relevant-to-any（与任何现有疾病临床相关），使系统可在不同 precision-recall 权衡下评估。

## 创新点
- **Constraint-Satisfaction-Based Retrieval（vs Similarity-Based）**（vs TrialGPT/BMRetriever/PubMedBERT/BGE 将约束作为 soft signals 评分）——将约束作为 binding requirements 形式化满足，将形式化方法（SMT）引入 IR 检索阶段。
- **SMT-to-Relational Algebra 投影**——SMT 求解器不可扩展到数千试验×百万患者，SATIR 将 SMT 公式投影为数据库可执行的 CNF 子句，用 SQL 查询实现大规模约束满足。
- **Ontology-Grounded 形式化**——结合 SNOMED 概念蕴含，在形式化层处理临床歧义。消融证明这是最大贡献因子（移除后 true positives 下降 42.2%）。
- **可解释性**——每个检索/拒绝决策可追溯到具体约束子句。

## 效果
- Dataset: SIGIR 2016 | Metric: Macro Recall (treat-chief) | Result: 93.68 | Baseline: 70.14 (TrialGPT) | Δ: [+23.54pp]
- Dataset: SIGIR 2016 | Metric: Macro Recall (treat-any) | Result: 85.53 | Baseline: 56.50 | Δ: [+29.03pp]
- Dataset: TREC 2022 | Metric: Macro Recall (treat-chief) | Result: 80.37 | Baseline: 24.72 (TrialGPT) | Δ: [+55.65pp]
- Dataset: TREC 2022 | Metric: Recall qrel=2 (treat-chief) | Result: 0.445 | Baseline: 0.139 | Δ: +0.306
- Dataset: SIGIR 2016 | Metric: Retrieval time | Result: 146 ms/patient
- **Ablation**: w/o SNOMED Ontology: True Positives -42.2% — ontology entailment is the LARGER contributor
- **Ablation**: w/o Salience: True Positives -7.7% — smaller but consistent contributor
- Clinician validation: Gwet's AC1=0.82, acceptance 92.6%

## 关键引用
> "Similarity-based retrieval treats these constraints as soft signals rather than requirements to be individually verified, so relevant-but-ineligible candidates crowd out eligible ones." — Section 1, p.2

> "Our approach separates understanding constraints from satisfying them. We use LLMs to translate natural-language text into a formal representation, then use formal methods to perform the match." — Section 2, p.3

> "Rather than forcing all text into a rigid schema, we design a representation that is conservative and recall-oriented, avoiding the exclusion of potentially eligible trials." — Section 2, p.3

## 关联
- [[OntologyGraphRetrieval]] — 本体图检索核心概念
- [[OntologyGroundedRAG]] — 本体 grounding RAG
- [[neuron-clinical-explainability]] — Round 13 SNOMED CT 本体增强临床可解释性
- [[qime-ontology-embeddings]] — Round 10 本体驱动可解释医学嵌入
- [[deeproot-kg-multi-agent]] — Round 16 KG 协调多 Agent 医疗推理
