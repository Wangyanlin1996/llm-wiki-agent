---
title: "RARE：高相似语料的冗余感知检索评估框架"
type: source
tags: ['semantic-retrieval', 'evaluation']
sources: [rare-redundancy-eval]
source_file: raw/papers/rare-redundancy-eval.pdf
last_updated: 2026-07-02
arxiv_id: "2604.19047"
authors: ["Hanjun Cho", "Jay-Yoon Lee"]
year: 2026
venue: "ACL 2026"
citation_count: pending
---

## 概要

现有 QA 基准假设文档间最小重叠，但真实 RAG 系统运行于金融报告、法律条文、专利等高冗余、强文档间相似度的语料——这一失配破坏评估有效性：检索器即使检索到提供充分证据的文档也可能被不公低估（因冗余未被计入），而在标准基准上表现良好的检索器往往泛化到高相似语料时表现糟糕。本文提出 **RARE（Redundancy-Aware Retrieval Evaluation）**：将文档分解为原子事实以实现精确跨文档冗余追踪，并通过 **CRRF**（按标准分别评分、以排名融合决策）稳定 LLM 数据生成质量。应用于金融/法律/专利语料，引入 **RedQA** 基准，揭示强检索器基线从 4-hop General-Wiki 的 66.4% PerfRecall@10 骤降至 4-hop Finance/Legal 的 8.5%/5.0% 和 Patent 的 27.9%——暴露当前基准无法捕获的鲁棒性缺口，使从业者能在自有语料上构建忠实反映部署条件的领域 RAG 评估。

## 关键贡献

- **RARE 冗余感知评估框架**：原子事实分解 + 嵌入相似度召回 + LLM 验证精确度的两阶段冗余检测，使检索到有效替代证据的检索器不再被单规范文档标注惩罚
- **CRRF 多标准数据生成**：将复杂多标准推理分解为简单二值/标量判断，按标准独立评分后以排名聚合（而非置信度分数）稳定 LLM 判断，提升生成基准实例的可靠性
- **RedQA 基准与鲁棒性量化**：跨金融/法律/专利量化标准基准与企业语料的冗余/相似度差距，揭示 4-hop 深度下 PerfRecall 从 66.4% 降至 5.0–27.9% 的严重退化

## 关键引用

> "Retrievers can be unfairly undervalued even when they retrieve documents that provide sufficient evidence, because redundancy across documents is not accounted for in evaluation."

## 关联

- [[RetrievalEvaluation]] — 本文是该概念的核心贡献，填补高冗余语料评估维度空白
- [[RetrievalAugmentedGeneration]] — 直接服务于企业 RAG 系统的可靠性评估，揭示低重叠基准对高重叠语料性能的高估
- [[coverage-not-averages]] — 互补关系：本文从冗余相似度维度、后者从语料语义覆盖维度共同揭示聚合指标的系统性失效

## 矛盾

无已知矛盾。
