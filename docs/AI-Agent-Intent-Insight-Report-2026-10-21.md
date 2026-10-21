# OWL2 本体推理 × LLM 论文洞察日报 — 2026-10-21

**日期**: 2026-10-21
**累计论文**: 365 篇（本轮新增 17 篇）
**知识库页面**: 505 页（+21：17 source + 4 concept）

## 概览

| 方向 | 本轮新增 | 累计 | 代表趋势 |
|---|---|---|---|
| A. 规则型本体推理（OWL2 RL/SWRL）+ LLM | 4 | — | LLM 只填 ABox、推理器判类；图 grounding 决定性能 |
| B. OWL2 DL 推理工程应用 | 4 | — | 推理器从验证基准进化为修复环路；神经近似一致性加速 20× |
| C. 推理结果校验 LLM / 辅助生成 | 9 | — | SHACL 成为 LLM 生成物校验事实标准（4 对象 × 3 反馈去向） |
| **总计** | **17** | **365** | **确定性推理嵌入 LLM 管线成为工程标配** |

## 新增论文清单（速查表）

| # | 论文 | 年份 | Venue | arXiv | 引用 | 方向 |
|---|---|---|---|---|---|---|
| 1 | [Structured Decomposition](https://arxiv.org/abs/2601.01609) | 2026 | arXiv | 2601.01609 | 2 | A |
| 2 | [Ontology-Driven CEP + LLM（TB）](https://arxiv.org/abs/2510.09646) | 2025 | arXiv | 2510.09646 | 0 | A |
| 3 | [Cause-Effect Specification](https://arxiv.org/abs/2606.31614) | 2026 | IFAC 格式 | 2606.31614 | 0 | A |
| 4 | [SHACR](https://arxiv.org/abs/2606.22312) | 2026 | IEEE IoT-J（投稿） | 2606.22312 | 0 | A |
| 5 | [When Corrective Hints Hurt](https://arxiv.org/abs/2604.23398) | 2026 | ICAIDE 2026 | 2604.23398 | 3 | B |
| 6 | [GLaMoR](https://arxiv.org/abs/2504.19023) | 2025 | WI-IAT 2026 | 2504.19023 | 2 | B |
| 7 | [From Rule Engines to Ontologies](https://doi.org/10.3390/computers15080544) | 2026 | Computers (MDPI) | DOI-only | 0 | B |
| 8 | [Can LLMs Understand DL-Lite?](https://arxiv.org/abs/2406.17532) | 2024 | EMNLP 2024 | 2406.17532 | 6 | B |
| 9 | [G-SPEC](https://arxiv.org/abs/2512.20275) | 2025 | arXiv | 2512.20275 | 3 | C |
| 10 | [QRAKEN](https://arxiv.org/abs/2610.08095) | 2026 | GLOW @ ISWC 2026 WS | 2610.08095 | 0 | C |
| 11 | [xpSHACL](https://arxiv.org/abs/2507.08432) | 2025 | VLDB'25 LLM+Graph WS | 2507.08432 | 3 | C |
| 12 | [KG Repair with LLMs](https://arxiv.org/abs/2507.22419) | 2025 | arXiv (LNCS) | 2507.22419 | 1 | C |
| 13 | [AML + LLM + SHACL](https://arxiv.org/abs/2506.10678) | 2025 | IEEE ETFA 2025 | 2506.10678 | 4 | C |
| 14 | [LLM 生成能力本体（CaSk）](https://arxiv.org/abs/2404.17524) | 2024 | IEEE ETFA 2024 | 2404.17524 | 19 | C |
| 15 | [EntailLLM](https://arxiv.org/abs/2608.01763) | 2026 | under review (AAAI 格式) | 2608.01763 | 1 | C |
| 16 | [Neurosymbolic Alignment](https://arxiv.org/abs/2608.24534) | 2026 | IEEE J-BHI（在投） | 2608.24534 | 0 | C |
| 17 | [Transparent CTI](https://arxiv.org/abs/2509.00081) | 2025 | XAI-KRKG @ ECAI 2025 | 2509.00081 | 0 | C |

## 新增论文结构化分析

### A. 规则型本体推理（OWL2 RL / SWRL）+ LLM

---

#### 1. Structured Decomposition — LLM 填充 ABox + SWRL 确定性推理

**arXiv**: [2601.01609](https://arxiv.org/abs/2601.01609) | **Venue**: arXiv | **引用**: 2

**解决的问题**: LLM 擅长解释非结构化文本但无法保证规则应用一致性，符号系统有形式化保证却吃不了自由文本。直接改进对象是其自身 prior work（JSON schema + SMT）：仅在单一法律 hearsay 任务验证、依赖 ad-hoc 表示，缺乏与语义网标准工具链的互操作性。

**方法与技术**: (1) LLM 两步本体填充——entity identification + assertion extraction，任务定义完全由专家 TBox 提供；(2) OWL 2 本体 + SWRL 合取规则编码任务谓词，提示元数据以 annotation 编码在本体内；(3) Pellet 推理器对填充后 ABox 做一致性检查、分类与规则执行，每实例全新 OWL world 隔离；(4) 互补谓词（正/反成对断言）作为实验变量；(5) 任务适用性判据 + DDXPlus 负例验证。

**创新点**: vs 自身 prior work——用 OWL 2/SWRL 标准替换 ad-hoc 表示，任务可在 Protégé 编辑、ABox 可 SPARQL 查询、可导入 SNOMED-CT/FIBO；vs NL2FOL 等翻译管线——"本体填充+SWRL 推理"替代"ad-hoc FOL+SMT"，首次 3 领域 × 11 LLM 验证；vs 纯提示工程——架构级符号验证，消融证明贡献独立于提示结构。

**效果**: 总体 F1 79.8% vs few-shot 75.2%（+4.6pp, p=0.007）vs CoT 74.1%。
- Dataset: 3 任务 × 11 模型 | Metric: F1（SD vs SD-Direct 去掉 SWRL 验证）| Result: **79.8% vs 70.1%** | Δ: +9.7pp（p=0.001）
- **消融**: 只给断言规范不给符号验证反而低于 few-shot（70.1% vs 75.2%）；召回 +15.7pp（84.7% vs 69.0%）；互补谓词 −5.0pp 反例
- **负验证**: 统计边界任务（URTI）SD 仅 0.145 F1——确认适用性判据

**Wiki**: [[structured-decomposition-swrl]] | **概念**: [[ReasonerGuidedRepair]] · [[OntologyConstrainedGeneration]]

---

#### 2. Real-Time Health Analytics — BFO+SWRL+CEP+LLM 结核病实时检测

**arXiv**: [2510.09646](https://arxiv.org/abs/2510.09646) | **Venue**: arXiv | **引用**: 0

**解决的问题**: 本体建模、CEP、AI 诊断长期三条平行线：前作 OCEP（85% 准确率）无 LLM；模糊规则 CEP 无语义层；OntoTB/O4TBSS 静态本体无实时能力。缺口是统一平台 + 本体无法随医学知识演化。

**方法与技术**: (1) Kafka→Spark Streaming→Siddhi CEP 五组件管线；(2) BFO 顶层 TB 本体（continuant/occurrent 二分，RNTCP 行政体系建模）；(3) SWRL 规则库（分期 5 + 筛查 13 + 管理 13 + 重症 10 条）；(4) 选择性触发——SWRL 命中才跑 SPARQL；(5) LLM 三重角色：FAISS+嵌入 QA、告警解释、本体半自动演化（LLM 建议→专家审核→Pellet 一致性校验→部署）。

**创新点**: vs OCEP——增加 LLM 推理层与本体演化回路；vs 模糊规则 CEP——SWRL 语义规则替代纯模糊逻辑；vs 静态 TB 本体——实时流 + 首个"LLM 建议+专家在环+推理器校验"演化回路；LLM 输出被本体双重校验。

**效果**: SWRL 规模 240 条；SPARQL 时延 0.20–0.25s（简单）；LLM QA F1 0.702–0.778；端到端 4.2–4.7s/患者。
- Dataset: Kaggle TB（1,000 患者）| Metric: 本体结构 | Result: AR 0.496、RR 0.749
- ⚠️ TB 检测任务无 baseline 对比数值——具体数值待补充

**Wiki**: [[ontology-cep-health-analytics]] | **概念**: [[OntologyConstrainedGeneration]]

---

#### 3. Automating Cause-Effect Specification — KG+SWRL 安全联锁规格生成

**arXiv**: [2606.31614](https://arxiv.org/abs/2606.31614) | **Venue**: IFAC 格式 | **引用**: 0

**解决的问题**: 流程工业 C&E 矩阵/interlock/报警表仍靠手工。CERN CEM 规范只给手工矩阵语义；P&ID/HAZOP 抽取靠启发式无形式语义；现有 LLM 生成 SWRL 工作（Laurenzi/Soularidis）缺乏流程工程语义与 KG 接地。

**方法与技术**: (1) 五层管线（Data→RML Mapping→CPSMod KG→SPARQL CONSTRUCT 物化→约束 LLM 验证）；(2) CPSMod 复用 5 组 ODP（VDI 3682/2206、DIN 17359、UML StateMachine、OpenMath）；(3) DIN 17359 故障类模板 + SPARQL UPDATE 实例化；(4) SPARQL CONSTRUCT 自动物化 CauseEffectRow（零手工 C&E 逻辑）；(5) 约束 LLM 转写为叙事+SWRL 双工件，禁止发明本体外语汇。

**创新点**: vs Soularidis——SWRL 从 KG 物化行生成，语义接地率 100%；vs CERN CEM——一致性 by construction；vs 启发式抽取——SWRL 可被 Jess/Drools 做冲突/冗余分析；单一 KG 源产出三种一致工件。

**效果**: 15 条 C&E 行（8 故障/8 诊断对象/6 缓解动作）；语义接地率 **100%**；SWRL 语法有效 **100%**；冲突/不可达/冗余 **0**；零幻觉设备（定性，量化待补充）。

**Wiki**: [[cause-effect-spec-kg-llm]] | **概念**: [[OntologyConstrainedGeneration]]

---

#### 4. SHACR — 智能家居 IoT 多类冲突消解

**arXiv**: [2606.22312](https://arxiv.org/abs/2606.22312) | **Venue**: IEEE IoT-J（投稿） | **引用**: 0

**解决的问题**: 智能家居规则并发执行产生隐藏冲突。IoTC2/TapChecker 只查语法矛盾；IoTMon/IoT-Praetor 需手工设备行为模型；LLM-only 缺拓扑信息不可靠。无系统同时覆盖逻辑/语义/物理三类冲突并给出修复。

**方法与技术**: (1) Neo4j 类型化图，AFFECTS 边编码物理因果；(2) 三类冲突形式化为图遍历模式（0 跳/1 跳/多跳）；(3) MCP 工具白名单（4 读 1 写，写操作用户批准门控）；(4) Scan–Explain–Repair–Validate 闭环，修复动作空间白名单；(5) 检索架构迭代教训（大 Cypher 超时→拆分并行）。

**创新点**: vs 形式规则分析器——物理冲突可检出（文本法上限 0.54）；vs 语义框架——跨平台统一+可执行修复；vs LLM-only——同模型 F1 0.59→0.79，表示决定性能。

**效果**: Zero-shot F1 **0.79**（P 0.78/R 0.80）。
- Dataset: 自建 203 规则/70 公寓 | Metric: 图消融 | Result: YAML-only 0.59 → 加图 **0.79** | Δ: 错误 −36.7%
- Dataset: few-shot 校准 | Metric: F1 | Result: 7 样本 **0.95**（P 1.00）——仅在图存在时起效
- Dataset: vs IoTC2/VISCR | Metric: F1 | Result: 0.79 vs **0.54**/**0.49**

**Wiki**: [[shacr-smart-home-conflict]] | **概念**: [[ValidationFeedbackLoop]]

### B. OWL2 DL 推理工程应用

---

#### 5. When Corrective Hints Hurt — OWL2 DL 推理器引导修复 LLM 过度谨慎

**arXiv**: [2604.23398](https://arxiv.org/abs/2604.23398) | **Venue**: ICAIDE 2026 | **引用**: 3

**解决的问题**: 已有 DL 推理基准只测单次正确率，不测可审计性（错误能否在有限轮反馈内被纠正）。发现 GPT-5.4 在 OWL 2 DL 蕴含查询上的系统性"过度谨慎"：推理器可推导否定时频繁答 unknown。

**方法与技术**: (1) 一致性试插入判定金标准（O⁺/O⁻ 各跑一次 HermiT/Pellet 一致性检查）；(2) 180 查询扩展集（FunctionalProperty+disjointness 笛卡尔网格）+ 18 held-out；(3) 四种交互模式（direct/naïve retry/verdict+OWA hint/verdict-only）；(4) McNemar+Bonferroni 统计；(5) 跨模型对照。

**创新点**: 首次将可审计性操作化为独立评测轴；证伪"解释越多越好"——逻辑正确的 OWA 提示使修复差 14.4pp；verdict-only 更便宜更准。

**效果**: 直答 **43.9%** → naïve retry 81.7% → verdict+hint **67.2%（反噬）** → verdict-only **97.8%**。
- Dataset: 180 查询 | Metric: McNemar | Result: direct→verdict-only **+53.9pp**（p=1.3×10⁻²⁹）；naïve→hint **−14.4pp**
- **失败指纹**: 101 错误中 **99 个** expected=no, got=unknown；hint 变体 59 错误中 56 个同指纹（3 轮反馈都告知正确答案仍不改）
- 成本: verdict-only 1.63 轮 vs hint 1.93 轮（省 16%）

**Wiki**: [[reasoner-guided-repair-owl2dl]] | **概念**: [[ReasonerGuidedRepair]]

---

#### 6. GLaMoR — 图语言模型做 OWL 一致性检查

**arXiv**: [2504.19023](https://arxiv.org/abs/2504.19023) | **Venue**: WI-IAT 2026 | **引用**: 2

**解决的问题**: 经典推理器在大规模本体上开销过高；已有 ML 方法只做 A-Box；LLM 直接做逻辑推理差（Llama 3 零样本 52.53%）。T-Box 一致性的可扩展近似推理缺失。

**方法与技术**: (1) OAPT 模块化 + 14 种反模式注入构造不一致样本；(2) Manchester 语法→英文三元组→GLM 输入；(3) T5 底座 Graph Transformer + Levi 图变换 + 全局注意力 + 二分类头；(4) 基线族（经典 ML/ModernBERT/LongT5/PRODIGY/Llama 3），HermiT 定义标签；(5) 反模式族剔除鲁棒性研究。

**创新点**: 首个 T-Box 一致性神经检查器（vs Paulheim 仅 A-Box）；比 HermiT 快 ~20×（122h vs 训练 4.5h+推理 18min）；证明全局图注意力必要（vs 同底座 LongT5 +10%）。

**效果**: gGLM-base **95.13%** acc（P 96.10/R 94.17）。
- Dataset: BioPortal 4,169+4,169 模块 | Metric: acc | Result: **95.13%** | Baseline: ModernBERT 94.27%、Llama3 52.53%、经典 ML 56–61%
- **消融**: 全局 GLM 任何单反模式族剔除下保持 >90%；UE* 族剔除影响最大（−4.2pp）
- 代价: 95.13% vs HermiT 精确 100%

**Wiki**: [[glamor-owl-consistency-glm]] | **概念**: [[NeuralConsistencyChecking]]

---

#### 7. From Rule Engines to Ontologies — OWL2 DL 本体驱动评估信息系统

**DOI**: [10.3390/computers15080544](https://doi.org/10.3390/computers15080544) | **Venue**: Computers (MDPI) 15(8):544 | **引用**: 0

> ⚠️ 仅摘要源（MDPI 全文抓取被拒），关键引用出自 Abstract

**解决的问题**: 领域信息系统把数据模型/规则库/基础设施维护为分离工件，部署前验证复杂。能否统一进可验证的本体到代码管线且不改变分类结果？

**方法与技术**: (1) MDA：OWL 2 DL 本体三合一表达领域结构/分类规则/生成元数据；(2) HermiT 生成前验证门（一致性+可满足性+包含，OWA 下）；(3) 生成器产出四层 Java 应用；(4) OWA 验证→CWA 运行双语义，重叠类目用本体声明优先级消解。

**创新点**: vs Jess 规则引擎分离工件——形式验证的单一事实来源；OWA/CWA 显式分工；明确边界声明（算术/时序场景不适用）。

**效果**: 塞尔维亚科研评价系统**完全复现** Jess M30/M33 分类；产前诊断应用 **6/6** 运行时分类与 HermiT 蕴含一致。性能指标未报告（论文明言不声称优越性）。

**Wiki**: [[rule-engines-to-ontologies]] | **概念**: [[OntologyReasoning]]

---

#### 8. Can LLMs Understand DL-Lite Ontologies? — 六任务实证

**arXiv**: [2406.17532](https://arxiv.org/abs/2406.17532) | **Venue**: EMNLP 2024 | **引用**: 6

**解决的问题**: LLM 能否理解 DL 本体未被系统研究——已有工作测 KG 事实记忆或通用逻辑推理，无一针对 DL 语法/模型论语义/推理服务。

**方法与技术**: (1) 6 任务框架（语法/包含/实例检查/QA/可满足性/属性特征）；(2) DL-Lite 推理规则体系（2 PI + 11 NI + 5 ABox 传递）嵌入提示；(3) HermiT 经 Protégé 生成金标准；(4) 3 模型 × 3 提示档（NI/WI/WIE）；(5) 数据集族（GO/FMA/UOBM/LUBM/MIS）。

**创新点**: 首个 DL 本体理解综合评测；NI 规则隔离 case study 发现"幻觉解释"现象；覆盖句法到模型论语义全谱。

**效果**: 小本体包含/实例检查近 **100%**；UOBM1/2 超上下文 → **0%**；LUBM 14 查询 **无一完全正确**。
- Dataset: MIS 可满足性 | Metric: F1 | Result: economy-Inc. GPT-3.5 **96.4** / MaasMatch 全模型 55–73
- **关键失败**: TBox NI 传递规则系统性失败，指令与示例改善有限且解释幻觉

**Wiki**: [[llm-understand-dllite]] | **概念**: [[ReasonerGuidedRepair]]（失败面实证基础）

### C. 推理结果校验 LLM / 辅助 LLM 生成

---

#### 9. G-SPEC — 5G 自治网络 SHACL 策略执行

**arXiv**: [2512.20275](https://arxiv.org/abs/2512.20275) | **Venue**: arXiv | **引用**: 3

**解决的问题**: LLM agent 进入 5G 运维的治理缺口（通用 LLM 14.6% 网络操作幻觉）。DRL 泛化鸿沟、脚本自动化规则爆炸、RAG 式 KG 只检索不强制。

**方法与技术**: (1) Governance Triad：NKG（映射 3GPP TS 28.623）+ TSLAM-4B + SHACL 控制平面；(2) 4 类 88 条 SHACL 策略（拓扑/资源/状态/新鲜度护栏）；(3) 假设图状态预执行校验（SimulateAction→SHACLValidate→违规整体拒绝）；(4) 语义爆炸半径控制（±20%）；(5) 结构化 RejectionReason 反馈重新规划。

**创新点**: 消融证明图接地比微调重要（NKG 68% vs TSLAM 8%）；KG 从检索对象升级为"可执行状态机+语义防火墙"；本体继承使 88 条 shape 治理 450 节点（命令式需 450+）；事前预防 vs 事后监控。

**效果**: 修复成功率 **94.1%** vs GPT-4 ZS 82.4%（+11.7pp）；安全违规 **0.0%** vs 8.2%；幻觉率 **0.2%** vs 14.6%。
- Dataset: 450 节点 5G 核心、500 场景 | Metric: 消融 | Result: 去 NKG → 修复率 76.2%、违规 7.8%
- 扩展性: 100K 节点校验延迟 314ms（L(n)=142·(k/12)^1.2）；142ms 开销适配 SMO 层

**Wiki**: [[g-spec-5g-policy]] | **概念**: [[ValidationFeedbackLoop]] · [[OntologyConstrainedGeneration]]

---

#### 10. QRAKEN — 图蒸馏 + 语义自愈 Text-to-SPARQL

**arXiv**: [2610.08095](https://arxiv.org/abs/2610.08095) | **Venue**: GLOW @ ISWC 2026 WS | **引用**: 0

**解决的问题**: 预训练分布外图上的主导失败不是语法而是图接地正确性（查询合法却歪曲数据模型）。在线 agentic 探索慢、微调不适应 schema 漂移、shape 提示基于"应当有什么"而非"实际有什么"。

**方法与技术**: (1) 离线图蒸馏器穷举构建共现矩阵（零支持=确定性不可能证明）；(2) TTQL 描述语言（观测模式+条件频率+字面量示例，8× 压缩）；(3) 三级确定性校验（语法→词法→数据模型）；(4) 校验失败→定向诊断→修复 prompt（≤5 轮）；(5) 机器侧/提示侧分工（矩阵不占上下文）。

**创新点**: vs ARUQULA 同基座 F1 +30% 且快 17×；vs auto-SHACL +64%——描述性经验内容优于规范性形状；vs 微调冠军 training-free 且更便宜。

**效果**: strict F1 **0.643**（gpt-4.1-mini）/ **0.652**（gpt-5.4）。
- Dataset: CK25（50 题）| Metric: strict F1 | Result: **0.643** | Baseline: ARUQULA 0.493 | Δ: +30%
- Dataset: 同上 | Metric: SHACL-auto 基线 | Result: 0.376 | Δ: **+64%**
- **消融**: TTQL 模式块贡献 +0.309；自愈循环是"确定性失败过滤器"（94% 首轮放行）；Qwen3.6-35B 4-bit 本地 0.491 持平最强参赛者

**Wiki**: [[qraken-graph-distillation]] | **概念**: [[ValidationFeedbackLoop]] · [[OntologyConstrainedGeneration]]

---

#### 11. xpSHACL — RAG+LLM 可解释 SHACL 校验

**arXiv**: [2507.08432](https://arxiv.org/abs/2507.08432) | **Venue**: VLDB'25 LLM+Graph WS | **引用**: 3

**解决的问题**: 传统 SHACL 引擎报告简短不可行动；形式化解释（EYE/repair 语义）需逻辑学背景。缺面向非技术用户的直觉性多语言解释。

**方法与技术**: (1) 包装 pyshacl 提取细粒度违规信息；(2) Justification Tree（Premise/Observation/Inference 三类节点）保证事实根基；(3) RAG 四类上下文（本体片段/shape 文档/相似案例/领域规则）；(4) LLM 合成多语言解释+修复建议；(5) Violation KG 签名缓存（MD5 of 组件+路径+类型）。

**创新点**: 首个把解释质量作为一等公民的 SHACL 系统；KG 缓存对抗 LLM 非确定性保证一致解释；判定树保证接地。

**效果**: LOV 431 本体发现 **145,910 违规**；缓存命中率 **99.48%**（2,289/2,301）。
- Dataset: LOV | Metric: 性能 | Result: 均 13.03s/本体（解释生成仅 0.12s）
- ⚠️ 解释质量正式用户研究列为 future work——定量数值待补充

**Wiki**: [[xpshacl-explainable-validation]] | **概念**: [[ValidationFeedbackLoop]]

---

#### 12. Systematic Evaluation of KG Repair with LLMs — VIO 评测框架

**arXiv**: [2507.22419](https://arxiv.org/abs/2507.22419) | **Venue**: arXiv (LNCS) | **引用**: 1

**解决的问题**: KG 修复评估依赖临时数据集，无法细粒度刻画修复行为。符号修复方法无法利用词法/领域信息，选不出语义最优修复。

**方法与技术**: (1) VIO 形式化——可控制造违规且正确修复已知；(2) 抽象重写系统处理 shape 嵌套依赖（Theorem 1 强规范化）；(3) 拓扑排序+DFS 收集约束路径；(4) 3×3 提示策略因子（manifest 上下文 × KG 上下文）；(5) 四级阶梯指标+LMM 统计。

**创新点**: 首个可系统化可扩展的 KG 修复评测框架；揭示"修好≠修对"鸿沟；prompt 上下文裁剪方法论。

**效果**: 语法有效 **97.35%**、语义有效 **86.17%**、relaxed iso **54.07%**、exact iso **49.94%**。
- Dataset: Brick/LUBM/QUDT（348 用例）| Metric: 消融 | Result: M→S 显著提升（整 manifest "过载并分散注意力"）；**S+F+ 成本/性能最优**
- 模型: GPT-4o ≈ Llama 405B ≈ Claude Opus，Gemini 显著差

**Wiki**: [[kg-repair-shacl-llm]] | **概念**: [[ValidationFeedbackLoop]]

---

#### 13. AutomationML 文本约束 LLM+SHACL 校验

**arXiv**: [2506.10678](https://arxiv.org/abs/2506.10678) | **Venue**: IEEE ETFA 2025 | **引用**: 4

**解决的问题**: AML 建模规范是自然语言且无校验机制。前作实现 AML→OWL 映射但 SHACL 需专家手工编写；其他 LLM-SHACL 工作只生成简单 shape。

**方法与技术**: (1) RML 声明式映射 AML→OWL 本体；(2) few-shot LLM 把文本约束翻译为 SHACL shapes；(3) 标准 SHACL 校验；(4) LLM one-shot 解释验证报告为自然语言修复建议；(5) 命令行原型开源。

**创新点**: vs 手工 SHACL——文本约束半自动形式化；vs 已有 LLM-SHACL——AML 特有复杂约束（接口基数/InternalLink 方向性）+完整闭环；双向 LLM 接入（生成+解释）。

**效果**: 3 条 AR APC 规则——生成 shape "大体正确仅需轻度后编辑"；故意违规模型 **3/3 违规检出**且 LLM 均正确解释。
- ⚠️ 无量化基准（work-in-progress）——具体数值待补充
- 关键局限: 自然语言约束本身欠精确（InternalLink 有向 vs 约束隐含双向）

**Wiki**: [[aml-shacl-validation-llm]] | **概念**: [[ValidationFeedbackLoop]] · [[OntologyConstrainedGeneration]]

---

#### 14. LLM 生成能力本体（CaSk）— OWL 推理+SHACL 三道门校验

**arXiv**: [2404.17524](https://arxiv.org/abs/2404.17524) | **Venue**: IEEE ETFA 2024 | **引用**: 19

**解决的问题**: 工业 4.0 能力本体建模专家密集。已有工作或无验证方法（Xia）、或仅人工评估（Trajanoska）、或结论 zero-shot 不足（LLMs4OL）。缺系统方法+自动验证+提示技术对比。

**方法与技术**: (1) CaSk 本体（VDI 3682/DIN EN 61360/OpenMath）作 TBox 上下文放入 prompt；(2) 因子实验 2 LLM × 3 提示 × 7 复杂度递增能力；(3) 三道形式化门：Protégé 语法检查→Pellet 推理检测不一致→6 个 closed SHACL shapes 检测幻觉与缺失；(4) 错误数/三元组数归一化；(5) 全部数据开源。

**创新点**: vs Xia——完整本体+形式化验证方法；vs Trajanoska——系统对比+复杂模型+半自动评估；首个 S/C/H/I 四类错误归一化质量框架。

**效果**: Claude 3 Opus few-shot 平均相对错误分 **0.03**（近乎完美）；GPT-4 few-shot **0.12**。
- Dataset: 7 能力 × 6 组合 | Metric: zero→one 降幅 | Result: GPT **−0.37**、Claude **−0.43**（结构模板注入是最大增益）
- **消融**: zero-shot 下 GPT 大量幻觉被禁元素、Claude 零幻觉；transport 能力全部失败（示例缺 resource provider）
- 成本: $0.31–0.65/prompt

**Wiki**: [[llm-capability-ontologies]] | **概念**: [[OntologyConstrainedGeneration]] · [[ValidationFeedbackLoop]]

---

#### 15. EntailLLM — 时序标注逻辑蕴含校验 LLM 漏洞路径

**arXiv**: [2608.01763](https://arxiv.org/abs/2608.01763) | **Venue**: under review (AAAI 格式) | **引用**: 1

**解决的问题**: LLM 推理漏洞时静默违反领域知识（memset 被推断能做整数计算）。已有方法把输出当预测打分或约束单 KG 游走，无方法检验 LLM 对二进制推理与独立领域知识的一致性。

**方法与技术**: (1) 跨图蕴含：调用图 × 独立 CWE DKG（105–188 实体，手册/公告自动抽取）；(2) 时序标注逻辑 + PyReason（不动点多项式收敛、精确可判定、首个错误步定位+推理 trace）；(3) 42 条非 ground 规则（标签/关系传播+传递闭包+游走控制），跨 CWE 复用；(4) LLM 生成标签模板→beam search 实例化→蕴含过滤喂 fuzzer；(5) 医疗设备固件 REST 部署。

**创新点**: vs graph-constrained reasoning——两图对齐验证非单图游走；vs safe RL shielding——DK 回注生成器反而 +37% 路径（shield 只会挡）；统计清理 vs 语义清理的区分（只有逻辑推理器能做后者）。

**效果**: pooled entailment **78.0%→97.9%**（94 配置：59 升/32 平/3 降，Wilcoxon p<10⁻¹⁰）。
- Dataset: 真实医疗设备二进制 | Metric: entailment | Result: 71.4% → **98.0%**（100% 配置 17→38）
- **消融**: self-refinement+DK 蕴含路径 1,054→1,445（**+37%**）；无 DK 时 self-refinement 最不可靠（60.9%）
- 稳定性: 10 次重复标准差 10.7→4.2；随机基线仅 18.0%/46.4%

**Wiki**: [[entailllm-vulnerability-verification]] | **概念**: [[ReasonerGuidedRepair]] · [[ValidationFeedbackLoop]]

---

#### 16. Neurosymbolic Alignment — 生理世界模型对齐临床 LLM

**arXiv**: [2608.24534](https://arxiv.org/abs/2608.24534) | **Venue**: IEEE J-BHI（在投） | **引用**: 0

**解决的问题**: 临床 LLM 事实正确但生理不安全（加重高钾血症）。RAG/微调不强制生理一致性；偏好优化受限于标注数据质量。缺训练时自动偏好信号。

**方法与技术**: (1) 847K 节点/3.2M 边异构生物医学 KG（UMLS/DrugBank/Reactome/HPO 等 8 源）；(2) 4 层 HGNN 评分器，PhysioScore = S_hom·σ(S_path)·(1−P_int) 乘法组合；(3) 迭代 ORPO（T=5 轮，on-policy 采样 K=8，HGNN 排名诱导偏好对）；(4) CSB 2,500 场景防泄漏基准；(5) 反循环论证设计：3 个 HGNN 独立端点（RSS 规则引擎/DID/医生盲评）三角验证。

**创新点**: vs ORPO 人工标注——CSS +21.3pp 且免标注；vs 推理时自纠——训练时对齐 +11.4pp；**HGNN 只在训练期使用，推理期零开销**（与 SHACL 推理时校验互补的光谱位置）。

**效果**: CSS 69.5% → **90.8%**（+21.3pp）。
- Dataset: CSB 2,500 场景 | Metric: RSS 独立端点 | Result: 65.2% → **86.4%**（一致性 r=0.97）；医生盲评不安全率 14.1%→**5.1%**
- **消融**: 去 HGNN 评分 **−16.2pp**；去迭代训练 −11.5pp
- 残余违规 9.2%（图覆盖稀疏 4.2% 为主因）；成本 42.6 GPU-hours

**Wiki**: [[neurosymbolic-alignment-clinical]] | **概念**: [[ReasonerGuidedRepair]]（训练时变体）

---

#### 17. Transparent CTI — 本体+SHACL 约束 LLM 日志抽取

**arXiv**: [2509.00081](https://arxiv.org/abs/2509.00081) | **Venue**: XAI-KRKG @ ECAI 2025 | **引用**: 0

**解决的问题**: 蜜罐日志非结构化且语义歧义；UCO/STIX/SEPSES 假设输入已解析（SEPSES 明确不支持引导自由文本抽取）；纯 prompt LLM 精度不足。缺既能引导输出结构又能 SHACL 验证的轻量中间本体层。

**方法与技术**: (1) 轻量平面日志本体（Event 核心 + W3C Time）；(2) 配套 SHACL 规范（基数/类型/必备属性）；(3) MMR few-shot 示例检索；(4) Pydantic 结构化输出 + 失败模式约束 prompt；(5) 迭代修正回路（≤3 轮，仍不合规输出空图防脏入库）。

**创新点**: vs prompt-only——同 LLM 直接对照全指标胜出；vs UCO/STIX——专为"自由文本输入+SHACL 合规生成"设计的最小扁平 schema；透明性（prompt 可检查、中间产物可审计）。

**效果**: F1 最高 **0.859**（Claude 3.5 Sonnet）；Qwen 2.5 Coder 14B **0.009→0.811**（+0.802）。
- Dataset: AIT-LDS 70 日志 × 10 次重复 | Metric: G-Eval | Result: 全模型提升（Qwen 0.008→0.723）
- **反例**: Mistral Large 退化 0.539→0.423——约束收益存在模型相关性
- 关键发现: 结构化输出工具表达力弱于 SHACL，需外层校验兜底

**Wiki**: [[transparent-cti-ontology-shacl]] | **概念**: [[OntologyConstrainedGeneration]] · [[ValidationFeedbackLoop]]

## 新增趋势洞察

1. **推理器从"裁判"进化为"教练"**：[[reasoner-guided-repair-owl2dl]] 的 verdict-only 修复把 OWL 2 DL 蕴含查询忠实度从 43.9% 拉到 97.8%，[[entailllm-vulnerability-verification]] 把 DKG 派生标签回注 prompt 后蕴含路径 +37%——验证器不仅拒绝，还主动改善生成。但两条反例（hint 反噬 −14.4pp、整 manifest 过载）确立"最小充分反馈"设计原则。
2. **SHACL 成为 LLM 生成物校验的事实标准**：7/17 篇使用 SHACL，覆盖四个校验对象——agent 动作（[[g-spec-5g-policy]] 零违规）、查询（[[qraken-graph-distillation]] F1 0.652）、本体（[[llm-capability-ontologies]] 错误分 0.03）、KG（[[transparent-cti-ontology-shacl]] F1 0.009→0.811）；三种反馈去向（修复/解释/拒绝）由 [[kg-repair-shacl-llm]]、[[xpshacl-explainable-validation]]、G-SPEC 分别代表。
3. **描述性经验内容优于规范性 schema 约束**：[[qraken-graph-distillation]] 证明"数据实际长什么样"（TTQL）比"数据应当长什么样"（SHACL-auto）接地 LLM 效果高 64%——约束之外还需分布知识，这对 wiki 的 query 工作流是直接启示。
4. **图 grounding 比模型微调更重要**：[[g-spec-5g-policy]] 消融 NKG 贡献 68% vs TSLAM 微调 8%；[[shacr-smart-home-conflict]] 同一模型加图后 F1 +0.20——"中等 LLM + 强形式化接地"是可复制的工程配方，与 Round 13 [[OntologyFirstAgentDesign]] 的本体优先设计收敛。
5. **LLM 理解 DL 本体随规模非线性坍缩**（[[llm-understand-dllite]]：小本体近 100% → 大 ABox 0%，NI 传递规则指令也救不回），而 [[glamor-owl-consistency-glm]] 证明图语言模型可以 20× 加速近似一致性检查（95.13%）——两者的组合结论：LLM 做语义理解、专用神经/符号推理器做形式裁决，分工边界清晰。

## 知识库状态

| 指标 | 上轮 | 本轮 | 变化 |
|---|---|---|---|
| 论文（source 页） | 348 | 365 | +17 |
| Concept 页面 | 129 | 133 | +4 |
| PDF 文件 | 341 | 357 | +16 |
| Wiki 总页面 | 484 | 505 | +21 |
| 空文件 | 0 | 0 | ✅ |
| 索引同步 | 0 | 0 | ✅ |
| 日志覆盖标记 | 存量误报 | 存量误报 | ℹ️ health.py 期望逐篇标题，log.md 采用轮次汇总格式（历史一致，非本轮回归） |

## 方法说明

- 检索路径：arXiv 搜索页（WebFetch/urllib）+ Semantic Scholar（部分 429，批量接口最终成功获取全部引用数）+ Crossref（DOI-only 论文）
- 全部 16 篇 arXiv 论文下载 PDF 并深度阅读（4 个并行提取代理），5 节结构化分析均含 PDF 正文数据；1 篇 DOI-only（MDPI 全文被拒）标注"仅摘要源"
- 4 处子代理误读的 arXiv ID 已通过 arXiv abs 页逐一验证纠正
