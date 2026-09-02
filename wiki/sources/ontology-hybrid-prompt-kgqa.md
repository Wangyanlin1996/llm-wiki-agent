---
title: "OntoSCPrompt: 本体引导混合提示学习用于 KGQA 泛化（Ontology-Guided Hybrid Prompt Learning for KGQA Generalization）"
type: source
tags: [ontology-graph-retrieval]
sources: [ontology-hybrid-prompt-kgqa]
source_file: raw/papers/ontology-hybrid-prompt-kgqa.pdf
last_updated: 2026-08-31
arxiv_id: "2502.03992"
authors: ["Longquan Jiang", "Junbo Huang", "Cedric Möller", "Ricardo Usbeck"]
year: 2025
venue: "ICSC 2025 (IEEE International Conference on Semantic Computing)"
citation_count: 0
doi: ""
---

## 概要
该论文提出 OntoSCPrompt，一种基于 LLM 的两阶段 KGQA 方法，将语义解析与 KG 相关交互分离：Stage-S 预测 KG 无关的 SPARQL 查询结构（含 6 种占位符），Stage-C 用 KG 特定的 entity/relation/concept 填充占位符。为增强对底层 KG 的理解，作者提出 ontology-guided hybrid prompt learning 策略，将 KG ontology 通过 verbalization 转为文本后整合到离散文本 prompt 和连续可学习向量的学习过程中，并设计了 grammar-constrained、structure-guided 和 subgraph constrained 三种解码策略确保生成 SPARQL 的语法正确性。该方法在 WebQSP、CWQ、LC-QuAD 1.0 上达到 SOTA 或 competitive 表现，并能泛化到未见 KG。

## 解决的问题
现有 KGQA 系统通常为特定 KG（如 Wikidata、DBpedia、Freebase）定制，由于底层 KG 存在三类异构性——schema heterogeneity（如 Person 在不同 KG 中命名不同）、topology heterogeneity（如 Wikidata 使用 qualifier 节点）和 assertions heterogeneity（同一事实在不同 KG 中用不同 relation 表示），系统无法泛化到未见 KG 而不需大量训练数据。EmbedKGQA、PullNet、TERP 等方法仅处理 assertion heterogeneity，无法应对 schema 或 topology 差异。LLM 在知识密集型 KGQA 任务中存在 hallucination 和 factual inaccuracy 问题，缺乏与异构 KG 的交互。

## 方法与技术
1. **两阶段框架（Stage-S + Stage-C）**：Stage-S 将问题翻译为 KG 无关的通用 SPARQL 结构，使用 6 种占位符：[ent]（entity）、[cct]（concept）、[rel]（relation）、[var]（variable）、[val]（literal）、[con]（constraint），支持 HAVING/GROUP BY/ORDER BY 等复杂子句；Stage-C 用 KG 特定的 schema elements 填充占位符。
2. **Ontology-Guided Textual Prompts**：Stage-S 使用结构 prompt（question + ontology），Stage-C 使用内容 prompt（structure + question + ontology），其中 ontology 通过 verbalization 方法转为文本格式。
3. **Aspect-aware Continuous Prompts**：引入 4 个可学习向量——vQ（学习 question 特征）、vG（学习 ontology 特征）、vB（输入起始任务特征）、vE（输入末尾任务特征），与文本 embedding 拼接构造 hybrid prompt。
4. **Grammar-constrained Decoding（Stage-S）**：基于标准 SPARQL 语法规则，在 decoding 时过滤不符合 grammar 的输出。
5. **Structure-guided + Subgraph Constrained Decoding（Stage-C）**：Structure-guided 在 beam search 中将与 Stage-S 占位符不一致的 candidate token 分数设为−∞；Subgraph Constrained 基于 question entity 的 top-K=20 路径子图，优先选择子图中存在的 relation。

## 创新点
- **首次将 prompt tuning 应用于 KGQA 泛化与评估任务**（vs. STaG-QA 和 HGNet 等两阶段方法使用 softly-tied query sketch/hierarchical autoregressive decoding 但未使用 prompt learning）——仅优化 prompt 向量即可在 LC-QuAD 1.0 达 70.3%、WebQSP 达 62.1%。
- **扩展的 SPARQL 结构表示（6 种占位符）**（vs. 先前工作仅支持基本结构）——新增 [cct]（concept）和 [con]（constraint）占位符，支持 FILTER/ORDER BY/GROUP BY/HAVING 等复杂子句。
- **Ontology-guided hybrid prompt 同时整合离散与连续 prompt**（vs. 纯 textual prompt 或纯 continuous prompt 方法）——将 verbalized ontology 同时注入文本 prompt 模板和 4 个 aspect-aware 可学习向量。
- **三种 task-specific constrained decoding 策略**（vs. 无约束的 autoregressive decoding）——grammar/structure/subgraph 三种约束分别确保 SPARQL 语法正确性、两阶段结构一致性和 relation disambiguation。

## 效果
- Dataset: LC-QuAD 1.0 | Metric: F1 (%) | Result: 79.1 (w/ constraints) | Baseline: 75.1 (HGNet) | Δ: [+5.3%]
- Dataset: LC-QuAD 1.0 | Metric: F1 (%) | Result: 79.1 | Baseline: 51.4 (STaG-QA) | Δ: [+53.9%]
- Dataset: WebQSP | Metric: Hits@1 (%) | Result: 73.8 (w/ constraints) | Baseline: 70.6 (HGNet) | Δ: [+4.5%]
- Dataset: CWQ (fine-tuned on DA, GA) | Metric: Hits@1 (%) | Result: 70.4 | Baseline: 58.1 (HGNet) | Δ: [+21.2%]
- Dataset: DBLP-QuAD | Metric: F1 (%) | Result: 84.6 (pre-trained variant) | Baseline: 78.2 (non-pre) | Δ: [+8.2%]
- Dataset: CoyPuKGQA | Metric: F1 (%) | Result: 83.3 (pre-trained variant) | Baseline: 80.2 (non-pre) | Δ: [+3.9%]
- **Ablation**: LC-QuAD 1.0 F1: w/ constraints 79.1 vs w/o constraints 70.2 (Δ +12.7%)
- **Ablation**: WebQSP Hits@1: w/ constraints 73.8 vs w/o constraints 65.5 (Δ +12.7%)
- **Ablation**: PT+FT vs PT only: LC-QuAD F1 79.1 vs 70.3 (Δ +12.5%); WebQSP Hits@1 73.8 vs 62.1 (Δ +18.8%)

## 关键引用
> "we utilize a two-stage framework: 1) Query Structure Prediction, wherein questions are translated into generic SPARQL query structures independent of any particular KG. 2) KG Content Population, where the SPARQL structures are populated with schema elements specific to the given KG." — Section II.A, p.2

> "only optimizing ontology-guided hybrid prompt results in 70.3% on LC-QuAD 1.0 and 62.1% on WebQSP. This highlights its importance in understanding the semantics of the underlying KG and adapting to unseen KG without extensive re-training." — Section IV.B, p.6

> "Constrained decoding approaches facilitate the generation of text sequences in a controllable and expected fashion." — Section II.D, p.3

## 关联
- [[OntologyGuidedQueryGeneration]] — 本体引导查询构造
- [[d3st-description-driven-tod]] — Round 10 schema 描述替代名称
- [[beyond-ontology-dst]] — Round 10 无本体目标导向 DST
- [[nlkgq-nl-ontology-query]] — Round 15 OWL 本体零样本查询生成
- [[researcher-agents-kgqa]] — Round 15 Agentic text-to-SPARQL
