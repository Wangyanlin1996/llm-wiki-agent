---
title: "Neuro-symbolic learning over OWL 2 DL via Consequence-based Compilation to Differentiable Circuits（Baobab：SROIQ编译为可微电路）"
type: source
tags: [ontology-reasoning, llm-reasoner-hybrid, neuro-symbolic]
sources: [owl2dl-differentiable-circuits]
source_file: raw/papers/owl2dl-differentiable-circuits.pdf
last_updated: 2026-10-09
arxiv_id: "2608.17741"
authors: ["Olga Mashkova", "Asaad Mohammedsaleh", "Fernando Zhapa-Camacho", "Robert Hoehndorf"]
year: 2026
venue: "arXiv (KAUST)"
citation_count: 0
---

## 概要

Baobab 将 **SROIQ（OWL 2 DL 的基础描述逻辑）本体编译为 Sentential Decision Diagram（SDD）**，支持在**非 Horn 描述逻辑**上做可微神经符号学习。它用基于后果（consequence-based）演算饱和命题核心（ALCHOQ），再在活跃域上实例化 SROIQ 特有特征（nominals、数量限制、角色公理）。SDD 的证据条件加权模型计数（WMC）作为训练信号，驱动感知网络在部分 ABox 监督下识别真实图像并恢复本体潜在概念。更重要的是：当监督允许多个本体一致补全时，独立感知会"坍缩"到单一补全（推理捷径），本文证明以查询 justification 索引的**混合分布**能表示校准后验，并用电路枚举的补全做种子，在真实图像 MNIST 任务上达到贝叶斯最优后验——首个刻画并缓解非 Horn DL 中推理捷径的工作。

## 解决的问题

神经符号学习器分两大族：嵌入法（EL Embeddings、OWL2Vec*、BoxEL、Box2EL、FALCON）把本体投到连续空间，**丢失经典蕴含**（满足损失却违反本体蕴含）；知识编译法（DeepProbLog、Semantic Loss、SPL、Scallop、NeuPSL）计算编译约束的 WMC，但**仅限命题公式或 Datalog 形程序**——针对 DL 本体的方法只覆盖 ALC 或 Horn profile。SROIQ 的析取、经典否定、限定基数、nominals 与完整角色公理族使 Horn-only 饱和演算无法处理。此外，多一致补全下独立感知的"推理捷径"问题此前未在非 Horn DL 中被刻画与缓解。

## 方法与技术

1. **SROIQ→SDD 编译**：接受任意 OWL 2 DL 本体，结合 ALCHOQ 命题核心的基于后果饱和（Sequoia/ELK 谱系）与 SROIQ 扩展（nominals、限定基数、六类角色公理）的有限域 grounding；OWL loader 将每种公理映射到编译器语法——grounding 覆盖的片段上 sound。
2. **证据条件 WMC 训练**：SDD 的 WMC 对感知网络可微（感知后验逐原子）；部分 ABox 监督下训练 CNN 识别真实图像（MNIST 数字 + 后继关系耦合），从未直接标注的 ABox 中恢复潜在本体概念。
3. **JustWMC 混合**：监督允许多一致补全时，以查询 justification 索引的混合分布表示校准后验；用电路枚举的补全作为种子初始化，达贝叶斯最优校准后验。
4. **Lean 4 机器验证**：编译器与表示结果的 soundness 经 Lean 4 机器证明。
5. **真实本体验证**：同一工作流驱动 ResNet 通过 Pizzaiolo OWL 本体的角色片段，恢复潜在披萨类。

## 创新点

- **首个支持非 Horn（SROIQ 全特征）本体的知识编译型 NeSy 学习器**——23% 的 SROIQ 公理超出 DeepProbLog 的 Horn 片段（per-axiom 对比）。
- 首个在非 Horn DL 中**刻画并缓解推理捷径**：单 WMC 与 BEARS 集合假设类无法达贝叶斯最优，JustWMC 可以。
- 相对嵌入法：端到端保留经典语义（WMC 恰为"采样世界满足本体"的概率），不牺牲可微训练。
- 编译器 soundness 与表示结果 Lean 4 机器证明——工程正确性背书。

## 效果

- **潜在概念学习（MNIST）**：部分 ABox 监督下感知恢复从未直接展示的潜在概念（digit identity 0.25→**0.99**），本体违反驱动到 0，独立感知停在随机水平。
- **多一致补全（推理捷径）**：真实图像 MNIST 任务上 JustWMC 达贝叶斯最优校准后验；单 WMC 与 BEARS 集合假设类不能。
- **覆盖度**：per-axiom 对比显示 23% 的 SROIQ 公理超出 DeepProbLog Horn 片段。
- **真实本体**：ResNet 经 Pizzaiolo 角色片段恢复潜在披萨类。
- 代码：github.com/bio-ontology-research-group/baobab。

## 关键引用

> "We present Baobab, which compiles a SROIQ ontology with a finite ABox into a Sentential Decision Diagram (SDD): it saturates a propositional core under a consequence-based calculus and instantiates the remaining SROIQ features over the active domain." — Abstract

> "on an ontology that exercises every distinctive SROIQ feature, a CNN learns to read MNIST digits coupled by a successor relation and recovers latent ontology concepts that an independent perception leaves at chance." — Abstract

> "to our knowledge the first to characterize and mitigate reasoning shortcuts in a non-Horn description logic." — Abstract

## 关联

- [[OntologyReasoning]] — SROIQ 全特征编译是本概念页"从符号推理器到可微编译"路线的前沿。
- [[dl-ontologies-probabilistic-circuits]] — 姊妹工作：均为"本体→可微电路"；Baobab 支持完整 SROIQ 非 Horn 特征并关注推理捷径。
- [[NeurosymbolicOrchestration]] — 本体的 SDD 表示是神经符号编排中"符号可验证执行"的可微落地。
- [[VerificationCoEvolution]] — 推理捷径的刻画呼应"验证与生成协同演化"：单一感知无法校准多补全后验。
