---
title: "When Corrective Hints Hurt（OWL2 DL 推理器引导修复 LLM 过度谨慎）"
type: source
tags: [owl2-reasoning]
sources: [reasoner-guided-repair-owl2dl]
source_file: raw/papers/reasoner-guided-repair-owl2dl.pdf
last_updated: 2026-10-21
arxiv_id: "2604.23398"
authors: ["Yijiashun Qi", "Xiang Xu", "Yuxuan Li"]
year: 2026
venue: "ICAIDE 2026"
citation_count: 3
doi: ""
---

## 概要
论文发现 GPT-5.4 在 OWL 2 DL 合规查询上的一个可复现系统性错误模式：当推理器可推导出否定答案（经 FunctionalProperty 闭包或类不相交性）时，模型频繁答 "unknown" 而非 "no"——101 个错误中 99 个是同一指纹。以 HermiT/Pellet 一致性检查为判定 oracle，比较四种交互模式：直答 43.9%、通用重试 81.7%、推理器裁决+OWA 提示 67.2%（**反而更差**）、仅裁决（verdict-only）**97.8%**。核心警示：推理器-LLM 混合系统中，提示框架比纠正内容更重要。

## 解决的问题
已有 DL 推理基准（DL-ReasonSuite 4k 任务、OntoURL、Wang et al. DL-Lite 评测）只测单次正确率，不测**可审计性**——错误答案能否在有限轮验证反馈内被纠正。本文把可审计性操作化为独立于单次忠实度的第二评测维度，并研究三种反馈机制的修复效果，揭示"解释越多越好"假设的失效条件。

## 方法与技术
1. **一致性试插入判定金标准（Algorithm 1）**：对每个查询构造 O⁺=O∪{C(x)} 与 O⁻=O∪{¬C(x)}，用推理器各跑一次一致性检查：pos∧¬neg→yes，¬pos∧neg→no，皆一致→unknown——区分"推导否定"与开放世界 unknown。推理器 HermiT（Java 11）/ Pellet；片段 OWL 2 DL。
2. **基准集**：10 个人工 mini-本体（38 查询）+ 30 个程序化变体扩展为 180 查询（FunctionalProperty hasSpend + equivalentClass VIPCustomer + AllDisjointClasses + 链式等价类的笛卡尔网格）+ 18 个保险/临床领域 held-out 查询。
3. **四种交互模式（匹配预算）**：direct（单次 JSON 作答）；naïve repair（"你的答案错了，重新考虑"）；cx repair v1（推理器裁决 + OWA 提示 "consider OWA: missing triples are not negations"）；cx repair v3（仅推理器裁决，无提示）。
4. **统计方法**：Wilson 95% CI；McNemar 精确双侧检验 + Bonferroni 校正（α=0.01）。
5. **跨模型描述性对照**：GLM-5、Kimi-k2.5、Minimax-2.7（开发集，非受控比较）。

## 创新点
- **vs DL-ReasonSuite/OntoURL 等大规模基准**：以规模换逐查询推理器审计，首次将"可审计性"（≤k 轮反馈后错误被纠正的条件概率）作为独立评测轴。
- **vs "解释越多越好"假设（Explanation-Refiner 类系统）**：逻辑正确但模式错配的 OWA 提示使修复比 generic retry 差 14.4pp——推理器-LLM 混合系统的提示框架比纠正内容本身更重要。
- **vs 通用 retry**：verdict-only 模板更便宜且更准（97.8% vs 81.7%，修复轮数 1.63 vs 1.93）。

## 效果
- Dataset: 180 查询扩展集（GPT-5.4）| Metric: 忠实度（最终答案与推理器裁决一致率）| Result: direct **43.9%** → naïve retry **81.7%** → verdict+hint **67.2%** → verdict-only **97.8%**（CI [94.4, 99.1]）
- Dataset: 同上 | Metric: McNemar 两两差异（全部 p<10⁻⁵）| Result: direct→verdict-only **+53.9pp**（p=1.3×10⁻²⁹）；naïve→hint **−14.4pp**；hint→verdict-only +30.6pp
- **失败指纹**：direct 模式 101 错误中 **99 个**为 "expected=no, got=unknown"——结构化过度谨慎而非随机幻觉；held-out 18 查询同指纹 4/4
- **消融**：hint 变体 59 个错误中 56 个仍是指纹错误（尽管 3 轮反馈都告知正确答案）；verdict-only 仅 4 个
- 成本：verdict-only 4.77s/查询、平均 1.63 轮，比 hint 变体省 16% 修复成本
- 跨模型（开发集 direct）：GLM-5 38/38、Kimi-k2.5 36/38、Minimax-2.7 29/30

## 关键引用
> "Of the 101 errors GPT-5.4 makes in direct mode on the expansion set, 99 share the exact pattern 'expected=no, got=unknown'. The failure is therefore not random hallucination but structural overcaution against entailed negation." — Section IV.C

> "A natural assumption in reasoner–LLM hybrid systems is that more reasoner output ⇒ better LLM correction. Our data refute this." — Section V.C

## 关联
- [[ReasonerGuidedRepair]] — 本论文是该概念的命名来源与核心实证：verdict-only 原则
- [[LLMReasonerHybrid]] — Round 18"推理器做 LLM 输出法官"的修复环扩展：法官不仅打分还参与修复
- [[ontology-grounded-reasoner-benchmarks]] — 同为推理器验证 LLM 推理的评测工作，本文加"可审计性"维度
- [[owl2dl-differentiable-circuits]] — 同为 OWL 2 DL（SROIQ）片段上的推理工作，Baobab 走可微编译路线
- [[VerificationCoEvolution]] — 验证器（推理器提示词）与生成器（LLM）需协同设计，否则修复反噬

## 矛盾
- "给 LLM 更多推理器上下文更好"的直觉被直接证伪：含正确逻辑提示的修复反而差 14.4pp——与 Explanation-Refiner 类系统的设计假设冲突
