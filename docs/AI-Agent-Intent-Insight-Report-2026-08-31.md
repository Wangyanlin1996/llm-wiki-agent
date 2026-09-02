# 本体图增强精准检索 论文洞察日报 — 2026-08-31

**日期**: 2026-08-31
**累计论文**: 312 篇（本轮新增 18 篇）
**知识库页面**: 439 页

## 概览

| 方向 | 本轮新增 | 累计 | 代表趋势 |
|---|---|---|---|
| A. 本体图直接增强检索精度 | 6 | — | 法律时序图+垂直域深化 |
| B. 本体感知图/记忆引擎 | 4 | — | 本体从描述到操作化 |
| C. 本体引导查询构造 | 3 | — | CQ→可执行计划+HOM |
| D. 构建验证+检索诊断 | 5 | — | 检索状态锁定诊断 |
| **总计** | **18** | **312** | |

## 新增论文清单（速查表）

| # | 论文 | 年份 | Venue | arXiv | 引用 | 方向 |
|---|---|---|---|---|---|---| 
| 1 | [SAT-Graph RAG](https://arxiv.org/abs/2505.00039) | 2025 | JURIX 2025 | 2505.00039 | 0 | A |
| 2 | [KG2QA](https://arxiv.org/abs/2506.07037) | 2025 | — | 2506.07037 | 0 | A |
| 3 | [OPI](https://arxiv.org/abs/2606.28076) | 2026 | PVLDB | 2606.28076 | 0 | A |
| 4 | [OntoLogX](https://arxiv.org/abs/2510.01409) | 2025 | — | 2510.01409 | 0 | A |
| 5 | [RAGulating](https://arxiv.org/abs/2508.09893) | 2025 | — | 2508.09893 | 0 | A |
| 6 | [TransU](https://arxiv.org/abs/2504.02889) | 2025 | — | 2504.02889 | 0 | A |
| 7 | [OaK](https://arxiv.org/abs/2608.22974) | 2026 | — | 2608.22974 | 0 | B |
| 8 | [MOOSEDev](https://arxiv.org/abs/2608.13662) | 2026 | NeSy 2026 | 2608.13662 | 0 | B |
| 9 | [OwlPath](https://arxiv.org/abs/2607.27249) | 2026 | — | 2607.27249 | 0 | B |
| 10 | [DeepRoot](https://arxiv.org/abs/2606.15931) | 2026 | ICML 2026 WS | 2606.15931 | 0 | B |
| 11 | [CQ-Plans](https://arxiv.org/abs/2604.02545) | 2026 | ESWC 2026 | 2604.02545 | 0 | C |
| 12 | [AgentMap](https://arxiv.org/abs/2607.27130) | 2026 | — | 2607.27130 | 0 | C |
| 13 | [OntoExtend](https://arxiv.org/abs/2607.17963) | 2026 | Semantics 2026 | 2607.17963 | 0 | C |
| 14 | [Beyond-Similarity](https://arxiv.org/abs/2606.09724) | 2026 | — | 2606.09724 | 0 | D |
| 15 | [Lock-In](https://arxiv.org/abs/2606.22728) | 2026 | — | 2606.22728 | 0 | D |
| 16 | [OmniRetrieval](https://arxiv.org/abs/2605.29250) | 2026 | — | 2605.29250 | 0 | D |
| 17 | [Manufacturing-KG](https://arxiv.org/abs/2507.22619) | 2025 | ECCAI 2026 | 2507.22619 | 0 | D |
| 18 | [OntoSCPrompt](https://arxiv.org/abs/2502.03992) | 2025 | ICSC 2025 | 2502.03992 | 0 | D |

## 新增论文结构化分析

### A. 本体图直接增强检索精度

---

#### 1. SAT-Graph RAG — 法律规范本体驱动时序图检索

**arXiv**: [2505.00039](https://arxiv.org/abs/2505.00039) | **Venue**: JURIX 2025 | **引用**: 0

**解决的问题**: 标准 flat-text RAG 对法律文本的层级结构（标题/章节/条款）和历时性演变（修正案/废止/合并）视而不见，导致时代错位答案。Graph RAG 用 NER 构建图，但法律核心语义实体是抽象概念而非专有名词，导致图稀疏。缺乏将法律规范版本演变与 RAG+provenance 结合的工作。

**方法与技术**: (1) LRMoo 本体四类节点（Norm/Component/CTV/CLV）实现 what/when/how 分离；(2) 聚合式版本传播（Aggregation, 非 Composition）复用未变更组件 CTV；(3) Action 节点因果具象化连接源条款和 CTV；(4) Multi-aspect 检索（内容/因果/元数据多路径）；(5) Planner-guided 8 步确定性查询管线。

**创新点**: 法律内在层级作为图骨架（vs Graph RAG 算法社区检测）；聚合非组合版本传播（vs 朴素 Composition 数据冗余）；立法事件作为一等可检索单元（vs Akoma Ntoso metadata 标签）。

**效果**: 概念框架+定性案例研究（巴西宪法），无定量实验。论文提出未来评估指标：Temporal Precision/Recall、Action-Attribution Accuracy、Causal-Chain Completeness。具体数值待补充。

**Wiki**: [[ontology-driven-graph-rag-legal]] | **概念**: [[LegalTemporalGraphRAG]]

---

#### 2. KG2QA — 通信标准知识图谱增强问答

**arXiv**: [2506.07037](https://arxiv.org/abs/2506.07037) | **Venue**: — | **引用**: 0

**解决的问题**: 通信标准数量爆炸，通用 LLM 在专业术语上表现受限。LoRA 微调缺乏事实 grounding，Text-RAG 无法提供结构化精确关联，通信标准领域缺乏专用 ontology 和自动化三元组抽取管线。

**方法与技术**: (1) LoRA 微调 Qwen2.5-7B（rank=16, 6,587 QA 数据集）；(2) 自定义 ontology（6 实体类型+10 关系类型+domain/range 约束）；(3) 三步式 LLM 辅助三元组抽取（头实体→关系→尾实体，θ=0.8）；(4) KG-RAG 管线（Neo4j+Ollama 量化部署）；(5) LLM-as-Judge 五维评估。

**创新点**: 通信标准专用 Ontology 设计（vs 通用 KG 无约束）；模块化 LLM 辅助 KG 构建（vs 人工标注）；微调+KG-RAG 集成（vs 单纯 Text-RAG）。

**效果**: BLEU-4 18.86→66.90（+255%）；超越 DeepSeek/ChatGPT/Gemini；KG-RAG Overall Avg 0.8134 vs w/o KG 0.7908（+2.26%）；Factual Accuracy 0.8045 vs 0.728（+3.17%）。
- Dataset: ITU-T Test | Metric: BLEU-4 | Result: 66.893 | Baseline: 18.8564 | Δ: [+255.0%]
- Dataset: 5-dim judge | Metric: Overall | Result: 0.8134 | Baseline: 0.7908 | Δ: [+2.26%]

**Wiki**: [[kg2qa-communication-standards]] | **概念**: [[OntologyGraphRetrieval]]

---

#### 3. OPI — 本体引导双向证据路径推理

**arXiv**: [2606.28076](https://arxiv.org/abs/2606.28076) | **Venue**: PVLDB | **引用**: 0

**解决的问题**: 多跳 KGQA 的 topic-centered expansion 面临路径爆炸（无约束前向扩展产生大量异构类型候选路径）和语义错配（路径到达答案类型兼容实体但违反隐式约束）。现有方法 ToG/RoG/GCR 检索阶段仍以主题侧探索为主。

**方法与技术**: (1) Relation-centric ontology graph（类型签名 c_h,r,c_t）；(2) 答案类型预测→末跳关系映射；(3) Ontology-guided 双向检索（前缀扩展+末跳匹配会合，搜索空间 O(b^x)→O(b^(x-1)·β)）；(4) Generator-Refiner 迭代精炼；(5) 自适应停止（减少 56.4% 轮次）。

**创新点**: Relation-centric ontology 作为答案侧约束接口（vs ToG/RoG 仅主题侧）；双向检索会合（vs 单向前向）；Generator-Refiner 精度过滤（vs 单次生成）。

**效果**: WebQSP Hit@1 92.3 vs 87.7（+4.6pts）；CWQ Hit@1 76.5 vs 66.8（+9.7pts）；候选路径-98.7%，检索时间-95.1%。
- Dataset: WebQSP | Metric: Hit@1 | Result: 92.3 | Baseline: 87.7 | Δ: [+4.6 pts]
- Dataset: CWQ | Metric: Hit@1 | Result: 76.5 | Baseline: 66.8 | Δ: [+9.7 pts]

**Wiki**: [[ontology-evidence-path-kgqa]] | **概念**: [[OntologyGuidedQueryGeneration]]

---

#### 4. OntoLogX — 网安日志本体 KG 提取

**arXiv**: [2510.01409](https://arxiv.org/abs/2510.01409) | **Venue**: — | **引用**: 0

**解决的问题**: 网络安全日志非结构化、语法异构、跨设备碎片化。传统 rule-based 解析（SLOGERT/KRYSTAL）依赖预定义规则，LogPrécis 需 fine-tune，CyKG-RAG 仍需 rule-based 步骤。缺乏在单一 LLM 框架内集成 retrieval+ontology+SHACL 校验的系统。

**方法与技术**: (1) 轻量级日志 ontology+SHACL schema（Event 核心类映射 prov:Entity）；(2) 混合检索（vector+full-text 归一化合并）；(3) MMR 重排序确保 few-shot 多样性；(4) 结构化输出+三阶段 SHACL 校验（语法/ontology 合规/语义一致，最多 3 轮迭代修正）；(5) Session 聚合+MITRE ATT&CK tactics 预测。

**创新点**: vs SLOGERT/KRYSTAL（rule-based）用 LLM 直接生成 KG；vs LogPrécis（fine-tune）用预训练 LLM+RAG；vs CyKG-RAG（仍需 rule-based）首次整合 retrieval+ontology+SHACL。

**效果**: F1 0.832（Claude Sonnet 4, Populated DB）vs Baseline 0.283（+194%）；Entity Linking 0.762 vs 0.278（+174%）；Retrieval 贡献最大（0.283→0.758→0.786）。
- Dataset: AIT-LDS | Metric: F1 | Result: 0.832 | Baseline: 0.283 | Δ: [+194%]

**Wiki**: [[ontologx-cybersecurity-kg]] | **概念**: [[OntologyGroundedRAG]]

---

#### 5. RAGulating Compliance — 合规多 Agent KG 问答

**arXiv**: [2508.09893](https://arxiv.org/abs/2508.09893) | **Venue**: — | **引用**: 0

**解决的问题**: 监管合规要求高精度可验证问答，LLM 存在 hallucination。传统 KG 依赖预定义 ontology，在法规快速演变场景下初始化开销大。缺乏在无需 ontology 前提下通过多智能体自动提取三元组并融合 RAG 的方案。

**方法与技术**: (1) Ontology-free 三元组提取+provenance 关联；(2) 三元组嵌入+统一向量数据库（BERT+eCFR 训练）；(3) 多智能体编排（KG 构建 agent+QA agent）；(4) Triplet-level kNN 检索+文本证据回溯；(5) 检索子图可视化。

**创新点**: Ontology-free/schema-light bottom-up（vs DBpedia/YAGO 预定义 ontology）；Triplet 级检索（vs 纯文本 RAG）；导航度量量化跨章节连通性。

**效果**: Section Overlap θ=0.75: 0.2888 vs 0.1684（+71.5%）；Average Degree 1.6080 vs 1.2939（+24.3%）；Avg Shortest Path 1.33 vs 2.02（-34% faster）。
- Dataset: eCFR | Metric: Section Overlap (θ=0.75) | Result: 0.2888 | Baseline: 0.1684 | Δ: [+71.5%]

**Wiki**: [[ragulating-compliance-kg]] | **概念**: [[AuditableStructuredRetrieval]]

---

#### 6. TransU — 密集本体 KGE

**arXiv**: [2504.02889](https://arxiv.org/abs/2504.02889) | **Venue**: — | **引用**: 0

**解决的问题**: 现有 KGE 方法将 property 和 entity 视为独立集，忽略 RDF 允许 property 作为节点出现的特性。同一 property 作为边和节点时表示不同向量，无法利用 ontology 中 property 间关系进行 link prediction。

**方法与技术**: (1) 统一实体集表示 E2⊂E1⊂E（property 是 entity 子集）；(2) 初始化阶段向量共享（property 作为 entity 时复用同一向量）；(3) 即插即用组合架构（与 TransE/TransH/ComplEx 组合）；(4) 评估阶段实体/属性区分。

**创新点**: vs TransE 统一 property-entity 表示；vs TransH/TransR 不改变学习算法仅施加初始化约束；vs ComplEx 证明 property 统一与复值建模互补。

**效果**: speckled string MeanRank 1.42（TransU+ComplEx）vs 1.47（ComplEx）（-3.4%）；FB15K 上略低于 baseline（缺乏丰富 property ontology）。
- Dataset: speckled string | Metric: MeanRank | Result: 1.42 | Baseline: 1.47 | Δ: [-3.4%]

**Wiki**: [[dense-ontology-kge]] | **概念**: [[OntologyGraphRetrieval]]

---

### B. 本体感知图/记忆引擎

---

#### 7. OaK — 动态本体作为 LLM Agent 内核

**arXiv**: [2608.22974](https://arxiv.org/abs/2608.22974) | **Venue**: — | **引用**: 0

**解决的问题**: LLM agent 行为可控性是核心挑战。Reflexion/MemP/AFlow 将 admissible concepts 隐含在 prompt 中，无法提供可检查的 semantic-procedural contract。GraphRAG/G-Retriever 将 graph 作为外部知识层但未指定 task-level 可复用计算。

**方法与技术**: (1) Ontology Kernel K=(S,F)——schema+typed functions 作为 agent 访问数据唯一通道；(2) Schema construction 三阶段（需求分析→起草→HermiT 形式化验证五类逻辑有效性）；(3) KG instantiation（chunk-map-merge 通过 primary key 等价类合并）；(4) Function composition（recurring reasoning steps 编译为 typed function）；(5) Judge-driven iterative refinement（修复 schema 和 function 本身）。

**创新点**: Ontology as operational kernel（vs descriptive ontology）；Automated schema+formal verification（vs manual expert ontology）；Judge-driven refinement of schema+functions（vs response-level 修正）。

**效果**: TravelPlanner Final Pass Rate 55.90% vs 15.30%（+265.4%）；CRMArenaPro B2B 78.38% vs 60.78%（+28.9%）；w/o Function Module 9.90%（-50.0% ablation）。
- Dataset: TravelPlanner (DeepSeek) | Metric: Final Pass Rate | Result: 55.90% | Baseline: 15.30% | Δ: [+265.4%]

**Wiki**: [[dynamic-ontology-llm-agents]] | **概念**: [[DynamicOntologyKernel]]

---

#### 8. MOOSEDev — 编码 Agent 本体接地项目记忆

**arXiv**: [2608.13662](https://arxiv.org/abs/2608.13662) | **Venue**: NeSy 2026 | **引用**: 0

**解决的问题**: Coding agent 产生大量变更后团队丧失"代码为何如此"的理解（comprehension debt）。Vector memory 能找相近词但无法区分记录类型（decision/constraint/rationale）、是否当前有效、记录间如何关联——这些区分本质上是 ontological 的。

**方法与技术**: (1) 双 ontology+SHACL shapes（SE 9 classes+SA 11 classes，51 properties）；(2) Typed records with lifecycle&supersession；(3) Neurosymbolic engine（LLM as unreliable sensor，symbolic 层 traversal/fusion/ranking）；(4) MCP 接口暴露四组工具；(5) Temporal commit-history bootstrap 恢复 supersession chains。

**创新点**: Coding agent memory as ontology problem（vs vector memory）；Supersession as first-class relationship（100% vs 8%）；Neurosymbolic with small models（8-32B）；Temporal bootstrap（vs flat graph）。

**效果**: Set completeness 1.00 vs 0.18（+455.6%）；Negation 0.98 vs 0.06（+1533%）；Supersession 100% vs 8%。
- Dataset: CodeGraph | Metric: Set completeness | Result: 1.00 | Baseline: 0.18 | Δ: [+455.6%]

**Wiki**: [[ontology-project-memory-coding]] | **概念**: [[DynamicOntologyKernel]]

---

#### 9. OwlPath — 无损知识压缩 LLM Bug Repair

**arXiv**: [2607.27249](https://arxiv.org/abs/2607.27249) | **Venue**: — | **引用**: 0

**解决的问题**: LLM SE agent 受限于 100K context window，传统检索（grep/BM25/embedding）将代码建模为 flat text，在 bug ground truth 与 issue 描述结构关联但无字符串重叠时失效。Graph-based 方法提供 1-hop 查询但缺少 transitive closure。

**方法与技术**: (1) Tree-sitter 代码图提取（SQLite nodes/edges）；(2) OWL2 ontology projection（bijection，每个 source tuple→一个 axiom，保证无损）；(3) Transitive-closure engine（SPARQL property paths，O(1) amortized）；(4) OWL-SKM 3KB advisory（module map+issue map）；(5) On-demand ReAct 集成。

**创新点**: OWL2 bijection projection（vs string-match/BM25）；SPARQL 传递闭包 O(1)（vs SQL recursive CTE O(n^k)）；3KB advisory（vs 全量上下文）；On-demand tool design（vs forced injection，+100% token 仅 +0.4pp）。

**效果**: Strict-apply 68.4% vs 66.7%（+1.7pp）；token -28.8%；time -39.5%；Recall 0.464 vs 0.226（+105.3%）；Structural recall 28.8% vs 4.4%（6.5×）。
- Dataset: SWE-bench Pro | Metric: Avg total tokens | Result: 1,416K | Baseline: 1,989K | Δ: [-28.8%]
- Dataset: SWE-bench Pro offline | Metric: Recall | Result: 0.464 | Baseline: 0.226 | Δ: [+105.3%]

**Wiki**: [[owlpath-bug-repair]] | **概念**: [[OntologyGraphRetrieval]]

---

#### 10. DeepRoot — KG 协调多智能体治疗推理

**arXiv**: [2606.15931](https://arxiv.org/abs/2606.15931) | **Venue**: ICML 2026 WS | **引用**: 0

**解决的问题**: 历史医学文献包含前本体论散文和非标准分类法，无法直接用于现代生物医学流水线。Tool-calling/RAG/agentic deep-research 都无法将这类文本大规模转化为可验证的药物发现线索。OpenTCM 依赖专家监督且未做消融。

**方法与技术**: (1) 七智能体 Assembly 流水线（Extractor/Auditor/3 Linkers/Mapper/Reviewer）；(2) Neo4j KG Schema（6 节点类型+7 边类型，机制环闭合验证）；(3) 实体身份坍缩（InChIKey/ChEMBL ID/ICD-10）；(4) Discovery 阶段 Cypher 遍历；(5) 盲恢复实验（删除 KNOWN_TREATS 边重新排序）。

**创新点**: Grounding 和 reasoning 作为可分离轴组合（Graph-only 幻觉 0%但 RC=2.69，DeepRoot KG+LLM 唯一两轴同时获胜）；Agent 式 KG 构建替代推理时 API 调用（幻觉 7% vs 87%）；自置信度受检索精度约束（0.48 vs 0.87）。

**效果**: R@20 47.6% vs 4.8%（+891%）；Hallucination rate 0.07 vs 0.87（-92%）；Overall score 3.83 vs 2.47（+55%）；KG: 21,111 nodes / 52,467 edges。
- Dataset: 神农本草经 | Metric: R@20 | Result: 47.6% | Baseline: 4.8% | Δ: [+891%]
- Dataset: 30 claims | Metric: Hallucination rate | Result: 0.07 | Baseline: 0.87 | Δ: [-92%]

**Wiki**: [[deeproot-kg-multi-agent]] | **概念**: [[OntologyGroundedRAG]]

---

### C. 本体引导查询构造

---

#### 11. CQ-Plans — Competency Questions 作为可执行计划

**arXiv**: [2604.02545](https://arxiv.org/abs/2604.02545) | **Venue**: ESWC 2026 | **引用**: 0

**解决的问题**: LLM 生成文化遗产叙事时容易幻觉。RAG 检索模糊文本块导致碎片化，KG 缺乏将高层用户意图转化为结构化可审计叙事计划的方法论。

**方法与技术**: (1) CQ 驱动 beat plan（有序 CQ 序列绑定 KG 实体参数，每个 CQ 关联参数化 SPARQL 模板，查询不由 LLM 运行时生成防止幻觉检索）；(2) 三种检索策略（KG-RAG/Hybrid-RAG/Graph-RAG）；(3) Evidence-closed 两步生成（content pass+surface pass，空证据包触发 beat 抑制）；(4) 句子-证据映射审计；(5) Live Aid KG（20,343 三元组，40 类，109 谓词）。

**创新点**: CQ 从设计时验证→运行时叙事驱动器（首次）；统一框架首次系统对比三种 KG-RAG（揭示三难困境）；Beat plan 可审计检索步骤。

**效果**: KG-RAG Support 76.21% vs Graph-RAG 32.64%（+134%）；Hybrid-RAG Coverage 92.17% vs Graph-RAG 14.72%（+526%）；Graph-RAG Global Cohesion 1.000 vs KG-RAG 0.482。
- Dataset: Live Aid KG | Metric: Support% | Result: 76.21% (KG-RAG) | Baseline: 32.64% (Graph-RAG) | Δ: [+134%]

**Wiki**: [[competency-questions-executable-rag]] | **概念**: [[OntologyGuidedQueryGeneration]]

---

#### 12. AgentMap — 联合等价与包含发现本体匹配

**arXiv**: [2607.27130](https://arxiv.org/abs/2607.27130) | **Venue**: — | **引用**: 0

**解决的问题**: 传统 OM 系统仅发现单一类型映射（equivalence 或 subsumption），实际知识集成中需同时考虑两种。BERTSub 假设正确 subsumer 在候选列表中，仅做被动排序。

**方法与技术**: (1) 双候选集语义检索（C0 top-5 供 LLM 推理，C+ top-20 供词法匹配）；(2) 三智能体等价优先流水线（AgentES→AgentEV→AgentSD）；(3) 层次引导迭代 subsumption 搜索（逐层向上遍历本体层次，d_max=2）；(4) 词法匹配+冲突解决；(5) HOM 基准数据集构建。

**创新点**: 首次提出 HOM 任务统一 equivalence+subsumption；分阶段多智能体推理替代单步 LLM 判断；本体结构引导迭代搜索（vs BERTSub 被动排序）。

**效果**: SNOMED-NCIT-Pharm subsumption 0.398 vs 0.046（+765%）；equivalence 0.981 vs 0.919（+6.7%）；w/o Hierarchical Search SubAcc -58.2%。
- Dataset: SNOMED-NCIT-Pharm | Metric: Acc_sub | Result: 0.398 | Baseline: 0.046 | Δ: [+765%]

**Wiki**: [[agentmap-ontology-matching]] | **概念**: [[HybridOntologyMatching]]

---

#### 13. OntoExtend — 需求驱动可扩展本体扩展

**arXiv**: [2607.17963](https://arxiv.org/abs/2607.17963) | **Venue**: Semantics 2026 | **引用**: 0

**解决的问题**: LLM-based ontology 生成主要关注从零构建，很少将扩展绑定到 requirements（CQs）。Phrase2Onto 仅限 toy ontologies；Taxoria 无法控制 hallucinated nodes；输入 ontology 超出 LLM 上下文窗口。

**方法与技术**: (1) Ontology Retriever（OWL 实体序列化+FAISS 索引+top-k 检索）；(2) Ontology Extender（Turtle snippets 注入 prompt+两阶段验证：Turtle parser+constraint checker）；(3) Ontology Integrator（去重拼接+重新索引）；(4) 多维评估（OOPS!+Pellet+CQ Verification+人工评估 6 位工程师）；(5) 数据集构造（系统性移除 classes 构造 CQs）。

**创新点**: vs Phrase2Onto 通过 RAG 处理大规模真实 ontology；vs Taxoria 支持完整 OWL+SHACL+两阶段验证；vs 先前工作 superfluous<2% vs 30%。

**效果**: CQ-verification 100%；Superfluous elements EU 2%/Industry 0% vs 先前 30%；Correctness 4.91/5（Fleiss Po 0.97）。
- Dataset: Industry | Metric: Correctness (1-5) | Result: 4.91 | Baseline: N/A
- Dataset: EU+Industry | Metric: Superfluous % | Result: 2% | Baseline: 30% | Δ: [-28%]

**Wiki**: [[ontoextend-ontology-extension]] | **概念**: [[OntologyGuidedQueryGeneration]]

---

### D. 构建验证+检索诊断

---

#### 14. Beyond Probabilistic Similarity — RAG 法律领域局限理论

**arXiv**: [2606.09724](https://arxiv.org/abs/2606.09724) | **Venue**: — | **引用**: 0

**解决的问题**: 法律 RAG 虽减少 citation fabrication 但转向更隐蔽失败：引用真实文档但 anachronistic/structurally incomplete/缺乏 institutional grounding。Graph RAG 的 structure 是 inferred 而非从 legal hierarchy 继承。

**方法与技术**: (1) 三重本体论承诺（Kelsen Stufenbau+Hart rules+Luhmann operational closure）；(2) 三种 pathology 诊断（mereological/diachronic/causal）；(3) 正式诊断规范（KG partOf/stateOf/transforms）；(4) 四个架构承诺 C1-C4（ontological primacy/event reification/bitemporal correctness/deterministic protocol）；(5) Pathology-organized critical review。

**创新点**: vs Graph RAG 提出 ontological primacy（structure 从 formally decreed hierarchy 继承）；vs temporal KG timestamped triples 提出 event reification；vs PROV-O/XAI 提出 deterministic interaction protocol。

**效果**: 理论驱动批判性综述，不含 benchmark 数据。具体数值待补充。

**Wiki**: [[beyond-probabilistic-rag-limitations]] | **概念**: [[LegalTemporalGraphRAG]]

---

#### 15. Retrieval-State Lock-In — RAG 检索状态锁定诊断

**arXiv**: [2606.22728](https://arxiv.org/abs/2606.22728) | **Venue**: — | **引用**: 0

**解决的问题**: Black-box uncertainty estimators 通过采样答案一致性判断 confidence，但当 retrieval 反复返回相同 defective state 时，答案一致是 error stable 而非正确。缺乏 name、measurable signature 和 prevalence bound。

**方法与技术**: (1) 三对象 confidence 分解 p(r,c,s|q)=p(s|q)·p(c|q,s)·p(r|q,c,s)；(2) SD-UQ（answer-state，question-conditioned embedding-dispersion+SVD）；(3) GPS（retrieval-state，Graph Path Support，答案实体可达性）；(4) SEU（evidence-state，NLI entailment-contradiction deficit）；(5) 合取审计规则（三检查全部通过才认证 low-risk）。

**创新点**: vs semantic entropy/SelfCheckGPT 三对象分解（answer-only ceiling 41-58%）；vs FRANQ/SURE-RAG GPS 首个 graph-side 诊断；vs BRINK operationalize absence lock-in+新增 presence lock-in。

**效果**: Silent error 42% KG / 59% dense / 84% strict；合取审计 precision 91.9% vs 69.7%（+22.2%）；RealMedQA 100%（48/48）；48/48 silent = empty-retrieval（absence lock-in）。
- Dataset: Pooled | Metric: Silent error rate | Result: 42% KG | Baseline: N/A
- Dataset: Pooled | Metric: Conjunctive precision | Result: 91.9% | Baseline: 69.7% | Δ: [+22.2%]

**Wiki**: [[retrieval-state-lock-in]] | **概念**: [[RetrievalStateLockIn]]

---

#### 16. OmniRetrieval — 异构知识源统一检索

**arXiv**: [2605.29250](https://arxiv.org/abs/2605.29250) | **Venue**: — | **引用**: 0

**解决的问题**: 现有检索器每次只操作一种知识源且使用固定查询语言。统一表示空间方法会抹去各源结构特性（schema/ontology/组合算子），导致 modality gap 和原生查询算子丢失。

**方法与技术**: (1) Long-Context Source Selection（所有源 structural descriptors 输入 LLM 返回 top-k）；(2) Per-Source Native Query Generation（SQL/SPARQL/Cypher/free-text 各自原生查询）；(3) Cross-Source Evidence Selection（异构输出 verbalize 为文本后 LLM 筛选）；(4) Registration-based 扩展机制。

**创新点**: 首个保留各源原生查询语言的统一检索框架（vs 统一 embedding/文本表示）；Long-context LLM 直接读取源描述符（vs embedding 排序）；Multi-candidate+deferred commitment（vs KB Routing 无 fallback）。

**效果**: Source Selection 65.71 vs 61.65（+6.6%）；Retrieval 44.34 vs 39.98（+10.9%）；LLM-as-Judge 65.88 vs 57.99（+13.6%）；Unified Rep vs OmniRetrieval: 68.58 vs 31.00（+121.2%）。
- Dataset: 13 datasets/309 KBs | Metric: LLM-as-a-Judge | Result: 65.88 | Baseline: 57.99 | Δ: [+13.6%]

**Wiki**: [[omni-retrieval-heterogeneous]] | **概念**: [[OntologyGuidedQueryGeneration]]

---

#### 17. Manufacturing Knowledge Access — 制造业 KG LLM 访问

**arXiv**: [2507.22619](https://arxiv.org/abs/2507.22619) | **Venue**: ECCAI 2026 | **引用**: 0

**解决的问题**: 制造业 KG（LIS KG 15+工厂/2700+产线/16000+机器）对非专家难以使用，需编写复杂 SPARQL。LLM 生成查询缺乏领域特异性且容易 hallucinate。先前工作缺乏对 context-aware content selection 的系统性探索。

**方法与技术**: (1) 四级 Content Selection（Entire/Naive Reduction/Context-based Reduction）；(2) 三种 Content Enrichment（Ontology-based/LLM-based/External）；(3) 三种 Representation（Graph/Table/Table-Sorted）；(4) 三种 Prompt Engineering（Simple/Generic Example/Domain-specific Example）；(5) Hallucination Accuracy 评估方法。

**创新点**: 系统性 OntA/B/C/D 四级框架（vs LangChain 忽略 inter-class 关系）；Table-Sorted 格式（vs LangChain 平铺）；制造业专门 benchmark（vs life science/scholarly domain）。

**效果**: Hallucination Accuracy 0.97（OntC+Pdomain+table）vs 0.47（OntA+Psimple）（+106.4%）；Correctness 3.14 vs 2.54（+23.6%）；context-aware reduction 准确率 +20-30%。
- Dataset: LIS (GPT3.5) | Metric: Hallucination Accuracy | Result: 0.97 | Baseline: 0.47 | Δ: [+106.4%]

**Wiki**: [[manufacturing-knowledge-llm]] | **概念**: [[OntologyGuidedQueryGeneration]]

---

#### 18. OntoSCPrompt — 本体引导混合提示 KGQA 泛化

**arXiv**: [2502.03992](https://arxiv.org/abs/2502.03992) | **Venue**: ICSC 2025 | **引用**: 0

**解决的问题**: KGQA 系统为特定 KG 定制，存在三类异构性（schema/topology/assertions），无法泛化到未见 KG。LLM 在知识密集型 KGQA 中存在 hallucination 和 factual inaccuracy。

**方法与技术**: (1) 两阶段框架（Stage-S 预测 KG 无关 SPARQL 结构含 6 占位符；Stage-C 用 KG 特定 elements 填充）；(2) Ontology-Guided Textual Prompts（ontology verbalization 转文本）；(3) Aspect-aware Continuous Prompts（4 个可学习向量 vQ/vG/vB/vE）；(4) Grammar-constrained Decoding；(5) Structure-guided+Subgraph Constrained Decoding。

**创新点**: 首次将 prompt tuning 应用于 KGQA 泛化；扩展 6 种占位符（vs 先前基本结构）；Ontology-guided hybrid prompt（离散+连续）；三种 task-specific 约束解码。

**效果**: LC-QuAD F1 79.1 vs 75.1（+5.3%）；WebQSP Hits@1 73.8 vs 70.6（+4.5%）；w/ constraints 79.1 vs w/o 70.2（+12.7% ablation）；跨 KG 泛化 DBLP-QuAD F1 84.6 vs 78.2（+8.2%）。
- Dataset: LC-QuAD 1.0 | Metric: F1 (%) | Result: 79.1 | Baseline: 75.1 | Δ: [+5.3%]
- Dataset: DBLP-QuAD | Metric: F1 (%) | Result: 84.6 | Baseline: 78.2 | Δ: [+8.2%]

**Wiki**: [[ontology-hybrid-prompt-kgqa]] | **概念**: [[OntologyGuidedQueryGeneration]]

---

## 新增趋势洞察

1. **本体从 descriptive 到 operational 的范式转换**（[[dynamic-ontology-llm-agents]] OaK +265%、[[ontology-project-memory-coding]] MOOSEDev supersession 100% vs 8%）：本体不再仅描述"域中存在什么"，而是作为 agent 访问数据的唯一通道——约束可调用概念（schema）和可执行计算（typed functions），使 agent 行为可检查、可审计。OaK 的 HermiT reasoner 形式化验证和 MOOSEDev 的 SHACL shapes 代表两种互补的操作化路径。

2. **构建验证 KG 比推理时查询更有效抑制幻觉**（[[deeproot-kg-multi-agent]] DeepRoot 幻觉率 7% vs Tool-call LLM 87%）：DeepRoot 的一次性 Assembly（$0.25/语料）构建验证 KG，而 Tool-call LLM 在推理时访问相同 API（ChEMBL/Open Targets/PubMed/MeSH）仍产生 87% 幻觉率。边扰动消融验证系统对图谱结构的真实依赖——50% 扰动时 Critic confidence 收敛至 raw LLM baseline。这表明"for corpora that predate modern ontologies, agents need a construction pass first, rather than on-demand calling"。

3. **检索状态锁定是 RAG 的隐蔽失败模式**（[[retrieval-state-lock-in]] silent error 42% KG-RAG / 59% dense）：42% KG-RAG 错误携带零 answer dispersion（silent errors），answer-only 方法（semantic entropy/SelfCheckGPT）structural ceiling 最多 recall 41-58% 错误。三对象 confidence 分解（answer/evidence/retrieval-state）+合取审计规则在 7.7% 覆盖率下达 91.9% precision。48/48 strict clinical silent errors 均为 empty-retrieval（absence lock-in），揭示 KG-RAG 在图谱不完整时回退到参数记忆的失败路径。

4. **法律正确性不是 semantic similarity 而是 validity grounding**（[[beyond-probabilistic-rag-limitations]] + [[ontology-driven-graph-rag-legal]]）：法律 RAG 的失败不是 LLM confabulation，而是 probabilistic retrieval 与法律知识的 hierarchical/temporal/institutional 结构的架构性不匹配。三种 pathology（mereological/diachronic/causal）需要四个架构承诺（ontological primacy/event reification/bitemporal correctness/deterministic protocol）解决。SAT-Graph RAG 的聚合式版本传播（Aggregation, 非 Composition）是 C1+C2 的工程实现——复用未变更组件 CTV 避免数据冗余。

5. **无损知识压缩是本体图检索的工程优势**（[[owlpath-bug-repair]] OwlPath token -28.8% + recall 2.06× + [[ontology-driven-graph-rag-legal]] 聚合版本传播）：OwlPath 的 OWL2 bijection 投影保证每个 source tuple 恰好产生一个 axiom——无结构信息丢失。SPARQL 传递闭包 O(1) amortized（vs SQL recursive CTE O(n^k)），3KB advisory 引导首次查询命中正确模块。On-demand 设计严格优于 forced injection（+100% token 仅 +0.4pp strict-apply）。

## 知识库状态

| 指标 | 上轮 | 本轮 | 变化 |
|---|---|---|---|
| 论文 | 294 | 312 | +18 |
| Source 页面 | 421 | 439 | +18 |
| Concept 页面 | 119 | 123 | +4 |
| PDF 文件 | 293 | 311 | +18 |
| 空文件 | 0 | 0 | ✅ |
| 索引同步 | 0 | 0 | ✅ |
