---
title: "CodeWiki：大规模代码库整体文档生成的多智能体框架"
type: source
tags: [multi-agent-long-context]
sources: [codewiki]
source_file: raw/papers/codewiki.pdf
last_updated: 2026-07-24
arxiv_id: "2510.24428"
authors: ["A. Hoang", "Minh Le-Anh", "Bach Le", "Nghi D. Q. Bui"]
year: 2025
venue: "Annual Meeting of the Association for Computational Linguistics"
citation_count: 6
doi: "10.48550/arXiv.2510.24428"
---

## 概要
CodeWiki 引入三项创新：(i) 保持架构上下文的层级分解，(ii) 带动态任务委派的递归多智能体处理用于可扩展生成，(iii) 整合文本描述与视觉制品（如架构图和数据流表示）的多模态综合。引入 CodeWikiBench 基准。实验显示 CodeWiki 达到 68.79% 质量分，超过闭源 DeepWiki 基线 4.73%。发表于 ACL 2026。

## 关键贡献
- 层级分解保持架构上下文 + 递归多智能体 + 动态任务委派
- 多模态综合：文本描述 + 架构图 + 数据流表示
- CodeWikiBench 基准 + 68.79% 质量分超 DeepWiki 4.73%

## 关键引用
> "CodeWiki introduces three key innovations: (i) hierarchical decomposition that preserves architectural context, (ii) recursive multi-agent processing with dynamic task delegation, and (iii) multi-modal synthesis."

## 关联
- [[MemDocAgent]] — MemDocAgent 也处理仓库级文档但用共享记忆
- [[MultiAgentLongContext]] — 多智能体处理大规模代码库长上下文
- [[RecursiveMultiAgent]] — 递归多智能体处理范式

## 矛盾
- (暂无)
