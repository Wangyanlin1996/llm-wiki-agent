---
title: "检索评估（Retrieval Evaluation）"
type: concept
tags: ['semantic-retrieval', 'evaluation']
sources: ["rag-evaluation-survey", "coverage-not-averages", "rare-redundancy-eval", "hakari-bench", "hteb-harder-embedding-bench"]
last_updated: 2026-07-02
---

检索评估超越 nDCG/Recall@k 的多维评估。RAG 评估需覆盖系统性能、事实准确性、安全性和计算效率四维度（[[rag-evaluation-survey]]）。语义分层将评估形式化为统计估计问题，提供形式化覆盖保证（[[coverage-not-averages]]）。高冗余语料（金融/法律/专利）需原子事实分解和冗余感知评估（[[rare-redundancy-eval]]）。嵌入模型评估从静态单分数到多维度动态鲁棒性（[[hteb-harder-embedding-bench]]）。相关论文：[[rag-evaluation-survey]]、[[coverage-not-averages]]、[[rare-redundancy-eval]]
