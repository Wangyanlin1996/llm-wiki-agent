---
title: "KG2QA: 通信标准知识图谱增强问答（KG-Enhanced RAG for Communication Standards QA）"
type: source
tags: [ontology-graph-retrieval]
sources: [kg2qa-communication-standards]
source_file: raw/papers/kg2qa-communication-standards.pdf
last_updated: 2026-08-31
arxiv_id: "2506.07037"
authors: ["Zhongze Luo", "Weixuan Wan", "Tianya Zhang", "Dan Wang", "Xiaoying Tang"]
year: 2025
venue: "arXiv preprint"
citation_count: 0
doi: ""
---

## 概要
KG2QA 是一个面向通信标准问答的框架，将 LoRA 微调的 LLM 与领域知识图谱（KG）通过 RAG 管线集成。框架包含从 ITU-T 建议书构建的 6,587 条 QA 数据集（用于微调 Qwen2.5-7B-Instruct）、基于自定义 ontology 和 LLM 辅助三元组抽取构建的结构化 KG（13,906 实体、13,524 关系），以及 KG-RAG 问答系统。微调后 BLEU-4 从 18.86 提升至 66.90，超越 DeepSeek/ChatGPT/Gemini 等主流 API 模型。

## 解决的问题
通信标准数量爆炸式增长，传统依赖专家的咨询方法效率低下。通用 LLM（GPT-4o、Gemini）在通信标准等专门领域的表现受限于预训练数据中专业术语和领域知识的稀疏表示。单纯的 LoRA 微调虽能增强语义理解，但缺乏事实性 grounding；而标准文本检索（Text-RAG）无法提供结构化知识的精确关联。领域 KG 虽能提供结构化表示，但通信标准领域的 KG 构建缺乏专用 ontology 和自动化三元组抽取管线。

## 方法与技术
1. **LoRA 微调领域适配**：基于 ITU-T 建议书的 28 个 PDF 构建 6,587 条 Alpaca 格式 QA 数据集，用 DeepSeek-V3 API 从源 PDF 抽取 QA 对，LoRA 参数 rank=16, alpha=32, lr=5.0e-5，在 Qwen2.5-7B-Instruct 和 Llama-3-8B-Instruct 上进行指令监督微调。
2. **自定义 Ontology 驱动的 KG 构建**：设计 6 类实体（Identifier, Structure-Composition, Suitability-Context, Action, Value, Function）和 10 类关系（contain, isReliedOn, accomplish, limit, relevant, execute, influence 及逆关系），定义 domain/range 约束。
3. **三步式 LLM 辅助三元组抽取管线**：依次执行头实体识别→潜在关系识别（带置信度阈值 θ=0.8 过滤）→尾实体类型判定，模块化地完成端到端 PDF→KG 三元组提取，最终导入 Neo4j。
4. **KG-RAG 问答管线**：微调后的 Qwen Merged 模型转换为 GGUF 格式、量化（q4_K_M）并本地部署于 Ollama，通过 Bolt 协议远程访问 Neo4j KG 实例；系统先从 KG 检索相关上下文，再输入微调模型生成答案。
5. **LLM-as-Judge 五维评估**：使用 DeepSeek-V3 作为公正裁判，在 similarity/fluency/coherence/relevance/factual accuracy 五个维度上对比 LM-Only 与 LM+KG 系统。

## 创新点
- **通信标准领域专用 Ontology 设计**（vs. 通用知识图谱无领域特定实体/关系类型约束）——定义 6 实体类型+10 关系类型，使 KG 结构精确映射通信标准文档语义。
- **模块化 LLM 辅助 KG 构建管线**（vs. 传统人工三元组标注效率低）——三步流水线配合置信度阈值过滤，实现 PDF 到 KG 的自动化构建。
- **微调 LLM + 领域 KG 的 RAG 集成**（vs. 单纯 Text-RAG 或单纯微调）——KG-RAG 在所有实验组上全面优于 Text-RAG 和无 RAG 基线。
- **开源可复现的通信标准 QA 框架**（vs. 该领域此前缺乏公开基准和系统）——代码和数据完全开源。

## 效果
- Dataset: ITU-T Test set (809 QA) | Metric: BLEU-4 | Result: 66.893 (Qwen Merged) | Baseline: 18.8564 (Qwen Base) | Δ: [+255.0%]
- Dataset: ITU-T Test set | Metric: ROUGE-L | Result: 61.4781 (Qwen Merged) | Baseline: 18.72 (Qwen Base) | Δ: [+228.4%]
- Dataset: ITU-T Test set | Metric: BLEU-4 vs API models | Result: 66.893 (Qwen Merged) | Baseline: 37.456 (DeepSeek) | Δ: [+78.5%]
- Dataset: 5-dim LLM judge | Metric: Overall Avg | Result: 0.8134 (Qwen Merged+KG-RAG) | Baseline: 0.7908 (Qwen Merged w/o KG-RAG) | Δ: [+2.26%]
- Dataset: 5-dim LLM judge | Metric: Factual Accuracy | Result: 0.8045 (Qwen Merged+KG-RAG) | Baseline: 0.728 (w/o KG-RAG) | Δ: [+3.17%]
- **Ablation**: Text-RAG vs KG-RAG: Overall Avg 0.8072 vs 0.8134，KG-RAG 优于 Text-RAG [+0.77%]
- **Ablation**: Base 模型 vs Merged 模型 KG-RAG 增益：Qwen Base 提升 +3.18% vs Qwen Merged 提升 +2.26%，未微调模型从 KG 获益更显著

## 关键引用
> "This approach overcomes the limitations of lexical-overlap metrics like BLEU/ROUGE, which may unfairly penalizes a RAG-generated answer for containing more correct facts than the static reference." — Section 2.3, p.3

> "the improvement effect of our KG-RAG pipeline in the Base group is better than that in the Merged group... for models that have not been fine-tuned with domain-specific knowledge, the impact brought by using domain-specific KG is more obvious." — Section 3.3, p.4

> "although the Llama base model has better native performance, the Qwen model is more adaptable to the data of this fine-tuning task." — Section 3.1, p.3-4

## 关联
- [[OntologyGraphRetrieval]] — 本体图检索核心概念
- [[OntologyGuidedQueryGeneration]] — 本体引导查询构造
- [[telco-orag]] — Round 9 电信场景混合检索+神经路由
- [[armor-telecom-retriever]] — Round 9 电信查询侧检索器自适应优化
- [[5GNetworkManagement]] — 3GPP 通信标准管理
