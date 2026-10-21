---
title: "From Rule Engines to Ontologies（OWL 2 DL 本体驱动评估信息系统）"
type: source
tags: [owl2-reasoning]
sources: [rule-engines-to-ontologies]
source_file: raw/papers/rule-engines-to-ontologies.md
last_updated: 2026-10-21
arxiv_id: ""
authors: ["Borivoj Bogdanović", "Siniša Nikolić"]
year: 2026
venue: "Computers (MDPI) 15(8):544"
citation_count: 0
doi: "10.3390/computers15080544"
---

> ⚠️ PDF deep reading incomplete — content based on abstract only（MDPI 全文抓取被拒，仅有摘要源；关键引用均出自 Abstract）

## 概要
纯工程应用论文：用 OWL 2 DL 本体统一领域信息系统原本分离的三类工件（数据模型、规则库、应用基础设施），构成"可验证的本体到代码"管线。HermiT 在代码生成前于开放世界语义（OWA）下验证一致性、可满足性与包含检查；生成器产出四层 Java 应用；运行时按封闭世界语义（CWA）评估记录，重叠类目用本体声明的优先级消解。塞尔维亚科研评价案例中，生成系统完全复现了既有 Jess 规则引擎实现的 M30/M33 分类。

## 解决的问题
领域专用信息系统通常把数据模型、规则库、应用基础设施维护为分离工件，导致维护与部署前验证复杂化。研究问题：这些工件能否统一进一条可验证的本体到代码管线且不改变既定分类结果。对照基线是既有 Jess 规则引擎实现——分类规则以过程式规则表达、无形式化验证。

## 方法与技术
1. **模型驱动架构（MDA）**：Business Application Builder 框架 + OWL 2 DL 本体同时表达领域结构、分类规则与生成元数据（三合一）。
2. **HermiT 作为生成前验证门**：代码生成前执行一致性检查、可满足性检查、包含检查（subsumption），全部在 OWA 下进行。
3. **代码生成器**：产出持久化、业务逻辑、数据传输、表示四层 Java 应用。
4. **双语义设计**：生成的 Java 应用运行时按 CWA 评估存储记录；重叠类目消解规则（优先级）本身编码进本体。
5. **验证方式**：用生成系统复现既有 Jess 实现的 M30、M33 分类；内部二次实验以 HermiT 蕴含为金标准对照运行时分类。

## 创新点
- **vs Jess 规则引擎 + 分离工件**：以形式验证过的 OWL 2 DL 本体为单一事实来源，生成前即可做一致性/可满足性/包含检查。
- **vs 单一语义系统**：推理期 OWA（可靠、可审计）与运行期 CWA（可执行、确定性）的显式分工，重叠类目消解编码进本体。
- **边界声明（反创新）**：明确不声称通用——算术风险计算与时间性事件处理仍更适合过程式技术。

## 效果
- Case: 塞尔维亚科研评价系统 | Metric: 分类复现 | Result: 生成系统**完全复现**既有 Jess 实现的 M30 与 M33 分类
- Case: 产前诊断应用（内部二次实验）| Metric: 运行时分类与 HermiT 蕴含一致率 | Result: **6/6 全部一致**
- 公开工件仅复现本体级实验（生成器与生成源码专有）；论文明言 "No performance superiority is claimed"
- 本体规模（公理/类/规则数量）等：具体数值待补充

## 关键引用
> "HermiT verifies consistency, satisfiability, and subsumption under open-world semantics before code generation." — Abstract

> "In a Serbian research-evaluation case study, the generated system reproduced the M30 and M33 classifications of an established Jess implementation." — Abstract

> "An internal secondary experiment generated and executed a prenatal-diagnosis application; all six runtime classifications matched the HermiT entailments and expected outcomes." — Abstract

## 关联
- [[OntologyReasoning]] — OWL 2 DL 全谱系推理任务（一致性/可满足性/包含）作为工程验证门的直接应用
- 其对比对象 Jess 规则引擎与 [[OntologyReasoningEngine]] 的 Datalog 物化路线同为规则推理基础设施
- [[agentic-redux]] — 同为"本体作为经形式验证的单一事实来源"工程哲学
- [[structured-decomposition-swrl]] — 互补视角：本文推理器门控代码生成（无 LLM），SD 推理器门控 LLM 输出
