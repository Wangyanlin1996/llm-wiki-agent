# 本体推理 论文洞察日报 — 2026-10-09

**日期**: 2026-10-09
**累计论文**: 342 篇（本轮新增 15 篇）
**知识库页面**: 472 页

## 概览

| 方向 | 本轮新增 | 累计 | 代表趋势 |
|---|---|---|---|
| A. 推理引擎与规模化 | 5 | — | 引擎优化从算法复杂度转向冗余消除（seminaïve/通信避免/句法化简/电路编译） |
| B. LLM-推理器混合 | 6 | — | 推理器从"被替代"转向"验证 LLM 输出的法官" |
| C. 推理鲁棒性 | 4 | — | 不一致处理三方向（检测/修复/容忍）成熟，神经方法在符号失效处价值凸显 |
| **总计** | **15** | **342** | |

## 新增论文清单（速查表）

| # | 论文 | 年份 | Venue | arXiv | 引用 | 方向 |
|---|---|---|---|---|---|---|
| 1 | [Syntactic Simplification of OWL Class Expressions](https://arxiv.org/abs/2608.18899) | 2026 | arXiv | 2608.18899 | 0 | A |
| 2 | [Compiling DL Ontologies to Probabilistic Circuits](https://arxiv.org/abs/2601.14894) | 2026 | arXiv | 2601.14894 | 3 | A |
| 3 | [Seminaïve Materialisation in DatalogMTL](https://arxiv.org/abs/2208.07100) | 2022 | RuleML+RR | 2208.07100 | 1 | A |
| 4 | [MeTeoR: Practical Reasoning in Datalog with Metric Temporal Operators](https://arxiv.org/abs/2201.04596) | 2022 | AAAI | 2201.04596 | 41 | A |
| 5 | [Datalog with First-Class Facts](https://arxiv.org/abs/2411.14330) | 2024 | PVLDB | 2411.14330 | 3 | A |
| 6 | [Ontology-Grounded, Reasoner-Verified Benchmarks](https://arxiv.org/abs/2610.00682) | 2026 | NeurIPS WS | 2610.00682 | 0 | B |
| 7 | [Neural Reasoning for Robust Instance Retrieval in SHOIQ (Ebr)](https://arxiv.org/abs/2510.20457) | 2025 | K-CAP | 2510.20457 | 2 | B |
| 8 | [Neuro-symbolic Learning over OWL 2 DL (Baobab)](https://arxiv.org/abs/2608.17741) | 2026 | arXiv | 2608.17741 | 0 | B |
| 9 | [From Subsumption to Satisfiability: LLM-Assisted Active Learning](https://arxiv.org/abs/2604.16672) | 2026 | arXiv | 2604.16672 | 1 | B |
| 10 | [Transformer-based LMs for Reasoning in ALCQ (DELTAD)](https://arxiv.org/abs/2410.09613) | 2024 | arXiv | 2410.09613 | 1 | B |
| 11 | [Neuro-Symbolic RDF and DL Reasoners Survey](https://arxiv.org/abs/2308.04814) | 2023 | NeSy Compendium | 2308.04814 | 4 | B |
| 12 | [FALCON: Scalable Reasoning over Inconsistent ALC](https://arxiv.org/abs/2208.07628) | 2022 | arXiv | 2208.07628 | 5 | C |
| 13 | [Ontology Revision based on PLMs](https://arxiv.org/abs/2310.18378) | 2023 | arXiv | 2310.18378 | 1 | C |
| 14 | [Embedding-based Inconsistency-tolerant Reasoning](https://arxiv.org/abs/2304.01664) | 2023 | IJCKG | 2304.01664 | 2 | C |
| 15 | [ABox Abduction for Inconsistent KBs under Repair Semantics](https://arxiv.org/abs/2605.01341) | 2026 | KR | 2605.01341 | 2 | C |

## 新增论文结构化分析

### A. 本体推理引擎与规模化

---

#### 1. CES — OWL 类表达式的句法无损简化

**arXiv**: [2608.18899](https://arxiv.org/abs/2608.18899) | **Venue**: arXiv (Paderborn U) | **引用**: 0

**解决的问题**: 类表达式学习（CEL）常产出冗长复杂 OWL 表达式，降低可读性并拖慢推理；已有工作聚焦语义推理/模块化，系统性的句法简化几乎空白（FaCT++ SNF 是最近却有限的对照点）。CES 在无推理器依赖、无背景本体的前提下解决复杂度问题。

**方法与技术**: ① 基于 SOIQ(D) 的重写规则库——吸收律/幂等律/支配律/排中律/量词分配/基数子sumption/析因分解；② 递归 `simplify(c,p)` single-dispatch 单趟应用尽可能多的规则；③ `apply_factorization` 转顶层 DNF 后成对识别公共子表达式；④ 经验验证语义保持（原/简化表达式实例检索集合等价）。

**创新点**: 首个专门的 OWL 类表达式**句法**简化器；推理器无关（不依赖背景本体）；作为 CEL 的"bonus"后处理，语义零风险。

**效果**: 最高长度缩减 **86%**、最高 runtime 缩减 **90%**；平均简化 0.11s（Mutagenesis）/0.16s（Carcinogenesis），最长表达式（4284）1.34s。
- Dataset: SML-bench Carcinogenesis + Mutagenesis | Metric: 长度/推理runtime | Result: -86%/-90% | 基线: 原始 TDL 表达式 | Δ: 见上

**Wiki**: [[syntactic-simplification-owl]] | **概念**: [[OntologyReasoningEngine]]

---

#### 2. DL 本体编译为概率电路 — 数据生成+GPU推理+NeSy

**arXiv**: [2601.14894](https://arxiv.org/abs/2601.14894) | **Venue**: arXiv (U. Pisa/Bologna/Edinburgh) | **引用**: 3

**解决的问题**: 深度模型在领域特定场景预测可能与背景本体矛盾；数据稀缺时无法靠一致数据规避。现有 NeSy 方法张力：FOL 概率推理昂贵、fuzzy 需精心设计、命题逻辑表达力不足——DL 本体作为 NeSy 载体此前未开发。

**方法与技术**: ① 本体知识编译为概率电路（SDD 类，输入/和/积单元）；② C1 电路采样生成语义保真合成数据；③ C2 GPU 前馈批量演绎推理；④ C3 hard/soft 变体可微 NeSy 分类器（近似或可证明与本体一致）。

**创新点**: 首个 DL 本体→概率电路编译；单电路服务数据生成+GPU 推理+NeSy 训练三用途；相对嵌入法（EL Embeddings 丢蕴含）保留端到端经典语义；提供可证明一致预测。

**效果**: 电路编译路径比可用推理器**快最多 3 个数量级**（GPU）；NeSy 分类器保持/超越神经网络基线且显著降低本体违规预测。
- Dataset: Wikidata 音乐艺术家本体 | Metric: 推理runtime | Result: 3个数量级快 | 基线: 可用DL推理器 | Δ: -99.9%

**Wiki**: [[dl-ontologies-probabilistic-circuits]] | **概念**: [[OntologyReasoningEngine]]

---

#### 3. Seminaïve Materialisation in DatalogMTL — 消除物化冗余

**arXiv**: [2208.07100](https://arxiv.org/abs/2208.07100) | **Venue**: RuleML+RR 2022 | **引用**: 1

**解决的问题**: DatalogMTL 物化推理（MeTeoR 等）采用朴素策略，同一时序规则实例被反复应用、旧事实被反复重派生，冗余计算随物化轮次递增。半朴素策略在经典 Datalog 成熟，但 DatalogMTL 的度量原子/coalescing/区间交叠使提升非平凡。

**方法与技术**: ① 增量集合 Δ + 语义差集 D1⧸D2 追踪"真新事实"；② `instr[D···Δ]` 只应用涉及 Δ 中事实的相关规则实例（非重复性）；③ 每轮 coalescing 后把合并结果纳入 Δ；④ 优化版在非递归谓词物化完成/前向传播程序最晚时点判定后丢弃规则。

**创新点**: 首次将 seminaïve 求值提升到含度量时序算子的 DatalogMTL；forward-propagating 程序的时序感知规则丢弃（经典 Datalog 无对应物）；无缝嵌入 MeTeoR。

**效果**: 相对朴素策略在时间与内存显著更优且随物化推进差距扩大；常数数扩展下朴素近似线性增长、seminaïve 受影响很小。
- Dataset: LUBM 时序扩展 9 个 10M 事实数据集 | Metric: 物化时间/内存 | Result: 显著低于朴素 | 基线: 朴素物化 | Δ: 随轮次扩大

**Wiki**: [[datalogmtl-seminaive-materialisation]] | **概念**: [[OntologyReasoningEngine]]

---

#### 4. MeTeoR — 首个完整 DatalogMTL 实用推理器

**arXiv**: [2201.04596](https://arxiv.org/abs/2201.04596) | **Venue**: AAAI 2022 | **引用**: 41

**解决的问题**: DatalogMTL（Datalog+度量时序逻辑）因 ExpSpace 高复杂度长期无实用推理器，Brandt et al. 原型仅限非递归程序。直接物化不终止、自动机指数规模——需要两者的实用结合。

**方法与技术**: ① 数据集按左端点排序区间列表+复合键索引（coalescing/蕴含检查加速）；② 优化物化 ApplyRules（index nested loop join + sort-merge 时序连接）；③ 优化自动机（只对相关事实子集一致性检查+MTL 语义约束状态搜索）；④ 混合决策：相关规则集→预物化→两线程并行竞速（物化 best-effort vs 自动机）。

**创新点**: 首个支持任意（含递归）DatalogMTL 的推理器；物化-自动机混合工程范式；实证 99.2% 事实走物化路径（T1-T4），仅 0.8% 需自动机。

**效果**: 支持至 **1.5 亿时序事实**；LUBM 上全数据集一致胜出 Brandt 基线（D1 Π1: 160.3→51.3s）；气象全 62 年 3.97 亿事实 2234.0→1050.8s；时序连接压力测试基线快速退化、MeTeoR 稳定。
- Dataset: LUBM 时序 + 气象 3.97 亿事实 | Metric: 蕴含测试 runtime | Result: 全胜基线 | 基线: Brandt 2018 | Δ: 2-3x

**Wiki**: [[meteror-metric-temporal-reasoning]] | **概念**: [[OntologyReasoningEngine]]

---

#### 5. DL∃!/Slog — 一等事实的并行 Datalog

**arXiv**: [2411.14330](https://arxiv.org/abs/2411.14330) | **Venue**: PVLDB 18(3) 2024 | **引用**: 3

**解决的问题**: Datalog 的扁平原子常量限制树形数据处理。Datalog±/∃ 需 unify 实现复杂，Soufflé ADT 无法触发规则求值且索引支持差——需要表达力与实现简单性的平衡点。

**方法与技术**: ① 唯一存在量化（∃!）语义——每个事实以特有 Skolem 项标识，禁头体合一防循环、保证有限扩张；② 受控 chase 语义（事实结构唯一→免 unify，每子事实唯一 intern id）；③ DLS 语言编译到 DL∃!（直接嵌套事实语法）；④ Slog 基于 MPI 的通信避免大规模并行。

**创新点**: 相对 Datalog∃（一般存在量化需 unify）——∃! 换来实现简单性+平凡并行；相对 Soufflé ADT——一等事实参与规则求值且支持高效索引；首个通信避免的树形事实 Datalog 并行实现。

**效果**: 多样基准上 Slog 超越 Nemo、Vlog、RDFox、Soufflé；可扩展到数千线程；支持 provenance/ADT/函数式编程/结构抽象解释/类型系统多应用。
- Dataset: 多样 Datalog 基准 | Metric: 推理吞吐 | Result: 超越4大系统 | 基线: Nemo/Vlog/RDFox/Soufflé | Δ: 见论文

**Wiki**: [[datalog-first-class-facts]] | **概念**: [[OntologyReasoningEngine]]

### B. LLM 与推理器混合

---

#### 6. 本体接地+推理器验证的 LLM 推理基准

**arXiv**: [2610.00682](https://arxiv.org/abs/2610.00682) | **Venue**: NeurIPS 2026 WS | **引用**: 0

**解决的问题**: 科学 AI 中 LLM 逻辑推理不可靠，但可靠评测缺失——手动构建无法扩展、LLM 生成嵌入缺陷。现有基准（OntoLAMA/LLM-ORBench/OntoURL/MALLS/FOLIO）至少缺"本体接地/双验证/自动扩展"之一。

**方法与技术**: ① 四阶段流水线（公理提取扰动→言语化平滑→distractor 排序→MCQ 组装）；② 正确答案由 class definition axioms 设计上锚定；③ distractor 错误性经 OWL 推理器蕴含检查形式化验证；④ 四类语义 distractor（类不可满足/基数矛盾/子填充/弱化子sumption）；⑤ 双形式输出（NL+符号）。

**创新点**: 首个同时满足三要求且 distractor 语义类型明确的 MCQ 流水线；相对 OntoURL（命名类作 distractor→实体回忆）强制逻辑推理；负样本也经推理器验证。

**效果**: Pizza/PMDco/DOID 生成 **112/2,491/15,216** MCQ；LLM judge 评分 4.02/4.36/3.36（5分）；正确答案-干扰项相似度>0.8；6 LLM 零样本 **41.1-76.8%** vs 25% 随机。
- Dataset: Pizza + PMDco + DOID | Metric: LLM 准确率 | Result: 41.1-76.8% | Baseline: 25% 随机 | Δ: +16.1pp起

**Wiki**: [[ontology-grounded-reasoner-benchmarks]] | **概念**: [[LLMReasonerHybrid]]

---

#### 7. Ebr — 嵌入鲁棒推理器（SHOIQ 全构造子）

**arXiv**: [2510.20457](https://arxiv.org/abs/2510.20457) | **Venue**: K-CAP 2025 | **引用**: 2

**解决的问题**: 概念学习依赖符号推理器实例检索，但真实知识库常不一致/不完整：不一致时符号推理器停机或无条件蕴含一切，不完整时无法推断缺失断言。需要古典方法失效处的数据驱动替代。

**方法与技术**: ① KB→三元组映射（rdf:type/subClassOf/subPropertyOf）；② KGE 训练+sigmoid 阈值化神经链接预测器（噪声断言可判假）；③ SHOIQ 构造子映射为嵌入空间集合运算（⊓→∩、∃r.C→{x|∃y...}、≥n s.C→计数阈值）；④ 三任务评测（实例检索 Jaccard/噪声不完整鲁棒性/概念学习 F1）。

**创新点**: 首次将 KGE 嵌入语义扩展到表达性 SHOIQ 全构造子；相对符号推理器在噪声下继续运作（Pellet 失效处 F1 1.00）；阈值 γ 变化影响可忽略（免微调）。

**效果**: 完整一致数据 ComplEx d=128 起所有构造子 **Jaccard 1.00**；Carcinogenesis 合取 0.37(d=32)→0.99(d=64)→1.00(d=128)；噪声下概念学习 Carcinogenesis 10% 不一致 F1=1.00（Pellet *）；Vicodi 检索 Ebr 78.1s vs HermiT 300.2s。
- Dataset: Carcinogenesis/Mutagenesis/Vicodi 等6套 | Metric: Jaccard/F1 | Result: 1.00 | Baseline: Pellet/HermiT/FIC | Δ: Pellet 失效

**Wiki**: [[neural-shqoi-instance-retrieval]] | **概念**: [[LLMReasonerHybrid]]

---

#### 8. Baobab — 非 Horn SROIQ 编译为可微电路

**arXiv**: [2608.17741](https://arxiv.org/abs/2608.17741) | **Venue**: arXiv (KAUST) | **引用**: 0

**解决的问题**: 嵌入法（EL Embeddings/OWL2Vec*）丢经典蕴含；知识编译法（DeepProbLog/Semantic Loss）仅限命题/Datalog。SROIQ 的析取/否定/限定基数/nominals/角色公理族超出 Horn 饱和演算。且多一致补全下独立感知"推理捷径"问题在非 Horn DL 未被刻画。

**方法与技术**: ① SROIQ→SDD 编译（ALCHOQ 命题核心后果演算饱和 + SROIQ 扩展有限域 grounding）；② 证据条件 WMC 可微训练感知网络（MNIST 数字+后继关系耦合）；③ JustWMC 混合——以查询 justification 索引的混合分布表示校准后验，电路枚举补全作种子；④ Lean 4 机器验证 soundness。

**创新点**: 首个支持非 Horn（SROIQ 全特征）的知识编译型 NeSy 学习器（**23% 公理超出 DeepProbLog Horn 片段**）；首个在非 Horn DL 刻画并缓解推理捷径；端到端保留经典语义。

**效果**: 部分 ABox 监督下感知恢复潜在概念（digit identity **0.25→0.99**），本体违反驱动到 0；真实图像 MNIST 任务 JustWMC 达贝叶斯最优校准后验（单 WMC/BEARS 不能）；ResNet 经 Pizzaiolo 恢复潜在披萨类。
- Dataset: MNIST+后继关系本体 / Pizzaiolo | Metric: 潜在概念准确率 | Result: 0.25→0.99 | Baseline: 独立感知(随机) | Δ: +74pp

**Wiki**: [[owl2dl-differentiable-circuits]] | **概念**: [[LLMReasonerHybrid]]

---

#### 9. LLM 辅助本体主动学习 — 仅 II 类错误保证

**arXiv**: [2604.16672](https://arxiv.org/abs/2604.16672) | **Venue**: arXiv (Glasgow) | **引用**: 1

**解决的问题**: 本体工程依赖专家教师成本高；LLM 直接替代教师会因幻觉引入错误。核心矛盾：如何利用 LLM 常识辅助建模同时不污染本体逻辑后果。

**方法与技术**: ① 子sumption→可满足性归约（候选公理→反概念 C⊓¬D）；② CNL 受控自然语言言语化反概念；③ LLM 用真实世界例子近似反概念实例（辅助指导，专家交互不变）；④ OWA 下混淆矩阵误差分析——证明只产生 II 类错误；⑤ recall 度量评测。

**创新点**: 首次将"子sumption→可满足性"归约引入 LLM 辅助建模；形式化保证仅 II 类错误（最坏延迟构建、绝不引入错误公理）；13 个商用 LLM 系统评测。

**效果**: 13 个商用 LLM 上 recall 保持稳定；OWA 下证明只产生 II 类错误、不引入不一致公理；成熟本体（生物医学/能源/交通）与新兴本体均适用。
- Dataset: 多成熟本体 + 新兴本体 | Metric: recall (II类错误) | Result: 稳定 | Baseline: 无（仅II类错误保证） | Δ: 无污染

**Wiki**: [[llm-active-learning-owl]] | **概念**: [[LLMReasonerHybrid]]

---

#### 10. DELTAD — 表达性 ALCQ 的 transformer 推理基准

**arXiv**: [2410.09613](https://arxiv.org/abs/2410.09613) | **Venue**: arXiv (Boston U/ATC/NKUA) | **引用**: 1

**解决的问题**: TLM 逻辑推理评测长期基于短 FOL 片段（少量算子/量词），无法评估表达性推理。需回答：TLM 能否在表达性 DL（ALCQ）推理？推理深度/语言复杂度是否影响性能？

**方法与技术**: ① ALCQ 形式化（∃/∀/≥n/≤n/布尔）；② DELTAD 384K 样例沿推理深度+语言复杂度双维度受控扩展；③ True/False/Unknown 三分蕴含检查；④ DeBERTa 微调 vs GPT-3.5/GPT-4 9-shot 评测；⑤ 分维度报告定位退化点。

**创新点**: 首个表达性 ALCQ 规模化（384K）NL DL 推理基准；双维度受控分离"逻辑难度 vs 语言难度"；证明小模型可在表达性 DL 蕴含检查达标。

**效果**: 384K 样例；DeBERTa 微调掌握蕴含检查任务；GPT 9-shot 显著提升；性能随推理深度与语言复杂度变化（高语言复杂度更具挑战）。
- Dataset: DELTAD 384K | Metric: 蕴含检查准确率 | Result: DeBERTa达标 | Baseline: GPT-3.5/4 zero-shot | Δ: 9-shot显著提升

**Wiki**: [[transformer-alcq-reasoning]] | **概念**: [[LLMReasonerHybrid]]

---

#### 11. 神经符号 DL 推理器综述（坐标综述）

**arXiv**: [2308.04814](https://arxiv.org/abs/2308.04814) | **Venue**: NeSy Compendium 2023 | **引用**: 4

**解决的问题**: 本体越大越表达性（SROIQ），传统推理器扩展性差；自动构建的噪声不一致本体传统推理器无法处理。神经符号演绎推理技术此前缺乏统一梳理与边界划定。

**方法与技术**: ① 传统推理器优化分类（预处理/模型构造/推理任务相关）；② 按推理语言（RDF(S)/EL/ALC/OWL 2 RL）组织神经符号演绎推理技术；③ 任务-技术概览表；④ 互补工作（推理器评测挑战赛+本体基准）；⑤ 明确排除 KGC/本体学习/断言预测。

**创新点**: 首个系统梳理神经符号**演绎推理**（非 KGC/补全）综述；按语言粒度给出"表达力 vs 神经符号支持度"全景；标注 SROIQ 等表达性 DL 神经符号支持空白，为 Ebr/Baobab/FALCON 提供定位坐标系。

**效果**: 覆盖 RDF(S)/EL/ALC/OWL 2 RL；识别表达性 DL 神经符号支持空白；框架性结论：传统推理器在大/表达性/不一致本体上的双重失效是神经方法动机。
- Dataset: 无（综述） | Metric: 技术覆盖谱系 | Result: RDF(S)/EL/ALC/OWL2RL | Baseline: N/A | Δ: 识别SROIQ空白

**Wiki**: [[neuro-symbolic-dl-reasoners-survey]] | **概念**: [[LLMReasonerHybrid]]

### C. 本体推理鲁棒性

---

#### 12. FALCON — 模糊 ALC 神经推理器

**arXiv**: [2208.07628](https://arxiv.org/abs/2208.07628) | **Venue**: arXiv (KAUST/Toronto/Delft) | **引用**: 5

**解决的问题**: ALC 本体（尤其生物医学）大而人工作造，不一致/不完整致经典推理器失效：矛盾使一切蕴含、小矛盾瘫痪整本体；ALC 推理 EXPTIME 完备计算不可行。LTN 在多元谓词+常量多时扩展差。

**方法与技术**: ① 任意隶属函数泛化（非限定几何）；② 模糊逻辑算子表达复杂概念描述；③ 多近似模型采样近似蕴含（理论：模型越多越忠实）；④ 开放世界假设推理；⑤ 生物医学知识库补全应用。

**创新点**: 首个完整 ALC 表达力的模糊神经推理器；多模型采样为不一致本体提供"近似蕴含"语义；理论保证 representation completeness + faithfulness → 逼近语义蕴含；解决 LTN 扩展性问题。

**效果**: 不一致本体上近似蕴含可用（经典推理器无条件蕴含一切）；大型本体显著更快；Yeast 蛋白相互作用预测 AUC/AUPR 提升。
- Dataset: Yeast benchmark | Metric: AUC/AUPR | Result: 优于BoxEL等 | Baseline: BoxEL/嵌入方法 | Δ: 见论文

**Wiki**: [[falcon-inconsistent-alc]] | **概念**: [[InconsistencyTolerantReasoning]]

---

#### 13. PLM 驱动的本体修订

**arXiv**: [2310.18378](https://arxiv.org/abs/2310.18378) | **Venue**: arXiv (NJUPT/CACM/Southeast U) | **引用**: 1

**解决的问题**: 本体修订要无缝并入新本体，但**不协调（不可满足概念）是致不一致的主因**。已有修订方法定义算子与排序策略但很少利用公理语义——公理被等权对待。

**方法与技术**: ① 公理翻译 NL 句子→PLM 稠密向量→Cosine 相似度；② 四个评分函数（如 reliableOnt_cos）编码公理可靠性差异；③ 一次处理所有不可满足概念的修订算法；④ 逐组处理适配算法提效；⑤ 19 对本本体评测。

**创新点**: 首次系统研究 PLM 应用于本体修订（公理语义驱动排序）；四评分函数显式编码公理语义差异；适配算法实现质量-效率权衡。

**效果**: 19 对本本体上适配算法最多省 **~90%** 时间；reliableOnt_cos 在困难对（OM8）显著更优；提供按语义与性能选算法的指南。
- Dataset: 19 对本本体 | Metric: 修订质量/时间 | Result: 优于现有算子 | Baseline: 已有修订算法 | Δ: 时间-90%

**Wiki**: [[ontology-revision-plm]] | **概念**: [[InconsistencyTolerantReasoning]]

---

#### 14. 嵌入语义的 MCS 不一致容忍推理

**arXiv**: [2304.01664](https://arxiv.org/abs/2304.01664) | **Venue**: IJCKG 2023 | **引用**: 2

**解决的问题**: 用不一致本体推理得无意义答案，自然应对是选最大一致子集（MCS），但已有 MCS 选择很少考虑公理语义致推理弱、质量差；怀疑式/基数 MCS 把公理等权对待；通用单调选择关系限于命题逻辑。

**方法与技术**: ① 句嵌入（BERT 类）编码公理 NL 语义；② KGE（TransE 类）编码本体结构语义；③ 基于语义相似度的 MCS 可靠性排序选择；④ 由所选 MCS 定义不一致容忍推理关系；⑤ 考察逻辑性质证明合理性。

**创新点**: 首次将公理语义嵌入引入 MCS 选择；两种互补编码（语言 vs 结构语义）；推理关系具备可考察逻辑性质。

**效果**: 多个本体（含 OpenCyc 案例）上优于怀疑式推理/基数 MCS 推理等基线；句嵌入+KGE 均有效、互补。
- Dataset: OpenCyc 等多不一致本体 | Metric: 推理合理性 | Result: 优于MCS基线 | Baseline: 怀疑式/基数MCS | Δ: 见论文

**Wiki**: [[embedding-inconsistency-tolerant]] | **概念**: [[InconsistencyTolerantReasoning]]

---

#### 15. 知识图谱不一致推理综述

**arXiv**: [2502.19023](https://arxiv.org/abs/2502.19023) | **Venue**: arXiv (NCSR Demokritos) | **引用**: 2

**解决的问题**: KG 由（半）自动抽取/异构集成构建致不一致，阻碍推理（IR/QA/新知识推导）。已有综述各偏一面，缺专门面向不一致 KG 推理的统合视角，尤其 ABox（大规模易错）侧。

**方法与技术**: ① 一致性检测（大型 KG 上定位矛盾 TBox/ABox）；② 修复（ABox 为重点，改动不一致部分恢复一致）；③ 不一致容忍推理（paraconsistent/Bienvenu 谱系）；④ 跨领域整合（Semantic Web/数据质量/查询回答）；⑤ 开放挑战识别。

**创新点**: 首次以检测/修复/容忍三方向统合不一致 KG 推理综述；把重心放 ABox 修复（区别于 Lambrix TBox 综述）；为"修复 vs 容忍"提供选择框架。

**效果**: 覆盖三方向（含 DL 族 SROIQ/ALC/EL 不一致语义）；跨领域方法归类；边界与 KG 补全/错误检测/质量管理综述清晰界定；识别大规模定位/信息保留权衡/语义选择持久挑战。
- Dataset: 无（综述） | Metric: 三方向框架 | Result: 检测/修复/容忍 | Baseline: N/A | Δ: ABox修复重心

**Wiki**: [[inconsistency-kg-reasoning-survey]] | **概念**: [[InconsistencyTolerantReasoning]]

---

#### 16. 修复语义下的 ABox 溯因（KR 2026）

**arXiv**: [2605.01341](https://arxiv.org/abs/2605.01341) | **Venue**: KR 2026 | **引用**: 2

**解决的问题**: ABox 溯因（找假设 H 使 ⟨T,A∪H⟩|=Φ）在一致 KB 上成熟，但真实数据含错误致不一致——经典语义下一切蕴含、溯因失去意义。修复语义（基于 ABox 最大一致子集）可恢复推理，但其溯因此前只有 Du et al. 针对 IAR 的实用系统。

**方法与技术**: ① 修复语义（Brave/AR）下定义溯因；② 有用性准则——conflict-confining/非平凡/最小化（≤-min/⊆-min 变体）；③ DL-Lite 与 EL⊥ 存在/验证问题复杂度分析；④ 医学病例演示 Brave vs AR 假设差异；⑤ 与 IAR/paraconsistent 对照。

**创新点**: 首个系统刻画修复语义下 ABox 溯因复杂度全景（DL-Lite/EL⊥ × Brave/AR × 存在/验证 × 签名约束）；定义冲突受限等修复语义特有标准；揭示修复语义下非平凡条件不再平凡的经典理论新结果。

**效果**: DL-Lite（Brave 存在性 NL 级至更复杂）/EL⊥ 各变体复杂度完整刻画；Brave 下 {OverdosedInsulin}/{Ketoacidosis} 均成立、AR 下仅 {Ketoacidosis}（谨慎医生应先查）。
- Dataset: 糖尿病医学本体病例 | Metric: 复杂度/假设集 | Result: NL-NP全景 | Baseline: 经典溯因 | Δ: AR语义更谨慎

**Wiki**: [[abox-abduction-repair-semantics]] | **概念**: [[InconsistencyTolerantReasoning]]

## 新增趋势洞察

1. **推理器从"被替代"到"被依赖"**：神经符号融合的成熟标志是推理器成为验证 LLM 输出的法官——[[ontology-grounded-reasoner-benchmarks]] 用蕴含检查形式化验证 15,216 个 distractor 的错误性（LLM 41.1-76.8% vs 25% 随机），[[owl2dl-differentiable-circuits]] 用 Lean 4 机器证明编译器 soundness。确定性不再让位于鲁棒性，而是两者分层共存，呼应 [[VerificationCoEvolution]]。

2. **冗余消除是引擎优化的统一杠杆**：三条独立引擎线指向同一主题——[[datalogmtl-seminaive-materialisation]] 保证"每个规则实例至多考虑一次"（时间/内存显著低于朴素）、[[datalog-first-class-facts]] 用通信避免 MPI 并行超越 Nemo/Vlog/RDFox/Soufflé、[[syntactic-simplification-owl]] 句法化简使最长表达式推理 runtime -90%。与 [[ContextOptimization]] 的缓存复用共享"消除重复计算"原则。

3. **不一致处理三方向各有适用域**：[[inconsistency-kg-reasoning-survey]]（Round 10 已收录）的检测-修复-容忍框架下，容忍路线（[[embedding-inconsistency-tolerant]] MCS 语义排序、[[falcon-inconsistent-alc]] 多模型近似蕴含、[[neural-shqoi-instance-retrieval]] 嵌入推理 F1 1.00）保留信息但失经典保证，修复路线（[[ontology-revision-plm]] 修订省 90% 时间、[[abox-abduction-repair-semantics]] 溯因建议）恢复一致性但可能删信息——按不一致范围与信息价值选择。

4. **非 Horn 全特征是可微编译的前沿**：[[owl2dl-differentiable-circuits]] 揭示 23% 的 SROIQ 公理超出 DeepProbLog Horn 片段，用"后果演算饱和命题核心+有限域实例化扩展"打通，并在多一致补全场景用 JustWMC 达贝叶斯最优（0.25→0.99）——表达力与可微性不再二选一，与 [[dl-ontologies-probabilistic-circuits]] 的电路编译（GPU 快 3 数量级）构成同一范式。

5. **时序推理进入生产级**：[[meteror-metric-temporal-reasoning]]（AAAI 2022, 41 citations）支持 1.5 亿时序事实、99.2% 事实走物化路径，为电信告警/网络流异常检测等 [[IntentDrivenMnS]] 场景的闭环提供时序推理底座——与 5G 自智网络的闭环可解释性框架呼应。

## 知识库状态

| 指标 | 上轮 | 本轮 | 变化 |
|---|---|---|---|
| 论文 | 327 | 342 | +15 |
| Source 页面 | — | — | +15 |
| Concept 页面 | 126 | 129 | +3 |
| PDF 文件 | 326 | 341 | +15 |
| 空文件 | 0 | 0 | ✅ |
| 索引同步 | 0 | 0 | ✅ |

> 注：inconsistency-kg-reasoning-survey (2502.19023) 已在 Round 10 收录，本轮仅深化引用，不计入新增。
