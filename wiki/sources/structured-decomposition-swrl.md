---
title: "Structured Decomposition for LLM Reasoning（LLM填充ABox+SWRL确定性推理）"
type: source
tags: [owl2-reasoning]
sources: [structured-decomposition-swrl]
source_file: raw/papers/structured-decomposition-swrl.pdf
last_updated: 2026-10-21
arxiv_id: "2601.01609"
authors: ["Albert Sadowski", "Jarosław A. Chudziak"]
year: 2026
venue: "arXiv preprint"
citation_count: 2
doi: ""
---

## 概要
Structured Decomposition（SD）框架将 LLM 定位为**本体填充引擎（ontology population engine）**：LLM 只负责把自然语言文本翻译为 OWL ABox 断言，最终分类决策完全交给 SWRL 规则 + Pellet 推理器确定性执行。任务定义由专家编写的 TBox 提供（实体描述、断言规范以 annotation 编码在本体内），同一本体既驱动符号推理又生成 LLM 提示。在法律 hearsay、科学文献方法-任务关系、临床资格 3 领域 × 11 个 LLM 上验证，总体 F1 79.8% 显著超过 few-shot 基线，且消融证明符号验证贡献独立于提示结构。

## 解决的问题
LLM 擅长解释非结构化文本但无法保证规则应用的一致性，符号系统有形式化保证却无法消化自由文本——SD 要弥合这个鸿沟并给出可审计决策。直接改进对象是其自身 prior work（structured decomposition + JSON schema + SMT 验证）：该方法仅在单一法律 hearsay 任务上验证、依赖 ad-hoc 表示，缺乏与语义网标准工具链的互操作性。对比 NL2FOL（FOL+SMT）、Thought-Like-Pro（Prolog CoT）等定制符号形式体系同样存在"不可复用、不可组合领域词汇表"的缺陷。

## 方法与技术
1. **LLM 两步本体填充**：entity identification（按 TBox 类定义抽取 individual）+ assertion extraction（对每个断言规范做 true/false 判定并映射为 OWL 类断言或对象属性）；任务定义完全由专家 TBox 提供，LLM 无需自行设计表示。
2. **OWL 2 本体 + SWRL 规则编码任务谓词**：分类逻辑写成 SWRL 合取规则（如 hearsay 的 5 条件合取）；任务级提示元数据以 annotation 编码在本体内，实现"同一本体驱动符号推理与神经解释"。
3. **Pellet 推理器执行**：对填充后的 ABox 做一致性检查、分类与 SWRL 规则执行，目标类成员资格即预测结果；每个测试实例用全新 OWL world 保证隔离（owlready2 v0.45 + LangChain + Pydantic 结构化输出）。
4. **互补谓词（complementary predicates）作为实验变量**：成对正/反断言（IsOutOfCourt/IsInCourt）应对 OWA 下确认偏误——prior work 的默认组件在本文明确定位为待检验变量。
5. **任务适用性判据 + 负验证**：适用条件为（a）规则可表达的决策边界 +（b）可形式化谓词结构；用 DDXPlus 的 URTI 诊断任务做负例（可形式化谓词但决策边界是统计性的）验证判据有效性。

## 创新点
- **vs 自身 prior work（JSON schema + SMT）**：用 OWL 2/SWRL 语义网标准替换 ad-hoc 表示——任务定义可在 Protégé 编辑、ABox 可 SPARQL 查询、可组合导入 SNOMED-CT/FIBO 等领域词汇表。
- **vs NL2FOL 等翻译管线**："本体填充 + SWRL 推理"替代"ad-hoc FOL 翻译 + SMT 验证"，且首次跨 3 领域 × 11 个 LLM 验证泛化性。
- **vs 纯提示工程（CoT/Decomposed Prompting）**：引入外部符号验证的架构级改变，消融证明其贡献独立于提示结构。

## 效果
- Dataset: LegalBench hearsay + SciERC Used-For + NLI4CT（各 94 test）| Metric: 总体 F1 | Result: SD **79.8%** | Baseline: few-shot 75.2% / CoT 74.1% | Δ: +4.6pp（t(32)=2.88, p=0.007）/ +5.7pp（p=0.008）
- Dataset: 3 任务合并 | Metric: F1（SD vs SD-Direct 去掉 SWRL 验证）| Result: **79.8% vs 70.1%** | Δ: +9.7pp（p=0.001, d=0.65）；且 SD-Direct 反而低于 few-shot 基线（70.1% vs 75.2%）
- **消融**：只给结构化断言规范不给符号验证会伤害性能；分任务 SD vs SD-Direct 临床资格 74.5% vs 54.6%（−19.9pp）差距最大
- **消融**：召回率 SD 84.7% vs few-shot 69.0%（+15.7pp, p<0.001, d=1.22），精确率略降（79.4% vs 85.3%）
- **消融**：互补谓词反而有害——SD 79.8% vs SD-C 74.8%（−5.0pp），与 prior work 结论相反
- **负验证**：URTI/DDXPlus 上 SD 仅 0.145 F1 vs few-shot 0.979——确认适用性判据（统计边界任务不适用）
- 模型层面：o3 平均 +9.5pp（SD 84.7% F1 最高）；大模型受益大于小模型（Gemini Pro +6.9pp vs Flash −1.1pp）

## 关键引用
> "The critical insight is that LLMs excel at the interpretive work symbolic systems cannot perform, while symbolic systems provide the verification guarantees LLMs cannot offer." — Section 1, p.3

> "providing structured assertion specifications without symbolic verification actually degrades performance compared to few-shot prompting (70.1% vs. 75.2% F1)." — Section 6.2, p.15

> "The difficulty lies not in the complexity of the rule but in the accumulation of small extraction errors across predicates... Symbolic verification eliminates one source of error entirely, yielding improvements even when the underlying logic is trivial." — Section 7.2, p.19

## 关联
- [[ReasonerGuidedRepair]] — 同属"推理器校验 LLM 输出"谱系，但 SD 是事前分工（LLM 只填 ABox）而非事后修复
- [[OntologyConstrainedGeneration]] — LLM 输出被 TBox 断言规范严格约束的极致形态
- [[LLMReasonerHybrid]] — Round 18 提出的 LLM-推理器混合概念的本管带实例：Pellet 做法官
- [[satir-constraint-ir-clinical]] — 同为"约束满足替代相似性"思路，SATIR 用 SMT、SD 用 SWRL
- [[llm-active-learning-owl]] — 同样利用 OWL 推理任务（子sumption/一致性）与 LLM 协作的本体工程

## 矛盾
- 互补谓词消融结果（−5.0pp）与其自身 prior work 的默认建议相反——prior work 认为 OWA 下需要正/反成对断言防确认偏误，本文实证其为净伤害
