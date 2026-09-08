# 本体辅助技能路由/精准推理/循环检测 论文洞察日报 — 2026-09-08

**日期**: 2026-09-08
**累计论文**: 327 篇（本轮新增 15 篇）
**知识库页面**: 454 页

## 概览

| 方向 | 本轮新增 | 累计 | 代表趋势 |
|---|---|---|---|
| A. 本体辅助多级 skill 路由 | 5 | — | Task Ontology+Skill Ontology+WSA分解 |
| B. 本体精准推理（偏检索向） | 5 | — | 约束满足检索+inverse calibration |
| C. Agent loop 循环检测与消解 | 5 | — | 轨迹验证+确定性控制+harness修复 |
| **总计** | **15** | **327** | |

## 新增论文清单（速查表）

| # | 论文 | 年份 | Venue | arXiv | 方向 |
|---|---|---|---|---|---|
| 1 | [SCX Router](https://arxiv.org/abs/2609.02292) | 2026 | — | 2609.02292 | A |
| 2 | [Domain-Grounded Tool](https://arxiv.org/abs/2608.30696) | 2026 | — | 2608.30696 | A |
| 3 | [SkillNet](https://arxiv.org/abs/2603.04448) | 2026 | — | 2603.04448 | A |
| 4 | [Generative Ontology](https://arxiv.org/abs/2602.05636) | 2026 | — | 2602.05636 | A |
| 5 | [Workflow-to-Skill](https://arxiv.org/abs/2606.06893) | 2026 | — | 2606.06893 | A |
| 6 | [SatIR](https://arxiv.org/abs/2604.08849) | 2026 | COLM 2026 | 2604.08849 | B |
| 7 | [DeepRAG](https://arxiv.org/abs/2506.00671) | 2025 | IJCAI 2025 | 2506.00671 | B |
| 8 | [RAGged Events](https://arxiv.org/abs/2506.07042) | 2025 | — | 2506.07042 | B |
| 9 | [RIGOR](https://arxiv.org/abs/2506.01232) | 2025 | ISWC 2026 | 2506.01232 | B |
| 10 | [RareDxR1](https://arxiv.org/abs/2607.00147) | 2026 | IEEE ICME | 2607.00147 | B |
| 11 | [TROVE](https://arxiv.org/abs/2609.05019) | 2026 | — | 2609.05019 | C |
| 12 | [Gubernaut](https://arxiv.org/abs/2607.24339) | 2026 | — | 2607.24339 | C |
| 13 | [Argus](https://arxiv.org/abs/2608.05144) | 2026 | — | 2608.05144 | C |
| 14 | [MASC](https://arxiv.org/abs/2510.14319) | 2026 | — | 2510.14319 | C |
| 15 | [HARNESSFIX](https://arxiv.org/abs/2606.06324) | 2026 | — | 2606.06324 | C |

## 新增论文结构化分析

### A. 本体辅助多级 skill 路由

#### 1. SCX Router — Task Ontology 驱动零样本模型选择
**arXiv**: [2609.02292](https://arxiv.org/abs/2609.02292) | **引用**: 0

**解决的问题**: 推理 endpoint 在质量/价格/延迟/领域上高度异构，RouteLLM 固定 binary gate，FrugalGPT cascade 带来 decoding 延迟，均无法在会话内复用对话状态反复路由。

**方法与技术**: (1) 0.6B GLiClass 架构 Qwen3 causal decoder + DeBERTa-v2 bidirectional scorer；(2) Decoder-KV 持久/瞬态分离（对话走持久 cache，label 走 transient suffix）；(3) Task Ontology 三层 23/115/345；(4) Multi-label 训练 + label shuffling；(5) Cache-aware 部署策略。

**创新点**: Multi-label 动态标签 vs fixed binary gate；Decoder-KV 持久会话缓存 vs embedding 重嵌入；routing 监督分离为多独立预测头。

**效果**: Macro F1 0.7586；Top-1 score 0.707 vs 0.696 (+1.7%)；Difficulty Top-1/2/3: 0.507/0.748/0.873。Ablation: k=3 时 router 反而劣于 fixed（优势依赖候选间有意义分歧）。
- Dataset: LiveBench | Metric: Top-1 | Result: 0.707 | Baseline: 0.696 | Δ: [+1.7%]

**Wiki**: [[scx-router-task-ontology]] | **概念**: [[OntologySkillRouting]]

---

#### 2. Domain-Grounded Tool Orchestration — 领域本体约束科学分析
**arXiv**: [2608.30696](https://arxiv.org/abs/2608.30696) | **引用**: 0

**解决的问题**: LLM 辅助科学可视化生成脚本隐式编码领域知识且常常错误，产生"能执行但结果错误"的代码——最危险的失败模式。现有系统缺领域 ontology 约束规划且不返回结构化结果。

**方法与技术**: (1) Plan-Execute-Interpret 闭环；(2) 五字段 domain ontology schema（phenomenon/indicators/tools/follow-ups/significance）；(3) 两层 MCP 工具+动态字段解析；(4) 安全 pipeline 管理；(5) Client-server + in-situ 控制。

**创新点**: 结构化返回驱动闭环 vs 一次性脚本；Domain ontology 约束规划到物理合法链；按构造消除整类失败（API hallucination + module error）；跨领域同栈复用（新增 TTK 仅 60 行 JSON + 400 行 Python）。

**效果**: Accuracy 0.91 (with ontology) vs 0.41 (unaided) (+122%)。Ablation null result: tool selection 不变（选择已可靠），ontology 价值在解读。
- Dataset: 34-case | Metric: Accuracy | Result: 0.91 | Baseline: 0.41 | Δ: [+122%]

**Wiki**: [[domain-grounded-tool-orchestration]] | **概念**: [[OntologySkillRouting]]

---

#### 3. SkillNet — 创建、评估与连接 AI 技能
**arXiv**: [2603.04448](https://arxiv.org/abs/2603.04448) | **引用**: 0

**解决的问题**: Agent 长期进步受制于缺乏系统化 skill 积累与迁移——反复"reinvent the wheel"。现有仓库（ClawHub/SkillsMP/SkillHub）无自动创建、无多维评估、无关系分析。

**方法与技术**: (1) 多源自动 skill 创建（轨迹/GitHub/文档/NL）；(2) 三层 Skill Ontology（taxonomy+relation graph+package library）；(3) 五维 LLM 评估（Safety/Completeness/Executability/Maintainability/Cost）；(4) SkillNet-Gym 动态基准；(5) SkillNet-Fabric 路由层。

**创新点**: 全生命周期基础设施 vs 单点仓库；场景介导有向 skill 图构建（pre/post-scenario + Louvain 聚类）；五维评估 MAE<0.03 QWK≈1.000。

**效果**: ALFWorld reward 60→91.43 (+52.4%)；WebShop 31.66→53.02 (+67.5%)；avg reward +40%, steps -30%。
- Dataset: ALFWorld | Metric: Reward | Result: 91.43 | Baseline: 60.00 | Δ: [+52.4%]

**Wiki**: [[skillnet-ai-skills]] | **概念**: [[OntologySkillRouting]]

---

#### 4. Generative Ontology — 当结构化知识学会创造
**arXiv**: [2602.05636](https://arxiv.org/abs/2602.05636) | **引用**: 0

**解决的问题**: 结构性幻觉——LLM 生成"听起来合理但无法游玩"的游戏设计，机制没有对应组件、目标没有结束条件。传统 ontology 精确但被动，LLM 创造力丰富但无结构约束。

**方法与技术**: (1) Executable Schema（Pydantic BaseModel + enum 约束）；(2) DSPy Signature 操作化；(3) Anxiety-Driven 多 Agent 流水线（5 个 agent 各带"职业焦虑"）；(4) 两阶段 RAG（ontology filtering + embedding ranking）；(5) Validation Contract。

**创新点**: Ontology 作为生成语法（vs DRAGON-AI/OLLM 用 LLM 生成 ontology，方向相反）；Constraint Paradox 实证发现（约束单独不提升创造，约束+架构特化才提升）；Anxiety-Driven Agent 设计；ICC 信度验证。

**效果**: Consistency Errors 5.03→0.10 (d=4.78)；Strategic Depth d=1.59；Fun d=1.12。Published benchmark: Tension parity (d=0.35, ns)。
- Dataset: GameGrammar | Metric: Errors | Result: 0.10 | Baseline: 5.03 | Δ: d=4.78

**Wiki**: [[generative-ontology]] | **概念**: [[OntologySkillRouting]]

---

#### 5. Workflow-to-Skill — WSA 分解技能创建
**arXiv**: [2606.06893](https://arxiv.org/abs/2606.06893) | **引用**: 0

**解决的问题**: Skill 主要靠手工编写。现有 trace-grounded skill induction 将轨迹压缩为自由文本摘要，丢失运行时结构——激活条件、分支 criteria、retry/fallback 规则、验证检查、终止条件。

**方法与技术**: (1) Skill-IR 的 WSA 分解（R+W+S+A，8 种类型 T0-T7）；(2) 证据驱动 WSA 重建（记录 provenance：直接观测/推断/未观测）；(3) WSA 约束生成三条规则；(4) 类型化反馈精修循环（coverage/consistency/executability check）；(5) W-path 枚举与场景对齐。

**创新点**: Skill = Runtime Specification 而非文本摘要；WSA 三部分分离使错误可归因；Evidence Provenance 纪律保留低频安全关键操作；直接对标 Anthropic Skill Creator。

**效果**: Fidelity 0.503 vs 0.455 (+10.5%)。T5（W+A 无语义）是唯一输给 ASC 的类型（attachment-heavy workflow 最具挑战）。
- Dataset: WSASkill | Metric: Fidelity | Result: 0.503 | Baseline: 0.455 (ASC) | Δ: [+10.5%]

**Wiki**: [[workflow-to-skill]] | **概念**: [[OntologySkillRouting]]

---

### B. 本体精准推理（偏检索向）

#### 6. SatIR — 约束满足临床试验检索
**arXiv**: [2604.08849](https://arxiv.org/abs/2604.08849) | **Venue**: COLM 2026 | **引用**: 0

**解决的问题**: 相似性检索将资格约束视为软信号而非硬性要求。临床试验匹配需对照同一患者记录逐一检查尖锐约束（否定、时间性、数值阈值、偏侧性）。

**方法与技术**: (1) TRIALREPR 形式化表示（SMT + SNOMED ontology 概念同一性）；(2) LLM 语义解析器；(3) SMT-to-Relational Algebra 投影（SQL 查询联合评估）；(4) Salience-Based Missingness Handling；(5) 三档检索目标。

**创新点**: Constraint-Satisfaction-Based Retrieval vs Similarity-Based；SMT-to-Relational Algebra 投影实现可扩展；Ontology-Grounded 形式化（消融 -42.2% 最大贡献因子）；可解释性（每个决策可追溯到约束子句）。

**效果**: SIGIR recall 93.68 vs 70.14 (+23.54pp)；TREC recall 80.37 vs 24.72 (+55.65pp)；146ms/patient；clinician AC1=0.82。
- Dataset: TREC 2022 | Metric: Macro Recall | Result: 80.37 | Baseline: 24.72 | Δ: [+55.65pp]

**Wiki**: [[satir-constraint-ir-clinical]] | **概念**: [[OntologyPreciseRetrievalReasoning]]

---

#### 7. DeepRAG — 层次化推理+过程监督
**arXiv**: [2506.00671](https://arxiv.org/abs/2506.00671) | **Venue**: IJCAI 2025 | **引用**: 0

**解决的问题**: 生物医学多跳 QA 需跨异构来源顺序推理。DeepSeek 不显式管理多层级推理依赖；RAG-Gym 用 LLaMA backbone 缺乏层次化分解精度。

**方法与技术**: (1) 两阶段层次化推理管线（Reasoning Module + Query Module）；(2) Hierarchical Indicators 跟踪嵌套依赖；(3) Process Supervision via MDP（三类奖励）；(4) Concept-Level Rewards（UMLS semantic matching）；(5) DPO 微调。

**创新点**: 层次化推理+指示器（vs standalone DeepSeek）；Backbone 替换 LLaMA→DeepSeek R1；UMLS Concept-Level Rewards。

**效果**: EM 54.3→62.4% (+8.1%)；Concept Accuracy 66.5→71.8% (+5.3%)。Ablation: w/o Hierarchical Reasoning EM -5.0（最大贡献）。
- Dataset: MedHopQA | Metric: EM | Result: 62.4% | Baseline: 54.3% | Δ: [+8.1%]

**Wiki**: [[deeprag-hierarchical-reasoning]] | **概念**: [[OntologyPreciseRetrievalReasoning]]

---

#### 8. RAGged Events — 事件KB+证明助手
**arXiv**: [2506.07042](https://arxiv.org/abs/2506.07042) | **引用**: 0

**解决的问题**: RDF/OWL reasoning 局限于 FOL 可判定子集，无法处理复杂时间语义和多步因果推理。"外部知识增强普遍提升性能"的假设可能不成立。

**方法与技术**: (1) 三策略对比（Base/KG-Enhanced/RAG）；(2) 级联查询管线；(3) RDF→Coq 四阶段翻译管线（Ontological Discovery→Type System→Relationship Formalization→Theorem Generation）；(4) 标准化 RDF/Turtle 输出；(5) 确定性实验设置。

**创新点**: Inverse Calibration Principle（enhancement 与模型能力反向相关）；RAG-discovered event types 的 Coq 形式化验证；RDF→Coq 翻译管线支持高阶推理。

**效果**: Claude Base 39 events → RAG 10 events（RAG 降低 74%）；Llama Base 10→RAG1 38→RAG4 0（inverted-U 灾难性崩溃）。
- Dataset: Thucydides | Metric: Events | Result: 39 (Claude Base) | Baseline: 10 (Llama Base) | Δ: [+290%]
- Key: RAG 持续降低强模型 coverage

**Wiki**: [[ragged-events-reasoning]] | **概念**: [[OntologyPreciseRetrievalReasoning]]

---

#### 9. RIGOR — 关系库到本体迭代 RAG
**arXiv**: [2506.01232](https://arxiv.org/abs/2506.01232) | **Venue**: ISWC 2026 | **引用**: 0

**解决的问题**: 从 RDB schema 自动构建 rich OWL ontology 是 labor-intensive 的。现有方法仅依赖 structural cues 产出 shallow ontology。BURR benchmark 显示 LLM 方法在 mapping 上 underperform rule-based。

**方法与技术**: (1) FK-Guided Iterative Traversal（BFS 按 FK 依赖）；(2) Direct Mapping + Delta Ontology；(3) 三源 Dense Retrieval（core ontology + documentation + external）；(4) Judge-LLM 双阶段验证（14 criteria, 3 severity）；(5) Incremental Core Ontology Merging。

**创新点**: Iterative RAG + Growing Core Ontology（cross-table context accumulation）；Judge-LLM in-loop validation；Provenance-annotated Delta Ontology；唯一产生 disjointWith axioms 的方法。

**效果**: LLM-Judge avg 3.93 vs 2.05 (+91.7%)；OOPS! pitfalls 665→个位数 (~-99%)；Ranked 1st 31/31；BURR Class F1 0.73 逆转 LLM underperform 结论。
- Dataset: eICU-CRD | Metric: OOPS! Pitfalls | Result: single digits | Baseline: 665 | Δ: [~-99%]

**Wiki**: [[rag-ontology-relational-db]] | **概念**: [[OntologyPreciseRetrievalReasoning]]

---

#### 10. RareDxR1 — 罕见病自主推理
**arXiv**: [2607.00147](https://arxiv.org/abs/2607.00147) | **Venue**: IEEE ICME 2026 | **引用**: 0

**解决的问题**: 现有 AI 方法依赖 pipeline phenotype 提取或 RAG，因预定义 ontology 和检索瓶颈导致关键信息丢失。标准 Rejection Sampling 在罕见病场景效率低下。

**方法与技术**: (1) Knowledge Internalization（HPO/Orphanet/OMIM→QA对）；(2) RERS（从失败轨迹学习，注入知识+反馈自我纠正）；(3) DCRL 双层课程（Task+Case level）；(4) CRR 多模型协作推理。

**创新点**: 首次端到端从临床笔记直接诊断罕见病（无 phenotype 提取）；RERS weak-to-strong generalization（14B 超越 671B teacher）；DCRL 推理与知识解耦优化。

**效果**: Top-1 60.29% vs 44.20% (+16.09%)；Top-10 78.73% vs 59.02% (+19.71%)；Zero-shot Top-10 50% vs 28.85% (+21.15%)。
- Dataset: RareArena | Metric: Top-1 | Result: 60.29% | Baseline: 44.20% (671B) | Δ: [+16.09%]

**Wiki**: [[raredxr1-rare-disease]] | **概念**: [[OntologyPreciseRetrievalReasoning]]

---

### C. Agent loop 循环检测与消解

#### 11. TROVE — 轨迹验证路由编辑
**arXiv**: [2609.05019](https://arxiv.org/abs/2609.05019) | **引用**: 0

**解决的问题**: Pre-execution commitment vs runtime mismatch——当中间结果使后续计划失效时（continuation invalidation），要么执行过时步骤导致错误累积，要么广泛重规划浪费计算并丢弃已完成进度。

**方法与技术**: (1) Offline Experience Extraction（原子/复合技能+transition graph）；(2) One-Step Commitment（planner 提出≤4 技能路线，仅执行第一个）；(3) Observation-Guided Route Update（Retain/Insert/Replace）；(4) Iterative Execution with bounds（最多 6 个 top-level calls）。

**创新点**: 首次将 continuation invalidation 形式化为独立编排问题；Retain-Insert-Replace 中间粒度策略；Transition graph 边来自评估过的局部修改（含 score/time delta）。

**效果**: 18 设置中 15 个最优；MATH 80.86% vs 74.07% (+6.79%)；GSM8K 时间-83.3%；token -36.3%。
- Dataset: HumanEval | Metric: pass@1 | Result: 97.71% | Baseline: 93.89% | Δ: [+3.82%]
- Dataset: GSM8K | Metric: Time | Result: 9.63min | Baseline: 57.73min | Δ: [-83.3%]

**Wiki**: [[trove-trace-route-validation]] | **概念**: [[AgentLoopDetectionResolution]]

---

#### 12. Gubernaut — 确定性恒温控制器
**arXiv**: [2607.24339](https://arxiv.org/abs/2607.24339) | **引用**: 0

**解决的问题**: LLM agent 继承 reactive failure modes（provocation 升级、sycophantic drift、perseveration）。Training-time alignment 不透明且纠缠——调节机制与生成机制是同一网络。

**方法与技术**: (1) Nelson-Narens 双级架构（object level 读写文本，meta level 仅读 3 数值）；(2) Arousal 动力学（provocation drive 积分上升+恒定衰减）；(3) 离散 posture 词汇（DEFAULT/INHIBIT/REGROUND/Recovery）；(4) Instant trigger；(5) Pre-registered generate-once/judge-many 协议。

**创新点**: Token-free meta level（prompt injection 构造上不存在攻击通道）；确定性控制定律（无采样/无学习参数，完全可复现）；Homeostatic recovery signature；Headroom gradient（效果与 host reactivity 成反比）。

**效果**: 15/16 格子更冷静（13/16 p<.05）；Gemini +1.48 (4/4 p<.05)；recovery by T8 4/4 cooks；endurance all p<.05。
- Dataset: 4×4 matrix | Metric: cells favoring regulated | Result: 15/16 | p<.05: 13/16

**Wiki**: [[gubernaut-homeostatic-controller]] | **概念**: [[AgentLoopDetectionResolution]]

---

#### 13. Argus — 通用 Agent 推理 Runtime
**arXiv**: [2608.05144](https://arxiv.org/abs/2608.05144) | **引用**: 0

**解决的问题**: 真正重要的研究任务往往 underdefined——objective 无法精确陈述，measurement 本身是问题的一部分，可用反馈稀疏/延迟/存争议。当 score 无法信任时，pivoting 应被允许但需与 goal drift 区分。

**方法与技术**: (1) Working contract Kt=(ι,ot,ct,vt)（standing intent+objective+constraints+verification）；(2) Four-role state machine M→P→E⇄R→M；(3) Verification-gated runtime self-evolution；(4) Stage dynamics {hold,advance,rollback}；(5) Dense-intelligence density。

**创新点**: Verified pivoting（vs prior work fixed objective）；Verification-gated fixed-model self-evolution（model weights 不变，evolution 在 persistent state）；Contract refinement typed/logged/role-owned surfaces；Endogenous harnessing 诊断（bottleneck 是 methodological 非 cognitive）。

**效果**: SWE-Bench Pro ~78% vs 59% (+19pp)；Tokens/task 2.95M→2.33M (-21%)；Time 8.52→7.25min (-15%)；Reviewer 466/731 tasks, 79.1% recovery。
- Dataset: SWE-Bench Pro | Metric: Accuracy | Result: ~78% | Baseline: 59% | Δ: [+19pp]

**Wiki**: [[argus-agentic-reasoning-runtime]] | **概念**: [[AgentLoopDetectionResolution]]

---

#### 14. MASC — 元认知自纠正
**arXiv**: [2510.14319](https://arxiv.org/abs/2510.14319) | **引用**: 0

**解决的问题**: 单 agent 错误通过协作结构 cascade 传播导致系统级崩溃——预实验显示单错误可造成 over 50% 性能下降。现有方法需大量监督或 costly training。

**方法与技术**: (1) Next-Execution Reconstruction（从 history 预测下一步 embedding）；(2) Prototype-Guided Enhancement（learnable prototype 作 normality anchor）；(3) Training 仅在 normal trajectories 无监督；(4) Anomaly scoring（L2 reconstruction + cosine prototype misalignment）；(5) Anomaly-triggered correction agent。

**创新点**: Step-level error detection 形式化为 history-conditioned unsupervised anomaly detection（不需 error labels）；Next-Execution Reconstruction 利用 causal structure；Prototype prior 解决 early-step 问题；Plug-and-play architecture-agnostic。

**效果**: AUC-ROC 77.84% vs 65.79% (+12.05pp)；AgentErrorBench GAIA 86.78% vs 84.26% (+2.52pp)；GSM8K+Debate 93.39% vs 91.40% (+1.99pp)。
- Dataset: Who&When | Metric: AUC-ROC | Result: 77.84% | Baseline: 65.79% | Δ: [+12.05pp]

**Wiki**: [[masc-metacognitive-self-correction]] | **概念**: [[AgentLoopDetectionResolution]]

---

#### 15. HARNESSFIX — Harness 缺陷诊断修复
**arXiv**: [2606.06324](https://arxiv.org/abs/2606.06324) | **引用**: 0

**解决的问题**: Agent harness（ETCLOVG 七层 runtime infrastructure）failures 无法直接映射到实现位置。现有方法做 runtime supervision（不修复根因）或 outcome-driven 优化（不先定位 responsible evidence）。

**方法与技术**: (1) HTIR（TraceSteps+TraceLinks+implementation anchors 对齐 runtime 与 static artifacts）；(2) Failure Attribution 四步法（symptom localization→backtracking→adjudication→layer assignment）；(3) Harness Flaw Consolidation；(4) Scoped Repair Operators（七层，基于 30 repos/57,780 records empirical study）；(5) Patch Generation + Regression-aware Validation。

**创新点**: Trace-grounded diagnosis-driven repair vs outcome-driven prompt evolution；HTIR 对齐 runtime behavior 与 static harness artifacts；Scoped repair operators 约束 free-form editing；Cross-model transfer（+5.5-9.5% 一致增益说明修复 model-agnostic flaws）。

**效果**: GAIA 43.3→61.7% (+18.4pp)；SWE-Bench 45.3→57.3% (+12.0pp)；Cross-model: Claude +5.5pp, DeepSeek +7.8pp, Qwen +9.5pp。Diagnosis: 85.0% step accuracy vs 55.0% raw trace。
- Dataset: GAIA | Metric: TCR | Result: 61.7% | Baseline: 43.3% | Δ: [+18.4pp]

**Wiki**: [[failed-trajectories-harness-flaws]] | **概念**: [[AgentLoopDetectionResolution]]

---

## 新增趋势洞察

1. **本体在 skill 路由中的价值不在选择而在解读和累积**（[[domain-grounded-tool-orchestration]] null result: tool selection 不变 + [[skillnet-ai-skills]] reward +40% + [[scx-router-task-ontology]] task ontology 23/115/345）：Domain-Grounded Tool Orchestration 的消融实验证明 ontology 不改变 tool selection precision/recall（null result），但将 interpretation accuracy 从 0.41 提升到 0.91（+122%）。SkillNet 的三层 Skill Ontology 使平均 reward +40%、steps -30%——本体在路由中的核心价值是"结构化解读结果"和"累积能力"，而非"选择控制"。

2. **Inverse Calibration Principle 挑战 RAG 普遍有效假设**（[[ragged-events-reasoning]] Claude Base 39 events → RAG 10 events, GPT-4o Base 36→20 + [[raredxr1-rare-disease]] 知识内化 14B 超越 671B）：enhancement 效果与模型能力反向相关——强模型（GPT-4o/Claude）在 base generation 下最优，RAG 反而引入 hallucination 和 temporal conflation；弱模型（Llama）呈 inverted-U pattern（简单 RAG 提升→复杂 RAG 灾难性崩溃到 0 events）。RareDxR1 的 RERS 进一步证明知识内化（非 RAG）可实现 14B 超越 671B。直接挑战"更多检索必然更好"的领域假设。

3. **约束满足检索超越相似性检索**（[[satir-constraint-ir-clinical]] recall +55.65pp, 146ms + [[rag-ontology-relational-db]] OOPS! 665→个位数）：SATIR 将约束作为 binding requirements 形式化满足（SMT→关系代数投影），在 TREC 2022 上 recall 80.37 vs TrialGPT 24.72（+55.65pp），SNOMED ontology 消融是最大贡献因子（-42.2%）。RIGOR 的 Judge-LLM in-loop 验证将 OOPS! pitfalls 从 665 降至个位数（~-99%），逆转了 BURR benchmark 中"LLM methods underperform rule-based"的结论——formal methods + LLM 的组合在检索阶段实现了新范式。

4. **确定性控制层比 LLM-based guardrail 更可靠**（[[gubernaut-homeostatic-controller]] 15/16 更冷静, prompt injection 免疫 + [[argus-agentic-reasoning-runtime]] SWE-Bench 59→78%）：Gubernaut 的 token-free meta level（仅接受 3 个数值/tick，无 prompt/context window/text channel）使 prompt injection 在构造上不存在攻击通道——区别于基于第二 LLM pass 的 guardrail（governor 由被治理的 substrate 构成，继承同样纠缠）。确定性 arousal 动力学的 homeostatic recovery 在 4/4 模型家族中复制，15/16 格子更冷静。Argus 的 verified pivoting 将目标修正从 goal drift 中区分，SWE-Bench Pro 59→78%。

5. **循环消解需要中间粒度策略**（[[trove-trace-route-validation]] 18设置15最优 + [[masc-metacognitive-self-correction]] AUC 77.84% + [[failed-trajectories-harness-flaws]] GAIA +18.4pp）：TROVE 的 Retain-Insert-Replace 三操作在粗粒度工作流重选（丢进度）和细粒度逐步重规划（延迟+方差）间开辟新设计空间——保留已完成前缀仅修复无效后缀，18 设置中 15 个最优，时间-83.3%。MASC 的 Next-Execution Reconstruction 无监督检测异常步骤防止级联（单错误可造成 50% 性能下降）。HARNESSFIX 的 HTIR 对齐+scoped repair operators 使 GAIA +18.4pp 且跨模型迁移 +5.5-9.5%，证明修复的是 model-agnostic 的 harness-level flaws。

## 知识库状态

| 指标 | 上轮 | 本轮 | 变化 |
|---|---|---|---|
| 论文 | 312 | 327 | +15 |
| Source 页面 | 439 | 454 | +15 |
| Concept 页面 | 123 | 126 | +3 |
| PDF 文件 | 311 | 326 | +15 |
| 空文件 | 0 | 0 | ✅ |
| 索引同步 | 0 | 0 | ✅ |
