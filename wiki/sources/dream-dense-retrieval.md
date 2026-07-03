---
title: "DREAM：基于自回归建模的稠密检索嵌入"
type: source
tags: ['semantic-retrieval', 'dense-retrieval']
sources: [dream-dense-retrieval]
source_file: raw/papers/dream-dense-retrieval.pdf
last_updated: 2026-07-02
arxiv_id: "2606.24667"
authors: ["Yixuan Tang", "Yi Yang"]
year: 2026
venue: "arXiv"
citation_count: pending
---

## 概要

大多数稠密检索器依赖对比学习目标训练，需要标注的正例和负例文档对，这些标注成本高且难以获取。DREAM（Dense Retrieval Embeddings via Autoregressive Modeling）提出一种全新范式：利用冻结 LLM 的自回归 next-token prediction（NTP）目标为稠密检索器提供无标注监督。核心直觉是——如果候选文档包含与 query 相关的信息，那么条件化于该文档应使 LLM 更容易预测目标输出，从而降低 NTP loss；反之，不相关的文档不会降低 loss。关键技术挑战在于 NTP loss 在 LLM 内部计算，而检索器是独立的嵌入模型。DREAM 通过将检索器计算的 query-document 相似度分数注入冻结 LLM 的"查询聚焦检索头"（query-focused retrieval heads）来解决这一 disconnect：相似度分数决定每个候选文档获得的注意力权重，NTP loss 的梯度通过注意力机制回传到检索器。文档分数跨候选归一化形成注意力竞争，使 loss 能隐式抑制无用文档，无需显式构造负例。在 BEIR 和 RTEB 基准上，0.5B-3B 参数规模均一致超越 RePlug 和 Revela 基线，BEIR NDCG@10 提升 0.015-0.081，RTEB 提升 0.068-0.102。

## 关键贡献

- **自回归建模作为检索监督信号**：首次证明 LLM 的 next-token prediction 目标可为稠密检索器提供有效监督，无需对比学习或标注数据对——开辟了"生成式监督检索"新路径
- **检索分数注入查询聚焦注意力头**：通过识别 LLM 中已执行检索功能的注意力头并将检索器分数注入其中，使 NTP loss 对检索质量敏感——注入随机头则效果大幅下降，验证了注意力头选择的关键性
- **注意力竞争隐式负例挖掘**：候选文档共享固定注意力预算，提升一文档权重必然降低其他文档权重，使 loss 隐式抑制不帮助预测的文档——消除显式负例构造需求

## 关键引用

> "If a candidate document contains useful information for answering a query, conditioning on that document should make the target output easier to predict and reduce the next-token prediction loss. Conversely, documents that do not provide useful information should contribute little to prediction."

> "Because candidates share a fixed attention budget, increasing the weight of one document necessarily reduces the weights of others. This allows the prediction loss to implicitly suppress documents that do not help predict the target output, eliminating the need for explicitly constructed negative examples."

## 关联

- [[DenseRetrieval]] — 本文是该概念的核心实现之一，提出自回归建模替代对比学习作为稠密检索训练范式
- [[RetrievalAugmentedGeneration]] — 检索文档最终被 LLM 消费用于生成，DREAM 直接以"文档是否帮助 LLM 生成"作为检索质量信号
- [[scaling-dense-retrieval]] — 两者均解决训练数据获取难题：DREAM 用无标注 NTP 监督，后者用 LLM 标注的结构化挖掘
- [[coder-constraint-retrieval]] — 同属稠密检索创新，但 DREAM 改训练目标，CoDeR 改评分维度（约束兼容性）

## 矛盾

无已知矛盾。与对比学习范式的"需要标注对 vs 无需标注"形成方法论分歧，但实验表明自回归监督可达到竞争性性能。
