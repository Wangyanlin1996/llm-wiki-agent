---
title: "RareDxR1: 罕见病自主医学推理超越人工标注（Autonomous Medical Reasoning for Rare Disease Diagnosis）"
type: source
tags: [ontology-precise-retrieval]
sources: [raredxr1-rare-disease]
source_file: raw/papers/raredxr1-rare-disease.pdf
last_updated: 2026-09-08
arxiv_id: "2607.00147"
authors: ["Deyang Jiang", "Haoran Wu", "Ziyi Wang", "Yiming Rong", "Yunlong Zhao"]
year: 2026
venue: "IEEE ICME 2026"
citation_count: 0
---

## 概要
RareDxR1 是一个端到端推理型大语言模型，专用于从非结构化临床笔记直接进行罕见病诊断，无需 phenotype 提取或 RAG。通过知识内化（Knowledge Internalization）与自主进化学习（RERS + DCRL）的两阶段训练框架，将碎片化罕见病知识编码进模型参数。14B 参数模型在多个 benchmark 上超越 671B 的 DeepSeek-R1，并在未见疾病的 zero-shot 设置中实现 50.00% Top-10 Recall（vs baseline 28.85%）。

## 解决的问题
现有 AI 方法依赖 pipeline 式 phenotype 提取或 RAG，因预定义 ontology、检索瓶颈和缺乏诊断逻辑导致关键信息丢失。传统方法受限于封闭标签空间，难以识别未见疾病；Medical-LLM 缺乏长尾疾病覆盖且推理不足。标准 Rejection Sampling 在罕见病场景效率低下——通用模型极少生成正确初始解，丢弃错误样本浪费了从失败中学习的宝贵机会。

## 方法与技术
1. **Knowledge Internalization (RareKnowledgeQA)**：将 HPO/Orphanet/OMIM 结构化数据与 PubMed 非结构化文献统一为 QA 对，用规则模板+LLM 生成混合方式编码进模型参数。
2. **Reflection-Enhanced Reasoning Sampling (RERS)**：对 teacher 模型（DeepSeek-R1）失败轨迹，注入检索知识 K 和专家反馈 E 进行自我纠正，将"失败"转化为密集训练信号；配合随机信息掩码+知识约束过滤确保鲁棒性。
3. **Dual-Level Curriculum RL (DCRL)**：基于 DAPO 框架，Task-level（鉴别诊断→最终诊断）和 Case-level（四档难度分层）双维度渐进训练。
4. **Collaborative Reasoning Refinement (CRR)**：推理阶段聚合外部模型诊断 E 和检索知识 K，由 RareDxR1 作为主诊断医师综合初始假设生成最终诊断。

## 创新点
- **首次提出端到端从非结构化临床笔记直接诊断罕见病的推理型 LLM**（vs PhenoBrain 封闭集方法和 RAG 方法）——无需 phenotype 提取步骤。
- **RERS 创新性地从失败轨迹学习**（vs 标准 RS 丢弃策略）——weak-to-strong generalization，使 14B 模型仅经 SFT 即超越 671B teacher。
- **DCRL 双层级课程**（vs Med-R1/Med-RLVR 聚焦通用医学 QA）——将推理能力与领域知识解耦优化。
- **CRR 验证了模型间互补诊断优势**——利用 RERS 培养的批判能力进行多模型协作推理。

## 效果
- Dataset: RareArena-Test (ID) | Metric: Top-1 | Result: 60.29% | Baseline: 44.20% (DeepSeek-R1-671B) | Δ: [+16.09%]
- Dataset: RareArena-Test (ID) | Metric: Top-10 | Result: 78.73% | Baseline: 59.02% | Δ: [+19.71%]
- Dataset: MIMIC-IV-Rare (OOD) | Metric: Top-10 | Result: 69.83% | Baseline: 54.58% | Δ: [+15.25%]
- Dataset: RareArena Zero-shot (unseen) | Metric: Top-10 | Result: 50.00% | Baseline: 28.85% | Δ: [+21.15%]
- **Ablation**: SFT w/o RERS: Top-1 45.85→47.12 (+1.27) — RERS 贡献
- **Ablation**: SFT+RL w/o Curriculum: Top-10 65.56→69.27 (+3.71) — 课程学习贡献
- **Ablation**: Base → Full: Top-1 25.76→52.29 (+26.53) — 全管线贡献

## 关键引用
> "Standard Rejection Sampling (RS) is inefficient as it discards the vast majority of trajectories where the teacher model fails." — Section III.D, p.3

> "a 'weak-to-strong' generalization phenomenon was observed. Even though powerful models like DeepSeek-R1-671B served as teachers in the generation of our RareDxCOT, our model, after only SFT, substantially surpassed its teachers' performance." — Section IV.C, p.5

> "RareDxR1 demonstrates robust cross-modal transfer without phenotype training. Despite operating in a more challenging open-domain setting compared to PhenoBrain's closed-set paradigm, it outperforms this specialized SOTA." — Section IV.D, p.5

## 关联
- [[OntologyGraphRetrieval]] — 本体图检索核心概念
- [[deeproot-kg-multi-agent]] — Round 16 KG 协调多 Agent 医疗推理
- [[neuron-clinical-explainability]] — Round 13 SNOMED CT 临床可解释性
- [[qime-ontology-embeddings]] — Round 10 本体驱动医学嵌入
- [[satir-constraint-ir-clinical]] — 本轮约束满足临床试验检索
