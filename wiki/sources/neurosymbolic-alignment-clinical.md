---
title: "Neurosymbolic Alignment（生理世界模型对齐临床 LLM）"
type: source
tags: [owl2-reasoning]
sources: [neurosymbolic-alignment-clinical]
source_file: raw/papers/neurosymbolic-alignment-clinical.pdf
last_updated: 2026-10-21
arxiv_id: "2608.24534"
authors: ["Abdulhady Abas Abdullah", "Erik Cambria", "Milena Živković"]
year: 2026
venue: "IEEE J-BHI (在投)"
citation_count: 0
doi: ""
---

## 概要
临床 LLM 会产出"事实正确但生理不安全"的推荐（加重高钾血症、忽略情境性禁忌）——事实正确性≠临床安全。本文提出训练时对齐框架：异构生物医学 KG（847,392 节点/3,241,567 边，整合 UMLS/DrugBank/Reactome/HPO 等 8 源）+ HGNN 生理可行性评分器（PhysioScore = 体内稳态门控 × 路径合理性 × 药物相互作用惩罚）自动生成偏好对，驱动迭代 ORPO 更新 Mistral-7B。关键设计：**HGNN 只在训练期使用，推理期只有对齐后的 LLM**（无图推理延迟）。CSS 69.5%→90.8%（+21.3pp），反循环论证设计用三个 HGNN 独立端点（规则引擎 RSS、DID、盲评医生 HR）做三角验证。

## 解决的问题
临床 LLM 事实正确但生理不安全：RAG 只改善证据获取、医学微调只改善术语风格，都不直接强制多步推荐中的生理一致性；偏好优化（DPO/ORPO/KTO/SimPO）受限于细微 relational violation 的偏好标注数据的可得性与质量。缺口：用结构化生理知识在**训练时**自动生成偏好信号做安全对齐，替代昂贵的临床医生人工标注。

## 方法与技术
1. **Physiological World Model**：异构生物医学 KG（847,392 节点/3,241,567 边），整合 UMLS、DrugBank 5.1、Reactome、HPO、SIDER、PharmGKB、DisGeNET、STRING 八源；12 种节点类型（Drug/Disease/Organ/Pathway 等）。
2. **HGNN 生理可行性评分器**：4 层 relation-aware HGNN（R-GAT, L=4, H=8, 256 维，链接预测预训练）；**PhysioScore = S_hom · σ(S_path) · (1 − P_int)**（乘法组合：任一环节不安全即整体趋零）——体内稳态软边界门控 × ≤3 跳路径合理性 × 药物相互作用惩罚；实体抽取 scispaCy→UMLS 链接。
3. **Iterative ORPO（T=5 轮）**：每轮从当前策略 on-policy 采样 K=8 候选响应，HGNN 排名诱导偏好对；损失 L_SFT + λ(t)L_OR + γL_KG，线性课程 λ(t)=λ₀(1+αt)。
4. **Clinical Safety Benchmark (CSB)**：2,500 专家撰写的生理约束违规场景（1750/250/500）；防泄漏：独立撰写测试集、时间新颖性切分、实体级 Jaccard<0.40 过滤、扣留 15% KG 药物实体及其边。
5. **反循环论证设计**：CSS/PC 由训练所用同一 HGNN 计算，另设三个 HGNN 完全独立端点（RSS 规则引擎、DID 禁忌对识别、5 位医生盲评 HR，κ=0.84）做三角验证，CSS–RSS 一致性 r=0.97。

## 创新点
- **vs ORPO（5K 人类偏好标注）**：CSS 90.8% vs 69.5%（+21.3pp）——HGNN 自动生成偏好对替代临床医生人工撰写。
- **vs 推理时自纠（SFT+SelfCorrect：生成→规则引擎检查→重生成≤3 轮）**：CSS +11.4pp（90.8 vs 79.4）——训练时对齐胜过运行时 guardrail。
- **vs GPT-4 (5-shot)**：所有安全指标胜出（CSS 90.8 vs 80.6）但参数少 10×（GPT-4 仅保留 MA 优势 +3.9pp）。
- 训练时用图、推理时不用图的部署经济性设计——与推理时 SHACL 校验路线形成互补光谱。

## 效果
- Dataset: CSB 2,500 场景 | Metric: CSS（零违规响应比例）| Result: ORPO 69.5% → **90.8%**（+21.3pp，Bonferroni p<10⁻⁴，5 种子）
- Dataset: 同上 | Metric: RSS（HGNN 独立规则引擎端点）| Result: 65.2% → **86.4%**（+21.2pp）；CSS–RSS 一致性 r=0.97
- Dataset: 600 响应医生盲评 | Metric: HR 不安全率 | Result: 14.1% → **5.1%**（−9.0pp）；重度幻觉 3.7%→0.4%
- Dataset: 同上 | Metric: DID 禁忌药物对识别 F1 | Result: 72.8% → **91.6%**（+18.8pp）；MA 医学问答 70.1→75.2（+5.1pp，未牺牲通用能力）；vs SFT+RAG：CSS +27.6pp
- **消融**：去 HGNN 评分 **−16.2pp**；去迭代训练 −11.5pp；分量 S_hom −8.7pp、P_int −6.5pp、S_path −3.9pp
- 校准：PhysioScore ECE=0.038、κ=0.91；噪声鲁棒性：三重扰动下保留 84.2% CSS；残余违规 9.2%（主因：图覆盖稀疏 4.2%、多系统交互 3.1%、缺时间生理学 2.8%）；成本 42.6 GPU-hours（8×A100）

## 关键引用
> "A response may contain correct biomedical facts while still proposing an action that is incompatible with the implied patient state, for example by worsening hyperkalemia or ignoring context-dependent contraindications. Therefore, factual correctness alone is insufficient for clinical safety." — Section I

> "The design objective is to improve safety during training while keeping deployment simple: the HGNN scorer is used only during alignment, and inference uses the aligned LLM alone." — Section I

> "Until such validation is completed, the results should be interpreted as evidence of mechanism effectiveness on a controlled benchmark rather than as deployment-ready safety guarantees." — Section VI-B

## 关联
- [[ReasonerGuidedRepair]] — "推理结果辅助 LLM"的训练时变体：世界模型评分替代推理器 verdict 驱动对齐
- [[ValidationFeedbackLoop]] — 与推理时校验（SHACL/verdict）互补的离线对齐路线；反循环论证设计是校验管线的方法学贡献
- [[neuron-clinical-explainability]] — 同为 SNOMED/UMLS 类生物医学本体+临床场景，NEURON 推理时检索、本文训练时对齐
- [[deeproot-kg-multi-agent]] — 同为医疗 KG 抑制 LLM 错误，DeepRoot 构建验证 KG 查询、本文 HGNN 排序偏好
- [[provenance-authorization]] — 同为"独立验证器防循环论证"设计哲学（AuthGraph 双图对齐 vs 三端点三角验证）

## 矛盾
- 与 OWL/SHACL 符号路线不同：KG 未做形式本体建模，是统计图推理（GNN）而非符号逻辑——安全保证是概率性的（CSS 90.8% 而非 100%），与 G-SPEC 的确定性零违规形成光谱两端
