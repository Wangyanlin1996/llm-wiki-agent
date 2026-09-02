---
title: "OwlPath: LLM Bug Repair 无损知识压缩（Lossless Knowledge Compression via OWL2 Reasoning）"
type: source
tags: [ontology-graph-retrieval]
sources: [owlpath-bug-repair]
source_file: raw/papers/owlpath-bug-repair.pdf
last_updated: 2026-08-31
arxiv_id: "2607.27249"
authors: ["Bo Zhang", "Ren Pan", "Huan Chen", "Xiang Song"]
year: 2026
venue: "arXiv preprint"
citation_count: 0
doi: ""
---

## 概要
OwlPath 是一个构建在 CodeGraph 之上的 OWL2 reasoning layer，将源代码通过 tree-sitter 提取的 code graph（SQLite nodes/edges）投影为 OWL2 ontology，实现 lossless knowledge compression。它集成两个机制：transitive-closure engine 用单条 SPARQL property-path query 检索所有结构关联符号（O(1) amortized），OWL-SKM advisory layer 预计算 3KB 结构化摘要引导 agent 首次查询命中正确模块。在 18 个 SWE-bench Pro 匹配实例上，OwlPath 消耗 28.8% 更少 token 和 39.5% 更少时间，同时保持相当的 strict-apply rate。

## 解决的问题
LLM-based SE agent 受限于约 100K token 的 context window，必须从百万行代码库中检索结构相关的小子集。传统检索工具（grep、BM25、embedding search）将代码建模为 flat text，在 bug 的 ground truth 与 issue 描述结构关联但无字符串重叠时失效——如 subclass chain、transitive caller path、interface implementation hierarchy。Graph-based 方法（CodeGraph、SourceGraph）提供 1-hop 邻域查询但缺少 transitive closure，agent 必须逐跳迭代，既慢又消耗 turn budget。

## 方法与技术
1. **Tree-sitter 代码图提取**：确定性解析每个源文件生成 SQLite 数据库，nodes（classes/functions/methods/interfaces/structs/variables/routes）携带 qualified_name/file_path/kind/start_line/end_line，edges（extends/implements/calls/references/contains/imports）表示结构关系；相同源码产生 bit-identical 数据库。
2. **OWL2 ontology projection（bijection）**：单次 SQL pass 将每个 node 映射为 owl:NamedIndividual（带 data properties），每条 edge 映射为对应 OWL axiom——extends→rdfs:subClassOf、calls→:calls（均声明 owl:TransitiveProperty）、contains→:contains（非传递）；每个 source tuple 恰好产生一个 axiom，保证无损。
3. **Transitive-closure engine**：用 SPARQL 1.1 property paths（:extends+、:calls+、:implements+）通过 rdflib 执行；closure 在首次查询时 materialize（单次 SPARQL SELECT DISTINCT），缓存在内存 (s,o) pair 集合中，后续查询为 O(1) hash lookup。
4. **OWL-SKM 两层 advisory**：Layer 1 Module Map——获取文件树，解析为 hierarchical module structure，按 score = log(symbols)×0.5 + log(files)×0.3 + log(symbols_per_file)×0.2 评分选取 top modules；Layer 2 Issue Map——从 problem statement 提取关键词，收集 issue-relevant symbol candidates。
5. **On-demand ReAct 集成**：SKM 仅在 agent 首次调用 owlpath search 时作为一次性 advisory 发出（3KB），closure expansion 通过 -with-closure flag 由 agent opt-in；agent 自主决定何时调用。

## 创新点
- **OWL2 bijection projection（vs. string-match/BM25/embedding retrieval）**：projection 是双射——每个 source tuple 恰好产生一个 OWL axiom，保证无结构信息丢失；string matching 在 anchor 名称不出现在 ground-truth 文件中时 recall 为 0%。
- **Transitive-closure via SPARQL property paths（vs. SQL recursive CTE / 逐跳迭代）**：SPARQL t+ 单次遍历 materialize closure（O(n+m) 一次性，O(1) amortized），而 SQL recursive CTE 对 k-hop 查询为 O(n^k)。
- **OWL-SKM 3KB advisory（vs. flat file listing / 全量上下文）**：将数千文件压缩为 3KB 结构化摘要，引导 agent 首次查询命中正确模块。
- **On-demand tool design（vs. forced context injection）**：annotated arm（强制注入 SKM+closure）消耗 2.0× token 但 strict-apply 仅 +0.4%——证明 forced prompt inflation 适得其反。

## 效果
- Dataset: SWE-bench Pro (18 instances) | Metric: Strict-apply rate | Result: 68.4% | Baseline: 66.7% (CodeGraph-only) | Δ: [+1.7pp]
- Dataset: SWE-bench Pro | Metric: Avg total tokens | Result: 1,416K | Baseline: 1,989K | Δ: [−28.8%]
- Dataset: SWE-bench Pro | Metric: Avg wall-clock time | Result: 648s | Baseline: 1,071s | Δ: [−39.5%]
- Dataset: SWE-bench Pro offline | Metric: Recall | Result: 0.464 (OwlPath) | Baseline: 0.226 (CodeGraph string-match) | Δ: [+105.3% (2.06×)]
- Dataset: SWE-bench Pro offline | Metric: Hit rate | Result: 88.1% | Baseline: 59.7% | Δ: [+28.4pp (1.48×)]
- Dataset: Structural retrieval | Metric: recall@all | Result: 28.8% | Baseline: 4.4% (string-match) | Δ: [+24.4pp (6.5×)]
- Dataset: Structural retrieval (Transitive callers) | Metric: Recall | Result: 69% | Baseline: 0% (string-match) | Δ: [+69pp]
- **Ablation**: annotated arm (forced SKM+closure) Avg total tokens 2,835K vs hybrid 1,416K (+100.0% token inflation for only +0.4pp strict-apply)

## 关键引用
> "Conventional retrieval tools—grep, BM25, embedding search—model code as flat text, returning files that contain matching strings. This approach fails when the bug's ground truth is structurally connected to the issue description but shares no string overlap." — Introduction

> "The projection is a bijection: every source tuple produces exactly one OWL axiom, and distinct tuples produce distinct axioms. This guarantees that no structural information is lost during the ontology encoding—the lossless property we claim." — Method

> "what matters is not the volume of information, but its precision and timing: the right 3KB at the exact moment the agent's reasoning requires it outperforms 15KB of forced context injected preemptively." — Discussion

## 关联
- [[OntologyGraphRetrieval]] — 本体图检索核心概念
- [[OntologyGuidedQueryGeneration]] — 本体引导查询构造
- [[ontology-project-memory-coding]] — 同轮编码 Agent 本体记忆
- [[codewiki]] — Round 12 递归多智能体代码库文档
- [[NeurosymbolicOrchestration]] — Round 8 LLM 编排+符号引擎
