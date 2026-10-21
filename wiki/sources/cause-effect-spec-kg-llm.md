---
title: "Automating Cause-Effect Specification（KG+SWRL 安全联锁规格自动生成）"
type: source
tags: [owl2-reasoning]
sources: [cause-effect-spec-kg-llm]
source_file: raw/papers/cause-effect-spec-kg-llm.pdf
last_updated: 2026-10-21
arxiv_id: "2606.31614"
authors: ["Javal Vyas", "Milapji Singh Gill", "Mehmet Mercangöz"]
year: 2026
venue: "arXiv preprint (IFAC format)"
citation_count: 0
doi: ""
---

## 概要
面向流程工业安全工程：interlock 清单、报警 rationalization 表、C&E（cause-and-effect）矩阵的创建仍靠手工且易不一致。本文提出语义-AI 框架——知识图谱（CPSMod 对齐本体）先通过 SPARQL CONSTRUCT 自动**物化**出 C&E 行，再由严格约束的 LLM（gpt-4o-mini）把每行转换为操作员安全叙事 + 同语义 SWRL 规则。LLM 角色"interpretive rather than generative"：禁止发明本体中不存在的阈值/位号/设备，语义接地率 100%、零幻觉设备。

## 解决的问题
C&E 规格创建仍 predominantly 手工、文档驱动。已有路线各有不足：CERN CEM 规范只给手工矩阵严格语义；从 P&ID/HAZOP 抽取的方法（Thambirajah 2009、Single 2020）靠程序化启发式、无形式语义、难验证复用；LLM 生成 SWRL 的现有工作（Laurenzi 2024、Soularidis 2024）缺乏流程工程语义与 KG 接地。缺口：没有框架能从过程 KG 自动生成语义接地、机器可验证的 C&E 规格，同时产出叙事文本与 SWRL 规则。

## 方法与技术
1. **五层管线**：Data（P&ID、PLC 逻辑、仿真、设备规格）→ Mapping（RML/R2RML 语义提升为 RDF）→ Knowledge（CPSMod 对齐本体 KG）→ C&E Generation（SPARQL CONSTRUCT 物化）→ Validation（约束 LLM + 人在环审核）。
2. **CPSMod 对齐本体**复用 5 组 ODP：VDI 3682（功能/过程操作符）、VDI 2206（系统-模块-组件）、DIN 17359（特征-症状-故障诊断链）、UML StateMachine ODP（离散行为/守卫条件）、OpenMath ODP（连续动力学方程），离散+连续行为都锚定在功能模型上。
3. **DIN 17359 fault class 模板**：不逐设备手工定义故障，而是模板化复现诊断模式（阀门半开/卡死/泄漏、泵降额/气蚀、管路堵塞等），模板经 SPARQL UPDATE 实例化到具体设备。
4. **SPARQL CONSTRUCT 自动物化 CauseEffectRow**：从 :SafetyAction 入口沿 :mitigatesFault → DiagnosticSubjectHasFault → FaultIsDescribedBySymptom → CausesFault → occursInMode 遍历诊断图逐行生成——除模板外零手工 C&E 逻辑。
5. **约束 LLM 转换层**：prompt 明令禁止发明新阈值/位号/设备；每行产出操作员安全叙事 + SWRL 规则双工件（SWRL 只允许引用本体已有类/属性/个体）；随后自动验证冲突、不可达与冗余规则。

## 创新点
- **vs Soularidis et al. 2024（LLM 从自然语言生成 SWRL）**：SWRL 从 KG 物化的 C&E 行生成，语义接地率 100% 而非自由发挥。
- **vs CERN CEM 手工矩阵**：规格由单一语义源自动派生，一致性"by construction 而非靠评审"。
- **vs Thambirajah/Single 启发式抽取**：SWRL 可被标准规则引擎（Jess/Drools）做冲突、冗余、不变量分析——形式语义带来机器可验证性。
- 单一 KG 源同时产出三种互相一致的工件：正式 C&E 表 + 操作员叙事 + 机器可验证 SWRL 规则库。

## 效果
- Case: 模块化流程厂（混合模块 B201–B204 + 灌装模块 B401–B402）| Metric: C&E 行数 | Result: **15 条**，覆盖 8 故障 / 8 诊断对象 / 6 缓解动作；actions-per-fault 比 **1.00**
- Metric: 语义接地率（KG 实体）| Result: **100%**；SWRL 规则语法有效率 **100%**
- Metric: 检出动作冲突 | Result: **0**；不可达/冗余规则 **0**
- 叙事定性评估：零幻觉设备、零虚构故障模式（论文明确为 qualitative evaluation，量化指标待补充）
- 规模属可行性验证（无 baseline 对比数字）——具体数值待补充

## 关键引用
> "KGs alone cannot autonomously derive specification logic, and free-form LLM outputs lack the guarantees of formal syntax and verifiability required for safety-critical automation." — Section 1, p.1

> "The LLM's role is therefore interpretive rather than generative: it reformulates the formally defined C&E logic into operator-facing text and into rule syntax while preserving the semantics encoded in the KG." — Section 3.3(iii), p.3

> "No hallucinated equipment or spurious failure modes were produced, demonstrating the effectiveness of constraining the LLM with KG-derived context." — Section 5.2, p.4

## 关联
- [[OntologyConstrainedGeneration]] — 本体约束 LLM 生成的干净范例：生成 SWRL 规则 + 自然语言叙事双工件
- [[OntologyFirstAgentDesign]] — CPSMod 模块化 ODP 对齐本体是本体优先设计的工程实例
- [[structured-decomposition-swrl]] — 同用 SWRL 规则层，方向相反：SD 让 LLM 填 ABox 后推理，本文让推理器物化后 LLM 转写
- [[deontic-policies-agenticrei]] — 同为"LLM 外规则层治理"思路，道义策略 vs 安全联锁
- [[intent-driven-smart-manufacturing]] — 同为制造域"NL 意图→本体对齐结构化表示"翻译
