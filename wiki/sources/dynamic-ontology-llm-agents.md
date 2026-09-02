---
title: "OaK: 动态本体作为 LLM Agent 内核（Toward Effective and Reliable LLM Agents via Dynamic Ontology）"
type: source
tags: [ontology-graph-retrieval]
sources: [dynamic-ontology-llm-agents]
source_file: raw/papers/dynamic-ontology-llm-agents.pdf
last_updated: 2026-08-31
arxiv_id: "2608.22974"
authors: ["Xiaohui Zhang", "Zequn Sun", "Chengyuan Yang", "Yuanning Cui", "Lingbing Guo"]
year: 2026
venue: "arXiv preprint"
citation_count: 0
doi: ""
---

## 概要
OaK 是一个 ontology-as-a-kernel 框架，为 LLM agent 动态构建任务导向的 ontology。对于每个任务，OaK 自动构造 schema（S）和 typed reasoning functions（F），从任务数据实例化 knowledge graph，并利用 judge feedback 迭代精修两者后冻结为推理内核。推理阶段，ReAct agent 通过冻结的 kernel 调用 typed functions 作为工具，在 schema-constrained graph 上执行检索、过滤、遍历与聚合。在 TravelPlanner、CRMArenaPro 和 ToolQA 三个 benchmark 上，OaK 在两个 LLM backbone 上均取得最优聚合性能。

## 解决的问题
LLM agent 在多步执行中，行为是否可控、可信赖成为核心挑战——最终答案准确率无法揭示 supporting evidence 和 tool call 的合理性，也无法定位执行失败的根源。现有方法如 Reflexion（verbal reinforcement）、MemP（procedural memory）、AFlow/AgentSquare（workflow optimization）改善了规划与复用，但仍将 admissible concepts 和 action sequences 隐含在 prompt 中，无法提供可检查的 semantic-procedural contract。GraphRAG/G-Retriever 将 graph 作为外部知识层，但未指定 task-level 可复用计算。

## 方法与技术
1. **Ontology Kernel K=(S,F)**：S 是 task-oriented schema（YAML/JSON 格式的 named entity types、properties、typed relations），F 是从 generic operator library 编译出的 typed reasoning functions；kernel 是 agent 访问数据的唯一通道。
2. **Schema construction 三阶段**：requirement analysis（LLM 读任务描述+样本生成需求规格）→ schema drafting（基于需求和上一轮 repair feedback 起草）→ formal verification（编码为 OWL ontology，用 HermiT reasoner 检查 disjointness/restriction/property-level/global consistency/unsatisfiable classes 五类逻辑有效性，失败则带 counterexample 回退重试）。
3. **Knowledge Graph instantiation（chunk-map-merge）**：将语料切分为 token-bounded chunks，每个 chunk 独立用 LLM extractor 按 schema 提取 entity/relation candidates，再通过 schema-declared primary key 的 key signature 做等价类合并，消除跨 chunk 重复实体。
4. **Function composition**：LLM-based composer 通过观察 queries 在 graph 上的解析模式，将 recurring reasoning steps 编译为单个 typed function；每个 function 通过 compose/specialize/adapt 三种方式 grounded on generic operator library（lookup_entities, filter_numeric, traverse_relations, aggregate_values 等 9 个算子）。
5. **Judge-driven iterative refinement**：每轮用官方评分对 trajectory 打分，judge model 审查整个 kernel + trajectory + scores，产出 repair suggestions（target artifact, action ∈ {add, delete, modify}, patch, reason），反馈到下一轮的 schema 和 function 构造。

## 创新点
- **Ontology as operational kernel（vs. descriptive ontology）**：传统 ontology 仅描述域中存在什么，OaK 将 ontology 作为 semantic-procedural contract，既约束 agent 可调用的概念，又通过 typed functions 约束可执行的计算。
- **Automated schema construction + formal verification（vs. manual expert ontology）**：自动从任务描述和训练数据构造 schema，并用 HermiT reasoner 做形式化验证。
- **Judge-driven refinement of schema + functions（vs. Self-Refine/Reflexion 的 response-level 修正）**：不修改正文或响应，而是诊断并修复 schema 和 function 本身的缺陷。
- **Task-conditioned function catalog（vs. GraphRAG/G-Retriever 的纯检索层）**：不仅用 graph 检索证据，还将 recurring reasoning steps 编译为可复用的 typed function，减少 agent 内部推理。

## 效果
- Dataset: TravelPlanner (DeepSeek) | Metric: Final Pass Rate | Result: 55.90% | Baseline: 15.30% (ReAct) | Δ: [+265.4%]
- Dataset: TravelPlanner (DeepSeek) | Metric: HC Macro | Result: 61.57% | Baseline: 36.40% (ReAct) | Δ: [+69.1%]
- Dataset: TravelPlanner (DeepSeek) | Metric: HC Macro | Result: 61.57% | Baseline: 59.50% (MemP) | Δ: [+3.5%]
- Dataset: CRMArenaPro B2B (DeepSeek) | Metric: Avg. | Result: 78.38% | Baseline: 60.78% (ReAct) | Δ: [+28.9%]
- Dataset: CRMArenaPro B2B (DeepSeek) | Metric: Database | Result: 94.69% | Baseline: 71.56% (ReAct) | Δ: [+32.3%]
- Dataset: ToolQA (DeepSeek) | Metric: Avg. (weighted) | Result: 64.58% | Baseline: 51.96% (ReAct) | Δ: [+24.3%]
- **Ablation**: TravelPlanner (GPT-4o-mini) Final Pass Rate: OaK 19.70% → w/o Function Module 9.90% (Δ −50.0%)，function module 是最大贡献
- **Ablation**: w/o Iterative Refinement (1 round only) substantially worse，迭代精修显著有效

## 关键引用
> "the central challenge is no longer only whether an agent can act, but whether its behavior remains controllable and trustworthy as execution becomes longer and more autonomous" — Section 1, Introduction

> "satisfying individual constraints does not necessarily produce a jointly valid plan" — Section 4.3, Main Results

> "making domain semantics and reasoning procedures explicit can improve both effectiveness and inspectability in LLM agents" — Section 5, Conclusion

## 关联
- [[OntologyGraphRetrieval]] — 本体图检索核心概念
- [[OntologyFirstAgentDesign]] — Round 13 本体优先 Agent 设计
- [[worlddb-ontology-aware-memory]] — Round 15 本体感知图世界记忆引擎
- [[auto-ontology-construction-llm]] — Round 13 LLM 外部本体记忆层
- [[AgentMemory]] — Agent 记忆概念
